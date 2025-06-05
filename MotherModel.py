import google.generativeai as genai
import random
import sys

# کلیدهای API و نام مدل مستقیماً در این فایل قرار داده شده‌اند
# مطابق با نحوه تولید این فایل توسط اسکریپت اصلی شما
API_KEYS = [
    "AIzaSyBjOys1KPI62SNRc1Vt-rRNe-ivA9f__Pc",
    "AIzaSyB2XvgyPvBU4UKFA3EKTlultse1OEsddDs",
]
MODEL_NAME = "gemini-2.0-flash-lite"

def configure_model():
    # انتخاب یک کلید API به صورت تصادفی
    api_key = random.choice(API_KEYS)
    genai.configure(api_key=api_key)
    # ساخت و بازگرداندن مدل
    return genai.GenerativeModel(MODEL_NAME)

def generate_poem(initial_prompt, existing_feedback=""):
    model = configure_model()

    # آماده‌سازی بخش بازخورد، با پاکسازی ویرگول فارسی
    feedback_text = ""
    if existing_feedback:
        feedback_text = "نظرات و بازخوردهای قبلی برای بهبود:\n" + str(existing_feedback).replace('،', ',')

    # پاکسازی پرامپت اولیه از ویرگول فارسی
    sanitized_initial_prompt = str(initial_prompt).replace('،', ',')

    # تعریف قالب پرامپت نهایی
    # توجه: تمام ویرگول‌های فارسی در متن ثابت این قالب با ویرگول انگلیسی (,) جایگزین شده‌اند.
    final_prompt = f"""
پرامپت اولیه برای سرودن شعر:
{sanitized_initial_prompt}

{feedback_text}

وظیفه شما:
تنها و تنها یک شعر کوتاه, خلاقانه و کامل بر اساس پرامپت اولیه و بازخوردهای احتمالی بسرایید.
به هیچ وجه از توضیحات, مقدمه, عنوان یا هر متن اضافی دیگری به جز خود شعر استفاده نکنید.
شعر باید روان و قابل فهم باشد.
"""
    # یک پاکسازی نهایی روی کل پرامپت برای اطمینان (اگرچه متغیرها قبلاً پاکسازی شده‌اند)
    final_prompt = final_prompt.replace('،', ',')

    try:
        # ارسال پرامپت به مدل
        response = model.generate_content(final_prompt)
        # پاکسازی متن پاسخ از ویرگول فارسی قبل از بازگرداندن
        return response.text.strip().replace('،', ',')
    except Exception as e:
        # چاپ خطا در صورت بروز مشکل
        print(f"Error in MotherModel: {e}", file=sys.stderr)
        return None

if __name__ == "__main__":
    # بررسی اینکه آیا اسکریپت با آرگومان‌های کافی اجرا شده است
    if len(sys.argv) > 1:
        input_prompt_arg = sys.argv[1]
        # دریافت بازخورد اگر به عنوان آرگومان دوم ارسال شده باشد
        feedback_arg = sys.argv[2] if len(sys.argv) > 2 else ""

        # پاکسازی آرگومان‌های دریافت شده از خط فرمان از ویرگول فارسی
        sanitized_input_prompt_arg = input_prompt_arg.replace('،', ',')
        sanitized_feedback_arg = feedback_arg.replace('،', ',')

        # فراخوانی تابع تولید شعر با آرگومان‌های پاکسازی شده
        poem = generate_poem(sanitized_input_prompt_arg, sanitized_feedback_arg)
        
        # اگر شعری تولید شد، آن را چاپ کن
        if poem:
            # شعر بازگشتی از generate_poem قبلاً پاکسازی شده است
            print(poem)
    else:
        # چاپ راهنمای استفاده در صورت عدم ارسال آرگومان‌های کافی
        print("Usage: python MotherModel.py \"<initial_prompt>\" [\"<feedback>\"]", file=sys.stderr)
