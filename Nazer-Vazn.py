import google.generativeai as genai
import random
import sys

API_KEYS = ['AIzaSyC7Fg3tK1kXdRVwgAnxkjsBsxwzKPvhRhQ', 'AIzaSyD-0pEtICuBgcTkuHfLSFey5RVumSHRgbg']
MODEL_NAME = "gemini-1.5-pro-latest"

def configure_model():
    api_key = random.choice(API_KEYS)
    genai.configure(api_key=api_key)
    return genai.GenerativeModel(MODEL_NAME)

def review_poem_vazn(poem_text):
    model = configure_model()
    prompt = f"""
شعر زیر برای بررسی وزن و قافیه به شما ارائه شده است:
---
{poem_text}
---
وظیفه: این شعر را از منظر وزن عروضی (در صورت تطابق با اوزان کلاسیک) یا آهنگ و ریتم (در شعر نو) و همچنین کیفیت و سلامت قافیه‌ها و ردیف (در صورت وجود) بررسی کنید.
خروجی: نظر خود را بسیار کوتاه، دقیق و مستقیم در یک یا دو جمله بیان کنید.
مثال: "وزن شعر در اکثر ابیات روان است اما در بیت سوم سکته دارد. قافیه‌ها نو و مناسب هستند."
مثال دیگر: "آهنگ کلی شعر دلنشین است، اما برخی مصراع‌ها از نظر طول و ضرباهنگ با بقیه هماهنگ نیستند."
"""
    try:
        response = model.generate_content(prompt.format(poem_text=poem_text))
        return response.text.strip()
    except Exception as e:
        print(f"Error in Nazer-Vazn: {e}", file=sys.stderr)
        return "خطا در پردازش ناظر وزن."

if __name__ == "__main__":
    if len(sys.argv) > 1:
        poem_to_review = sys.argv[1]
        review = review_poem_vazn(poem_to_review)
        print(review)
    else:
        print("Usage: python Nazer-Vazn.py \"<poem_text>\"", file=sys.stderr)
