# extract_videos.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from gallery.models import Video

# আগের ডাটা ডিলিট করুন (চাইলে)
Video.objects.all().delete()

# ডা. শরীফ আহমেদ জোনায়েদের স্পাইন সার্জারি সম্পর্কিত ভিডিও ডাটা
videos_data = [
    {
        "title_bn": "মেরুদণ্ডের ডিস্ক সমস্যা ও চিকিৎসা - স্পাইন সার্জন ডা. জোনায়েদ",
        "title_en": "Spinal Disc Problems and Treatment - Spine Surgeon Dr. Jonayed",
        "description_bn": "মেরুদণ্ডের ডিস্ক হার্নিয়েশন, এর কারণ, লক্ষণ এবং আধুনিক চিকিৎসা পদ্ধতি নিয়ে বিস্তারিত আলোচনা। মাইক্রোডিসেক্টমি ও মিনিম্যালি ইনভেসিভ সার্জারি সম্পর্কে জানুন।",
        "description_en": "Detailed discussion on disc herniation, causes, symptoms, and modern treatment options including microdiscectomy and minimally invasive spine surgery.",
        "youtube_id": "dQw4w9WgXcQ",  # উদাহরণ ID, 실제 ID দিন
        "category_bn": "ডিস্ক সমস্যা",
        "category_en": "Disc Problems",
        "duration": "12:34",
        "views": "15K",
        "is_featured": True,
        "order": 1
    },
    {
        "title_bn": "স্কোলিওসিস (মেরুদণ্ডের বক্রতা) - কারণ ও চিকিৎসা",
        "title_en": "Scoliosis (Spinal Curvature) - Causes and Treatment",
        "description_bn": "কিশোর ও প্রাপ্তবয়স্কদের স্কোলিওসিস, রোগ নির্ণয় পদ্ধতি, বক্রতা সংশোধনে পেডিকেল স্ক্রু-রড সিস্টেম এবং অস্ত্রোপচার নিয়ে বিস্তারিত ভিডিও।",
        "description_en": "Complete guide on adolescent and adult scoliosis, diagnostic methods, pedicle screw-rod system for curve correction, and surgical treatment.",
        "youtube_id": "dQw4w9WgXcR",
        "category_bn": "স্কোলিওসিস",
        "category_en": "Scoliosis",
        "duration": "15:21",
        "views": "8.5K",
        "is_featured": True,
        "order": 2
    },
    {
        "title_bn": "সার্ভিকাল স্পন্ডাইলোসিস (ঘাড়ের ব্যথা) - ঘরোয়া ব্যায়াম ও চিকিৎসা",
        "title_en": "Cervical Spondylosis (Neck Pain) - Home Exercises & Treatment",
        "description_bn": "ঘাড়ের ব্যথা, সার্ভিকাল ডিস্ক সমস্যা, ঘরোয়া ব্যায়াম, ফিজিওথেরাপি এবং প্রয়োজনীয় চিকিৎসা পদ্ধতি নিয়ে আলোচনা।",
        "description_en": "Comprehensive discussion on neck pain, cervical disc problems, home exercises, physiotherapy, and necessary treatment approaches.",
        "youtube_id": "dQw4w9WgXcS",
        "category_bn": "সার্ভিকাল স্পাইন",
        "category_en": "Cervical Spine",
        "duration": "10:45",
        "views": "22K",
        "is_featured": False,
        "order": 3
    },
    {
        "title_bn": "লাম্বার স্পাইনাল স্টেনোসিস - কোমর ও পায়ে ব্যথার কারণ",
        "title_en": "Lumbar Spinal Stenosis - Cause of Back and Leg Pain",
        "description_bn": "স্পাইনাল স্টেনোসিস কী? কেন কোমর ও পায়ে ব্যথা হয়? চিকিৎসার আধুনিক পদ্ধতি এবং কখন অস্ত্রোপচার প্রয়োজন।",
        "description_en": "What is spinal stenosis? Why do back and leg pain occur? Modern treatment methods and when surgery is needed.",
        "youtube_id": "dQw4w9WgXcT",
        "category_bn": "লাম্বার স্পাইন",
        "category_en": "Lumbar Spine",
        "duration": "11:18",
        "views": "12K",
        "is_featured": False,
        "order": 4
    },
    {
        "title_bn": "মিনিম্যালি ইনভেসিভ স্পাইন সার্জারি (MISS) - কম ব্যথা, দ্রুত সুস্থতা",
        "title_en": "Minimally Invasive Spine Surgery (MISS) - Less Pain, Fast Recovery",
        "description_bn": "MISS পদ্ধতির সুবিধা, কীভাবে ছোট কাটাছেঁড়ায় অস্ত্রোপচার করা হয়, রোগীর দ্রুত সুস্থতা এবং আধুনিক প্রযুক্তি নিয়ে বিস্তারিত।",
        "description_en": "Benefits of MISS, how surgery is done with small incisions, faster patient recovery, and modern technology details.",
        "youtube_id": "dQw4w9WgXcU",
        "category_bn": "মিনিম্যালি ইনভেসিভ সার্জারি",
        "category_en": "Minimally Invasive Surgery",
        "duration": "14:03",
        "views": "9.8K",
        "is_featured": True,
        "order": 5
    },
    {
        "title_bn": "স্পাইনাল টিবি (মেরুদণ্ডের যক্ষ্মা) - লক্ষণ ও চিকিৎসা",
        "title_en": "Spinal TB (Tuberculosis of Spine) - Symptoms & Treatment",
        "description_bn": "মেরুদণ্ডের যক্ষ্মা রোগের কারণ, লক্ষণ, ওষুধ থেরাপি এবং জটিল ক্ষেত্রে অস্ত্রোপচারের প্রয়োজনীয়তা নিয়ে আলোচনা।",
        "description_en": "Discussion on causes, symptoms, drug therapy of spinal tuberculosis and necessity of surgery in complex cases.",
        "youtube_id": "dQw4w9WgXcV",
        "category_bn": "স্পাইনাল টিবি",
        "category_en": "Spinal TB",
        "duration": "13:42",
        "views": "6.2K",
        "is_featured": False,
        "order": 6
    },
    {
        "title_bn": "স্পন্ডাইলোলিস্থেসিস - কশেরুকা সরে যাওয়ার সমস্যা ও চিকিৎসা",
        "title_en": "Spondylolisthesis - Vertebral Slippage & Treatment",
        "description_bn": "Spondylolisthesis কী? কেন কশেরুকা সরে যায়? গ্রেড অনুযায়ী চিকিৎসা এবং স্পাইন ফিউশন সার্জারি নিয়ে বিস্তারিত।",
        "description_en": "What is Spondylolisthesis? Why does vertebra slip? Grade-wise treatment and spine fusion surgery details.",
        "youtube_id": "dQw4w9WgXcW",
        "category_bn": "স্পন্ডাইলোলিস্থেসিস",
        "category_en": "Spondylolisthesis",
        "duration": "12:55",
        "views": "7.4K",
        "is_featured": False,
        "order": 7
    },
    {
        "title_bn": "স্পাইন ট্রমা ও ফ্র্যাকচার - দুর্ঘটনার পর করণীয়",
        "title_en": "Spinal Trauma & Fracture - What to Do After Accident",
        "description_bn": "মেরুদণ্ডের আঘাত, ফ্র্যাকচারের ধরন, জরুরি অবস্থায় করণীয় এবং আধুনিক অস্ত্রোপচার পদ্ধতি নিয়ে আলোচনা।",
        "description_en": "Discussion on spinal injury, types of fractures, emergency measures, and modern surgical procedures.",
        "youtube_id": "dQw4w9WgXcX",
        "category_bn": "স্পাইন ট্রমা",
        "category_en": "Spinal Trauma",
        "duration": "16:20",
        "views": "5.1K",
        "is_featured": True,
        "order": 8
    },
    {
        "title_bn": "পোস্ট-অপারেটিভ কেয়ার - অস্ত্রোপচারের পর রোগীর করণীয়",
        "title_en": "Post-Operative Care - What Patients Should Do After Surgery",
        "description_bn": "স্পাইন সার্জারির পর পুনর্বাসন, ব্যায়াম, খাদ্যাভ্যাস এবং সতর্কতা সম্পর্কে প্রয়োজনীয় তথ্য।",
        "description_en": "Essential information about rehabilitation, exercises, diet, and precautions after spine surgery.",
        "youtube_id": "dQw4w9WgXcY",
        "category_bn": "পোস্ট-অপারেটিভ কেয়ার",
        "category_en": "Post-Operative Care",
        "duration": "09:48",
        "views": "4.3K",
        "is_featured": False,
        "order": 9
    },
    {
        "title_bn": "স্পাইন সার্জারির আধুনিক প্রযুক্তি - ৩ডি ন্যাভিগেশন ও রোবোটিক্স",
        "title_en": "Modern Technology in Spine Surgery - 3D Navigation & Robotics",
        "description_bn": "আধুনিক স্পাইন সার্জারিতে 3D ন্যাভিগেশন, রোবোটিক্স, ইন্ট্রাঅপারেটিভ মনিটরিং নিয়ে বিশেষ আলোচনা।",
        "description_en": "Special discussion on 3D navigation, robotics, intraoperative monitoring in modern spine surgery.",
        "youtube_id": "dQw4w9WgXcZ",
        "category_bn": "আধুনিক প্রযুক্তি",
        "category_en": "Modern Technology",
        "duration": "18:15",
        "views": "3.8K",
        "is_featured": False,
        "order": 10
    }
]

# ডাটা ইনসার্ট করুন
for data in videos_data:
    video = Video.objects.create(**data)
    print(f"✅ Added Video: {video.title_en[:50]}... - [{video.duration}]")

print(f"\n📊 মোট {Video.objects.count()} টি ভিডিও যোগ করা হয়েছে!")

# ক্যাটাগরি অনুযায়ী কাউন্ট
print("\n📂 ক্যাটাগরি অনুযায়ী ভিডিও:")
categories = Video.objects.values_list('category_en', flat=True).distinct()
for category in categories:
    count = Video.objects.filter(category_en=category).count()
    featured_count = Video.objects.filter(category_en=category, is_featured=True).count()
    print(f"  • {category}: {count} টি (Feature: {featured_count} টি)")

# Featured ভিডিও দেখান
print(f"\n⭐ Featured ভিডিও ({Video.objects.filter(is_featured=True).count()} টি):")
featured = Video.objects.filter(is_featured=True)
for video in featured:
    print(f"  • {video.title_en[:45]}... - {video.duration}")
    print(f"    🔗 Embed URL: {video.embed_url}")

# Sample embed URL দেখান
print(f"\n🔗 ভিডিও Embed URL এর উদাহরণ:")
sample = Video.objects.first()
print(f"  YouTube Embed URL: {sample.embed_url}")