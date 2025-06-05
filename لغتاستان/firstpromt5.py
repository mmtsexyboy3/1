

import random
import os
import sys
from datetime import datetime

# تابع دریافت کلمه تصادفی (با لیست‌های پشتیبان مرتبط با درد و جنگ)
def get_random_word_from_mysql():
    """
    استفاده از randreader.py برای گرفتن کلمه تصادفی با حال و هوای درد و جنگ.
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
            # لیست پشتیبان اول
            fallback_words = ["زخم", "خون", "فریاد", "سنگر", "گلوله", "ویرانه", "اشک", "خاکستر", "مرگ", "شمشیر"]
            return random.choice(fallback_words)
    except Exception as e:
        # print(f"Error in get_random_word_from_mysql (war_pain): {e}") # برای دیباگ
        # لیست پشتیبان دوم
        fallback_words = ["درد", "ناله", "اسارت", "داغ", "یتیم", "بیوه", "آواره", "ترکش", "انفجار", "سکوت_مرگبار"]
        return random.choice(fallback_words)

class WarTornMuseEngine: # الهه شعر جنگ‌زده
    """
    موتور الهه شعر جنگ‌زده برای تولید درخواست دوبیتی با رویکرد درد و جنگ.
    """
    def __init__(self):
        self.battlefield_echoes = self._load_battlefield_echoes() # پژواک‌های میدان نبرد
        self.scarred_landscapes = self._define_scarred_landscapes() # مناظر زخم‌خورده
        self.acts_of_defiance_or_despair = self._list_acts_of_defiance_or_despair() # اعمال سرکشی یا یأس
        self.shrapnel_of_truth = self._identify_shrapnel_of_truth() # ترکش‌های حقیقت
        self.voices_from_the_trenches = self._imagine_voices_from_the_trenches() # صداهایی از سنگرها

    def _load_battlefield_echoes(self):
        """بارگذاری پژواک‌های میدان نبرد و مفاهیم مرتبط با درد و جنگ"""
        return {
            'زخم_های_ماندگار': ['درد بی‌صدا و چسبناک', 'خاطره خونین که پاک نمی‌شود', 'داغی بر روح و جسم', 'جای خالی عزیزان'],
            'فریاد_های_خاموش': ['ناله‌های در گلو مانده', 'سکوت سنگین پس از نبرد', 'چشم‌های پر از حرف ناگفته', 'بغض چسبیده به حنجره'],
            'ویرانی_و_فقدان': ['خاکستر آرزوها', 'خانه‌های ویران و سرد', 'آوارگی و بی‌خانمانی', 'میراث جنگ: درد و اندوه'],
            'شجاعت_و_مقاومت_در_برابر_درد': ['ایستادگی در برابر طوفان', 'امید در دل خاکستر', 'آخرین سنگر مقاومت', 'اراده پولادین در جسمی خسته'],
            'پوچی_و_بی_رحمی_جنگ': ['رقص مرگ در میدان نبرد', 'بازی بی‌رحمانه قدرت', 'قربانیان بی‌گناه', 'چراغی که در باد خاموش شد']
        }

    def _define_scarred_landscapes(self):
        """تعریف مناظر زخم‌خورده و فضاهای جنگی"""
        return {
            'لمس_سرد_و_خشن': ['زره چرمین و خون‌آلود', 'خاک سرد و خیس از خون', 'سنگ سخت سنگر', 'سیم خاردار زنگ‌زده و تیز'],
            'اصوات_جنگ_و_سکوت_پس_از_آن': ['غرش توپ‌ها و صدای انفجار', 'فریادهای زخمی‌ها در میان دود و آتش', 'سکوت وهم‌آور پس از کشتار', 'زوزه باد در ویرانه‌ها'],
            'تصاویر_ویرانی_و_اندوه': ['آسمان سربی و دودآلود', 'زمین سوخته و ترک‌خورده', 'چهره‌های خسته و غبارگرفته سربازان', 'چشم‌های بی‌فروغ کودکان جنگ'],
            'بوی_باروت_خون_و_خاکستر': ['بوی تند باروت و آهن گداخته', 'بوی چرم سوخته و خون تازه', 'عطر تلخ خاکستر و دود', 'نفس سنگین هوای آلوده به مرگ']
        }

    def _list_acts_of_defiance_or_despair(self):
        """فهرست کردن اعمال سرکشی یا یأس در شعر جنگ"""
        return [
            "با خون دل بر دیوار تاریخ بنگار", "فریاد بزن از عمق زخم‌هایت", "مرثیه‌ای برای افتادگان بسرای",
            "آخرین مقاومت را به تصویر بکش", "با کلمات، سنگری در برابر فراموشی بساز",
            "دردهای چسبیده به استخوان را روایت کن", "از میان دود و آتش، حقیقتی را بیرون بکش"
        ]

    def _identify_shrapnel_of_truth(self):
        """شناسایی ترکش‌های حقیقت در میان ویرانه‌های جنگ"""
        return ['ترکش تیز یک خاطره دردناک', 'بارقه امیدی در دل تاریکی مطلق', 'فریاد خاموش یک قربانی بی‌نام', 'سؤال بی‌جوابی که در هوا معلق مانده']

    def _imagine_voices_from_the_trenches(self):
        """تصور صداهایی از سنگرها و خطوط مقدم"""
        return [
            "از زبان یک سرباز خسته که آخرین نامه‌اش را بر تکه چرمی خونین می‌نویسد",
            "همچون یک مادر داغدار که بر مزار فرزندش مویه می‌کند",
            "مانند یک کودک جنگ‌زده که تنها عروسکش را در آغوش گرفته",
            "به روایت یک تاریخ‌نگار که شاهد بی‌رحمی‌های جنگ بوده و بر پوستینی کهنه ثبت می‌کند"
        ]

    def _get_war_torn_inspiration(self):
        """دریافت الهام جنگ‌زده"""
        core_echo_name = random.choice(list(self.battlefield_echoes.keys()))
        core_echo_terms = random.sample(self.battlefield_echoes[core_echo_name], random.randint(1,2))
        
        scarred_landscape_name = random.choice(list(self.scarred_landscapes.keys()))
        scarred_details = random.sample(self.scarred_landscapes[scarred_landscape_name], random.randint(1,2))
        
        return {
            'echo_name': core_echo_name,
            'echo_terms': core_echo_terms,
            'landscape_name': scarred_landscape_name,
            'landscape_details': scarred_details,
            'act_of_defiance_or_despair': random.choice(self.acts_of_defiance_or_despair),
            'shrapnel_of_truth': random.choice(self.shrapnel_of_truth),
            'voice_from_the_trenches': random.choice(self.voices_from_the_trenches) if random.random() < 0.7 else None # احتمال بالا برای صدای راوی
        }

    def create_war_torn_prompt(self):
        """تولید پرامپت دوبیتی با رویکرد درد و جنگ"""
        
        battle_scars = [] # کلمات کلیدی
        for _ in range(random.randint(1, 2)):
            word = get_random_word_from_mysql()
            if word:
                battle_scars.append(word)
        
        if not battle_scars:
            battle_scars.append(random.choice(["جنگ", "درد", "سرباز"]))

        inspiration = self._get_war_torn_inspiration()
        
        prompt_parts = []

        # سرآغاز: ورود به میدان نبرد کلمات
        openings = [
            "از میان غبار و خون میدان نبرد کلمات، ای شاعر زخم‌خورده،",
            "در سنگر اندیشه‌ات، جایی که فریادها به شعر بدل می‌شوند،",
            "با قلمی آغشته به درد و جوهری از اشک و خون،"
        ]
        prompt_parts.append(random.choice(openings))

        # معرفی عناصر خام (جراحات جنگ)
        if battle_scars:
            scar_intro = f"این جراحات زبانی را: «{ ' »، «'.join(battle_scars) }» بردار و"
            prompt_parts.append(scar_intro)
        
        # درخواست دوبیتی با عمل سرکشی یا یأس
        prompt_parts.append(f"{inspiration['act_of_defiance_or_despair']} و دوبیتی‌ای بساز")

        # پژواک میدان نبرد
        echo_phrase = f"که پژواک «{inspiration['echo_name']}» باشد و طعم گزنده «{ '» و «'.join(inspiration['echo_terms']) }» را بر جان بنشاند، زخمی که به روح می‌چسبد."
        prompt_parts.append(echo_phrase)

        # منظر زخم‌خورده
        landscape_phrase = f"بگذار این شعر با لمس «{ '» و «'.join(inspiration['landscape_details']) }» از منظر «{inspiration['landscape_name']}» جان بگیرد، گویی بر زرهی چرمین و خونین حک شده."
        prompt_parts.append(landscape_phrase)
        
        # ترکش حقیقت
        shrapnel_phrase = f"و بگذار «{inspiration['shrapnel_of_truth']}» در قلب آن بدرخشد یا فرو رود."
        prompt_parts.append(shrapnel_phrase)

        # صدای از سنگر (اختیاری)
        if inspiration['voice_from_the_trenches']:
            prompt_parts.append(f"این دوبیتی را {inspiration['voice_from_the_trenches']} بسرای.")

        # چالش یا ویژگی خاص مرتبط با جنگ و درد (اختیاری)
        if random.random() < 0.4:
            war_challenges = [
                "با پایانی که چون صدای آخرین گلوله، سکوت را می‌شکند.",
                "چنانکه هر مصرع، داغی تازه بر دل بگذارد.",
                "با تضادی تلخ میان آرزوی صلح و واقعیت جنگ.",
                "به گونه‌ای که سکوت میان واژه‌ها، خود مرثیه‌ای برای از دست رفتگان باشد.",
                "با استفاده از یک نماد مرکزی که یادآور زخم‌های فراموش‌نشدنی جنگ باشد."
            ]
            prompt_parts.append(random.choice(war_challenges))

        # پایان‌بندی: انتظار برای مرثیه یا فریاد
        closings = [
            "منتظر این مرثیه خونین یا فریاد دردآلود هستم.",
            "ببینم چگونه از این ویرانه‌ها، شعری می‌سازی که تاریخ را به لرزه درآورد.",
            "هنر مقاومت یا سوگواری خود را در این آفرینش به نمایش بگذار."
        ]
        prompt_parts.append(random.choice(closings))
        
        return " ".join(prompt_parts)


def generate_war_torn_dobeiti_request():
    """
    تولیدکننده نهایی با رویکرد درد و جنگ (الهه شعر جنگ‌زده)
    """
    engine = WarTornMuseEngine()
    return engine.create_war_torn_prompt()

# تابع اصلی
def main():
    """تابع اصلی رویکرد درد و جنگ"""
    prompt = generate_war_torn_dobeiti_request()
    print(prompt)

if __name__ == "__main__":
    main()


