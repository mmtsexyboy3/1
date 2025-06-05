import google.generativeai as genai
import random
import sys
import os
import re

API_KEYS = ['AIzaSyCjblGVNqiNXPr_gJ_D1mzKzR8jn5KhLc4', 'AIzaSyA0HaBhBdvSO_BJZTgFLXLPGNskXuI8E']
MODEL_NAME = "gemini-1.5-flash-8b"

# پوشه ذخیره سازی شعرهای تایید شده
ACCEPTED_POEMS_BASE_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "yeah")
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

def clean_poem_text_for_acceptance(raw_text_containing_poem):
    model = configure_model()
    # پرامپت مشابه summator اما شاید با تاکید کمتر روی "شکست خورده"
    prompt = f"""
متن زیر یک شعر تایید شده است اما ممکن است هنوز دارای توضیحات، مقدمه، عنوان یا کاراکترهای اضافی در ابتدا یا انتهای آن باشد.
---
{raw_text_containing_poem}
---
وظیفه: با دقت بسیار بالا، فقط و فقط متن اصلی شعر را استخراج کنید. هیچ کلمه، علامت نگارشی اضافی (مگر اینکه جزئی از خود شعر باشد)، توضیح، عنوان، مقدمه یا هر چیز دیگری نباید در خروجی شما باشد. فقط و فقط خود شعر، تمیز و آماده برای آرشیو نهایی.
مثال ورودی:
"شعر برگزیده این دوره:
در باغ عدم، گلی شکفتم
اسرار وجود را بگفتم
پایان."
مثال خروجی صحیح:
در باغ عدم، گلی شکفتم
اسرار وجود را بگفتم
"""
    try:
        response = model.generate_content(prompt.format(raw_text_containing_poem=raw_text_containing_poem))
        return response.text.strip()
    except Exception as e:
        print(f"Error in Slipter cleaning: {e}", file=sys.stderr)
        return raw_text_containing_poem.strip() # Fallback

if __name__ == "__main__":
    if len(sys.argv) > 1:
        poem_to_process = sys.argv[1]
        cleaned_poem = clean_poem_text_for_acceptance(poem_to_process)
        
        if cleaned_poem:
            filepath = get_next_filepath(ACCEPTED_POEMS_BASE_DIR)
            os.makedirs(os.path.dirname(filepath), exist_ok=True)
            with open(filepath, "w", encoding="utf-8") as f:
                f.write(cleaned_poem)
            print(f"Slipter: Saved cleaned accepted poem to {filepath}", file=sys.stderr)
            print(cleaned_poem) # Output cleaned poem to stdout
        else:
            print("Slipter: Failed to clean accepted poem.", file=sys.stderr)
    else:
        print("Usage: python slipter.py \"<raw_accepted_poem_text_to_clean_and_save>\"", file=sys.stderr)
