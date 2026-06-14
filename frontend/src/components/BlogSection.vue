<template>
  <section id="blog">
    <div class="container">
      <div class="section-header fade-up">
        <span class="section-eyebrow">{{ t("ব্লগ", "Blog") }}</span>
        <h2 class="section-title">{{ t("স্বাস্থ্য পরামর্শ", "Health Tips") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div class="blog-grid">
        <div v-for="post in posts" :key="post.id" class="blog-card fade-up">
          <div class="blog-img">
            <img v-if="post.image" :src="post.image" :alt="post.title_bn" />
            <div v-else class="blog-img-placeholder">
              <i class="fas fa-brain"></i>
            </div>
            <span class="blog-category">{{ t(post.category_bn, post.category_en) }}</span>
          </div>
          <div class="blog-body">
            <div class="blog-meta">
              <span><i class="fas fa-calendar"></i> {{ formatDate(post.date) }}</span>
              <span><i class="fas fa-clock"></i> {{ post.read_time }} {{ t("মিনিট", "min") }}</span>
            </div>
            <h4>{{ t(post.title_bn, post.title_en) }}</h4>
            <p>{{ t(post.summary_bn, post.summary_en) }}</p>
            <a :href="`/blog/${post.id}`" class="blog-link">
              {{ t("পড়ুন", "Read More") }} <i class="fas fa-arrow-right"></i>
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
const posts = ref([])

function formatDate(d) {
  return new Date(d).toLocaleDateString("bn-BD", { year: "numeric", month: "long", day: "numeric" })
}

onMounted(async () => {
  const res = await api.getBlogPosts()
  posts.value = res.data
})
</script>