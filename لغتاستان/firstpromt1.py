import random
import os
import sys

def get_random_word_from_mysql():
    """
    استفاده از randreader.py برای گرفتن کلمه تصادفی
    """
    try:
        mysql_path = os.path.join(os.getcwd(), 'mysql')
        if mysql_path not in sys.path:
            sys.path.append(mysql_path)
        
        from randreader import get_random_word
        result = get_random_word()
        if result['success']:
            return result['word'].strip()
        else:
            fallback_words = ["آفتاب"]
            return random.choice(fallback_words)
    except:
        fallback_words = ["آسایش"]
        return random.choice(fallback_words)

def create_dobeiti_request():
    """
    رویکرد جدید برای ساخت درخواست دوبیتی - بر اساس الگوهای معنایی
    """
    
    # دریافت کلمات تصادفی
    inspiration_words = []
    for _ in range(random.randint(1, 5)):
        word = get_random_word_from_mysql()
        if word and word not in inspiration_words:
            inspiration_words.append(word)
    
    # پترن‌های مختلف شروع پرامپت
    opening_patterns = [
        "لطفاً برایم", "میشه", "دوست دارم", "امکانش هست که",
        "خواهش می‌کنم", "اگر ممکنه", "می‌تونی", "کمکم کن تا"
    ]
    
    # انواع مختلف اشاره به دوبیتی
    dobeiti_references = [
        "یک دوبیتی زیبا", "دوبیتی پرمعنا", "دوبیتی دلنشین", "رباعی‌ای",
        "شعری چهار مصرعی", "بیتی در چهار سطر", "دوبیتی‌ای عاشقانه",
        "یک قطعه شاعرانه", "دوبیتی با مضمون عمیق", "رباعی‌ای حکیمانه"
    ]
    
    # روش‌های مختلف درخواست سرودن
    creation_methods = [
        "بسرایی", "خلق کنی", "بنویسی", "تحریر کنی", "رقم بزنی",
        "نظم کنی", "آفریده شود", "ساخته شود", "پرداخته شود",
        "به وجود آوری", "انشا کنی", "بیافرینی"
    ]
    
    # عمق و کیفیت مطلوب
    quality_descriptors = [
        "که دل را لرزاند", "که جان را نوازد", "که روح را آرام دهد",
        "با عمق بالا", "با معنای ژرف", "با مفهوم عمیق", "پرمغز و پربار",
        "که خاطره‌انگیز باشد", "که تأثیرگذار باشد", "که ماندگار باشد",
        "با زیبایی خاص", "با ظرافت تمام", "با لطافت بی‌نظیر"
    ]
    
    # محیط و فضای شعر
    atmosphere_settings = [
        "در فضای رؤیایی", "با حال و هوای شاعرانه", "در قالب تصویری",
        "با فضاسازی زیبا", "در محیط طبیعی", "با پس‌زمینه عاطفی",
        "در بستر تاریخی", "با رنگ و بوی محلی", "در قاب خاطرات",
        "با نگاه نوستالژیک", "در حالت تأملی", "با روحیه امیدوارانه"
    ]
    
    # سبک‌های بیان
    expression_styles = [
        "به شکل نمادین", "با زبان استعاری", "به روش تلمیحی",
        "با کنایه‌های ظریف", "به صورت مبهم و رمزی", "با وضوح تمام",
        "به سبک کلاسیک", "با طعم مدرن", "در قالب سنتی",
        "با نوآوری در بیان", "به شیوه عامیانه", "با لحن فصیح"
    ]
    
    # عناصر موسیقایی
    musical_elements = [
        "با آهنگ دلپذیر", "با ریتم آرام", "با موزون بودن خاص",
        "با هماهنگی صوتی", "با وزن مناسب", "با ترنم زیبا",
        "با قافیه‌بندی جذاب", "با ردیف مؤثر", "با واج‌آرایی هنرمندانه"
    ]
    
    # محتوا و مضمون
    content_themes = [
        "درباره رمز زندگی", "در وصف زیبایی", "راجع به عشق ناب",
        "پیرامون حکمت", "درمورد گذر زمان", "راجع به طبیعت سرسبز",
        "درباره احساسات انسانی", "در مورد معنای هستی", "راجع به دوستی",
        "درباره آرزوها", "در وصف خاطرات شیرین", "راجع به امید و آینده"
    ]
    
    # ساختار و شکل
    structural_patterns = [
        "در قالب سوال و جواب", "با شروع قدرتمند", "با پایان تأثیرگذار",
        "با حلقه معنایی", "به شکل مکالمه", "در قالب توصیف",
        "با ترتیب زمانی", "به صورت مقایسه‌ای", "با ساختار متقارن"
    ]
    
    # تأثیرات فرهنگی
    cultural_flavors = [
        "با عطر تاریخ ایران", "با طعم فرهنگ اصیل", "با رنگ بومی",
        "با نکهت سنتی", "با روح ملی", "با هویت ایرانی",
        "با مضامین کلاسیک", "با ریشه در فولکلور", "با پیوند به اصالت"
    ]
    
    # الگوهای ترکیبی پیچیده
    def create_complex_pattern():
        """ایجاد الگوهای پیچیده‌تر با ترکیب چندین عنصر"""
        patterns = []
        
        # الگوی شرطی
        if random.random() < 0.3:
            conditions = [
                "طوری که", "به گونه‌ای که", "چنان که", "بطوری که",
                "به نحوی که", "به شکلی که"
            ]
            effects = [
                "خواننده متأثر شود", "احساسات برانگیخته شود", "تصویری ذهنی بسازد",
                "خاطره‌ای زنده شود", "حس نوستالژی پیدا کند", "درونش لرزید"
            ]
            patterns.append(f"{random.choice(conditions)} {random.choice(effects)}")
        
        # الگوی مقایسه‌ای
        if random.random() < 0.25:
            comparisons = [
                "همچون شعرای بزرگ", "مانند استادان قدیم", "چون نوای چوپان",
                "مثل زمزمه عاشقان", "همانند نجوای درویش", "چون آواز بلبل"
            ]
            patterns.append(random.choice(comparisons))
        
        return patterns
    
    # شروع ساخت پرامپت با رویکرد جدید
    def build_layered_prompt():
        """ساخت پرامپت با لایه‌های مختلف معنایی"""
        
        # لایه اول: درخواست اولیه
        base_request = f"{random.choice(opening_patterns)} {random.choice(dobeiti_references)} {random.choice(creation_methods)}"
        
        # لایه دوم: کیفیت و خصوصیت
        quality_layer = random.choice(quality_descriptors)
        
        # لایه سوم: محتوا و کلمات کلیدی
        content_layer = ""
        if inspiration_words and random.random() < 0.8:
            if len(inspiration_words) == 1:
                content_layer = f"که در آن از کلمه '{inspiration_words[0]}' الهام گرفته شده"
            else:
                word_list = "، ".join(inspiration_words[:-1]) + " و " + inspiration_words[-1]
                content_layer = f"با الهام از کلمات {word_list}"
        
        # لایه چهارم: مضمون اصلی
        theme_layer = ""
        if random.random() < 0.7:
            theme_layer = random.choice(content_themes)
        
        # لایه پنجم: سبک و شیوه
        style_layer = ""
        if random.random() < 0.6:
            chosen_styles = []
            if random.random() < 0.4:
                chosen_styles.append(random.choice(expression_styles))
            if random.random() < 0.3:
                chosen_styles.append(random.choice(musical_elements))
            if random.random() < 0.25:
                chosen_styles.append(random.choice(atmosphere_settings))
            
            if chosen_styles:
                style_layer = " و ".join(chosen_styles)
        
        # لایه ششم: ساختار
        structure_layer = ""
        if random.random() < 0.4:
            structure_layer = random.choice(structural_patterns)
        
        # لایه هفتم: عناصر فرهنگی
        culture_layer = ""
        if random.random() < 0.3:
            culture_layer = random.choice(cultural_flavors)
        
        # لایه هشتم: الگوهای پیچیده
        complex_layer = ""
        if random.random() < 0.35:
            complex_patterns = create_complex_pattern()
            if complex_patterns:
                complex_layer = " ".join(complex_patterns)
        
        # ترکیب لایه‌ها
        layers = [base_request, quality_layer, content_layer, theme_layer, 
                 style_layer, structure_layer, culture_layer, complex_layer]
        
        # حذف لایه‌های خالی و ترکیب
        active_layers = [layer for layer in layers if layer.strip()]
        
        # استفاده از کلمات ربط مختلف
        connectors = ["،", " که", " و", " ضمناً", " همچنین", " در ضمن", " علاوه بر این"]
        
        final_prompt = active_layers[0]
        for i, layer in enumerate(active_layers[1:], 1):
            if i < len(active_layers) - 1:
                connector = random.choice(connectors)
                final_prompt += f"{connector} {layer}"
            else:
                final_prompt += f" و {layer}"
        
        return final_prompt
    
    return build_layered_prompt()

def generate_narrative_dobeiti_request():
    """
    روش داستانی برای ساخت درخواست دوبیتی
    """
    
    # شخصیت‌ها و حالات
    characters = [
        "عاشق دلشکسته", "مسافر غریب", "کودک معصوم", "پیرمرد حکیم",
        "دختر جوان", "شاعر تنها", "درویش سالک", "مادر مهربان"
    ]
    
    situations = [
        "در شب تاریک", "زیر نور ماه", "کنار رودخانه", "در کوچه‌های قدیمی",
        "بر فراز کوه", "در باغ پر از گل", "در خانه خالی", "پای درخت کهنسال"
    ]
    
    emotions = [
        "غم عمیق", "شادی بی‌پایان", "حسرت سوزان", "امید نوپا",
        "عشق پاک", "دلتنگی شدید", "آرامش عجیب", "هیجان ملایم"
    ]
    
    # ساخت داستان کوتاه
    character = random.choice(characters)
    situation = random.choice(situations)
    emotion = random.choice(emotions)
    
    narrative_prompts = [
        f"تصور کن {character} {situation} نشسته و {emotion} دارد. حالا برای این صحنه دوبیتی بساز",
        f"داستان {character} را به خاطر بیاور که {situation} با {emotion} روبرو شده. این حس را در دوبیتی بگنجان",
        f"فکر کن {character} {situation} قدم می‌زند و {emotion} وجودش را فرا گرفته. این لحظه را شعر کن"
    ]
    
    return random.choice(narrative_prompts)

def create_metaphorical_request():
    """
    درخواست بر اساس استعاره و تشبیه
    """
    
    elements_a = ["زندگی", "عشق", "زمان", "خاطره", "امید", "غم", "شادی"]
    elements_b = ["رودخانه", "باد", "آتش", "گل", "ستاره", "مرغ", "دریا"]
    
    metaphor_patterns = [
        f"اگر {random.choice(elements_a)} مثل {random.choice(elements_b)} باشد، دوبیتی‌ای بساز که این تشبیه را نشان دهد",
        f"در دوبیتی نشان بده که {random.choice(elements_a)} و {random.choice(elements_b)} چه شباهتی دارند",
        f"با استعاره از {random.choice(elements_b)} درباره {random.choice(elements_a)} شعر بگو"
    ]
    
    return random.choice(metaphor_patterns)

def generate_enhanced_dobeiti_prompt():
    """
    تولیدکننده نهایی با انتخاب از روش‌های مختلف
    """
    
    method_choice = random.randint(1, 10)
    
    if method_choice <= 6:
        return create_dobeiti_request()
    elif method_choice <= 8:
        return generate_narrative_dobeiti_request()
    else:
        return create_metaphorical_request()

# تابع اصلی
def main():
    """تابع اصلی که پرامپت متفاوت تولید می‌کند"""
    prompt = generate_enhanced_dobeiti_prompt()
    print(prompt)

if __name__ == "__main__":
    main()
