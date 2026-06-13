# extract_blog_data.py
import os
import django
from datetime import date

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from blog.models import BlogPost

# আগের ডাটা ডিলিট করুন (চাইলে)
BlogPost.objects.all().delete()

# BlogPost মডেল অনুযায়ী ডাটা (order ফিল্ড বাদ দিয়ে)
blogs_data = [
    {
        "title_bn": "মেরুদণ্ডের ডিস্ক সমস্যা: কারণ, লক্ষণ ও চিকিৎসা",
        "title_en": "Spinal Disc Problems: Causes, Symptoms and Treatment",
        "summary_bn": "মেরুদণ্ডের ডিস্ক সমস্যা একটি সাধারণ সমস্যা। জেনে নিন কী কারণে ডিস্ক সমস্যা হয়, কী কী লক্ষণ দেখা দেয় এবং আধুনিক চিকিৎসা পদ্ধতি সম্পর্কে।",
        "summary_en": "Spinal disc problems are common. Learn about the causes, symptoms, and modern treatment options for disc problems.",
        "content_bn": """<h2>ডিস্ক সমস্যা কী?</h2>
<p>মেরুদণ্ডের প্রতিটি কশেরুকার মাঝে একটি নরম ও স্থিতিস্থাপক প্যাড থাকে যাকে ডিস্ক বলে। এই ডিস্ক আমাদের মেরুদণ্ডকে নমনীয় রাখে এবং হঠাৎ চাপ বা আঘাত থেকে কশেরুকাকে রক্ষা করে।</p>

<h2>ডিস্ক সমস্যার কারণ:</h2>
<ul>
<li>বয়স বাড়ার সাথে সাথে ডিস্ক পানিশূন্য হয়ে যায়</li>
<li>ভুল ভঙ্গিতে দীর্ঘক্ষণ বসে থাকা</li>
<li>ভারী জিনিস ভুলভাবে তোলা</li>
<li>জিনগত কারণ</li>
<li>ধূমপান</li>
</ul>

<h2>লক্ষণসমূহ:</h2>
<ul>
<li>কোমর বা ঘাড়ে ব্যথা</li>
<li>পা বা হাতে ব্যথা, অসাড়তা বা দুর্বলতা</li>
<li>হাঁটতে বা দাঁড়াতে অসুবিধা</li>
<li>প্রস্রাব বা পায়খানা নিয়ন্ত্রণে সমস্যা (জরুরি চিকিৎসা প্রয়োজন)</li>
</ul>

<h2>চিকিৎসা পদ্ধতি:</h2>
<p>আমাদের নিটর হাসপাতালে এবং ধানমন্ডির চেম্বারে আধুনিক চিকিৎসা পদ্ধতি রয়েছে:</p>
<ul>
<li>শারীরিক থেরাপি ও ব্যায়াম</li>
<li>ওষুধ ও ইনজেকশন থেরাপি</li>
<li>মিনিম্যালি ইনভেসিভ স্পাইন সার্জারি</li>
<li>মাইক্রোডিসেক্টমি</li>
<li>স্পাইন ফিউশন সার্জারি</li>
</ul>""",
        "content_en": """<h2>What is Disc Problem?</h2>
<p>Between each vertebra of the spine, there is a soft, gel-like cushion called a disc. These discs keep the spine flexible and protect vertebrae from sudden pressure or injury.</p>

<h2>Causes of Disc Problems:</h2>
<ul>
<li>Age-related disc dehydration</li>
<li>Prolonged sitting with poor posture</li>
<li>Improper lifting of heavy objects</li>
<li>Genetic factors</li>
<li>Smoking</li>
</ul>

<h2>Symptoms:</h2>
<ul>
<li>Lower back or neck pain</li>
<li>Pain, numbness, or weakness in legs or arms</li>
<li>Difficulty walking or standing</li>
<li>Loss of bladder or bowel control (emergency)</li>
</ul>

<h2>Treatment Options:</h2>
<p>At NITOR Hospital and Dhanmondi chamber, we offer modern treatments:</p>
<ul>
<li>Physical therapy and exercises</li>
<li>Medications and injection therapy</li>
<li>Minimally Invasive Spine Surgery</li>
<li>Microdiscectomy</li>
<li>Spinal Fusion Surgery</li>
</ul>""",
        "category_bn": "মেরুদণ্ডের রোগ",
        "category_en": "Spinal Disorders",
        "date": date(2024, 10, 15),
        "read_time": 8
    },
    {
        "title_bn": "স্কোলিওসিস (মেরুদণ্ডের বক্রতা): রোগীদের যা জানা জরুরি",
        "title_en": "Scoliosis (Spinal Curvature): What Patients Need to Know",
        "summary_bn": "স্কোলিওসিস একটি জটিল মেরুদণ্ডের সমস্যা। এর ধরন, রোগ নির্ণয় এবং চিকিৎসার আধুনিক পদ্ধতি সম্পর্কে বিস্তারিত জানুন।",
        "summary_en": "Scoliosis is a complex spinal problem. Learn about its types, diagnosis, and modern treatment approaches.",
        "content_bn": """<h2>স্কোলিওসিস কী?</h2>
<p>স্কোলিওসিস হলো মেরুদণ্ডের অস্বাভাবিক পার্শ্বীয় বক্রতা। সাধারণত মেরুদণ্ড সোজা থাকে, কিন্তু স্কোলিওসিসে এটি S বা C আকৃতি ধারণ করে।</p>

<h2>স্কোলিওসিসের প্রকারভেদ:</h2>
<ul>
<li><strong>ইডিওপ্যাথিক স্কোলিওসিস:</strong> সবচেয়ে সাধারণ ধরন, বিশেষ করে কিশোর-কিশোরীদের মধ্যে</li>
<li><strong>কনজেনিটাল স্কোলিওসিস:</strong> জন্মগত ত্রুটির কারণে</li>
<li><strong>নিউরোমাসকুলার স্কোলিওসিস:</strong> সেরিব্রাল প্যালসি, পেশি ডিসট্রফির কারণে</li>
<li><strong>ডিজেনারেটিভ স্কোলিওসিস:</strong> বয়স্কদের মধ্যে দেখা যায়</li>
</ul>

<h2>লক্ষণ:</h2>
<ul>
<li>কাঁধ একটু উঁচু বা নামা</li>
<li>কোমর অসম</li>
<li>একটি পা অন্যটির চেয়ে ছোট মনে হওয়া</li>
<li>মেরুদণ্ড বাঁকা দেখা</li>
<li>পিঠে ব্যথা</li>
</ul>

<h2>চিকিৎসা পদ্ধতি:</h2>
<p>আমি জাপান, যুক্তরাষ্ট্র, কানাডা এবং ভারতে প্রশিক্ষণপ্রাপ্ত। নিটর হাসপাতালে আমরা করি:</p>
<ul>
<li>পেডিকেল স্ক্রু-রড সিস্টেম দিয়ে বক্রতা সংশোধন</li>
<li>Vertebral Column Resection (VCR) - জটিল বক্রতার জন্য</li>
<li>গ্রোথ রড - শিশুদের জন্য</li>
<li>পোস্ট-অপারেটিভ রিহ্যাবিলিটেশন</li>
</ul>""",
        "content_en": """<h2>What is Scoliosis?</h2>
<p>Scoliosis is an abnormal lateral curvature of the spine. Normally the spine is straight, but in scoliosis, it takes an S or C shape.</p>

<h2>Types of Scoliosis:</h2>
<ul>
<li><strong>Idiopathic Scoliosis:</strong> Most common type, especially in adolescents</li>
<li><strong>Congenital Scoliosis:</strong> Due to birth defects</li>
<li><strong>Neuromuscular Scoliosis:</strong> Due to cerebral palsy, muscular dystrophy</li>
<li><strong>Degenerative Scoliosis:</strong> Seen in elderly</li>
</ul>

<h2>Symptoms:</h2>
<ul>
<li>Uneven shoulders</li>
<li>Asymmetric waist</li>
<li>One leg appearing shorter</li>
<li>Visible spinal curvature</li>
<li>Back pain</li>
</ul>

<h2>Treatment Options:</h2>
<p>I am trained in Japan, USA, Canada, and India. At NITOR Hospital, we offer:</p>
<ul>
<li>Curve correction with pedicle screw-rod system</li>
<li>Vertebral Column Resection (VCR) for complex curves</li>
<li>Growth rods for children</li>
<li>Post-operative rehabilitation</li>
</ul>""",
        "category_bn": "স্কোলিওসিস",
        "category_en": "Scoliosis",
        "date": date(2024, 10, 10),
        "read_time": 10
    },
    {
        "title_bn": "সার্ভিকাল স্পাইন (ঘাড়ের মেরুদণ্ড) সমস্যা: আপনার যা জানা দরকার",
        "title_en": "Cervical Spine Problems: What You Need to Know",
        "summary_bn": "ঘাড়ের ব্যথা একটি সাধারণ সমস্যা। সার্ভিকাল ডিস্ক, স্পন্ডাইলোসিস এবং আঘাতজনিত সমস্যার আধুনিক চিকিৎসা সম্পর্কে জানুন।",
        "summary_en": "Neck pain is a common problem. Learn about modern treatment for cervical disc, spondylosis, and traumatic injuries.",
        "content_bn": """<h2>সার্ভিকাল স্পাইন সমস্যা কী?</h2>
<p>সার্ভিকাল স্পাইন হলো ঘাড়ের অংশের ৭টি কশেরুকা (C1-C7)। বিভিন্ন কারণে এখানে সমস্যা হতে পারে।</p>

<h2>সাধারণ সমস্যা:</h2>
<ul>
<li>সার্ভিকাল ডিস্ক হার্নিয়েশন</li>
<li>সার্ভিকাল স্পন্ডাইলোসিস (বয়সজনিত ক্ষয়)</li>
<li>হুইপ্ল্যাশ ইনজুরি</li>
<li>সার্ভিকাল স্পাইনাল স্টেনোসিস</li>
</ul>

<h2>লক্ষণ:</h2>
<ul>
<li>ঘাড় ও কাঁধে ব্যথা</li>
<li>হাতে ব্যথা, ঝিঁঝিঁ ধরা বা অসাড়তা</li>
<li>মাথা ঘোরা</li>
<li>হাতের পেশি দুর্বল হওয়া</li>
<li>হাঁটার সময় ভারসাম্য হারানো</li>
</ul>

<h2>আমার চিকিৎসা পদ্ধতি:</h2>
<p>আমি ISIC (India), ROH (UK), এবং জাপানে প্রশিক্ষণ নিয়েছি। আধুনিক চিকিৎসার মধ্যে রয়েছে:</p>
<ul>
<li>এন্টিরিয়র সার্ভিকাল ডিকম্প্রেশন ও ফিউশন (ACDF)</li>
<li>আর্টিফিশিয়াল ডিস্ক রিপ্লেসমেন্ট</li>
<li>পোস্টেরিয়র সার্ভিকাল ফিক্সেশন (CPS/LMS)</li>
<li>মিনিম্যালি ইনভেসিভ পদ্ধতি</li>
</ul>
<p>আমাদের ১০০+ রোগীর সিরিজে সিঙ্গেল এন্টিরিয়র অ্যাপ্রোচের চমৎকার ফলাফল পেয়েছি।</p>""",
        "content_en": """<h2>What are Cervical Spine Problems?</h2>
<p>The cervical spine consists of 7 vertebrae (C1-C7) in the neck region. Problems can occur due to various reasons.</p>

<h2>Common Problems:</h2>
<ul>
<li>Cervical Disc Herniation</li>
<li>Cervical Spondylosis (age-related wear and tear)</li>
<li>Whiplash Injury</li>
<li>Cervical Spinal Stenosis</li>
</ul>

<h2>Symptoms:</h2>
<ul>
<li>Neck and shoulder pain</li>
<li>Pain, tingling or numbness in arms</li>
<li>Dizziness</li>
<li>Weakness in hand muscles</li>
<li>Loss of balance while walking</li>
</ul>

<h2>My Treatment Approach:</h2>
<p>I have trained at ISIC (India), ROH (UK), and Japan. Modern treatments include:</p>
<ul>
<li>Anterior Cervical Decompression and Fusion (ACDF)</li>
<li>Artificial Disc Replacement</li>
<li>Posterior Cervical Fixation (CPS/LMS)</li>
<li>Minimally Invasive Approaches</li>
</ul>
<p>In our series of 100+ patients, the single anterior approach has shown excellent results.</p>""",
        "category_bn": "সার্ভিকাল স্পাইন",
        "category_en": "Cervical Spine",
        "date": date(2024, 10, 5),
        "read_time": 7
    },
    {
        "title_bn": "মেরুদণ্ডের যক্ষ্মা (স্পাইনাল টিবি): চিকিৎসার আধুনিক পদ্ধতি",
        "title_en": "Spinal Tuberculosis (Spinal TB): Modern Treatment Approaches",
        "summary_bn": "মেরুদণ্ডের যক্ষ্মা একটি গুরুতর রোগ। কীভাবে এটি নির্ণয় ও চিকিৎসা করা হয় এবং আমাদের ৫৮২+ রোগীর অভিজ্ঞতা সম্পর্কে জানুন।",
        "summary_en": "Spinal TB is a serious disease. Learn about diagnosis, treatment, and our experience with 582+ patients.",
        "content_bn": """<h2>স্পাইনাল টিবি কী?</h2>
<p>মেরুদণ্ডের যক্ষ্মা একটি ব্যাকটেরিয়াজনিত সংক্রমণ যা মেরুদণ্ডকে ধ্বংস করে দেয়। এটি সাধারণত ফুসফুসের যক্ষ্মা থেকে ছড়ায়।</p>

<h2>লক্ষণ:</h2>
<ul>
<li>দীর্ঘস্থায়ী পিঠে ব্যথা (বেশি রাতে)</li>
<li>জ্বর, ওজন কমে যাওয়া</li>
<li>মেরুদণ্ডের বিকৃতি (কাইফোসিস)</li>
<li>পায়ে দুর্বলতা বা প্যারালাইসিস (জটিল ক্ষেত্রে)</li>
</ul>

<h2>আমাদের অভিজ্ঞতা:</h2>
<p>আমরা ৫৮২টি স্পাইনাল টিবি রোগীর চিকিৎসা করেছি, যা 'জার্নাল অফ স্পাইন সার্জারি' এবং 'গ্লোবাল স্পাইন জার্নাল'-এ প্রকাশিত হয়েছে।</p>

<h2>চিকিৎসা পদ্ধতি:</h2>
<ul>
<li>এন্টি-টিউবারকুলার ড্রাগ থেরাপি</li>
<li>পোস্টেরিয়র ডিকম্প্রেশন ও স্ট্যাবিলাইজেশন</li>
<li>সিঙ্গেল স্টেজ PVCR (পোস্টেরিয়র ভার্টিব্রাল কলাম রিসেকশন)</li>
<li>সার্ভিকাল ও থোরাকোলাম্বার টিবির জন্য বিশেষ পদ্ধতি</li>
</ul>""",
        "content_en": """<h2>What is Spinal TB?</h2>
<p>Spinal tuberculosis is a bacterial infection that destroys the spine. It usually spreads from pulmonary TB.</p>

<h2>Symptoms:</h2>
<ul>
<li>Chronic back pain (worse at night)</li>
<li>Fever, weight loss</li>
<li>Spinal deformity (Kyphosis)</li>
<li>Leg weakness or paralysis (in advanced cases)</li>
</ul>

<h2>Our Experience:</h2>
<p>We have treated 582 spinal TB patients, published in 'Journal of Spine Surgery' and 'Global Spine Journal'.</p>

<h2>Treatment Approaches:</h2>
<ul>
<li>Anti-tubercular drug therapy</li>
<li>Posterior decompression and stabilization</li>
<li>Single stage PVCR (Posterior Vertebral Column Resection)</li>
<li>Special approaches for cervical and thoracolumbar TB</li>
</ul>""",
        "category_bn": "স্পাইনাল টিবি",
        "category_en": "Spinal TB",
        "date": date(2024, 9, 28),
        "read_time": 9
    },
    {
        "title_bn": "মিনিম্যালি ইনভেসিভ স্পাইন সার্জারি (MISS): কম ব্যথা, দ্রুত সুস্থতা",
        "title_en": "Minimally Invasive Spine Surgery (MISS): Less Pain, Faster Recovery",
        "summary_bn": "আধুনিক মিনিম্যালি ইনভেসিভ স্পাইন সার্জারি সম্পর্কে জানুন। কীভাবে এতে কম ব্যথা, কম রক্তক্ষরণ এবং দ্রুত সুস্থতা সম্ভব।",
        "summary_en": "Learn about modern Minimally Invasive Spine Surgery. How it offers less pain, less bleeding, and faster recovery.",
        "content_bn": """<h2>মিনিম্যালি ইনভেসিভ স্পাইন সার্জারি কী?</h2>
<p>এটি একটি আধুনিক অস্ত্রোপচার পদ্ধতি যেখানে ছোট ছোট কাটাছেঁড়ার মাধ্যমে মেরুদণ্ডের সমস্যার সমাধান করা হয়।</p>

<h2>সুবিধাসমূহ:</h2>
<ul>
<li>কম ব্যথা</li>
<li>কম রক্তক্ষরণ</li>
<li>হাসপাতালে কম দিন থাকা</li>
<li>দ্রুত স্বাভাবিক জীবনে ফেরা</li>
<li>ছোট দাগ</li>
</ul>

<h2>আমরা যে MISS পদ্ধতি করি:</h2>
<ul>
<li>মাইক্রোডিসেক্টমি</li>
<li>টিউবুলার রিট্র্যাক্টর ব্যবহার করে ডিকম্প্রেশন</li>
<li>পারকিউটেনিয়াস পেডিকেল স্ক্রু ফিক্সেশন</li>
<li>এন্ডোস্কোপিক স্পাইন সার্জারি</li>
</ul>

<h2>কোন কোন সমস্যায় MISS করা যায়:</h2>
<ul>
<li>হার্নিয়েটেড ডিস্ক</li>
<li>স্পাইনাল স্টেনোসিস</li>
<li>ডিজেনারেটিভ ডিস্ক ডিজিজ</li>
<li>কিছু ধরনের ফ্র্যাকচার</li>
</ul>""",
        "content_en": """<h2>What is Minimally Invasive Spine Surgery?</h2>
<p>This is a modern surgical technique where spine problems are treated through small incisions.</p>

<h2>Benefits:</h2>
<ul>
<li>Less pain</li>
<li>Less blood loss</li>
<li>Shorter hospital stay</li>
<li>Faster return to normal life</li>
<li>Smaller scars</li>
</ul>

<h2>MISS Procedures We Perform:</h2>
<ul>
<li>Microdiscectomy</li>
<li>Tubular retractor decompression</li>
<li>Percutaneous pedicle screw fixation</li>
<li>Endoscopic spine surgery</li>
</ul>

<h2>Conditions Treatable with MISS:</h2>
<ul>
<li>Herniated disc</li>
<li>Spinal stenosis</li>
<li>Degenerative disc disease</li>
<li>Certain types of fractures</li>
</ul>""",
        "category_bn": "মিনিম্যালি ইনভেসিভ সার্জারি",
        "category_en": "Minimally Invasive Surgery",
        "date": date(2024, 9, 20),
        "read_time": 6
    },
    {
        "title_bn": "মেরুদণ্ডের আঘাত (স্পাইনাল ট্রমা): জরুরি করণীয়",
        "title_en": "Spinal Trauma: Emergency Guidelines",
        "summary_bn": "মেরুদণ্ডের আঘাত একটি জটিল অবস্থা। দুর্ঘটনার পর করণীয় এবং আধুনিক চিকিৎসা পদ্ধতি সম্পর্কে জানুন।",
        "summary_en": "Spinal trauma is a complex condition. Learn what to do after an accident and modern treatment approaches.",
        "content_bn": """<h2>দুর্ঘটনার পর করণীয়:</h2>
<ul>
<li>রোগীকে না নাড়াচাড়া করা</li>
<li>হেলমেট বা কাপড় সরানো যাবে না</li>
<li>অবিলম্বে হাসপাতালে ভর্তি করা</li>
<li>স্ট্রেচারে সোজা করে নিয়ে যাওয়া</li>
</ul>

<h2>আমাদের চিকিৎসা পদ্ধতি:</h2>
<p>আমি এসওপি অরথোপেডিক হসপিটাল (জাপান) এবং ডেনভার (USA) এ প্রশিক্ষণ নিয়েছি। নিটর হাসপাতালে আমরা করি:</p>
<ul>
<li>সার্ভিকাল, থোরাসিক ও লাম্বার ফ্র্যাকচারের জন্য নির্দিষ্ট পদ্ধতি</li>
<li>এন্টিরিয়র ডিকম্প্রেশন ও স্ট্যাবিলাইজেশন</li>
<li>পোস্টেরিয়র পেডিকেল স্ক্রু ফিক্সেশন</li>
<li>শর্ট ও লং সেগমেন্ট ফিক্সেশন</li>
<li>সিঙ্গেল স্টেজ পোস্টেরিয়র সার্জারি</li>
</ul>

<h2>কেন রোগীরা আমাদের বেছে নেন:</h2>
<ul>
<li>আমাদের ৯১+ সার্ভিকাল ইনজুরি রোগীর সিরিজে চমৎকার ফলাফল</li>
<li>আন্তর্জাতিক প্রশিক্ষণ ও দক্ষতা</li>
<li>আধুনিক অপারেশন থিয়েটার ও ইমেজিং</li>
</ul>""",
        "content_en": """<h2>What to do after an accident:</h2>
<ul>
<li>Do not move the patient</li>
<li>Do not remove helmet or clothes</li>
<li>Immediate hospitalization</li>
<li>Transport on a rigid stretcher</li>
</ul>

<h2>Our Treatment Approaches:</h2>
<p>I trained at SOP Orthopedic Hospital (Japan) and Denver (USA). At NITOR Hospital, we perform:</p>
<ul>
<li>Specific approaches for cervical, thoracic & lumbar fractures</li>
<li>Anterior decompression & stabilization</li>
<li>Posterior pedicle screw fixation</li>
<li>Short & long segment fixation</li>
<li>Single stage posterior surgery</li>
</ul>

<h2>Why Patients Choose Us:</h2>
<ul>
<li>Excellent results in our 91+ cervical injury patient series</li>
<li>International training & expertise</li>
<li>Modern OT and imaging facilities</li>
</ul>""",
        "category_bn": "স্পাইনাল ট্রমা",
        "category_en": "Spinal Trauma",
        "date": date(2024, 9, 15),
        "read_time": 7
    }
]

# ডাটা ইনসার্ট করুন
for data in blogs_data:
    blog = BlogPost.objects.create(**data)
    print(f"✅ Added Blog: {blog.title_en[:50]}... - {blog.date}")

print(f"\n📊 মোট {BlogPost.objects.count()} টি ব্লগ পোস্ট যোগ করা হয়েছে!")

# ক্যাটাগরি অনুযায়ী কাউন্ট দেখান
print("\n📚 ক্যাটাগরি অনুযায়ী ব্লগ পোস্ট:")
categories = BlogPost.objects.values_list('category_en', flat=True).distinct()
for category in categories:
    count = BlogPost.objects.filter(category_en=category).count()
    print(f"  • {category}: {count} টি")

# সাম্প্রতিক ব্লগ দেখান
print(f"\n📝 সাম্প্রতিক ৩টি ব্লগ পোস্ট:")
recent_blogs = BlogPost.objects.all()[:3]
for blog in recent_blogs:
    print(f"  • {blog.date.strftime('%d-%m-%Y')}: {blog.title_en}")
    print(f"    🕐 {blog.read_time} min read | 📂 {blog.category_en}")