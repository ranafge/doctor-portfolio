import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from services.models import Service

# Delete existing services (optional)
Service.objects.all().delete()

# Services data with 100% WORKING icons
services_data = [
    {
        "icon": "fas fa-stethoscope",
        "title_bn": "মেরুদণ্ডের অস্ত্রোপচার",
        "title_en": "Spine Surgery",
        "description_bn": "সব ধরনের মেরুদণ্ডের জটিল অস্ত্রোপচার যেমন হার্নিয়েটেড ডিস্ক, স্পাইনাল স্টেনোসিস, স্পন্ডাইলোলিস্থেসিস ইত্যাদি।",
        "description_en": "All types of complex spine surgeries including herniated disc, spinal stenosis, spondylolisthesis, etc.",
        "order": 1
    },
    {
        "icon": "fas fa-child",
        "title_bn": "স্কোলিওসিস সার্জারি",
        "title_en": "Scoliosis Surgery",
        "description_bn": "কিশোর ও প্রাপ্তবয়স্কদের স্কোলিওসিস (মেরুদণ্ডের বক্রতা) সংশোধনে অস্ত্রোপচার।",
        "description_en": "Surgical correction of scoliosis (spinal curvature) in adolescents and adults.",
        "order": 2
    },
    {
        "icon": "fas fa-lungs",
        "title_bn": "স্পাইন টিউবারকিউলোসিস চিকিৎসা",
        "title_en": "Spinal TB Treatment",
        "description_bn": "মেরুদণ্ডের যক্ষ্মা রোগের অস্ত্রোপচার ও চিকিৎসা ব্যবস্থাপনা।",
        "description_en": "Surgical and medical management of spinal tuberculosis.",
        "order": 3
    },
    {
        "icon": "fas fa-arrow-up",  # ✅ FIXED - Working icon for Cervical (neck/upper spine)
        "title_bn": "সার্ভিকাল স্পাইন সার্জারি",
        "title_en": "Cervical Spine Surgery",
        "description_bn": "ঘাড়ের মেরুদণ্ডের ডিস্ক, ইনজুরি ও অন্যান্য সমস্যার অস্ত্রোপচার।",
        "description_en": "Surgery for cervical disc, injury and other neck spine problems.",
        "order": 4
    },
    {
        "icon": "fas fa-walking",
        "title_bn": "লাম্বার স্পাইন সার্জারি",
        "title_en": "Lumbar Spine Surgery",
        "description_bn": "কোমরের মেরুদণ্ডের ডিস্ক, স্টেনোসিস ও ফ্র্যাকচারের অস্ত্রোপচার।",
        "description_en": "Surgery for lumbar disc, stenosis and fracture of the lower back.",
        "order": 5
    },
    {
        "icon": "fas fa-truck-medical",
        "title_bn": "স্পাইন ট্রমা সার্জারি",
        "title_en": "Spinal Trauma Surgery",
        "description_bn": "মেরুদণ্ডের আঘাতজনিত ফ্র্যাকচার ও ডিসলোকেশনের অস্ত্রোপচার।",
        "description_en": "Surgery for traumatic fractures and dislocations of the spine.",
        "order": 6
    },
    {
        "icon": "fas fa-sync-alt",
        "title_bn": "স্পাইন ডিফরমিটি সংশোধন",
        "title_en": "Spinal Deformity Correction",
        "description_bn": "কাইফোসিস (অতিরিক্ত বাঁকা) ও অন্যান্য মেরুদণ্ডের বিকৃতি সংশোধন।",
        "description_en": "Correction of kyphosis (excessive curvature) and other spinal deformities.",
        "order": 7
    },
    {
        "icon": "fas fa-microscope",
        "title_bn": "মিনিম্যালি ইনভেসিভ স্পাইন সার্জারি",
        "title_en": "Minimally Invasive Spine Surgery",
        "description_bn": "কম কাটাছেঁড়া ও দ্রুত সুস্থতা নিশ্চিত করে আধুনিক পদ্ধতিতে মেরুদণ্ডের অস্ত্রোপচার।",
        "description_en": "Spine surgery using modern techniques with less incision and faster recovery.",
        "order": 8
    }
]

# Bulk create services
for data in services_data:
    Service.objects.create(**data)

print(f"✅ Added {len(services_data)} services")