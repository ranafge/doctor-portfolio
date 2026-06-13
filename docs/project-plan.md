# Doctor Portfolio Website - Project Plan

## প্রোজেক্ট ওভারভিউ
- নাম: Prof. Dr. Md. Shah Alam - Portfolio Website
- টেকনোলজি: Django + Vue.js
- শুরু তারিখ: [বর্তমান তারিখ]
- শেষ তারিখ: [অনুমানিক]

## অ্যাপ স্ট্রাকচার (৫টি অ্যাপ)

### 1. core (মূল অ্যাপ)
- **উদ্দেশ্য**: ওয়েবসাইটের মূল ফিচার
- **মডেল**:
  - MenuItem (মেনু আইটেম)
  - SubMenuItem (ড্রপডাউন মেনু)
  - HeroSection (হোমপেজ হিরো সেকশন)
  - DoctorProfile (ডাক্তারের প্রোফাইল)
  - FooterInfo (ফুটার তথ্য)
  - SocialLink (সোশ্যাল মিডিয়া লিংক)

### 2. content (কন্টেন্ট অ্যাপ)
- **উদ্দেশ্য**: ব্লগ, নিউজ, পাবলিকেশন
- **মডেল**:
  - BlogPost
  - News
  - Publication
  - Award

### 3. medical (মেডিকেল অ্যাপ)
- **উদ্দেশ্য**: চিকিৎসা সেবা সম্পর্কিত
- **মডেল**:
  - Condition (Spine, Shoulder, Hip, Knee ইত্যাদি)
  - Service (জেনারেল সার্ভিস)
  - Treatment (চিকিৎসা পদ্ধতি)

### 4. media (মিডিয়া অ্যাপ)
- **উদ্দেশ্য**: ফটো ও ভিডিও গ্যালারি
- **মডেল**:
  - Photo
  - Video
  - Gallery (ঐচ্ছিক)

### 5. accounts (অ্যাকাউন্টস অ্যাপ)
- **উদ্দেশ্য**: যোগাযোগ ও মেম্বারশিপ
- **মডেল**:
  - ContactMessage
  - Membership
  - SocialInvolvement

## ডেভেলপমেন্ট টাইমলাইন
- সপ্তাহ ১: Django ব্যাকএন্ড সেটআপ
- সপ্তাহ ২: মডেল ও API তৈরি
- সপ্তাহ ৩: Vue.js ফ্রন্টএন্ড
- সপ্তাহ ৪: ইন্টিগ্রেশন ও টেস্টিং
