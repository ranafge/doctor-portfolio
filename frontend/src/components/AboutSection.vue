<template>
  <section id="about">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-eyebrow">{{ t("পরিচিতি", "About") }}</span>
        <h2 class="section-title">{{ t("আমার সম্পর্কে", "About Me") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div v-if="profile" class="about-grid">
        <!-- বাম কলাম -->
        <div class="about-img-box fade-left">
          <div class="doc-avatar">
            <img v-if="profile.photo" :src="profile.photo" :alt="profile.name_bn" />
            <i v-else class="fas fa-user-md" style="font-size:4rem;color:rgba(255,255,255,0.5)"></i>
          </div>
          <h3>{{ t(profile.name_bn, profile.name_en) }}</h3>
          <p>MBBS, FCPS, MD (Neurology)<br>{{ t("নিউরোলজি বিশেষজ্ঞ", "Neurology Specialist") }}</p>
          <div class="about-badges">
            <span class="badge">{{ t("স্ট্রোক বিশেষজ্ঞ", "Stroke Specialist") }}</span>
            <span class="badge">{{ t("মৃগীরোগ", "Epilepsy") }}</span>
            <span class="badge">{{ t("মাইগ্রেন", "Migraine") }}</span>
            <span class="badge">{{ t("স্নায়ুরোগ", "Neurology") }}</span>
          </div>
        </div>

        <!-- ডান কলাম -->
        <div class="about-content fade-right">
          <h3>{{ t("বিস্তারিত পরিচয়", "Detailed Profile") }}</h3>

          <!-- সংক্ষিপ্ত টেক্সট — সবসময় দেখায় -->
          <p>{{ t(
            "প্রফেসর ডা. মো. শাহ আলম বাংলাদেশের অন্যতম বিশিষ্ট নিউরোলজি বিশেষজ্ঞ। তিনি দীর্ঘ ৩০ বছরেরও বেশি সময় ধরে স্নায়ুরোগ চিকিৎসায় নিবেদিত।",
            "Prof. Dr. Md Shah Alam is one of Bangladesh\'s most distinguished neurologists with over 30 years of dedicated service in neurological medicine."
          ) }}</p>

          <!-- বিস্তারিত টেক্সট — শুধু expanded হলে দেখায় -->
          <div v-if="expanded">
            <p>{{ t(
              "তিনি দেশ-বিদেশে বহু গবেষণাপত্র প্রকাশ করেছেন এবং আন্তর্জাতিক সম্মেলনে বাংলাদেশকে প্রতিনিধিত্ব করেছেন। তাঁর চিকিৎসাধীন হাজার হাজার রোগী সুস্থ জীবন যাপন করছেন।",
              "He has published numerous research papers and represented Bangladesh at international conferences. Thousands of his patients are living healthy lives."
            ) }}</p>
            <p>{{ t(
              "ঢাকা মেডিকেল কলেজ হাসপাতালে নিউরোলজি বিভাগের প্রধান হিসেবে দীর্ঘদিন দায়িত্ব পালন করেছেন। তিনি সিঙ্গাপুরের ন্যাশনাল নিউরোসায়েন্স ইনস্টিটিউট থেকে ফেলোশিপ করেছেন।",
              "He served as Head of Neurology at Dhaka Medical College Hospital for many years and completed his fellowship at the National Neuroscience Institute, Singapore."
            ) }}</p>
          </div>

          <!-- বাটন -->
          <button class="btn-outline" style="margin-bottom:24px;cursor:pointer;border:2px solid var(--primary);background:transparent;color:var(--primary);padding:10px 24px;border-radius:8px;font-size:0.95rem;font-weight:600;display:inline-flex;align-items:center;gap:8px;" @click="expanded = !expanded">
            <i :class="expanded ? 'fas fa-chevron-up' : 'fas fa-chevron-down'"></i>
            {{ expanded ? t("সংক্ষেপ দেখুন", "Show Less") : t("বিস্তারিত দেখুন", "Read More") }}
          </button>

          <div class="info-grid">
            <div class="info-item">
              <i class="fas fa-hospital"></i>
              <div>
                <div class="label">{{ t("হাসপাতাল", "Hospital") }}</div>
                <div class="value">{{ t(profile.hospital_bn, profile.hospital_en) }}</div>
              </div>
            </div>
            <div class="info-item">
              <i class="fas fa-graduation-cap"></i>
              <div>
                <div class="label">{{ t("বিশেষজ্ঞতা", "Speciality") }}</div>
                <div class="value">{{ t(profile.speciality_bn, profile.speciality_en) }}</div>
              </div>
            </div>
            <div class="info-item">
              <i class="fas fa-phone"></i>
              <div>
                <div class="label">{{ t("যোগাযোগ", "Phone") }}</div>
                <div class="value">{{ profile.phone }}</div>
              </div>
            </div>
            <div class="info-item">
              <i class="fas fa-map-marker-alt"></i>
              <div>
                <div class="label">{{ t("চেম্বার", "Chamber") }}</div>
                <div class="value">{{ t(profile.address_bn, profile.address_en) }}</div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref } from "vue"
import { useScrollAnimation } from "@/composables/useScrollAnimation"
import { storeToRefs } from "pinia"
import { useDoctorStore } from "@/stores/doctor"
import { useI18nStore } from "@/stores/i18n"

const { profile } = storeToRefs(useDoctorStore())
const { t } = useI18nStore()
const expanded = ref(false)
useScrollAnimation()
</script>