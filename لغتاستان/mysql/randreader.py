# randreader.py
import random
import os

# این خط را اضافه کنید
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))

def get_random_word():
    """
    یک کلمه تصادفی از فایل‌های موجود برمی‌گرداند
    
    Returns:
        dict: اطلاعات کلمه تصادفی یافت شده
    """
    try:
        # مسیر فایل را با SCRIPT_DIR بسازید
        path_to_0_file = os.path.join(SCRIPT_DIR, '0NumberOfAllTxtFiles.txt')
        with open(path_to_0_file, 'r') as f:
            max_file_number = int(f.read().strip())
    except FileNotFoundError:
        return {
            'success': False,
            'error': f'فایل 0NumberOfAllTxtFiles.txt در مسیر {SCRIPT_DIR} یافت نشد', # برای دیباگ بهتر
            'word': None,
            'filename': None,
            'line_number': None
        }
    except ValueError:
        return {
            'success': False,
            'error': 'محتوای فایل 0NumberOfAllTxtFiles.txt معتبر نیست',
            'word': None,
            'filename': None,
            'line_number': None
        }
    
    if max_file_number < 1:
        return {
            'success': False,
            'error': 'هیچ فایلی برای خواندن وجود ندارد',
            'word': None,
            'filename': None,
            'line_number': None
        }
    
    # تلاش برای یافتن فایل معتبر (حداکثر 10 تلاش)
    attempts = 0
    max_attempts = 10
    
    while attempts < max_attempts:
        random_file_number = random.randint(1, max_file_number)
        # مسیر فایل را با SCRIPT_DIR بسازید
        filename_only = f"{random_file_number}.txt"
        full_path_to_file = os.path.join(SCRIPT_DIR, filename_only)
        
        if not os.path.exists(full_path_to_file):
            attempts += 1
            continue
        
        try:
            with open(full_path_to_file, 'r', encoding='utf-8') as f:
                lines = f.readlines()
            
            non_empty_lines = [line.strip() for line in lines if line.strip()]
            
            if not non_empty_lines:
                attempts += 1
                continue
            
            random_line_index = random.randint(0, len(non_empty_lines) - 1)
            random_word = non_empty_lines[random_line_index]
            
            return {
                'success': True,
                'error': None,
                'word': random_word,
                'filename': filename_only, # یا full_path_to_file اگر مسیر کامل را می‌خواهید
                'line_number': random_line_index + 1,
                'total_lines': len(non_empty_lines),
                'file_number': random_file_number
            }
            
        except Exception as e:
            attempts += 1
            continue
    
    return {
        'success': False,
        'error': f'پس از {max_attempts} تلاش، فایل معتبری یافت نشد',
        'word': None,
        'filename': None,
        'line_number': None
    }


def main():
    """تابع اصلی برای اجرای مستقل اسکریپت"""
    result = get_random_word()
    
    if result['success']:
        print(f"کلمه تصادفی: {result['word']}")
        print(f"از فایل: {result['filename']}")
        print(f"خط شماره: {result['line_number']} از {result['total_lines']}")
    else:
        print(f"خطا: {result['error']}")


if __name__ == "__main__":
    main()
