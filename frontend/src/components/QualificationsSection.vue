<template>
  <section id="qualifications">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-eyebrow">{{ t("শিক্ষা", "Education") }}</span>
        <h2 class="section-title">{{ t("শিক্ষাগত যোগ্যতা", "Qualifications") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div v-if="profile" class="qual-grid">
        <div v-for="q in profile.qualifications" :key="q.id" class="qual-card fade-up">
          <i class="fas fa-graduation-cap qual-icon"></i>
          <div class="qual-year">{{ q.year }}</div>
          <div class="qual-degree">{{ q.degree }}</div>
          <div class="qual-inst">{{ t(q.institution_bn, q.institution_en) }}</div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { storeToRefs } from "pinia"
import { useScrollAnimation } from "@/composables/useScrollAnimation"
import { useDoctorStore } from "@/stores/doctor"
import { useI18nStore } from "@/stores/i18n"

const { profile } = storeToRefs(useDoctorStore())
const { t } = useI18nStore()
useScrollAnimation()
</script>