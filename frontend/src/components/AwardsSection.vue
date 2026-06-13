<template>
  <section id="awards">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-eyebrow">{{ t("সম্মাননা", "Honours") }}</span>
        <h2 class="section-title">{{ t("পুরস্কার ও অর্জন", "Awards & Achievements") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div class="awards-grid">
        <div v-for="a in awards" :key="a.id" class="award-card fade-up">
          <i :class="a.icon"></i>
          <h5>{{ t(a.title_bn, a.title_en) }}</h5>
          <p>{{ t(a.organization_bn, a.organization_en) }}, {{ a.year }}</p>
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
const awards = ref([])

onMounted(async () => {
  const res = await api.getAwards()
  awards.value = res.data
})
</script>