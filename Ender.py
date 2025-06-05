import google.generativeai as genai
import random
import sys

API_KEYS = ['AIzaSyC_9rs3SbUb7ZoR9X8qsuLKoAXoqYZPRTE', 'AIzaSyBy2qwvbA71tWM79Z3HL2pi11YzKfBJhwE']
MODEL_NAME = "gemini-2.0-flash" # وزیر اعظم باید مدل قدرتمندی باشد

def configure_model():
    api_key = random.choice(API_KEYS)
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)

def decide_on_poem(poem_text, nazer_feedbacks_str):
    model = configure_model()
    prompt = f"""
شما وزیر اعظم تصمیم‌گیرنده در مورد کیفیت نهایی اشعار هستید.
شعر ارائه شده:
---
{poem_text}
---
نظرات هیئت داوران (ناظران):
{nazer_feedbacks_str}
---
وظیفه: با سخت‌گیری تمام و با در نظر گرفتن تمام نظرات داوران، تصمیم نهایی خود را اعلام کنید.
قوانین تصمیم‌گیری:
1. اگر شعر ایرادات اساسی دارد یا اکثریت نظرات داوران منفی و مهم است، آن را قاطعانه رد کنید.
2. تنها در صورتی شعر را تایید کنید که از کیفیت بسیار بالایی برخوردار باشد و اکثر نظرات داوران مثبت بوده یا به اصلاحات جزئی و قابل رفع اشاره داشته باشند.
3. به دنبال شعری بی‌نقص یا نزدیک به بی‌نقص باشید.

خروجی شما باید یکی از دو فرمت زیر باشد، بدون هیچ توضیح اضافی:
الف) اگر شعر را تایید می‌کنید، فقط و فقط کلمه "ACCEPT" را بنویسید.
ب) اگر شعر را رد می‌کنید، با "REJECT" شروع کنید، سپس دلایل اصلی رد شدن و مهمترین پیشنهادها برای بهبود (بر اساس نظرات داوران و تشخیص خودتان) را در یک یا دو جمله کوتاه و بسیار دقیق بیان کنید.
مثال رد: "REJECT وزن شعر همچنان ایراد دارد و تصاویر خلق شده به اندازه کافی بدیع نیستند. روی ارتباط عمودی ابیات و انتخاب واژگان دقیق‌تر کار شود."
"""
    try:
        response = model.generate_content(prompt.format(poem_text=poem_text, nazer_feedbacks_str=nazer_feedbacks_str))
        return response.text.strip()
    except Exception as e:
        print(f"Error in Ender: {e}", file=sys.stderr)
        return "REJECT خطای داخلی در سیستم تصمیم‌گیری وزیر اعظم."

if __name__ == "__main__":
    if len(sys.argv) > 2:
        poem = sys.argv[1]
        feedbacks = sys.argv[2]
        decision = decide_on_poem(poem, feedbacks)
        print(decision)
    else:
        print("Usage: python Ender.py \"<poem_text>\" \"<nazer_feedbacks_combined>\"", file=sys.stderr)
