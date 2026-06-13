# extract_awards.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from awards.models import Award

# আগের ডাটা ডিলিট করুন (চাইলে)
Award.objects.all().delete()

# CV থেকে Extract করা Awards এবং Achievements
awards_data = [
    {
        "icon": "fas fa-user-graduate",
        "title_bn": "এপিওএ ইয়াং অ্যাম্বাসেডর",
        "title_en": "APOA Young Ambassador",
        "organization_bn": "এশিয়া প্যাসিফিক অর্থোপেডিক অ্যাসোসিয়েশন",
        "organization_en": "Asia Pacific Orthopaedic Association (APOA)",
        "year": 2018,
        "order": 1
    },
    {
        "icon": "fas fa-award",
        "title_bn": "সেরা পেপার পুরস্কার",
        "title_en": "Best Paper Award",
        "organization_bn": "বিওএসকন (BOSCON)",
        "organization_en": "BOSCON",
        "year": 2018,
        "order": 2
    },
    {
        "icon": "fas fa-globe-asia",
        "title_bn": "এপিএসএস ট্রাভেলিং ফেলো",
        "title_en": "APSS Travelling Fellow",
        "organization_bn": "এশিয়া প্যাসিফিক স্পাইন সোসাইটি",
        "organization_en": "Asia Pacific Spine Society (APSS)",
        "year": 2017,
        "order": 3
    },
    {
        "icon": "fas fa-stethoscope",
        "title_bn": "এও স্পাইন ইন্টারন্যাশনাল ফেলো",
        "title_en": "AO Spine International Fellow",
        "organization_bn": "এও স্পাইন",
        "organization_en": "AO Spine",
        "year": 2018,
        "order": 4
    },
    {
        "icon": "fas fa-trophy",
        "title_bn": "এসআরএস ট্রাভেলিং ফেলো",
        "title_en": "SRS Travelling Fellow",
        "organization_bn": "স্কোলিওসিস রিসার্চ সোসাইটি",
        "organization_en": "Scoliosis Research Society (SRS)",
        "year": 2023,
        "order": 5
    },
    {
        "icon": "fas fa-medal",
        "title_bn": "এপিওএ ইয়াং অ্যাম্বাসেডর",
        "title_en": "APOA Young Ambassador",
        "organization_bn": "এশিয়া প্যাসিফিক অর্থোপেডিক অ্যাসোসিয়েশন",
        "organization_en": "Asia Pacific Orthopaedic Association",
        "year": 2018,
        "order": 6
    },
    {
        "icon": "fas fa-passport",
        "title_bn": "এও স্পাইন এশিয়া প্যাসিফিক ফেলো",
        "title_en": "AO Spine Asia Pacific Fellow",
        "organization_bn": "এও স্পাইন এশিয়া প্যাসিফিক",
        "organization_en": "AO Spine Asia Pacific",
        "year": 2015,
        "order": 7
    },
    {
        "icon": "fas fa-university",
        "title_bn": "এপিএসএস ডেপুই সিন্থেস স্পাইন ট্রাভেলিং ফেলো",
        "title_en": "APSS Depuy Synthes Spine Travelling Fellow",
        "organization_bn": "এশিয়া প্যাসিফিক স্পাইন সোসাইটি",
        "organization_en": "Asia Pacific Spine Society (APSS)",
        "year": 2017,
        "order": 8
    }
]

# ডাটা ইনসার্ট করুন
for data in awards_data:
    award = Award.objects.create(**data)
    print(f"✅ Added Award: {award.title_en} - {award.organization_en} ({award.year})")

print(f"\n📊 মোট {Award.objects.count()} টি অ্যাওয়ার্ড যোগ করা হয়েছে!")

# বছর অনুযায়ী কাউন্ট দেখান
print("\n📅 বছর অনুযায়ী অ্যাওয়ার্ড:")
years = Award.objects.values_list('year', flat=True).distinct().order_by('-year')
for year in years:
    count = Award.objects.filter(year=year).count()
    print(f"  {year}: {count} টি")