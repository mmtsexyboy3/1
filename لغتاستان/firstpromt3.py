

import random
import os
import sys
from datetime import datetime

# تابع دریافت کلمه تصادفی (مشابه نسخه‌های قبلی)
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
            # لیست پشتیبان اول در صورت عدم موفقیت randreader
            fallback_words = ["گوهر", "راز", "سکوت", "فریاد", "پرواز", "آینه", "خاکستر", "شراب", "جام", "ساقی"]
            return random.choice(fallback_words)
    except Exception as e:
        # print(f"Error in get_random_word_from_mysql: {e}") # برای دیباگ
        # لیست پشتیبان دوم در صورت بروز خطا در import یا اجرای randreader
        fallback_words = ["نقطه", "دایره", "خط", "نقش", "خیال", "وهم", "یقین", "سؤال", "جواب", "حکایت"]
        return random.choice(fallback_words)

class AlchemicalPoetryEngine:
    """
    موتور کیمیاگرانه تولید درخواست دوبیتی، با تمرکز بر شهود و فرآیند خلاق
    """
    def __init__(self):
        self.philosophical_essences = self._load_philosophical_essences()
        self.sensory_palettes = self._define_sensory_palettes()
        self.transformative_processes = self._list_transformative_processes()
        self.elemental_forces = self._identify_elemental_forces()
        self.poetic_personas = self._imagine_poetic_personas()

    def _load_philosophical_essences(self):
        """بارگذاری جوهرهای فلسفی و عرفانی"""
        return {
            'وحدت': ['یگانگی', 'اتحاد', 'همسویی', 'یکی شدن'],
            'کثرت': ['تنوع', 'تجلی', 'هزار آیینه', 'بازتاب‌ها'],
            'زمان': ['گذر', 'لحظه ابدی', 'بی‌زمانی', 'خاطره'],
            'مکان': ['لامکان', 'ناکجاآباد', 'درون', 'بیرون'],
            'عشق_عرفانی': ['سوز', 'جذبه', 'فنا', 'وصل'],
            'جستجو': ['طلب', 'سیر و سلوک', 'پرسشگری', 'کشف'],
            'زیبایی_باطنی': ['جمال درون', 'نور حقیقت', 'صفای دل', 'سیرت نیکو'],
            'تضاد_و_هماهنگی': ['شب و روز', 'ظلمت و نور', 'سکوت و فریاد', 'جمع اضداد']
        }

    def _define_sensory_palettes(self):
        """تعریف پالت‌های حسی برای غنی‌سازی شعر"""
        return {
            'نور_و_تاریکی': ['درخشش مهتاب', 'سوسوی ستاره', 'عمق شب', 'اولین پرتو فجر'],
            'صدا_و_سکوت': ['نجوای باد', 'سکوت کویر', 'آوای دوردست', 'همهمه درون'],
            'بافت_و_لمس': ['نرمی حریر', 'زبری سنگ', 'گرمای آتش', 'سردی برف'],
            'رایحه_و_طعم': ['عطر گل سرخ', 'بوی خاک باران‌خورده', 'طعم گس انتظار', 'شیرینی وصال'],
            'حرکت_و_سکون': ['رقص سایه‌ها', 'ایستایی کوه', 'جریان رود', 'آرامش برکه']
        }

    def _list_transformative_processes(self):
        """فهرست کردن فرآیندهای دگرگون‌ساز در کیمیای شعر"""
        return [
            "تقطیر کن", "ذوب کن", "متبلور ساز", "صیقل بده",
            "در هم بیامیز", "از هم جدا کن", "به آتش بکش", "در آب فرو بر",
            "بپالا", "تخمیر کن", "تصعید نما", "رسوب بده"
        ]

    def _identify_elemental_forces(self):
        """شناسایی نیروهای عنصری در شعر"""
        return ['آتش درون', 'آب روان اندیشه', 'خاک وجود', 'باد خیال', 'اثیری از الهام']

    def _imagine_poetic_personas(self):
        """تصور پرسوناها یا نقاب‌های شاعرانه"""
        return [
            "از زبان یک سالک در جستجوی حقیقت",
            "همچون یک ستاره‌شناس کهن که راز آسمان‌ها را می‌جوید",
            "مانند یک کیمیاگر در آزمایشگاه اسرارآمیزش",
            "به روایت یک قصه‌گوی شب‌های کویری",
            "از دید یک نقاش که با نور و سایه بازی می‌کند",
            "با صدای یک موسیقی‌دان که سکوت را به نت تبدیل می‌کند"
        ]

    def _get_alchemical_inspiration(self):
        """دریافت الهام کیمیاگرانه"""
        core_essence_name = random.choice(list(self.philosophical_essences.keys()))
        core_essence_terms = random.sample(self.philosophical_essences[core_essence_name], random.randint(1,2))
        
        sensory_palette_name = random.choice(list(self.sensory_palettes.keys()))
        sensory_details = random.sample(self.sensory_palettes[sensory_palette_name], random.randint(1,2))
        
        return {
            'essence_name': core_essence_name,
            'essence_terms': core_essence_terms,
            'sensory_palette_name': sensory_palette_name,
            'sensory_details': sensory_details,
            'transformative_process': random.choice(self.transformative_processes),
            'elemental_force': random.choice(self.elemental_forces),
            'persona': random.choice(self.poetic_personas) if random.random() < 0.5 else None
        }

    def create_alchemical_prompt(self):
        """تولید پرامپت دوبیتی با رویکرد کیمیاگرانه"""
        
        # دریافت کلمات پایه (مواد اولیه کیمیاگری)
        raw_materials = []
        for _ in range(random.randint(1, 3)):
            word = get_random_word_from_mysql()
            if word:
                raw_materials.append(word)
        
        if not raw_materials: # اگر هیچ کلمه‌ای از mysql نیامد
            raw_materials.append(random.choice(["هستی", "نیستی", "جان"]))

        inspiration = self._get_alchemical_inspiration()
        
        prompt_parts = []

        # سرآغاز: دعوت به کیمیاگری
        openings = [
            "ای کیمیاگر واژه‌ها،", "ای صنعتگر خیال،", "ای معمار لحظه‌های ناب،",
            "در کارگاه اندیشه‌ات،", "با آتش درون و جوهر جان،"
        ]
        prompt_parts.append(random.choice(openings))

        # معرفی مواد اولیه
        if raw_materials:
            material_intro = f"این عناصر خام را: «{ ' »، «'.join(raw_materials) }»"
            prompt_parts.append(material_intro)
        
        # درخواست دوبیتی
        prompt_parts.append(f"{inspiration['transformative_process']} و از آن دوبیتی‌ای بیافرین")

        # جوهر فلسفی
        essence_phrase = f"که حامل جوهر «{inspiration['essence_name']}» باشد و مفاهیمی چون «{ '» و «'.join(inspiration['essence_terms']) }» را در خود بپروراند."
        prompt_parts.append(essence_phrase)

        # پالت حسی
        sensory_phrase = f"بگذار این شعر با «{ '» و «'.join(inspiration['sensory_details']) }» از پالت حسی «{inspiration['sensory_palette_name']}» جان بگیرد."
        prompt_parts.append(sensory_phrase)
        
        # نیروی عنصری
        elemental_force_phrase = f"و بگذار «{inspiration['elemental_force']}» در تار و پود آن جاری شود."
        prompt_parts.append(elemental_force_phrase)

        # پرسونای شاعرانه (اختیاری)
        if inspiration['persona']:
            prompt_parts.append(f"این دوبیتی را {inspiration['persona']} بسرای.")

        # چالش یا ویژگی خاص (اختیاری، با الهام از رویکردهای قبلی)
        if random.random() < 0.3:
            challenges = [
                "با پایانی شگفت‌انگیز و تأمل‌برانگیز.",
                "چنانکه هر مصرع، دریچه‌ای به دنیایی دیگر بگشاید.",
                "با تضادی ظریف میان ظاهر و باطن.",
                "به گونه‌ای که سکوت میان واژه‌ها، خود سخن بگوید.",
                "با استفاده از یک استعاره مرکزی که تمام شعر را به هم پیوند دهد."
            ]
            prompt_parts.append(random.choice(challenges))

        # پایان‌بندی: انتظار برای نتیجه
        closings = [
            "منتظر تجلی این کیمیای سخن هستم.",
            "ببینم چگونه از این عناصر، گوهری جاودان می‌سازی.",
            "هنر خود را در این آفرینش به نمایش بگذار."
        ]
        prompt_parts.append(random.choice(closings))
        
        return " ".join(prompt_parts)


def generate_alchemical_dobeiti_request():
    """
    تولیدکننده نهایی با رویکرد کیمیاگرانه
    """
    engine = AlchemicalPoetryEngine()
    return engine.create_alchemical_prompt()

# تابع اصلی
def main():
    """تابع اصلی رویکرد کیمیاگرانه"""
    prompt = generate_alchemical_dobeiti_request()
    print(prompt)

if __name__ == "__main__":
    main()


