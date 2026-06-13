<template>
  <section id="chamber">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-eyebrow">{{ t("চেম্বার", "Chamber") }}</span>
        <h2 class="section-title">{{ t("চেম্বার ও সময়সূচি", "Chamber & Schedule") }}</h2>
        <div class="section-divider"></div>
      </div>
      <div class="chamber-grid">
        <div v-for="c in chambers" :key="c.id" class="chamber-card fade-up">
          <div class="chamber-head">
            <h4><i class="fas fa-clinic-medical"></i> {{ t(c.name_bn, c.name_en) }}</h4>
            <p>{{ t(c.subtitle_bn, c.subtitle_en) }}</p>
          </div>
          <div class="chamber-body">
            <div class="chamber-row">
              <i class="fas fa-map-marker-alt"></i>
              <div>
                <div class="ch-label">{{ t("ঠিকানা", "Address") }}</div>
                <div class="ch-val">{{ t(c.address_bn, c.address_en) }}</div>
              </div>
            </div>
            <div class="chamber-row">
              <i class="fas fa-clock"></i>
              <div>
                <div class="ch-label">{{ t("সময়", "Time") }}</div>
                <div class="ch-val">{{ t(c.time_bn, c.time_en) }}</div>
              </div>
            </div>
            <div class="chamber-row">
              <i class="fas fa-calendar"></i>
              <div>
                <div class="ch-label">{{ t("বার", "Days") }}</div>
                <div class="ch-val">{{ t(c.days_bn, c.days_en) }}</div>
              </div>
            </div>
            <div class="chamber-row">
              <i class="fas fa-phone"></i>
              <div>
                <div class="ch-label">{{ t("ফোন", "Phone") }}</div>
                <div class="ch-val">{{ c.phone }}</div>
              </div>
            </div>
            <a :href="c.map_url" target="_blank" class="btn-map">
              <i class="fas fa-map"></i> {{ t("গুগল ম্যাপে দেখুন", "View on Google Map") }}
            </a>
          </div>
        </div>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, onMounted } from "vue"
import { useScrollAnimation } from "@/composables/useScrollAnimation"
import { useI18nStore } from "@/stores/i18n"
import api from "@/services/api"

const { t } = useI18nStore()
useScrollAnimation()
const chambers = ref([])

onMounted(async () => {
  const res = await api.getChambers()
  chambers.value = res.data
})
</script>