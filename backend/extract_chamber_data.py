# extract_chamber_data.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

# সঠিকভাবে Chamber মডেল ইম্পোর্ট করুন (services না, chamber থেকে)
from chamber.models import Chamber

# আগের ডাটা ডিলিট করুন (চাইলে)
Chamber.objects.all().delete()

# CV থেকে extract করা Chamber তথ্য
chambers_data = [
    {
        "name_bn": "ন্যাশনাল ইনস্টিটিউট অব ট্রমাটোলজি এন্ড অর্থোপেডিক রিহ্যাবিলিটেশন (নিটর)",
        "name_en": "National Institute of Traumatology & Orthopaedic Rehabilitation (NITOR)",
        "subtitle_bn": "মেরুদণ্ড বিভাগের সহযোগী অধ্যাপক",
        "subtitle_en": "Associate Professor (Spine Surgery)",
        "address_bn": "শের-এ-বাংলা নগর, ঢাকা-১২০৭, বাংলাদেশ",
        "address_en": "Sher-E-Bangla Nagar, Dhaka-1207, Bangladesh",
        "time_bn": "সকাল ৯:০০ - বিকাল ৫:০০",
        "time_en": "9:00 AM - 5:00 PM",
        "days_bn": "রবিবার থেকে বৃহস্পতিব",
        "days_en": "Sunday to Thursday",
        "phone": "+8801711445840",
        "map_url": "https://maps.google.com/?q=NITOR,Dhaka",
        "order": 1
    },
    {
        "name_bn": "ডাঃ জোনায়েদ স্পাইন অ্যান্ড অর্থো কেয়ার সেন্টার",
        "name_en": "Dr. Jonayed Spine & Ortho Care Center",
        "subtitle_bn": "মেরুদণ্ড ও অর্থোপেডিক বিশেষজ্ঞ চিকিৎসা কেন্দ্র",
        "subtitle_en": "Spine & Orthopedic Specialist Care Center",
        "address_bn": "হাউস# ২৩, ফ্ল্যাট নং-৫বি, রোড# ৬, ধানমন্ডি, ঢাকা, বাংলাদেশ",
        "address_en": "House# 23, Flat No-5B, Road# 6, Dhanmondi, Dhaka, Bangladesh",
        "time_bn": "সন্ধ্যা ৬:০০ - রাত ৯:০০",
        "time_en": "6:00 PM - 9:00 PM",
        "days_bn": "শনিবার ও সোমবার",
        "days_en": "Saturday & Monday",
        "phone": "+8801711445840",
        "map_url": "https://maps.google.com/?q=Dhanmondi,Dhaka",
        "order": 2
    }
]

# ডাটা ইনসার্ট করুন
for data in chambers_data:
    chamber = Chamber.objects.create(**data)
    print(f"✅ Added: {chamber.name_en}")

print(f"\n📊 মোট {Chamber.objects.count()} টি চেম্বার যোগ করা হয়েছে!")

# দেখুন কি কি যোগ হয়েছে
print("\n📋 চেম্বার লিস্ট:")
for chamber in Chamber.objects.all():
    print(f"  {chamber.order}. {chamber.name_en}")
    print(f"     📍 {chamber.address_en[:50]}...")
    print(f"     🕐 {chamber.time_en} | {chamber.days_en}")
    print()