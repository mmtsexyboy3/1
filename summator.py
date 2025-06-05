import google.generativeai as genai
import random
import sys
import os
import re

API_KEYS = ['AIzaSyA91wAjqWish5dWohTFIufVT9UFty75j9Y']
MODEL_NAME = "gemini-1.5-flash-latest" # مدل سبک‌تر برای این کار کافی است

# پوشه ذخیره سازی شعرهای رد شده
FAILED_POEMS_BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "FAILED")
FILES_PER_SUBDIR = 100

def configure_model():
    api_key = random.choice(API_KEYS)
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)

def get_next_filepath(base_dir):
    os.makedirs(base_dir, exist_ok=True)
    
    sub_dir_idx = 0
    while True:
        current_sub_dir = os.path.join(base_dir, str(sub_dir_idx))
        os.makedirs(current_sub_dir, exist_ok=True)
        
        files_in_subdir = [f for f in os.listdir(current_sub_dir) if f.endswith(".txt")]
        
        # Find the highest numbered file in this subdir
        highest_num = 0
        for f_name in files_in_subdir:
            match = re.match(r"(\d+)\.txt", f_name) # Corrected regex to match literal dot
            if match:
                highest_num = max(highest_num, int(match.group(1)))
        
        next_potential_file_num = highest_num + 1
        # Only add if the directory has space AND the new file number is within the limit
        if len(files_in_subdir) < FILES_PER_SUBDIR and next_potential_file_num <= FILES_PER_SUBDIR:
            # The f-string {next_potential_file_num} is correct here as it's for the generated script
            return os.path.join(current_sub_dir, f"{next_potential_file_num}.txt")
        
        sub_dir_idx += 1


def clean_poem_text(raw_text_containing_poem):
    model = configure_model()
    prompt = f"""
متن زیر ممکن است حاوی یک شعر باشد، اما دارای توضیحات، مقدمه، عنوان یا کاراکترهای اضافی در ابتدا یا انتهای آن است.
---
{raw_text_containing_poem}
---
وظیفه: با دقت بسیار بالا، فقط و فقط متن اصلی شعر را استخراج کنید. هیچ کلمه، علامت نگارشی اضافی (مگر اینکه جزئی از خود شعر باشد)، توضیح، عنوان، مقدمه یا هر چیز دیگری نباید در خروجی شما باشد. فقط و فقط خود شعر، تمیز و بدون حاشیه.
مثال ورودی:
"این یک شعر زیبا در مورد بهار است:
گل آمد و بلبل نغمه خوان شد
فصل بهار آمد، جهان جوان شد
پاسخ من:"
مثال خروجی صحیح برای ورودی بالا:
گل آمد و بلبل نغمه خوان شد
فصل بهار آمد، جهان جوان شد

ورودی دیگر:
"شعر زیر را در نظر بگیرید:
...ای ساربان آهسته ران...
...کارام جانم می‌رود...
پایان شعر."
خروجی صحیح:
ای ساربان آهسته ران
کارام جانم می‌رود
"""
    try:
        response = model.generate_content(prompt.format(raw_text_containing_poem=raw_text_containing_poem))
        return response.text.strip()
    except Exception as e:
        print(f"Error in Summator cleaning: {e}", file=sys.stderr)
        # Fallback: return original text if model fails, so something is saved
        return raw_text_containing_poem.strip() 

if __name__ == "__main__":
    if len(sys.argv) > 1:
        poem_to_process = sys.argv[1]
        cleaned_poem = clean_poem_text(poem_to_process)
        
        if cleaned_poem:
            filepath = get_next_filepath(FAILED_POEMS_BASE_DIR)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(cleaned_poem)
            print(f"Summator: Saved cleaned rejected poem to {filepath}", file=sys.stderr)
            print(cleaned_poem) # Output cleaned poem to stdout for orchestrator if needed
        else:
            print("Summator: Failed to clean poem.", file=sys.stderr)

    else:
        print("Usage: python summator.py \"<raw_poem_text_to_clean_and_save>\"", file=sys.stderr)
