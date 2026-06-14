<template>
  <div class="blog-detail-page">
    <NavBar />

    <div v-if="loading" class="blog-detail-loading">
      <i class="fas fa-spinner fa-spin"></i>
      {{ t("লোড হচ্ছে...", "Loading...") }}
    </div>

    <div v-else-if="post" class="blog-detail-container">
      <!-- Hero Image -->
      <div class="blog-detail-hero" :style="post.image ? `background-image:url(${post.image})` : ``">
        <div class="blog-detail-hero-overlay" style="justify-content:center;align-items:center;">
          <div class="blog-detail-hero-content" style="text-align:center;">
            <span class="blog-category">{{ t(post.category_bn, post.category_en) }}</span>
            <h1>{{ t(post.title_bn, post.title_en) }}</h1>
            <div class="blog-detail-meta">
              <span><i class="fas fa-calendar"></i> {{ formatDate(post.date) }}</span>
              <span><i class="fas fa-clock"></i> {{ post.read_time }} {{ t("মিনিট পড়া", "min read") }}</span>
            </div>
          </div>
        </div>
      </div>

      <!-- Content -->
      <div class="blog-detail-body">
        <div class="blog-detail-content">
          <!-- Back Button -->
          <a href="/" @click.prevent="goBack" class="blog-back-btn">
            <i class="fas fa-arrow-left"></i>
            {{ t("ব্লগে ফিরুন", "Back to Blog") }}
          </a>

          <!-- Summary -->
          <div class="blog-summary">
            {{ t(post.summary_bn, post.summary_en) }}
          </div>

          <!-- Main Content -->
          <div class="blog-content-body" v-html="t(post.content_bn, post.content_en)"></div>

          <!-- Share -->
          <div class="blog-share">
            <span>{{ t("শেয়ার করুন:", "Share:") }}</span>
            <a :href="`https://www.facebook.com/sharer/sharer.php?u=${currentUrl}`" target="_blank">
              <i class="fab fa-facebook-f"></i>
            </a>
            <a :href="`https://twitter.com/intent/tweet?url=${currentUrl}&text=${post.title_en}`" target="_blank">
              <i class="fab fa-twitter"></i>
            </a>
            <a :href="`https://wa.me/?text=${post.title_en} ${currentUrl}`" target="_blank">
              <i class="fab fa-whatsapp"></i>
            </a>
          </div>
        </div>
      </div>
    </div>

    <div v-else class="blog-detail-loading">
      {{ t("পোস্ট পাওয়া যায়নি।", "Post not found.") }}
    </div>

    <FooterSection />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useI18nStore } from "@/stores/i18n"
import NavBar from "@/components/NavBar.vue"
import FooterSection from "@/components/FooterSection.vue"
import api from "@/services/api"

const route = useRoute()
const router = useRouter()
const { t } = useI18nStore()
const post = ref(null)
const loading = ref(true)
const currentUrl = computed(() => window.location.href)

function goBack() {
  router.push("/").then(() => {
    setTimeout(() => {
      document.getElementById("blog")?.scrollIntoView({ behavior: "smooth" })
    }, 300)
  })
}

function formatDate(d) {
  return new Date(d).toLocaleDateString("bn-BD", { year: "numeric", month: "long", day: "numeric" })
}

onMounted(async () => {
  try {
    const res = await api.getBlogPost(route.params.id)
    post.value = res.data
  } catch (e) {
    console.error("Blog post error:", e)
  } finally {
    loading.value = false
  }
})
</script>