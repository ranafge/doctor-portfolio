# extract_news.py
import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from news.models import News

# আগের ডাটা ডিলিট করুন (চাইলে)
News.objects.all().delete()

# CV থেকে Extract করা গুরুত্বপূর্ণ ইভেন্ট এবং অর্জনগুলো নিউজ আকারে
news_data = [
    {
        "title_bn": "ডাঃ শরীফ আহমেদ জোনায়েদ এসআরএস ট্রাভেলিং ফেলো নির্বাচিত",
        "title_en": "Dr. Sharif Ahmed Jonayed Selected as SRS Travelling Fellow",
        "summary_bn": "স্কোলিওসিস রিসার্চ সোসাইটি (SRS) ডাঃ জোনায়েদকে ২০২৩ সালের জন্য ট্রাভেলিং ফেলো হিসেবে নির্বাচিত করেছে। তিনি কানাডার টরন্টো স্পাইন প্রোগ্রাম এবং যুক্তরাষ্ট্রের কলাম্বিয়া বিশ্ববিদ্যালয়ের ওচ স্পাইন হাসপাতালে প্রশিক্ষণ গ্রহণ করেন।",
        "summary_en": "The Scoliosis Research Society (SRS) selected Dr. Jonayed as Travelling Fellow for 2023. He trained at Toronto Spine Program, Canada and Och Spine Hospital at Columbia University, USA.",
        "source": "Scoliosis Research Society (SRS)",
        "date": date(2023, 8, 14),
        "url": "",
        "order": 1
    },
    {
        "title_bn": "বাংলাদেশের প্রতিনিধি হিসেবে এপিওএ ইয়াং অ্যাম্বাসেডর মনোনীত",
        "title_en": "Appointed as APOA Young Ambassador from Bangladesh",
        "summary_bn": "এশিয়া প্যাসিফিক অর্থোপেডিক অ্যাসোসিয়েশন (APOA) ডাঃ জোনায়েদকে ২০১৮ সালের জন্য ইয়াং অ্যাম্বাসেডর হিসেবে মনোনীত করেছে। এটি বাংলাদেশের জন্য একটি গর্বের বিষয়।",
        "summary_en": "The Asia Pacific Orthopaedic Association (APOA) appointed Dr. Jonayed as Young Ambassador for 2018. This is a proud achievement for Bangladesh.",
        "source": "Asia Pacific Orthopaedic Association (APOA)",
        "date": date(2018, 1, 1),
        "url": "",
        "order": 2
    },
    {
        "title_bn": "ডাঃ জোনায়েদ পেলেন সেরা পেপার পুরস্কার BOSCON-২০১৮ এ",
        "title_en": "Dr. Jonayed Received Best Paper Award at BOSCON-2018",
        "summary_bn": "বাংলাদেশ অর্থোপেডিক সোসাইটির বার্ষিক সম্মেলন BOSCON-২০১৮ এ ডাঃ জোনায়েদ সেরা পেপার পুরস্কার অর্জন করেন। তার গবেষণা মেরুদণ্ডের জটিল অস্ত্রোপচার নিয়ে ছিল।",
        "summary_en": "Dr. Jonayed received the Best Paper Award at BOSCON-2018, the annual conference of Bangladesh Orthopaedic Society. His research was on complex spine surgery.",
        "source": "Bangladesh Orthopaedic Society (BOS)",
        "date": date(2018, 12, 15),
        "url": "",
        "order": 3
    },
    {
        "title_bn": "এও স্পাইন ইন্টারন্যাশনাল ফেলোশিপ সম্পন্ন করলেন ডাঃ জোনায়েদ",
        "title_en": "Dr. Jonayed Completed AO Spine International Fellowship",
        "summary_bn": "ডাঃ শরীফ আহমেদ জোনায়েদ যুক্তরাষ্ট্রের ডেনভারের স্পাইন এডুকেশন এন্ড রিসার্চ ইনস্টিটিউটে এও স্পাইন ইন্টারন্যাশনাল ফেলোশিপ সফলভাবে সম্পন্ন করেছেন।",
        "summary_en": "Dr. Sharif Ahmed Jonayed successfully completed AO Spine International Fellowship at Spine Education and Research Institute, Denver, USA.",
        "source": "AO Spine",
        "date": date(2018, 9, 28),
        "url": "",
        "order": 4
    },
    {
        "title_bn": "গ্লোবাল স্পাইন ডিপ্লোমা অর্জন",
        "title_en": "Achieved Global Spine Diploma",
        "summary_bn": "ডাঃ জোনায়েদ এও স্পাইন সুইজারল্যান্ড থেকে গ্লোবাল স্পাইন ডিপ্লোমা অর্জন করেছেন। এটি মেরুদণ্ডের চিকিৎসায় তার দক্ষতার স্বীকৃতি।",
        "summary_en": "Dr. Jonayed achieved the Global Spine Diploma from AO Spine Switzerland. This recognizes his expertise in spine surgery.",
        "source": "AO Spine Switzerland",
        "date": date(2024, 3, 15),
        "url": "",
        "order": 5
    },
    {
        "title_bn": "ফেলো অফ দি আমেরিকান কলেজ অফ সার্জনস (FACS) নির্বাচিত",
        "title_en": "Elected as Fellow of the American College of Surgeons (FACS)",
        "summary_bn": "ডাঃ শরীফ আহমেদ জোনায়েদ আমেরিকান কলেজ অফ সার্জনস এর ফেলো (FACS) নির্বাচিত হয়েছেন। এটি আন্তর্জাতিক স্বীকৃতির একটি বড় অর্জন।",
        "summary_en": "Dr. Sharif Ahmed Jonayed has been elected as Fellow of the American College of Surgeons (FACS), a major international recognition.",
        "source": "American College of Surgeons",
        "date": date(2019, 10, 15),
        "url": "",
        "order": 6
    },
    {
        "title_bn": "FRCS (গ্লাসগো) অর্জন",
        "title_en": "Achieved FRCS (Glasgow)",
        "summary_bn": "ডাঃ জোনায়েদ রাজকীয় কলেজ অফ ফিজিশিয়ান্স অ্যান্ড সার্জনস, গ্লাসগো থেকে FRCS ডিগ্রি অর্জন করেছেন।",
        "summary_en": "Dr. Jonayed achieved FRCS degree from the Royal College of Physicians and Surgeons, Glasgow.",
        "source": "Royal College of Physicians and Surgeons, Glasgow",
        "date": date(2023, 7, 15),
        "url": "",
        "order": 7
    },
    {
        "title_bn": "সিঙ্গাপুরে গ্লোবাল স্পাইন কংগ্রেস ২০২৪ এ বক্তৃতা",
        "title_en": "Lecture at Global Spine Congress 2024, Singapore",
        "summary_bn": "ডাঃ জোনায়েদ ব্যাংকক, থাইল্যান্ডে অনুষ্ঠিত গ্লোবাল স্পাইন কংগ্রেস (GSC) ২০২৪ এ গুরুত্বপূর্ণ গবেষণা উপস্থাপন করেন।",
        "summary_en": "Dr. Jonayed presented important research at the Global Spine Congress (GSC) 2024 held in Bangkok, Thailand.",
        "source": "Global Spine Congress",
        "date": date(2024, 5, 15),
        "url": "",
        "order": 8
    },
    {
        "title_bn": "বাংলাদেশ স্পাইন সোসাইটির বৈজ্ঞানিক সম্পাদক নির্বাচিত",
        "title_en": "Elected as Scientific Secretary of Bangladesh Spine Society",
        "summary_bn": "ডাঃ শরীফ আহমেদ জোনায়েদ বাংলাদেশ স্পাইন সোসাইটির বৈজ্ঞানিক সম্পাদক হিসেবে নির্বাচিত হয়েছেন।",
        "summary_en": "Dr. Sharif Ahmed Jonayed has been elected as Scientific Secretary of the Bangladesh Spine Society.",
        "source": "Bangladesh Spine Society",
        "date": date(2024, 1, 1),
        "url": "",
        "order": 9
    },
    {
        "title_bn": "জাপানে ক্লিনিক্যাল ফেলোশিপ সম্পন্ন",
        "title_en": "Completed Clinical Fellowship in Japan",
        "summary_bn": "ডাঃ জোনায়েদ জাপানের সাপ্পোরো অর্থোপেডিক হাসপাতাল- সেন্টার ফর স্পাইনাল ডিজঅর্ডার এ ক্লিনিক্যাল ফেলোশিপ সম্পন্ন করেন।",
        "summary_en": "Dr. Jonayed completed Clinical Fellowship at Sapporo Orthopedic Hospital-Centre For Spinal Disorder, Japan.",
        "source": "Sapporo Orthopedic Hospital, Japan",
        "date": date(2017, 6, 25),
        "url": "",
        "order": 10
    }
]

# ডাটা ইনসার্ট করুন
for data in news_data:
    news = News.objects.create(**data)
    print(f"✅ Added News: {news.title_en[:50]}... - {news.date}")

print(f"\n📊 মোট {News.objects.count()} টি নিউজ যোগ করা হয়েছে!")

# বছর অনুযায়ী নিউজ কাউন্ট
print("\n📅 বছর অনুযায়ী নিউজ:")
years = News.objects.values_list('date__year', flat=True).distinct().order_by('-date__year')
for year in years:
    count = News.objects.filter(date__year=year).count()
    print(f"  {year}: {count} টি")