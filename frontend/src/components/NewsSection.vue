<template>
  <section id="news">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-eyebrow">{{ t("সংবাদ", "News") }}</span>
        <h2 class="section-title">{{ t("সাম্প্রতিক সংবাদ", "Latest News") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div class="news-grid">
        <div v-for="n in news" :key="n.id" class="news-card fade-up">
          <div class="news-card-body">
            <div class="news-meta">
              <span class="news-source">
                <i class="fas fa-newspaper"></i> {{ n.source }}
              </span>
              <span class="news-date">
                <i class="fas fa-calendar"></i> {{ formatDate(n.date) }}
              </span>
            </div>
            <h4>{{ t(n.title_bn, n.title_en) }}</h4>
            <p>{{ t(n.summary_bn, n.summary_en) }}</p>
            <a v-if="n.url" :href="n.url" target="_blank" class="news-link">
              {{ t("বিস্তারিত পড়ুন", "Read More") }} <i class="fas fa-arrow-right"></i>
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
const news = ref([])

function formatDate(d) {
  return new Date(d).toLocaleDateString("bn-BD", { year: "numeric", month: "long", day: "numeric" })
}

onMounted(async () => {
  const res = await api.getNews()
  news.value = res.data
})
</script>