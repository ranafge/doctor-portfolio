# extract_photos.py
import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from gallery.models import Photo

# আগের ডাটা ডিলিট করুন (চাইলে)
Photo.objects.all().delete()

# CV এবং অনলাইন তথ্য থেকে ফটো ডাটা
photos_data = [
    # Conference Photos
    {
        "title_bn": "গ্লোবাল স্পাইন কংগ্রেস ২০২৪, ব্যাংকক - ডা. জোনায়েদের বক্তৃতা",
        "title_en": "Global Spine Congress 2024, Bangkok - Dr. Jonayed's Lecture",
        "category": "conference",
        "date": date(2024, 5, 15),
        "order": 1
    },
    {
        "title_bn": "এপিএসএস বার্ষিক সম্মেলন ২০২২, কোয়েম্বাটোর, ভারত",
        "title_en": "APSS Annual Meeting 2022, Coimbatore, India",
        "category": "conference",
        "date": date(2022, 10, 20),
        "order": 2
    },
    {
        "title_bn": "স্পাইনউইক ২০২৩, মেলবোর্ন, অস্ট্রেলিয়া - গবেষণা উপস্থাপনা",
        "title_en": "SpineWeek 2023, Melbourne, Australia - Research Presentation",
        "category": "conference",
        "date": date(2023, 5, 10),
        "order": 3
    },
    {
        "title_bn": "এও স্পাইন অ্যাডভান্স কোর্স অন স্কোলিওসিস ২০২২, ঢাকা",
        "title_en": "AO Spine Advance Course on Scoliosis 2022, Dhaka",
        "category": "conference",
        "date": date(2022, 12, 5),
        "order": 4
    },
    {
        "title_bn": "এপিএসএস ডেপু সিন্থেস স্পাইন ট্রাভেলিং ফেলোশিপ ২০১৭, সিঙ্গাপুর",
        "title_en": "APSS Depuy Synthes Spine Travelling Fellowship 2017, Singapore",
        "category": "conference",
        "date": date(2017, 8, 31),
        "order": 5
    },
    {
        "title_bn": "বিওএসকন ২০২৩ - মেরুদণ্ডের বিকৃতি সংশোধন নিয়ে বক্তৃতা",
        "title_en": "BOSCON 2023 - Lecture on Spinal Deformity Correction",
        "category": "conference",
        "date": date(2023, 12, 15),
        "order": 6
    },
    {
        "title_bn": "এও স্পাইন সেমিনার অন ডিজেনারেটিভ স্পাইন ২০২৩, ঢাকা",
        "title_en": "AO Spine Seminar on Degenerative Spine 2023, Dhaka",
        "category": "conference",
        "date": date(2023, 12, 9),
        "order": 7
    },
    {
        "title_bn": "৩য় কোলকাতা স্পাইন ডিফরমিটি কনফারেন্স ২০২৩, পশ্চিমবঙ্গ, ভারত",
        "title_en": "3rd Kolkata Spinal Deformity Conference 2023, West Bengal, India",
        "category": "conference",
        "date": date(2023, 11, 10),
        "order": 8
    },
    {
        "title_bn": "কেএসএসএস ২০২৩, সিওল, কোরিয়া - পিভিসিআর পদ্ধতি নিয়ে উপস্থাপনা",
        "title_en": "KSSS 2023, Seoul, Korea - PVCR Presentation",
        "category": "conference",
        "date": date(2023, 10, 15),
        "order": 9
    },
    {
        "title_bn": "এপিএসএস বেসিক স্পাইন কোর্স ২০২২, ঢাকা - স্থানীয় আয়োজক চেয়ারম্যান",
        "title_en": "APSS Basic Spine Course 2022, Dhaka - Local Organizing Chairman",
        "category": "conference",
        "date": date(2022, 3, 10),
        "order": 10
    },
    
    # Award Photos
    {
        "title_bn": "এসআরএস ট্রাভেলিং ফেলো ২০২৩ - সার্টিফিকেট গ্রহণ",
        "title_en": "SRS Travelling Fellow 2023 - Receiving Certificate",
        "category": "award",
        "date": date(2023, 9, 15),
        "order": 11
    },
    {
        "title_bn": "এপিওএ ইয়াং অ্যাম্বাসেডর অ্যাওয়ার্ড ২০১৮",
        "title_en": "APOA Young Ambassador Award 2018",
        "category": "award",
        "date": date(2018, 10, 15),
        "order": 12
    },
    {
        "title_bn": "বিওএসকন ২০১৮ - সেরা পেপার পুরস্কার গ্রহণ",
        "title_en": "BOSCON 2018 - Receiving Best Paper Award",
        "category": "award",
        "date": date(2018, 12, 15),
        "order": 13
    },
    {
        "title_bn": "এও স্পাইন ইন্টারন্যাশনাল ফেলো ২০১৮, ডেনভার, ইউএসএ",
        "title_en": "AO Spine International Fellow 2018, Denver, USA",
        "category": "award",
        "date": date(2018, 9, 28),
        "order": 14
    },
    {
        "title_bn": "এফআরসিএস (গ্লাসগো) ডিগ্রি অর্জন ২০২৩",
        "title_en": "FRCS (Glasgow) Degree Achievement 2023",
        "category": "award",
        "date": date(2023, 7, 15),
        "order": 15
    },
    {
        "title_bn": "এফএসিসি (ইউএসএ) ডিগ্রি অর্জন ২০১৯",
        "title_en": "FACS (USA) Degree Achievement 2019",
        "category": "award",
        "date": date(2019, 10, 15),
        "order": 16
    },
    {
        "title_bn": "গ্লোবাল স্পাইন ডিপ্লোমা ২০২৪ - এও স্পাইন সুইজারল্যান্ড",
        "title_en": "Global Spine Diploma 2024 - AO Spine Switzerland",
        "category": "award",
        "date": date(2024, 3, 15),
        "order": 17
    },
    
    # Chamber Photos
    {
        "title_bn": "নিটর হাসপাতাল - মেরুদণ্ড বিভাগের অপারেশন থিয়েটার",
        "title_en": "NITOR Hospital - Spine Department Operation Theater",
        "category": "chamber",
        "date": date(2024, 1, 15),
        "order": 18
    },
    {
        "title_bn": "ধানমন্ডি চেম্বার - রোগীর সাথে ডা. জোনায়েদ",
        "title_en": "Dhanmondi Chamber - Dr. Jonayed with Patient",
        "category": "chamber",
        "date": date(2024, 2, 10),
        "order": 19
    },
    {
        "title_bn": "নিটর হাসপাতালের আধুনিক স্পাইন সার্জারি সুবিধা",
        "title_en": "NITOR Hospital's Modern Spine Surgery Facilities",
        "category": "chamber",
        "date": date(2024, 1, 20),
        "order": 20
    },
    {
        "title_bn": "ধানমন্ডি চেম্বারের অপেক্ষমান রোগী ও সেবা প্রদান",
        "title_en": "Dhanmondi Chamber - Waiting Patients and Service",
        "category": "chamber",
        "date": date(2024, 2, 5),
        "order": 21
    },
    {
        "title_bn": "নিটর হাসপাতালের স্পাইন বিভাগের টিম মিটিং",
        "title_en": "NITOR Hospital Spine Department Team Meeting",
        "category": "chamber",
        "date": date(2024, 3, 5),
        "order": 22
    },
    
    # Other/International Training Photos
    {
        "title_bn": "জাপানের সাপ্পোরো অর্থোপেডিক হাসপাতালে ফেলোশিপ প্রশিক্ষণ ২০১৭",
        "title_en": "Fellowship Training at Sapporo Orthopedic Hospital, Japan 2017",
        "category": "other",
        "date": date(2017, 6, 10),
        "order": 23
    },
    {
        "title_bn": "যুক্তরাষ্ট্রের ডেনভার স্পাইন ইনস্টিটিউটে প্রশিক্ষণ ২০১৮",
        "title_en": "Training at Denver Spine Institute, USA 2018",
        "category": "other",
        "date": date(2018, 9, 10),
        "order": 24
    },
    {
        "title_bn": "কানাডার টরন্টো স্পাইন প্রোগ্রামে এসআরএস ফেলো ২০২৩",
        "title_en": "SRS Fellow at Toronto Spine Program, Canada 2023",
        "category": "other",
        "date": date(2023, 8, 20),
        "order": 25
    },
    {
        "title_bn": "ইন্ডিয়ান স্পাইন ইনজুরি সেন্টার (ISIC), নয়াদিল্লিতে ফেলোশিপ ২০১৪",
        "title_en": "Fellowship at Indian Spinal Injuries Center (ISIC), New Delhi 2014",
        "category": "other",
        "date": date(2014, 5, 15),
        "order": 26
    },
    {
        "title_bn": "রয়্যাল অর্থোপেডিক হাসপাতাল, বার্মিংহাম, ইউকে - ক্লিনিকাল ভিজিটর ২০১৪",
        "title_en": "Clinical Visitor at Royal Orthopaedic Hospital, Birmingham, UK 2014",
        "category": "other",
        "date": date(2014, 11, 15),
        "order": 27
    },
    {
        "title_bn": "গাঙ্গা হাসপাতাল, ভারত - এও স্পাইন এশিয়া প্যাসিফিক ফেলো ২০১৫",
        "title_en": "AO Spine Asia Pacific Fellow at Ganga Hospital, India 2015",
        "category": "other",
        "date": date(2015, 11, 5),
        "order": 28
    },
    {
        "title_bn": "সেরা পেপার পুরস্কার গ্রহণ - এসএসএস ২০২৪, সিঙ্গাপুর",
        "title_en": "Receiving Best Paper Award - SSS 2024, Singapore",
        "category": "award",
        "date": date(2024, 6, 15),
        "order": 29
    },
    {
        "title_bn": "নিউরোলজিক্যাল সোসাইটি অফ ইন্ডিয়া (NUSI) ওয়ার্কশপ ২০২৪",
        "title_en": "Neurological Society of India (NUSI) Workshop 2024",
        "category": "conference",
        "date": date(2024, 4, 10),
        "order": 30
    }
]

# ডাটা ইনসার্ট করুন
for data in photos_data:
    photo = Photo.objects.create(**data)
    print(f"✅ Added Photo: {photo.title_en[:50]}... - [{photo.get_category_display()}]")

print(f"\n📊 মোট {Photo.objects.count()} টি ফটো যোগ করা হয়েছে!")

# ক্যাটাগরি অনুযায়ী কাউন্ট
print("\n📂 ক্যাটাগরি অনুযায়ী ফটো:")
for category_code, category_name in Photo.CATEGORY_CHOICES:
    count = Photo.objects.filter(category=category_code).count()
    print(f"  • {category_name}: {count} টি")

# সাজেশন: কীভাবে ছবি যোগ করবেন
print("\n" + "="*60)
print("📸 ছবি যোগ করার নির্দেশনা:")
print("="*60)
print("উপরের প্রতিটি ফটোর জন্য আপনাকে আসল ছবি ফাইল নিতে হবে:")
print("1. gallery/photos/ ফোল্ডারে ছবি রাখুন")
print("2. অথবা এডমিন প্যানেল থেকে আপলোড করুন")
print("\nউদাহরণ ছবির নাম:")
for i, photo in enumerate(Photo.objects.all()[:5], 1):
    print(f"   {i}. {photo.category}/img_{photo.id}.jpg")
print("\n🔗 ছবির সোর্স:")
print("   • কনফারেন্সের ছবি: আয়োজকদের কাছ থেকে সংগ্রহ করুন")
print("   • অ্যাওয়ার্ডের ছবি: ব্যক্তিগত সংগ্রহ থেকে")
print("   • চেম্বারের ছবি: নিজে তুলুন")
print("   • আন্তর্জাতিক প্রশিক্ষণ: সংশ্লিষ্ট প্রতিষ্ঠান থেকে")