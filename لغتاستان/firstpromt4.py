

import random
import os
import sys
from datetime import datetime

# تابع دریافت کلمه تصادفی (با لیست‌های پشتیبان تاریک‌تر)
def get_random_word_from_mysql():
    """
    استفاده از randreader.py برای گرفتن کلمه تصادفی با حال و هوای تاریک.
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
            fallback_words = ["زنجیر", "قفل", "سایه", "شب", "خون", "استخوان", "سکوت", "راز", "طلسم", "گور"]
            return random.choice(fallback_words)
    except Exception as e:
        # print(f"Error in get_random_word_from_mysql (dark): {e}") # برای دیباگ
        # لیست پشتیبان دوم در صورت بروز خطا
        fallback_words = ["وهم", "کابوس", "ترس", "نفرت", "یأس", "اندوه", "مرگ", "فنا", "زهر", "تیغ"]
        return random.choice(fallback_words)

class NocturnalForgeEngine:
    """
    موتور کارگاه شبانه برای تولید درخواست دوبیتی با رویکردی تاریک و چسبناک.
    """
    def __init__(self):
        self.shadow_essences = self._load_shadow_essences()
        self.umbral_palettes = self._define_umbral_palettes() # Umbral: سایه‌ای، تیره
        self.binding_rituals = self._list_binding_rituals()
        self.abyssal_currents = self._identify_abyssal_currents() # Abyssal: ژرف، عمیق، مربوط به مغاک
        self.whispering_voices = self._conceive_whispering_voices()

    def _load_shadow_essences(self):
        """بارگذاری جوهرهای سایه و مفاهیم ممنوعه"""
        return {
            'فقدان_و_پوچی': ['تهی', 'نیستی محض', 'خلاء سرد', 'بی‌معنایی آزاردهنده'],
            'راز_های_ممنوعه': ['دانش پنهان', 'اسرار دفن‌شده در چرم کهنه', 'حقیقت تلخ و چسبناک', 'کلام ناگفتنی'],
            'زوال_و_فرسایش': ['پوسیدگی تدریجی', 'کهنگی ابدی', 'فراموشی چسبنده', 'سایه مرگ بر هر چیز'],
            'وسوسه_و_گناه_پنهان': ['جاذبه تاریک و لزج', 'میل ممنوع و شیرین', 'عهد شکسته در سکوت', 'بار گناهی که به روح چسبیده'],
            'انعکاس_درون_تاریک': ['سایه خود که رها نمی‌کند', 'هیولای درون در بند چرمین', 'ترس‌های نهفته و چسبناک', 'زخم‌های پنهان و عفونی']
        }

    def _define_umbral_palettes(self):
        """تعریف پالت‌های حسی تاریک و چسبناک"""
        return {
            'لمس_چسبناک_و_سرد': ['چرم نم‌دیده و سرد', 'جوهر روان و چسبنده روی پوست', 'تار عنکبوت کهنه و غبارآلود', 'خون خشکیده بر فلز زنگ‌زده'],
            'نجواهای_فراموش_شده_در_تاریکی': ['زمزمه در دخمه‌های نمور', 'صدای خراشیدن ناخن بر چرم قدیمی', 'سکوت سنگین گورستان در مه', 'نفس‌های نامرئی در هوای راکد'],
            'مناظر_کابوس_وار_و_مه_آلود': ['سایه‌های رقصان در آتش کم‌سوی شمع', 'مه غلیظ بر مرداب متعفن', 'خرابه‌های فراموش‌شده زیر ماه خونین', 'چشم‌های درخشان در تاریکی مطلق'],
            'بوی_کهنگی_فساد_و_جوهر_خشکیده': ['بوی کتاب قدیمی نم‌کشیده و چرمین', 'عطر خاک مرطوب سرداب و جوهر خشکیده', 'رایحه خفیف گوگرد و غبار قرون', 'نفس سرداب و چرم در حال پوسیدن']
        }

    def _list_binding_rituals(self):
        """فهرست کردن آیین‌های بستن و حک کردن در کیمیای تاریک شعر"""
        return [
            "در جوهر شب بپیچان", "با نخ‌های سایه و رگه‌های خون بدوز", "در سکوت مطلق و چسبناک محبوس کن",
            "به زنجیر کش کلمات را", "طلسم کن با حروف کهنه", "داغ بزن بر پیکر هر مصرع",
            "حک کن بر لوح سنگی فراموشی", "در چرم سیاه و چسبنده جلد کن"
        ]

    def _identify_abyssal_currents(self):
        """شناسایی جریان‌های مغاکی و نیروهای زیرین در شعر"""
        return ['جریان سرد فراموشی ابدی', 'نبض تاریک زمین زیر پای مردگان', 'نفس خلأ که همه چیز را می‌بلعد', 'آتش سیاه پشیمانی که نمی‌سوزاند اما می‌خورد']

    def _conceive_whispering_voices(self):
        """تصور صداهای نجواگر از اعماق تاریکی"""
        return [
            "از زبان یک زندانی ابدی در برج فراموشی، که بر دیوارهای چرمین می‌نویسد",
            "همچون آخرین کاتب یک کتاب ممنوعه که در حال سوختن در آتش سرد است",
            "مانند سایه‌ای که از گذشته‌ای چسبناک و دردآور سخن می‌گوید",
            "به روایت یک روح سرگردان در میان خرابه‌هایی که بوی چرم سوخته می‌دهند"
        ]

    def _get_nocturnal_inspiration(self):
        """دریافت الهام شبانه و تاریک"""
        core_essence_name = random.choice(list(self.shadow_essences.keys()))
        core_essence_terms = random.sample(self.shadow_essences[core_essence_name], random.randint(1,2))
        
        umbral_palette_name = random.choice(list(self.umbral_palettes.keys()))
        umbral_details = random.sample(self.umbral_palettes[umbral_palette_name], random.randint(1,2))
        
        return {
            'essence_name': core_essence_name,
            'essence_terms': core_essence_terms,
            'umbral_palette_name': umbral_palette_name,
            'umbral_details': umbral_details,
            'binding_ritual': random.choice(self.binding_rituals),
            'abyssal_current': random.choice(self.abyssal_currents),
            'whispering_voice': random.choice(self.whispering_voices) if random.random() < 0.6 else None # احتمال بیشتر برای صدای راوی
        }

    def create_nocturnal_prompt(self):
        """تولید پرامپت دوبیتی با رویکرد کارگاه شبانه"""
        
        raw_elements = []
        for _ in range(random.randint(1, 2)): # کلمات کمتر، تمرکز بیشتر بر فضا
            word = get_random_word_from_mysql()
            if word:
                raw_elements.append(word)
        
        if not raw_elements:
            raw_elements.append(random.choice(["تاریکی", "سکوت", "خاطره"]))

        inspiration = self._get_nocturnal_inspiration()
        
        prompt_parts = []

        # سرآغاز: ورود به کارگاه سایه‌ها
        openings = [
            "از اعماق تاریکی کارگاهت، ای خالق کابوس‌های منظوم،",
            "در دخمه‌ی الهام خود، جایی که نور هرگز نرسیده،",
            "با جوهر شب و قلمی از استخوان،"
        ]
        prompt_parts.append(random.choice(openings))

        # معرفی عناصر خام
        if raw_elements:
            element_intro = f"این ذرات اولیه را: «{ ' »، «'.join(raw_elements) }» بردار و"
            prompt_parts.append(element_intro)
        
        # درخواست دوبیتی با آیین بستن
        prompt_parts.append(f"با آیینی کهن، آن‌ها را {inspiration['binding_ritual']} و دوبیتی‌ای بساز")

        # جوهر سایه
        essence_phrase = f"که آغشته به جوهر «{inspiration['essence_name']}» باشد و طعم تلخ «{ '» و «'.join(inspiration['essence_terms']) }» را به کام خواننده بچشاند."
        prompt_parts.append(essence_phrase)

        # پالت حسی تاریک
        umbral_phrase = f"بگذار این شعر با لمس «{ '» و «'.join(inspiration['umbral_details']) }» از پالت «{inspiration['umbral_palette_name']}» جان بگیرد و به روح بچسبد."
        prompt_parts.append(umbral_phrase)
        
        # جریان مغاکی
        abyssal_current_phrase = f"و بگذار «{inspiration['abyssal_current']}» در رگ‌های خشکیده‌اش جاری شود."
        prompt_parts.append(abyssal_current_phrase)

        # صدای نجواگر (اختیاری)
        if inspiration['whispering_voice']:
            prompt_parts.append(f"این دوبیتی را {inspiration['whispering_voice']} بسرای, گویی بر چرمی کهنه حک می‌شود.")

        # چالش یا ویژگی خاص تاریک (اختیاری)
        if random.random() < 0.4:
            dark_challenges = [
                "با پایانی که چون طناب داری بر گردن حقیقت می‌پیچد.",
                "چنانکه هر کلمه چون قطره‌ای زهر سیاه و چسبناک بچکد.",
                "با تضادی گزنده میان زیبایی ظاهری و فساد باطنی.",
                "به گونه‌ای که سکوت میان واژه‌ها، خود فریادی از یأس باشد.",
                "با استفاده از یک نماد مرکزی که چون داغی بر پیشانی شعر بماند."
            ]
            prompt_parts.append(random.choice(dark_challenges))

        # پایان‌بندی: انتظار برای تجلی تاریک
        closings = [
            "منتظر این تجلی تاریک و چسبناک هستم.",
            "ببینم چگونه از این عناصر، نفرینی منظوم و جاودان می‌سازی.",
            "هنر سیاه خود را در این آفرینش به نمایش بگذار, تا بر پوست تاریخ حک شود."
        ]
        prompt_parts.append(random.choice(closings))
        
        return " ".join(prompt_parts)


def generate_nocturnal_dobeiti_request():
    """
    تولیدکننده نهایی با رویکرد کارگاه شبانه (تاریک و چسبناک)
    """
    engine = NocturnalForgeEngine()
    return engine.create_nocturnal_prompt()

# تابع اصلی
def main():
    """تابع اصلی رویکرد کارگاه شبانه"""
    prompt = generate_nocturnal_dobeiti_request()
    print(prompt)

if __name__ == "__main__":
    main()


