import os
import sys
import subprocess
import time
import glob
import json
import random
import concurrent.futures

# مسیرهای مورد نیاز
FARHANGESTAN_DIR = os.path.dirname(os.path.abspath(__file__))
LOGHASTAN_DIR = os.path.join(FARHANGESTAN_DIR, "لغتاستان")
RUNNER_SCRIPT = os.path.join(LOGHASTAN_DIR, "0Runner.py")

DATA_DIR = os.path.join(FARHANGESTAN_DIR, "data")
OUTPUTS_FILE = os.path.join(FARHANGESTAN_DIR, "OutPuts.txt")

# اسکریپت‌های مدل‌ها
MOTHER_MODEL_SCRIPT = os.path.join(FARHANGESTAN_DIR, "MotherModel.py")
ENDER_SCRIPT = os.path.join(FARHANGESTAN_DIR, "Ender.py")
SUMMATOR_SCRIPT = os.path.join(FARHANGESTAN_DIR, "summator.py")
SLIPTER_SCRIPT = os.path.join(FARHANGESTAN_DIR, "slipter.py")

MAX_ITERATIONS_PER_POEM = 3 # حداکثر تعداد تلاش برای بهبود یک شعر قبل از رها کردن
NAZER_TIMEOUT_SECONDS = 20 # مهلت ناظر (10 ثانیه اولیه + 10 ثانیه با API Key جدید)

def ensure_directories():
    os.makedirs(DATA_DIR, exist_ok=True)
    # پوشه‌های FAILED و yeah توسط summator و slipter ایجاد می‌شوند در صورت نیاز

def get_next_conversation_id():
    os.makedirs(DATA_DIR, exist_ok=True)
    existing_ids = [int(d) for d in os.listdir(DATA_DIR) if os.path.isdir(os.path.join(DATA_DIR, d)) and d.isdigit()]
    return max(existing_ids) + 1 if existing_ids else 0

def log_conversation_step(conversation_id, step_name, content, is_json=False):
    conv_path = os.path.join(DATA_DIR, str(conversation_id))
    os.makedirs(conv_path, exist_ok=True)
    
    step_files = glob.glob(os.path.join(conv_path, f"*_{step_name}.*"))
    next_idx = 0
    if step_files:
        indices = []
        for f_name in step_files:
            try:
                base_name = os.path.basename(f_name)
                idx_str = base_name.split('_')[0]
                if idx_str.isdigit():
                    indices.append(int(idx_str))
            except:
                pass
        if indices:
            next_idx = max(indices) + 1

    ext = ".json" if is_json else ".txt"
    log_file = os.path.join(conv_path, f"{next_idx:02d}_{step_name}{ext}") 
    
    with open(log_file, "w", encoding="utf-8") as f:
        if is_json:
            json.dump(content, f, ensure_ascii=False, indent=4)
        else:
            f.write(str(content))
    print(f"Logged to: {log_file}")


def run_script(script_path, *args, working_dir=FARHANGESTAN_DIR, timeout=None):
    # Sanitize args that are strings by replacing Farsi comma
    sanitized_args = []
    for arg in args:
        if isinstance(arg, str):
            sanitized_args.append(arg.replace('،', ','))
        else:
            sanitized_args.append(arg)

    command = [sys.executable, script_path] + list(sanitized_args)
    try:
        process = subprocess.run(
            command,
            capture_output=True,
            text=True,
            check=True,
            encoding='utf-8',
            cwd=working_dir,
            timeout=timeout
        )
        # Also sanitize the output if it's going to be used as input elsewhere
        return process.stdout.strip().replace('،', ',')
    except subprocess.TimeoutExpired:
        print(f"Timeout executing {script_path} with args {args}", file=sys.stderr)
        return None
    except subprocess.CalledProcessError as e:
        print(f"Error running {script_path} with args {args}:\nStdout: {e.stdout}\nStderr: {e.stderr}", file=sys.stderr)
        return None
    except Exception as e:
        print(f"Unexpected error running {script_path}: {e}", file=sys.stderr)
        return None

def run_nazer_script_with_retry(nazer_script, poem_text):
    # poem_text is already an argument to run_script, so it will be sanitized there.
    feedback = run_script(nazer_script, poem_text, timeout=NAZER_TIMEOUT_SECONDS / 2)
    if feedback and "خطا در پردازش" not in feedback:
        return feedback
    
    print(f"Retrying {os.path.basename(nazer_script)}...")
    feedback = run_script(nazer_script, poem_text, timeout=NAZER_TIMEOUT_SECONDS / 2)
    if feedback and "خطا در پردازش" not in feedback:
        return feedback
        
    print(f"Nazer {os.path.basename(nazer_script)} failed after retries.", file=sys.stderr)
    return None


def run_all_nazers_parallel(poem_text):
    nazer_scripts = glob.glob(os.path.join(FARHANGESTAN_DIR, "Nazer-*.py"))
    if not nazer_scripts:
        print("No Nazer scripts found!", file=sys.stderr)
        return {}

    feedbacks = {}
    # poem_text will be sanitized by run_nazer_script_with_retry -> run_script
    with concurrent.futures.ThreadPoolExecutor(max_workers=len(nazer_scripts)) as executor:
        future_to_nazer = {executor.submit(run_nazer_script_with_retry, script, poem_text): os.path.basename(script) for script in nazer_scripts}
        
        for future in concurrent.futures.as_completed(future_to_nazer):
            nazer_name = future_to_nazer[future]
            try:
                result = future.result() 
                if result is None:
                    print(f"Nazer {nazer_name} definitively failed to provide feedback.", file=sys.stderr)
                    feedbacks[nazer_name] = "ناظر پاسخ نداد یا در پردازش شکست خورد."
                    return None 
                # Result from run_script is already sanitized
                feedbacks[nazer_name] = result
            except Exception as exc:
                print(f"{nazer_name} generated an exception: {exc}", file=sys.stderr)
                feedbacks[nazer_name] = f"خطای استثنا در اجرای ناظر: {exc}"
                return None

    return feedbacks

def main_loop():
    poem_cycle_count = 0
    while True:
        poem_cycle_count += 1
        print(f"\n--- Starting Poem Cycle #{poem_cycle_count} ---")
        conversation_id = get_next_conversation_id()
        print(f"Current Conversation ID: {conversation_id}")

        print("Getting initial prompt from 0Runner.py...")
        initial_poem_prompt_idea = run_script(RUNNER_SCRIPT, working_dir=LOGHASTAN_DIR)
        if not initial_poem_prompt_idea:
            print("Failed to get prompt from 0Runner.py. Skipping this cycle.", file=sys.stderr)
            time.sleep(5)
            continue
        
        # initial_poem_prompt_idea is already sanitized by run_script's return value
        
        enhanced_prompt_for_mother = (
            f"{initial_poem_prompt_idea}\n" # Already sanitized
            f"نکات مهم: فقط و فقط شعر بنویس. هیچ متن اضافی، عنوان یا توضیحی اضافه نکن." # This string is safe
        )
        # Log the original (potentially unsanitized if 0Runner produced it) and the one used
        log_conversation_step(conversation_id, "prompt_idea_raw_from_0runner", initial_poem_prompt_idea) # Log the sanitized version
        log_conversation_step(conversation_id, "enhanced_prompt_mother", enhanced_prompt_for_mother)
        print(f"Initial prompt idea (sanitized): {initial_poem_prompt_idea}")

        current_poem_text = None
        nazer_feedback_history_str = "" 

        for iteration in range(MAX_ITERATIONS_PER_POEM):
            print(f"\n  --- Iteration #{iteration + 1} for poem ID {conversation_id} ---")
            
            print("Generating poem with MotherModel...")
            # enhanced_prompt_for_mother is sanitized.
            # nazer_feedback_history_str needs to be sanitized before passing.
            # Since nazer_feedback_history_str is constructed within this loop,
            # we ensure its components are sanitized.
            # The run_script call itself will sanitize its string arguments.
            poem_text_candidate = run_script(MOTHER_MODEL_SCRIPT, 
                                             enhanced_prompt_for_mother, # Already sanitized
                                             nazer_feedback_history_str) # Sanitized by run_script
            
            if not poem_text_candidate:
                print("MotherModel failed to generate a poem. Ending this poem's lifecycle.", file=sys.stderr)
                break 
            
            current_poem_text = poem_text_candidate # Already sanitized by run_script's return
            log_conversation_step(conversation_id, f"mother_model_v{iteration+1}", current_poem_text)
            print(f"Poem candidate v{iteration+1}:\n{current_poem_text}")

            print("Getting feedback from Nazers...")
            # current_poem_text is sanitized, run_all_nazers_parallel will pass it to run_script
            nazer_feedbacks = run_all_nazers_parallel(current_poem_text) 
            
            if nazer_feedbacks is None:
                print("Critical failure in Nazer stage. Ending this poem's lifecycle.", file=sys.stderr)
                if current_poem_text:
                    run_script(SUMMATOR_SCRIPT, current_poem_text) # Sanitized by run_script
                break

            log_conversation_step(conversation_id, f"nazer_feedback_v{iteration+1}", nazer_feedbacks, is_json=True)
            
            # Nazer feedbacks (values in the dict) are already sanitized by run_script's return
            combined_nazer_feedback_str = "\n".join([f"- {name}: {feedback}" for name, feedback in nazer_feedbacks.items()])
            print(f"Nazer feedbacks v{iteration+1}:\n{combined_nazer_feedback_str}")

            print("Getting decision from Ender...")
            # current_poem_text and combined_nazer_feedback_str are sanitized
            ender_decision = run_script(ENDER_SCRIPT, current_poem_text, combined_nazer_feedback_str)
            
            if not ender_decision: # ender_decision is sanitized by run_script's return
                print("Ender failed to make a decision. Ending this poem's lifecycle.", file=sys.stderr)
                if current_poem_text:
                    run_script(SUMMATOR_SCRIPT, current_poem_text)
                break

            log_conversation_step(conversation_id, f"ender_decision_v{iteration+1}", ender_decision)
            print(f"Ender's decision v{iteration+1}: {ender_decision}")

            if ender_decision.strip().upper() == "ACCEPT":
                print("Poem ACCEPTED by Ender!")
                with open(OUTPUTS_FILE, "a", encoding="utf-8") as f:
                    f.write(current_poem_text + "\n---\n") 
                
                run_script(SLIPTER_SCRIPT, current_poem_text)
                break 
            
            elif ender_decision.strip().upper().startswith("REJECT"):
                print("Poem REJECTED by Ender.")
                # ender_decision is sanitized.
                rejection_reason = ender_decision[len("REJECT"):].strip() 
                
                # combined_nazer_feedback_str and rejection_reason are already sanitized
                nazer_feedback_history_str = (
                    f"نظرات داوران:\n{combined_nazer_feedback_str}\n"
                    f"تصمیم و دلیل رد شدن از سوی وزیر اعظم:\n{rejection_reason}\n"
                    f"لطفا با در نظر گرفتن این موارد، شعر را بازنویسی و اصلاح کنید."
                )
                # This nazer_feedback_history_str will be passed to run_script in the next iteration,
                # and run_script will sanitize its string arguments. So it's fine.

                if iteration == MAX_ITERATIONS_PER_POEM - 1:
                    print("Max iterations reached. Poem finally rejected.")
                    run_script(SUMMATOR_SCRIPT, current_poem_text)
            else:
                print(f"Unknown decision from Ender: {ender_decision}. Treating as REJECT.", file=sys.stderr)
                run_script(SUMMATOR_SCRIPT, current_poem_text)
                break 
        
        print(f"--- End of Poem Lifecycle for ID {conversation_id} ---")
        time.sleep(2)


if __name__ == "__main__":
    print("Starting Farhangestan Poetry Ecosystem Orchestrator...")
    ensure_directories()
    try:
        main_loop()
    except KeyboardInterrupt:
        print("\nOrchestrator stopped by user.")
    except Exception as e:
        print(f"An unhandled error occurred in orchestrator: {e}", file=sys.stderr)
        import traceback
        traceback.print_exc()
    finally:
        print("Orchestrator shutting down.")
