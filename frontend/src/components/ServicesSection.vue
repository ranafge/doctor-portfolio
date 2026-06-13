<template>
  <section id="services">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-eyebrow">{{ t("সেবাসমূহ", "Services") }}</span>
        <h2 class="section-title">{{ t("চিকিৎসা সেবা", "Medical Services") }}</h2>
        <div class="section-divider"></div>
      </div>
      <div class="services-grid">
        <div v-for="s in services" :key="s.id" class="service-card fade-up">
          <div class="service-icon"><i :class="s.icon"></i></div>
          <h4>{{ t(s.title_bn, s.title_en) }}</h4>
          <p>{{ t(s.description_bn, s.description_en) }}</p>
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
const services = ref([])

onMounted(async () => {
  const res = await api.getServices()
  services.value = res.data
})
</script>