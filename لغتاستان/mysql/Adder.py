import os
import argparse # برای مدیریت آرگومان‌های خط فرمان

def add_word_to_file(word):
    """
    کلمه (یا خط) را به فایل‌های مدیریت شده اضافه می‌کند
    
    Args:
        word (str): کلمه‌ای که باید اضافه شود
    
    Returns:
        dict: اطلاعات عملیات انجام شده
    """
    # خواندن فایل boolean
    try:
        with open('0booleanIsEmpty.txt', 'r') as f:
            boolean_value = f.read().strip()
    except FileNotFoundError:
        boolean_value = '1'
        with open('0booleanIsEmpty.txt', 'w') as f:
            f.write('1')
    
    # خواندن تعداد فایل‌ها
    try:
        with open('0NumberOfAllTxtFiles.txt', 'r') as f:
            file_count = int(f.read().strip())
    except FileNotFoundError:
        file_count = 1
        with open('0NumberOfAllTxtFiles.txt', 'w') as f:
            f.write('1')
    
    result = {}
    
    # اگر کلمه پس از حذف فضاهای خالی، خالی باشد، آن را نادیده می‌گیریم.
    # این کار در تابع process_file_and_split هم انجام می‌شود،
    # اما برای اطمینان و زمانی که تابع به صورت مستقل فراخوانی می‌شود، اینجا هم لازم است.
    if not word.strip(): 
        return {
            'action': 'skipped_empty_line',
            'word': word, 
            'message': "خط ورودی خالی یا فقط شامل فضای خالی بود و نادیده گرفته شد."
        }

    # کلمه‌ای که قرار است به فایل اضافه شود (پس از strip شدن در تابع فراخواننده یا اینجا)
    line_to_add = word.strip() # اطمینان از حذف فضاهای خالی ابتدا و انتها

    if boolean_value == '1':
        filename = f"{file_count}.txt"
        
        if os.path.exists(filename):
            with open(filename, 'r', encoding='utf-8') as f:
                content = f.read()
        else:
            content = ""
        
        if content and not content.endswith('\n'):
            content += '\n'
        content += line_to_add + '\n'
        
        with open(filename, 'w', encoding='utf-8') as f:
            f.write(content)
        
        lines = content.split('\n')
        non_empty_lines = [line for line in lines if line.strip()]
        
        result = {
            'action': 'added_to_existing',
            'filename': filename,
            'word': line_to_add,
            'lines_count': len(non_empty_lines),
            'file_full': False
        }
        
        if len(non_empty_lines) >= 40:
            with open('0booleanIsEmpty.txt', 'w') as f:
                f.write('0')
            result['file_full'] = True
            result['message'] = f"خط '{line_to_add[:30]}...' به فایل {filename} اضافه شد. فایل کامل شد ({len(non_empty_lines)}/40 خط) و boolean به 0 تغییر کرد."
        else:
            result['message'] = f"خط '{line_to_add[:30]}...' به فایل {filename} اضافه شد. ({len(non_empty_lines)}/40 خط)"
    
    else: # boolean_value == '0'
        new_file_count = file_count + 1
        new_filename = f"{new_file_count}.txt"
        with open(new_filename, 'w', encoding='utf-8') as f:
            f.write(line_to_add + '\n')
        
        with open('0NumberOfAllTxtFiles.txt', 'w') as f:
            f.write(str(new_file_count))
        
        with open('0booleanIsEmpty.txt', 'w') as f:
            f.write('1')
        
        result = {
            'action': 'created_new_file',
            'filename': new_filename,
            'word': line_to_add,
            'lines_count': 1,
            'file_full': False,
            'message': f"فایل جدید {new_filename} ایجاد شد و خط '{line_to_add[:30]}...' در آن قرار گرفت."
        }
    
    return result

def process_file_and_split(filepath):
    """
    یک فایل ورودی را می‌خواند و محتوای آن را خط به خط
    با استفاده از add_word_to_file به فایل‌های مقصد تقسیم می‌کند.
    
    Args:
        filepath (str): مسیر فایل ورودی
    """
    try:
        with open(filepath, 'r', encoding='utf-8') as f_in:
            print(f"شروع پردازش فایل: {filepath}")
            
            source_file_line_count = 0 # شمارنده کل خطوط خوانده شده از فایل ورودی
            processed_lines_count = 0  # شمارنده خطوط غیرخالی که واقعا پردازش و اضافه شده‌اند

            # استفاده از enumerate برای گرفتن شماره خط (شروع از 1)
            for current_line_number, line_content in enumerate(f_in, 1):
                source_file_line_count = current_line_number # به‌روزرسانی کل خطوط خوانده شده
                
                # حذف کاراکتر خط جدید از انتهای هر خط خوانده شده
                # و همچنین فضاهای خالی احتمالی ابتدا و انتها
                cleaned_line = line_content.strip() 
                
                # اگر خط پس از پاکسازی خالی بود، آن را نادیده می‌گیریم
                if not cleaned_line:
                    print(f"  خط شماره {current_line_number} از فایل ورودی، خالی بود و نادیده گرفته شد.")
                    continue # برو به خط بعدی در فایل ورودی

                # اگر خط خالی نبود، آن را پردازش می‌کنیم
                processed_lines_count += 1
                # cleaned_line را به تابع پاس می‌دهیم (تابع add_word_to_file خودش هم strip می‌کند اگر لازم باشد)
                result = add_word_to_file(cleaned_line) 
                
                # نمایش بخشی از خط برای خوانایی بهتر در لاگ‌ها
                line_preview = cleaned_line[:40] + '...' if len(cleaned_line) > 40 else cleaned_line
                print(f"  پردازش خط {current_line_number} فایل ورودی ('{line_preview}'): {result['message']}")
            
            print(f"\nپردازش فایل {filepath} به اتمام رسید.")
            print(f"تعداد کل خطوط خوانده شده از فایل ورودی: {source_file_line_count}")
            print(f"تعداد کل خطوط غیرخالی پردازش شده و اضافه شده به فایل‌های مقصد: {processed_lines_count}")
            
    except FileNotFoundError:
        print(f"خطا: فایل ورودی {filepath} یافت نشد.")
    except Exception as e:
        print(f"خطایی در هنگام پردازش فایل {filepath} رخ داد: {e}")


def main():
    """تابع اصلی برای اجرای اسکریپت از خط فرمان"""
    parser = argparse.ArgumentParser(description="ابزاری برای اضافه کردن کلمات یا تقسیم فایل به فایل‌های کوچکتر.")
    
    # گروهی برای انتخاب یکی از دو حالت: یا فایل یا کلمه
    # required=True یعنی کاربر باید حتما یکی از این دو آرگومان را ارائه دهد
    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-f", "--file", help="مسیر فایل ورودی برای تقسیم بندی")
    group.add_argument("-w", "--word", help="یک کلمه/خط برای اضافه کردن مستقیم به فایل‌های مدیریت شده")

    args = parser.parse_args()

    if args.file:
        # اگر آرگومان فایل داده شده بود، فایل را پردازش و تقسیم کن
        process_file_and_split(args.file)
    elif args.word:
        # اگر آرگومان کلمه داده شده بود، فقط آن کلمه را اضافه کن
        # تابع add_word_to_file خودش ورودی را strip می‌کند اگر لازم باشد
        result = add_word_to_file(args.word)
        print(result['message'])

if __name__ == "__main__":
    main()
