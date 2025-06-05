# main_prompt_orchestrator_case_insensitive.py

import random
import os
import sys
import subprocess
import re

# نام اسکریپت اصلی که با احتمال بالا اجرا می‌شود (با حروف کوچک برای استانداردسازی)
PRIMARY_SCRIPT_NAME_TARGET = "firstpromt.py"

# پیشوند و پسوند برای شناسایی اسکریپت‌های جایگزین (با حروف کوچک)
SECONDARY_SCRIPT_PREFIX_TARGET = "firstpromt"
SECONDARY_SCRIPT_SUFFIX_TARGET = ".py"

def get_actual_filename_case_insensitive(target_filename, directory="."):
    """
    نام فایل واقعی را در پوشه بر اساس تطابق غیرحساس به حروف برمی‌گرداند.
    اگر پیدا نشد، None برمی‌گرداند.
    """
    target_lower = target_filename.lower()
    try:
        for filename_in_dir in os.listdir(directory):
            if filename_in_dir.lower() == target_lower:
                return filename_in_dir  # برگرداندن نام فایل با حروف اصلی خودش
    except FileNotFoundError:
        pass
    return None

def find_secondary_scripts(directory="."):
    """
    پیدا کردن اسکریپت‌های جایگزین با فرمت firstpromt<number>.py (غیرحساس به حروف).
    """
    secondary_scripts = []
    pattern_str = rf"^{re.escape(SECONDARY_SCRIPT_PREFIX_TARGET)}(\d+){re.escape(SECONDARY_SCRIPT_SUFFIX_TARGET)}$"
    pattern = re.compile(pattern_str, re.IGNORECASE)
    try:
        for filename in os.listdir(directory):
            if pattern.match(filename):
                secondary_scripts.append(filename) # نام فایل با حروف اصلی خودش اضافه می‌شود
    except FileNotFoundError:
        # خطا چاپ نمی‌شود، فقط لیست خالی برگردانده می‌شود اگر پوشه موجود نباشد
        pass
    return secondary_scripts

def execute_script_and_get_output(actual_script_filename):
    """
    یک اسکریپت پایتون را با نام فایل واقعی آن اجرا کرده و خروجی استاندارد آن را برمی‌گرداند.
    در صورت بروز خطا، None برمی‌گرداند.
    """
    # بررسی os.path.exists(actual_script_filename) در اینجا ضروری نیست
    # چون get_actual_filename_case_insensitive باید نام فایل موجود را برگردانده باشد.
    # اگر به هر دلیلی فایل وجود نداشته باشد، subprocess.run خطا خواهد داد.

    try:
        process = subprocess.run(
            [sys.executable, actual_script_filename],
            capture_output=True,
            text=True,
            check=True, # اگر کد بازگشتی غیر صفر باشد، CalledProcessError ایجاد می‌کند
            encoding='utf-8'
        )
        return process.stdout.strip()
    except subprocess.CalledProcessError:
        # خطا در اجرای اسکریپت (مثلاً خروج با کد غیر صفر)
        # هیچ چیزی چاپ نمی‌شود، فقط None برگردانده می‌شود
        return None
    except Exception:
        # سایر خطاهای غیرمنتظره (مثلاً FileNotFoundError اگر sys.executable مشکل داشته باشد)
        # هیچ چیزی چاپ نمی‌شود، فقط None برگردانده می‌شود
        return None

def main():
    """
    تابع اصلی برای انتخاب و اجرای اسکریپت تولیدکننده پرامپت.
    فقط خروجی اسکریپت اجرا شده (در صورت موفقیت) چاپ می‌شود.
    """
    # بررسی وجود mysql/randreader.py انجام نمی‌شود و هشداری چاپ نمی‌شود.
    # اگر اسکریپت‌های هدف به آن نیاز داشته باشند و موجود نباشد، خودشان با خطا مواجه می‌شوند
    # و execute_script_and_get_output مقدار None برمی‌گرداند.

    random_number = random.randint(0, 1000)
    chosen_script_actual_name = None
    prompt_output = None

    if random_number < 700:
        chosen_script_actual_name = get_actual_filename_case_insensitive(PRIMARY_SCRIPT_NAME_TARGET)
        # اگر پیدا نشد، chosen_script_actual_name همچنان None خواهد بود. پیامی چاپ نمی‌شود.
    
    if not chosen_script_actual_name:
        secondary_scripts = find_secondary_scripts()
        if secondary_scripts:
            chosen_script_actual_name = random.choice(secondary_scripts)
        else:
            # هیچ اسکریپت جایگزینی پیدا نشد. پیامی چاپ نمی‌شود.
            if random_number >= 950: 
                 chosen_script_actual_name = get_actual_filename_case_insensitive(PRIMARY_SCRIPT_NAME_TARGET)
                 # اگر اسکریپت اصلی به عنوان جایگزین نهایی هم پیدا نشد، پیامی چاپ نمی‌شود.


    if chosen_script_actual_name:
        prompt_output = execute_script_and_get_output(chosen_script_actual_name)
    # اگر اسکریپتی انتخاب نشد یا پیدا نشد، chosen_script_actual_name مقدار None خواهد داشت
    # و prompt_output نیز None خواهد بود. پیامی چاپ نمی‌شود.


    if prompt_output: # اگر prompt_output یک رشته غیرخالی باشد
        print(prompt_output)
    # اگر prompt_output مقدار None یا رشته خالی باشد (پس از strip)، هیچ چیزی چاپ نمی‌شود.
    # این شامل مواردی است که اسکریپت انتخاب شده با خطا مواجه شده یا خروجی نداشته است.

if __name__ == "__main__":
    main()
