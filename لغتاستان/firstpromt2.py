import random
import os
import sys
from datetime import datetime
import hashlib

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
            fallback_words = ["چشم", "لب", "موج", "برف", "سحر", "شفق", "نسیم", "صدف", "مروارید", "یاقوت"]
            return random.choice(fallback_words)
    except:
        fallback_words = ["محبت", "الفت", "رأفت", "شفقت", "حنان", "مروت", "کرم", "جود", "سخا", "ایثار"]
        return random.choice(fallback_words)

class IntelligentDoheitiEngine:
    """
    موتور هوشمند تولید درخواست دوبیتی با قابلیت یادگیری الگو
    """
    
    def __init__(self):
        self.mood_seeds = self._generate_mood_seeds()
        self.semantic_networks = self._build_semantic_networks()
        self.rhythm_patterns = self._create_rhythm_patterns()
        self.contextual_memory = {}
        
    def _generate_mood_seeds(self):
        """تولید بذرهای حالت روحی بر اساس زمان"""
        current_hour = datetime.now().hour
        current_month = datetime.now().month
        
        time_moods = {
            'dawn': ['طراوت', 'نشاط', 'تازگی', 'بیداری'],
            'morning': ['امید', 'نشاط', 'تحرک', 'پویایی'],
            'noon': ['شدت', 'قدرت', 'روشنایی', 'تابش'],
            'afternoon': ['آرامش', 'تأمل', 'نرمی', 'لطافت'],
            'evening': ['دلتنگی', 'رؤیا', 'خیال', 'شاعریت'],
            'night': ['رمز', 'راز', 'عمق', 'سکوت']
        }
        
        season_moods = {
            'spring': ['شکوفایی', 'تولد', 'رستاخیز', 'سرسبزی'],
            'summer': ['شور', 'حرارت', 'پختگی', 'فراوانی'],
            'autumn': ['نوستالژی', 'حکمت', 'تجربه', 'فروتنی'],
            'winter': ['سکون', 'صفا', 'درونگرایی', 'خلوت']
        }
        
        # تعیین زمان روز
        if 5 <= current_hour < 8:
            time_key = 'dawn'
        elif 8 <= current_hour < 12:
            time_key = 'morning'
        elif 12 <= current_hour < 15:
            time_key = 'noon'
        elif 15 <= current_hour < 18:
            time_key = 'afternoon'
        elif 18 <= current_hour < 22:
            time_key = 'evening'
        else:
            time_key = 'night'
            
        # تعیین فصل
        if current_month in [3, 4, 5]:
            season_key = 'spring'
        elif current_month in [6, 7, 8]:
            season_key = 'summer'
        elif current_month in [9, 10, 11]:
            season_key = 'autumn'
        else:
            season_key = 'winter'
            
        return {
            'time': time_moods[time_key],
            'season': season_moods[season_key],
            'current_energy': random.choice(time_moods[time_key] + season_moods[season_key])
        }
    
    def _build_semantic_networks(self):
        """ساخت شبکه‌های معنایی پیچیده"""
        networks = {
            'love_network': {
                'core': ['عشق', 'محبت', 'الفت'],
                'extensions': ['نگاه', 'لبخند', 'دست', 'قلب', 'روح'],
                'metaphors': ['آتش', 'دریا', 'باد', 'نور', 'عطر'],
                'emotions': ['شوق', 'اشتیاق', 'حسرت', 'امید', 'وجد']
            },
            'nature_network': {
                'core': ['طبیعت', 'هستی', 'آفرینش'],
                'extensions': ['کوه', 'دریا', 'جنگل', 'صحرا', 'آسمان'],
                'metaphors': ['مادر', 'معلم', 'کتاب', 'آینه', 'خانه'],
                'emotions': ['حیرت', 'تحسین', 'آرامش', 'اتحاد', 'تسلیم']
            },
            'time_network': {
                'core': ['زمان', 'عمر', 'لحظه'],
                'extensions': ['گذشته', 'حال', 'آینده', 'ابدیت', 'فنا'],
                'metaphors': ['رودخانه', 'باد', 'پرنده', 'سایه', 'موج'],
                'emotions': ['حسرت', 'امید', 'ترس', 'قبول', 'حکمت']
            },
            'wisdom_network': {
                'core': ['حکمت', 'دانش', 'بینش'],
                'extensions': ['تجربه', 'درد', 'رنج', 'شادی', 'آزمون'],
                'metaphors': ['نور', 'راه', 'کلید', 'خزانه', 'دریا'],
                'emotions': ['فروتنی', 'قناعت', 'صبر', 'بردباری', 'امید']
            }
        }
        return networks
    
    def _create_rhythm_patterns(self):
        """الگوهای ریتمیک و آهنگین"""
        return {
            'gentle': ['نرم نرم', 'آهسته آهسته', 'لطیف و ملایم'],
            'passionate': ['پرشور', 'آتشین', 'سوزان و گداز'],
            'mystical': ['رازآلود', 'عمیق و نهان', 'مرموز و جذاب'],
            'nostalgic': ['غم‌انگیز', 'دلتنگ', 'خاطره‌انگیز'],
            'hopeful': ['امیدوار', 'روشن و تابان', 'مژده‌آور']
        }
    
    def _create_word_constellation(self, seed_words):
        """ایجاد صورت فلکی کلمات مرتبط"""
        if not seed_words:
            return []
            
        constellation = []
        for word in seed_words:
            # جستجو در شبکه‌های معنایی
            for network_name, network in self.semantic_networks.items():
                for category, word_list in network.items():
                    if word in word_list:
                        # اضافه کردن کلمات مرتبط
                        related_words = random.sample(
                            [w for w in word_list if w != word], 
                            min(2, len(word_list) - 1)
                        )
                        constellation.extend(related_words)
                        
                        # اضافه کردن کلمات از دسته‌های مرتبط
                        for other_category, other_words in network.items():
                            if other_category != category and random.random() < 0.3:
                                constellation.append(random.choice(other_words))
        
        return list(set(constellation))  # حذف تکراری‌ها
    
    def _generate_contextual_directive(self):
        """تولید دستورالعمل متنی بر اساس متن"""
        directives = {
            'emotional_depth': [
                "عمق احساسی داشته باشد",
                "لایه‌هایی از معنا داشته باشد", 
                "قلب خواننده را لمس کند",
                "حس واقعی منتقل کند"
            ],
            'imagery': [
                "تصاویر ذهنی واضح بسازد",
                "صحنه‌ای زنده رسم کند",
                "حواس پنج‌گانه را درگیر کند",
                "فضای بصری خلق کند"
            ],
            'universality': [
                "برای همه قابل فهم باشد",
                "تجربه انسانی مشترک داشته باشد",
                "فراتر از زمان و مکان باشد",
                "با همه سنین ارتباط برقرار کند"
            ],
            'surprise': [
                "پایان غیرمنتظره داشته باشد",
                "نگاه تازه‌ای ارائه دهد",
                "زاویه دید متفاوت داشته باشد",
                "خواننده را شگفت‌زده کند"
            ]
        }
        
        chosen_aspects = random.sample(list(directives.keys()), random.randint(1, 3))
        result_directives = []
        
        for aspect in chosen_aspects:
            result_directives.append(random.choice(directives[aspect]))
            
        return result_directives
    
    def _create_constraint_challenge(self):
        """ایجاد چالش‌های خلاقانه"""
        challenges = [
            "هر مصرع با حرف متفاوتی شروع شود",
            "یک کلمه در تمام مصرع‌ها تکرار شود",
            "از هیچ حرف اضافه استفاده نشود",
            "فقط با کلمات دو هجایی",
            "بدون استفاده از کلمه 'است'",
            "هر مصرع سوالی باشد",
            "هر مصرع جوابی باشد",
            "فقط با اسامی ملموس",
            "بدون هیچ صفت"
        ]
        
        if random.random() < 0.2:  # 20% احتمال چالش
            return random.choice(challenges)
        return None
    
    def _generate_style_fusion(self):
        """ترکیب سبک‌های مختلف"""
        classical_elements = ['غزل‌وار', 'رباعی‌گونه', 'مثنوی‌طبع', 'قصیده‌مآب']
        modern_elements = ['آزاد', 'نو', 'معاصر', 'تجربه‌گرا']
        regional_elements = ['شیرازی', 'اصفهانی', 'خراسانی', 'آذربایجانی']
        
        fusion_types = []
        
        if random.random() < 0.4:
            fusion_types.append(f"با ترکیب سبک {random.choice(classical_elements)} و {random.choice(modern_elements)}")
        
        if random.random() < 0.3:
            fusion_types.append(f"با طعم {random.choice(regional_elements)}")
            
        return fusion_types
    
    def create_intelligent_prompt(self):
        """تولید پرامپت هوشمند و تطبیقی"""
        
        # دریافت کلمات پایه
        seed_words = []
        for _ in range(random.randint(1, 3)):
            word = get_random_word_from_mysql()
            if word:
                seed_words.append(word)
        
        # ایجاد صورت فلکی کلمات
        word_constellation = self._create_word_constellation(seed_words)
        all_words = seed_words + word_constellation[:3]  # محدود کردن تعداد
        
        # انتخاب حالت کلی
        current_energy = self.mood_seeds['current_energy']
        
        # ساخت پرامپت به روش تعاملی
        prompt_components = []
        
        # مقدمه تعاملی
        interactive_openings = [
            "با من همکاری کن و",
            "کمکم کن تا با هم",
            "بیا با هم",
            "دوست دارم که ما",
            "چطوره با هم"
        ]
        
        prompt_components.append(random.choice(interactive_openings))
        
        # هدف اصلی
        main_goals = [
            "دوبیتی خلق کنیم",
            "شعری بسازیم", 
            "رباعی‌ای بپردازیم",
            "بیتی خلاصه کنیم"
        ]
        
        prompt_components.append(random.choice(main_goals))
        
        # معرفی کلمات به شکل داستانی
        if all_words:
            word_intro_patterns = [
                f"که داستان {' و '.join(all_words)} را بگوید",
                f"که رابطه میان {' و '.join(all_words)} را نشان دهد", 
                f"که {' و '.join(all_words)} در آن زندگی کنند",
                f"که دنیای {' و '.join(all_words)} را بسازد"
            ]
            prompt_components.append(random.choice(word_intro_patterns))
        
        # تنظیم حالت بر اساس انرژی فعلی
        mood_descriptions = {
            'طراوت': 'با حس نو بودن و تازگی',
            'امید': 'با نگاه مثبت به آینده',
            'آرامش': 'با فضای آرام و دلپذیر',
            'رؤیا': 'با جو خیالی و شاعرانه',
            'حکمت': 'با عمق و اندیشه',
            'شور': 'با احساس قوی و پرشور'
        }
        
        if current_energy in mood_descriptions:
            prompt_components.append(mood_descriptions[current_energy])
        
        # اضافه کردن دستورالعمل‌های متنی
        contextual_directives = self._generate_contextual_directive()
        if contextual_directives:
            directive_text = f"طوری که {' و '.join(contextual_directives)}"
            prompt_components.append(directive_text)
        
        # ترکیب سبک‌ها
        style_fusions = self._generate_style_fusion()
        if style_fusions:
            prompt_components.extend(style_fusions)
        
        # چالش خلاقانه
        creative_challenge = self._create_constraint_challenge()
        if creative_challenge:
            prompt_components.append(f"با این چالش خلاقانه: {creative_challenge}")
        
        # پایان تشویقی
        encouraging_endings = [
            "بیا ببینیم چه زیبایی خلق می‌شود",
            "مطمئنم نتیجه فوق‌العاده خواهد بود",
            "با هم شاهکاری می‌سازیم",
            "این تجربه لذت‌بخش خواهد بود"
        ]
        
        if random.random() < 0.3:
            prompt_components.append(random.choice(encouraging_endings))
        
        # ترکیب نهایی
        return ". ".join(prompt_components) + "."

def generate_adaptive_dobeiti_request():
    """
    تولیدکننده تطبیقی بر اساس الگوریتم هوشمند
    """
    engine = IntelligentDoheitiEngine()
    return engine.create_intelligent_prompt()

def create_quantum_prompt():
    """
    رویکرد کوانتومی - ترکیب همه حالات ممکن به‌طور همزمان
    """
    
    # ماتریس حالات ممکن
    quantum_states = {
        'subjects': ['عشق', 'زندگی', 'طبیعت', 'زمان', 'رؤیا'],
        'moods': ['شاد', 'غمناک', 'امیدوار', 'متأمل', 'عاشقانه'],
        'styles': ['کلاسیک', 'مدرن', 'عرفانی', 'حماسی', 'طنز'],
        'structures': ['سوال-جواب', 'توصیفی', 'داستانی', 'فلسفی', 'تصویری']
    }
    
    # انتهاد کوانتومی (فروپاشی موجی!)
    collapsed_state = {}
    for dimension, options in quantum_states.items():
        collapsed_state[dimension] = random.choice(options)
    
    # ساخت پرامپت کوانتومی
    quantum_prompt = f"""
    در دنیای موازی شعر، جایی که همه احتمالات وجود دارند، 
    دوبیتی‌ای بساز که هم‌زمان درباره {collapsed_state['subjects']} باشد، 
    هم {collapsed_state['moods']} باشد و هم {collapsed_state['styles']}, 
    با ساختار {collapsed_state['structures']}. 
    این دوبیتی در تمام جهان‌های موازی معنا داشته باشد.
    """
    
    return quantum_prompt.strip()

def generate_green_dobeiti_prompt():
    """
    تولیدکننده نهایی رنگ سبز - ترکیب هوش مصنوعی و خلاقیت
    """
    
    method_selector = random.randint(1, 10)
    
    if method_selector <= 7:
        return generate_adaptive_dobeiti_request()
    else:
        return create_quantum_prompt()

# تابع اصلی
def main():
    """تابع اصلی رویکرد سبز - هوشمند و تطبیقی"""
    prompt = generate_green_dobeiti_prompt()
    print(prompt)

if __name__ == "__main__":
    main()
