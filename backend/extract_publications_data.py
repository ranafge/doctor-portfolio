# extract_publications.py
import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
django.setup()

from publications.models import Publication

# আগের ডাটা ডিলিট করুন (চাইলে)
Publication.objects.all().delete()

# CV থেকে Extract করা Publications
publications_data = [
    {
        "number": 1,
        "title": "Results of Anterior decompression & stabilization by cervical plate & screws in traumatic lower incomplete cervical spine injury",
        "journal": "Journal of Bangladesh Orthopaedic Society",
        "year": 2011,
        "tag": "Cervical Spine",
        "url": "",
        "order": 1
    },
    {
        "number": 2,
        "title": "Comparative study between conservative and operative management of traumatic unstable lower cervical spine injury with incomplete neurological lesion",
        "journal": "Journal of Bangladesh Orthopaedic Society",
        "year": 2012,
        "tag": "Cervical Spine",
        "url": "",
        "order": 2
    },
    {
        "number": 3,
        "title": "Correction of adolescent idiopathic scoliosis using pedicle screw-rod system: surgical technique & results",
        "journal": "Journal of Bangladesh Orthopaedic Society",
        "year": 2012,
        "tag": "Scoliosis",
        "url": "",
        "order": 3
    },
    {
        "number": 4,
        "title": "The role of selective nerve root block in the treatment of radicular leg pain",
        "journal": "Mymensingh Med Journal",
        "year": 2016,
        "tag": "Pain Management",
        "url": "",
        "order": 4
    },
    {
        "number": 5,
        "title": "Surgery for Spinal Tuberculosis: Multicenter Experience of 582 Cases",
        "journal": "Journal of Spine Surgery",
        "year": 2015,
        "tag": "Spinal TB",
        "url": "",
        "order": 5
    },
    {
        "number": 6,
        "title": "Correction of Cubitus Varus Deformity by Lateral Closing Wedge Osteotomy",
        "journal": "Journal of Bangladesh Orthopaedic Society",
        "year": 2015,
        "tag": "Orthopedics",
        "url": "",
        "order": 6
    },
    {
        "number": 7,
        "title": "Anterior Cervical Decompression, Fusion, and Stabilization by Cervical Plate and Screw for Traumatic Lower Cervical Spinal Injury: A Series of 62 Patients",
        "journal": "Global Spine Journal",
        "year": 2016,
        "tag": "Cervical Spine",
        "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=iYrohSIAAAAJ&sortby=pubdate&citation_for_view=iYrohSIAAAAJ:IjCSPb-OGe4C",
        "order": 7
    },
    {
        "number": 8,
        "title": "Surgery for spinal tuberculosis: a multi-center experience of 582 case",
        "journal": "Global Spine Journal",
        "year": 2016,
        "tag": "Spinal TB",
        "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=iYrohSIAAAAJ&sortby=pubdate&citation_for_view=iYrohSIAAAAJ:UeHWp8X0CEIC",
        "order": 8
    },
    {
        "number": 9,
        "title": "Three Column Fixation: A Dynamic Method in Scoliosis Surgery",
        "journal": "Global Spine Journal",
        "year": 2016,
        "tag": "Scoliosis",
        "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=iYrohSIAAAAJ&sortby=pubdate&citation_for_view=iYrohSIAAAAJ:qjMakFHDy7sC",
        "order": 9
    },
    {
        "number": 10,
        "title": "Utility of Fusion Surgery in Patients with Degenerative Lumbar Spondylolisthesis and their Outcome",
        "journal": "Global Spine Journal",
        "year": 2016,
        "tag": "Lumbar Spine",
        "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=iYrohSIAAAAJ&sortby=pubdate&citation_for_view=iYrohSIAAAAJ:u5HHmVD_uO8C",
        "order": 10
    },
    {
        "number": 11,
        "title": "Impact of COVID-19 in orthopaedic practice: What we must know",
        "journal": "Journal of Orthopaedics and Spine",
        "year": 2020,
        "tag": "COVID-19",
        "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=iYrohSIAAAAJ&sortby=pubdate&citation_for_view=iYrohSIAAAAJ:Y0pCki6q_DkC",
        "order": 11
    },
    {
        "number": 12,
        "title": "Efficacy, safety, and reliability of surgery on the lumbar spine under general versus spinal anesthesia- an analysis of 64 cases",
        "journal": "Journal of Clinical Orthopaedics and Trauma",
        "year": 2021,
        "tag": "Lumbar Spine",
        "url": "",
        "order": 12
    },
    {
        "number": 13,
        "title": "Short Segment Pedicle Screw Fixation Including Fracture Vertebrae for the Management of Unstable Thoracolumbar Burst Fracture",
        "journal": "Mymensingh Med Journal",
        "year": 2021,
        "tag": "Trauma",
        "url": "",
        "order": 13
    },
    {
        "number": 14,
        "title": "Efficacy, Safety, and Reliability of the Single Anterior Approach for Subaxial Cervical Spine Dislocation",
        "journal": "Cureus",
        "year": 2023,
        "tag": "Cervical Spine",
        "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=iYrohSIAAAAJ&sortby=pubdate&citation_for_view=iYrohSIAAAAJ:WF5omc3nYNoC",
        "order": 14
    },
    {
        "number": 15,
        "title": "Long-Segment Versus Short-Segment Pedicle Screw Fixation Including Fractured Vertebrae for the Management of Unstable Thoracolumbar Burst Fractures",
        "journal": "Cureus",
        "year": 2023,
        "tag": "Trauma",
        "url": "https://scholar.google.com/citations?view_op=view_citation&hl=en&user=iYrohSIAAAAJ&sortby=pubdate&citation_for_view=iYrohSIAAAAJ:ufrVoPGSRksC",
        "order": 15
    }
]

# ডাটা ইনসার্ট করুন
for data in publications_data:
    publication = Publication.objects.create(**data)
    print(f"✅ Added Publication {publication.number}: {publication.title[:50]}...")

print(f"\n📊 মোট {Publication.objects.count()} টি পাবলিকেশন যোগ করা হয়েছে!")

# ক্যাটাগরি ওয়াইজ কাউন্ট দেখান
print("\n📚 ক্যাটাগরি অনুযায়ী পাবলিকেশন:")
tags = Publication.objects.values_list('tag', flat=True).distinct()
for tag in tags:
    count = Publication.objects.filter(tag=tag).count()
    print(f"  {tag}: {count} টি")