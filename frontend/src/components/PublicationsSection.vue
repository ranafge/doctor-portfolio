<template>
  <section id="publications">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-eyebrow">{{ t("গবেষণা", "Research") }}</span>
        <h2 class="section-title">{{ t("গবেষণা ও প্রকাশনা", "Research & Publications") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div class="pub-list">
        <div v-for="p in publications" :key="p.id" class="pub-item fade-up">
          <div class="pub-num">{{ p.number }}</div>
          <div class="pub-content">
            <h5>{{ p.title }}</h5>
            <p>{{ p.journal }}, {{ p.year }}</p>
            <span class="pub-tag">{{ p.tag }}</span>
          </div>
        </div>
      </div>

      <div style="text-align:center; margin-top:30px;">
        <a href="https://scholar.google.com" target="_blank" class="btn-primary">
          <i class="fas fa-external-link-alt"></i>
          {{ t("সব গবেষণা দেখুন (Google Scholar)", "View All Publications (Google Scholar)") }}
        </a>
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
const publications = ref([])

onMounted(async () => {
  const res = await api.getPublications()
  publications.value = res.data
})
</script>