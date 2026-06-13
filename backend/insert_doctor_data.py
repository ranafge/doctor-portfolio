import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')  # Change 'your_project' to your project name
django.setup()

from doctor.models import DoctorProfile, Qualification  # Change 'your_app' to your app name

# Create DoctorProfile
# First, create or get the doctor
doctor, created = DoctorProfile.objects.get_or_create(
    phone="+8801977063412",
    defaults={
        "name_bn": "প্রফেসর ডা. মো. শাহ আলম",
        "name_en": "Prof. Dr. Md Shah Alam",
        "title_bn": "প্রাক্তন বিভাগীয় প্রধান, নিউরোলজি বিভাগ",
        "title_en": "Former Head of Department, Neurology",
        "speciality_bn": "নিউরোলজি বিশেষজ্ঞ",
        "speciality_en": "Neurology Specialist",
        "hospital_bn": "ঢাকা মেডিকেল কলেজ হাসপাতাল, ঢাকা",
        "hospital_en": "Dhaka Medical College Hospital, Dhaka",
        "address_bn": "১০ মেইন রোড, কল্যাণপুর বাস স্ট্যান্ড, ঢাকা-১২১৬",
        "address_en": "10 Main Road, Kalyanpur Bus Stand, Dhaka-1216",
        "email": "dr.s.alam@hotmail.com",
        "experience_years": 30,
        "patients_count": 50000,
        "publications_count": 500,
    }
)

# Corrected qualifications data
qualifications_list = [
    {
        "degree": "MBBS", 
        "institution_bn": "ঢাকা মেডিকেল কলেজ, ঢাকা বিশ্ববিদ্যালয়", 
        "institution_en": "Dhaka Medical College, University of Dhaka", 
        "year": 1985, 
        "order": 1
    },
    {
        "degree": "FCPS (Medicine)", 
        "institution_bn": "Bangladesh College of Physicians and Surgeons", 
        "institution_en": "Bangladesh College of Physicians and Surgeons", 
        "year": 1992, 
        "order": 2
    },
    {
        "degree": "MD (Neurology)", 
        "institution_bn": "Bangabandhu Sheikh Mujib Medical University", 
        "institution_en": "Bangabandhu Sheikh Mujib Medical University", 
        "year": 1997, 
        "order": 3
    },
    {
        "degree": "Fellowship (Neurology)", 
        "institution_bn": "National Neuroscience Institute, Singapore", 
        "institution_en": "National Neuroscience Institute, Singapore", 
        "year": 2002, 
        "order": 4
    },
]

# Insert qualifications
for q in qualifications_list:
    Qualification.objects.create(
        doctor=doctor,
        degree=q["degree"],
        institution_bn=q["institution_bn"],
        institution_en=q["institution_en"],
        year=q["year"],
        order=q["order"]
    )

print(f"✅ Added {len(qualifications_list)} qualifications for {doctor.name_en}")