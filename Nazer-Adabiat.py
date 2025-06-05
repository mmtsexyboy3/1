import google.generativeai as genai
import random
import sys

API_KEYS = ['AIzaSyDXBwGP1rG2Kw_LOmiqUJtyi8a7aMqf8rA', 'AIzaSyBuhbkhvWUEeJxlGdpTdHV6f49lmwo4OBg'] # می‌توانید لیست کلیدهای متفاوتی برای هر ناظر داشته باشید
MODEL_NAME = "gemini-1.5-flash"

def configure_model():
    api_key = random.choice(API_KEYS)
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)

def review_poem(poem_text):
    model = configure_model()
    prompt = f"""
شعر زیر برای بررسی ادبی به شما ارائه شده است:
---
{poem_text}
---
وظیفه: این شعر را از منظر کیفیت ادبی، صنایع بدیع، انسجام معنایی، نوآوری و احساسات بررسی کنید.
خروجی: نظر خود را بسیار کوتاه، دقیق و مستقیم در یک یا دو جمله بیان کنید. از هیچ عبارت اضافی مانند "نظر من این است:" یا تمجیدهای کلیشه‌ای استفاده نکنید. مستقیماً به نقد یا تحسین جنبه‌های خاص بپردازید.
مثال نقد: "تصاویر تکراری هستند و قافیه‌ها قابل پیش‌بینی‌اند. نیاز به خلاقیت بیشتری در مضمون‌پردازی دارد."
مثال تحسین: "استفاده از استعاره‌ها نو و تاثیرگذار است. جریان احساسی شعر خواننده را درگیر می‌کند."
"""
    try:
        response = model.generate_content(prompt.format(poem_text=poem_text))
        return response.text.strip()
    except Exception as e:
        print(f"Error in Nazer-Adabiat: {e}", file=sys.stderr)
        return "خطا در پردازش ناظر ادبیات."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        poem_to_review = sys.argv[1]
        review = review_poem(poem_to_review)
        print(review)
    else:
        print("Usage: python Nazer-Adabiat.py \"<poem_text>\"", file=sys.stderr)
