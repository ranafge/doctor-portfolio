<template>
  <section id="home">
    <div v-if="loading" class="loading fade-up">লোড হচ্ছে...</div>
    <div v-else-if="profile" class="hero-inner fade-up">
      <div class="hero-text">
        <span class="hero-badge">{{ t("স্পাইন সার্জারি(মেরুদণ্ডের অস্ত্রোপচার)", "Spine Surgery") }}</span>
        <h1>{{ t(profile.name_bn, profile.name_en) }}</h1>
        <p class="hero-subtitle">{{ t(profile.speciality_bn, profile.speciality_en) }}</p>
        <p class="hero-dept">{{ t(profile.hospital_bn, profile.hospital_en) }}</p>
        <div class="hero-stats">
          <div class="hero-stat">
            <div class="num">{{ profile.experience_years }}+</div>
            <div class="lbl">{{ t("বছরের অভিজ্ঞতা", "Years Experience") }}</div>
          </div>
          <div class="hero-stat">
            <div class="num">{{ profile.patients_count }}+</div>
            <div class="lbl">{{ t("রোগী", "Patients") }}</div>
          </div>
          <div class="hero-stat">
            <div class="num">{{ profile.publications_count }}+</div>
            <div class="lbl">{{ t("গবেষণাপত্র", "Publications") }}</div>
          </div>
        </div>
        <div class="hero-btns">
          <a href="#contact" class="btn-primary">{{ t("অ্যাপয়েন্টমেন্ট নিন", "Book Appointment") }}</a>
          <a href="#about" class="btn-outline">{{ t("বিস্তারিত জানুন", "Learn More") }}</a>
        </div>
      </div>
      <div class="hero-img-wrap">
        <div class="hero-img-circle">
          <img v-if="profile.photo" :src="profile.photo" :alt="profile.name_bn" />
          <i v-else class="fas fa-user-md placeholder-icon"></i>
        </div>
      </div>
    </div>
    <div v-else>ডেটা পাওয়া যায়নি</div>
  </section>
</template>

<script setup>
import { onMounted } from "vue"
import { storeToRefs } from "pinia"
import { useDoctorStore } from "@/stores/doctor"
import { useI18nStore } from "@/stores/i18n"

const doctorStore = useDoctorStore()
const { profile, loading } = storeToRefs(doctorStore)
const { t } = useI18nStore()

onMounted(() => doctorStore.fetchAll())
</script>