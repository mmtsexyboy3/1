import random
import os
import sys

def get_random_word_from_mysql():
    """
    استفاده از randreader.py برای گرفتن کلمه تصادفی
    """
    try:
        # تلاش برای import از mysql directory
        mysql_path = os.path.join(os.getcwd(), 'mysql')
        if mysql_path not in sys.path:
            sys.path.append(mysql_path)
        
        from randreader import get_random_word
        result = get_random_word()
        if result['success']:
            return result['word'].strip()
        else:
            fallback_words = ["گل"]
            return random.choice(fallback_words)
    except:
        fallback_words = ["زندگی"]
        return random.choice(fallback_words)

def generate_ultimate_dobeiti_prompt():
    """
    تولیدکننده نهایی و قدرتمند درخواست دوبیتی بدون باگ
    """
    
    # تولید تعداد تصادفی کلمات (1 تا 3)
    word_count = random.randint(1, 3)
    
    # گرفتن کلمات تصادفی (بدون تکرار)
    random_words = []
    used_words = set()
    
    for _ in range(word_count):
        attempts = 0
        while attempts < 10:  # جلوگیری از حلقه بی‌نهایت
            word = get_random_word_from_mysql()
            if word and word not in used_words:
                random_words.append(word)
                used_words.add(word)
                break
            attempts += 1
        
        if len(random_words) < len(used_words) + 1:
            # اگر نتونست کلمه جدید پیدا کنه، از لیست پشتیبان استفاده کن
            backup_words = ["گل", "عشق", "آسمان", "دریا", "ستاره", "نور", "شب", "روز", "باد", "خاک"]
            available_backup = [w for w in backup_words if w not in used_words]
            if available_backup:
                word = random.choice(available_backup)
                random_words.append(word)
                used_words.add(word)
    
    # آرایه‌ها (بدون دری و تاجیکی)
    language_variants = [
        "فارسی", "پارسی",
        "به زبان فارسی", "با زبان فارسی", "با زبان پارسی",
        "با زبان شیرین فارسی", "با زبان شیرین و جالب فارسی",
        "به سبک کلاسیک فارسی", "با لحن شاعرانه فارسی",
        "به شیوه باستانی پارسی", "با قالب سنتی فارسی",
        "به نثر شاعرانه فارسی", "با واژگان کهن فارسی",
        "با لسان عذب فارسی", "به زبان گهربار فارسی",
        "با لهجه شیراز", "به گویش اصفهان", "با لحن تبریز",
        "به سبک هندی فارسی", "با شیوه عراقی فارسی",
        "با زبان ملیح فارسی", "به لسان فصیح فارسی"
    ]
    
    literary_styles = [
        "تشبیه", "استعاره", "کنایه", "تلمیح", "ایهام", "تجرید", "تشخیص",
        "حسن تعلیل", "مبالغه", "تضاد", "طباق", "مقابله", "جناس", "تجنیس",
        "سجع", "قافیه داخلی", "ردیف", "لف و نشر", "عکس و تنسیک",
        "رد العجز الی الصدر", "تورق", "تشریع", "ترکیب", "تقسیم",
        "تعمیم و تخصیص", "احتراس", "ایغال", "اطناب", "ایجاز", "اختصار",
        "تکرار", "ترصیع", "توشیح", "تضمین", "تخلص", "قفل و کلید",
        "دور بر دور", "معما", "لغز", "چیستان", "حسن ابتدا", "حسن انتها",
        "مراعات النظیر", "تشطیر", "تصریع", "ترخیم", "تصغیر"
    ]
    
    request_verbs = [
        "بساز", "بسرود", "ایجاد کن", "بنویس", "خلق کن", "تولید کن",
        "آفرین", "پدید آور", "بنا کن", "تراش", "بافت کن", "درهم کن",
        "رقم بزن", "نظم کن", "سراید", "پرداز", "برآور", "انشا کن",
        "قرض کن", "وضع کن", "بر تار و پود بکش", "از نو بساز",
        "به نظم درآور", "بیافرین", "بپرداز", "برقص", "بتراش"
    ]
    
    # موضوعات با "با موضوع"
    themes_with_prefix = [
        "با موضوع عشق", "با موضوع طبیعت", "با موضوع حکمت", "با موضوع فلسفه",
        "با موضوع عرفان", "با موضوع زندگی", "با موضوع مرگ", "با موضوع زمان",
        "با موضوع جدایی", "با موضوع وصال", "با موضوع آرزو", "با موضوع امید",
        "با موضوع یأس", "با موضوع سفر", "با موضوع خاطره", "با موضوع بهار",
        "با موضوع پاییز", "با موضوع شب", "با موضوع صبح", "با موضوع کودکی",
        "با موضوع پیری", "با موضوع دوستی", "با موضوع تنهایی", "با موضوع نوستالژی",
        "با موضوع غربت", "با موضوع وطن", "با موضوع مادر", "با موضوع پدر",
        "با موضوع معشوق", "با موضوع دین", "با موضوع اخلاق", "با موضوع حرف و نصیحت"
    ]
    
    dobeiti_word_counts = [
        "بیست کلمه", "بیست و پنج کلمه", "سی کلمه", "سی و پنج کلمه",
        "چهل کلمه", "چهار مصرع", "یک بند چهار سطری", "یک دوبیتی کامل",
        "دوبیتی در چهار سطر", "رباعی کوتاه", "یک قطعه کامل"
    ]
    
    dobeiti_meters = [
        "هزج مثمن محذوف", "رجز مثمن", "متقارب مثمن محذوف",
        "هزج مسدس", "رمل مسدس", "کامل مسدس", "وافر مسدس"
    ]
    
    dobeiti_poets = [
        "خیام", "رودکی", "باباطاهر", "شهریار", "حافظ شیرازی",
        "سعدی شیرازی", "ابوسعید ابوالخیر", "عطار نیشاپوری",
        "مولانا", "فردوسی", "نظامی", "جامی"
    ]
    
    emotional_tones = [
        "غمناک", "شاد", "عاشقانه", "حماسی", "تأملی", "عرفانی", "طنز",
        "هجو", "مدح", "تشویق", "انتقادی", "اجتماعی", "ملی", "مذهبی",
        "فلسفی", "حکمی", "وعظی", "اخلاقی", "نصیحت‌آمیز", "تعلیمی",
        "داستانی", "تمثیلی", "رمزی", "عبرت‌آموز"
    ]
    
    special_combinations = [
        "با ترکیب چند سبک", "با آمیختن چندین آرایه", "با تداخل معنایی",
        "با لایه‌های مختلف تفسیری", "با رمز و راز عمیق", "با معنای ظاهری و باطنی",
        "با پیچیدگی معنایی", "با عمق فلسفی"
    ]
    
    dobeiti_features = [
        "با مطلع گیرا", "با مقطع تأثیرگذار", "با قافیه داخلی", "با واج‌آرایی خاص",
        "با ردیف یکسان", "با تکرار کلیدی", "با حلقه معنایی", "با بازگشت به آغاز",
        "با انتهای باز", "با پایان تأملی"
    ]
    
    rhyme_patterns = [
        "با قافیه عین", "با قافیه میم", "با قافیه دال", "با قافیه لام",
        "با قافیه نون", "با قافیه راء", "با قافیه سین", "با قافیه تاء"
    ]
    
    structures = [
        "با ساختار حلقوی", "با معنای دوگانه", "با رمز نهان", "با پیام مستتر",
        "با ترکیب زمان", "با فضای خیالی"
    ]
    
    time_elements = [
        "در زمان حال", "با نگاه به گذشته", "با چشم‌انداز آینده",
        "با ترکیب زمان‌ها", "در لحظه کنونی"
    ]
    
    cultural_aspects = [
        "با رنگ محلی", "با طعم سنتی", "با عطر تاریخی", "با فرهنگ بومی",
        "با سنت کهن", "با مضامین ایرانی"
    ]
    
    # شروع ساخت پرامپت
    prompt_parts = []
    
    # فعل درخواست (همیشه)
    chosen_verb = random.choice(request_verbs)
    prompt_parts.append(chosen_verb)
    
    # دوبیتی (همیشه)
    prompt_parts.append("دوبیتی")
    
    # زبان (همیشه)
    chosen_language = random.choice(language_variants)
    prompt_parts.append(chosen_language)
    
    # موضوع (احتمال 70%)
    if random.random() < 0.70:
        chosen_theme = random.choice(themes_with_prefix)
        prompt_parts.append(chosen_theme)
    
    # کلمات تصادفی (احتمال 65% و فقط اگر کلمه داریم)
    if random.random() < 0.65 and random_words:
        # تشخیص تعداد کلمات برای استفاده صحیح از "کلمه" یا "کلمات"
        if len(random_words) == 1:
            word_phrase = f"که شامل کلمه {random_words[0]} باشد"
        else:
            word_phrase = f"که شامل کلمات {', '.join(random_words)} باشد"
        
        # انواع مختلف برای بیان کلمات
        word_integration_methods = [
            word_phrase,
            f"با استفاده از واژگان {', '.join(random_words)}" if len(random_words) > 1 else f"با استفاده از واژه {random_words[0]}",
            f"که در آن کلمات {', '.join(random_words)} بکار رود" if len(random_words) > 1 else f"که در آن کلمه {random_words[0]} بکار رود",
            f"با محوریت کلمات {', '.join(random_words)}" if len(random_words) > 1 else f"با محوریت کلمه {random_words[0]}",
            f"که {', '.join(random_words)} در آن نهفته باشد" if len(random_words) > 1 else f"که {random_words[0]} در آن نهفته باشد"
        ]
        prompt_parts.append(random.choice(word_integration_methods))
    
    # سبک ادبی اصلی (احتمال 75%)
    if random.random() < 0.75:
        primary_style = random.choice(literary_styles)
        style_phrases = [
            f"با آرایه {primary_style}",
            f"به شیوه {primary_style}",
            f"با بکارگیری {primary_style}",
            f"با تکیه بر {primary_style}"
        ]
        prompt_parts.append(random.choice(style_phrases))
    
    # سبک‌های متعدد (احتمال 40%)
    if random.random() < 0.40:
        num_styles = random.randint(2, 4)
        multiple_styles = random.sample(literary_styles, min(num_styles, len(literary_styles)))
        combination_phrases = [
            f"با آرایه‌های {' و '.join(multiple_styles)}",
            f"با ترکیب {' و '.join(multiple_styles)}",
            f"با آمیختن {' و '.join(multiple_styles)}"
        ]
        prompt_parts.append(random.choice(combination_phrases))
    
    # بحر شعری (احتمال 35%)
    if random.random() < 0.35:
        chosen_meter = random.choice(dobeiti_meters)
        prompt_parts.append(f"در بحر {chosen_meter}")
    
    # سبک شاعر (احتمال 30%)
    if random.random() < 0.30:
        chosen_poet = random.choice(dobeiti_poets)
        poet_phrases = [
            f"به سبک {chosen_poet}",
            f"به شیوه {chosen_poet}",
            f"در قالب {chosen_poet}"
        ]
        prompt_parts.append(random.choice(poet_phrases))
    
    # لحن احساسی (احتمال 25%)
    if random.random() < 0.25:
        chosen_tone = random.choice(emotional_tones)
        prompt_parts.append(f"با لحن {chosen_tone}")
    
    # ویژگی خاص دوبیتی (احتمال 20%)
    if random.random() < 0.20:
        chosen_feature = random.choice(dobeiti_features)
        prompt_parts.append(chosen_feature)
    
    # ترکیب پیچیده (احتمال 18%)
    if random.random() < 0.18:
        chosen_combination = random.choice(special_combinations)
        prompt_parts.append(chosen_combination)
    
    # قافیه خاص (احتمال 15%)
    if random.random() < 0.15:
        chosen_rhyme = random.choice(rhyme_patterns)
        prompt_parts.append(chosen_rhyme)
    
    # ساختار خاص (احتمال 12%)
    if random.random() < 0.12:
        chosen_structure = random.choice(structures)
        prompt_parts.append(chosen_structure)
    
    # المان زمانی (احتمال 10%)
    if random.random() < 0.10:
        chosen_time = random.choice(time_elements)
        prompt_parts.append(chosen_time)
    
    # جنبه فرهنگی (احتمال 8%)
    if random.random() < 0.08:
        chosen_culture = random.choice(cultural_aspects)
        prompt_parts.append(chosen_culture)
    
    # تعداد کلمات نهایی (بالای 8 از 10)
    final_word_random = random.randint(0, 10)
    if final_word_random > 8:
        chosen_word_count = random.choice(dobeiti_word_counts)
        final_phrases = [
            f"در نهایت {chosen_word_count} تحویل بده",
            f"در حجم {chosen_word_count} ارائه کن",
            f"به اندازه {chosen_word_count} بنویس"
        ]
        prompt_parts.append(random.choice(final_phrases))
    
    # ترکیب نهایی
    final_prompt = " ".join(prompt_parts)
    
    return final_prompt

# تابع اصلی برای استفاده
def main():
    """تابع اصلی که فقط پرامپت را چاپ می‌کند"""
    prompt = generate_ultimate_dobeiti_prompt()
    print(prompt)

if __name__ == "__main__":
    main()
