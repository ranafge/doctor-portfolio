<template>
  <div>
    <NavBar />

    <section class="detail-section">
      <div class="container">

        <div v-if="loading" class="detail-loading">
          <div class="skeleton-title"></div>
          <div class="skeleton-body"></div>
        </div>

        <div v-else-if="error" class="detail-error">
          <i class="fas fa-exclamation-circle"></i>
          <h2>{{ t("সংবাদ পাওয়া যায়নি", "News Not Found") }}</h2>
          <p>{{ t("এই সংবাদটি খুঁজে পাওয়া যায়নি।", "This news article could not be found.") }}</p>
          <button @click="router.push('/')" class="btn-back">
            {{ t("হোমে ফিরুন", "Go Home") }}
          </button>
        </div>

        <div v-else-if="item" class="blog-detail">

          <button class="btn-back" @click="router.back()">
            <i class="fas fa-arrow-left"></i>
            {{ t("ফিরে যান", "Go Back") }}
          </button>

          <div class="detail-meta">
            <span class="detail-category">{{ t(item.category_bn, item.category_en) }}</span>
            <span><i class="fas fa-calendar"></i> {{ formatDate(item.published_date) }}</span>
            <span><i class="fas fa-newspaper"></i> {{ t(item.source_bn, item.source_en) }}</span>
          </div>

          <h1 class="detail-title">{{ t(item.title_bn, item.title_en) }}</h1>

          <div v-if="item.image" class="detail-img">
            <img :src="item.image" :alt="item.title_en" />
          </div>

          <div class="detail-content" v-html="t(item.content_bn, item.content_en)"></div>

          <div class="detail-share">
            <span>{{ t("শেয়ার করুন:", "Share:") }}</span>
            <a :href="`https://www.facebook.com/sharer/sharer.php?u=${currentUrl}`"
               target="_blank" class="share-btn fb">
              <i class="fab fa-facebook-f"></i>
            </a>
            <a :href="`https://wa.me/?text=${currentUrl}`"
               target="_blank" class="share-btn wa">
              <i class="fab fa-whatsapp"></i>
            </a>
          </div>

        </div>
      </div>
    </section>

    <FooterSection />
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from "vue"
import { useRoute, useRouter } from "vue-router"
import { useI18nStore } from "@/stores/i18n"
import NavBar        from "@/components/NavBar.vue"
import FooterSection from "@/components/FooterSection.vue"
import api from "@/services/api"

const route  = useRoute()
const router = useRouter()
const i18n   = useI18nStore()
const { t }  = i18n

const item    = ref(null)
const loading = ref(true)
const error   = ref(false)

const currentUrl = computed(() => window.location.href)

onMounted(async () => {
  try {
    const res  = await api.getNewsDetail(route.params.id)
    item.value = res.data
  } catch (e) {
    error.value = true
    console.error("News detail error:", e)
  } finally {
    loading.value = false
  }
})

function formatDate(dateStr) {
  if (!dateStr) return ""
  return new Date(dateStr).toLocaleDateString(
    i18n.lang === "bn" ? "bn-BD" : "en-GB",
    { year: "numeric", month: "long", day: "numeric" }
  )
}
</script>

<style scoped>
.detail-section { padding: 100px 5% 60px; min-height: 80vh; }
.container { max-width: 860px; margin: 0 auto; }

.btn-back {
  display: inline-flex; align-items: center; gap: 8px;
  background: var(--light2); color: var(--primary);
  border: none; padding: 9px 18px; border-radius: 8px;
  font-size: 0.88rem; font-weight: 600; cursor: pointer;
  margin-bottom: 28px; transition: 0.2s; font-family: inherit;
}
.btn-back:hover { background: var(--primary); color: #fff; }

.detail-meta {
  display: flex; gap: 16px; flex-wrap: wrap;
  margin-bottom: 16px; align-items: center;
}
.detail-meta span {
  font-size: 0.82rem; color: var(--text-muted);
  display: flex; align-items: center; gap: 5px;
}
.detail-meta i { color: var(--accent); }
.detail-category {
  background: var(--gold); color: var(--primary);
  font-size: 0.75rem !important; font-weight: 700;
  padding: 3px 14px; border-radius: 20px;
}
.detail-title {
  font-size: clamp(1.4rem, 3vw, 2rem);
  font-weight: 800; color: var(--primary);
  line-height: 1.35; margin-bottom: 24px;
}
.detail-img { border-radius: 16px; overflow: hidden; margin-bottom: 28px; }
.detail-img img { width: 100%; object-fit: cover; max-height: 400px; }
.detail-content {
  font-size: 1rem; color: var(--text);
  line-height: 1.9; margin-bottom: 32px;
}
.detail-content p  { margin-bottom: 16px; }
.detail-content h2 { font-size: 1.3rem; color: var(--primary); margin: 24px 0 10px; }

.detail-share {
  display: flex; align-items: center; gap: 10px;
  padding-top: 24px; border-top: 1px solid var(--border);
  font-size: 0.88rem; font-weight: 600; color: var(--text-muted);
}
.share-btn {
  width: 36px; height: 36px; border-radius: 8px;
  display: flex; align-items: center; justify-content: center;
  color: #fff; text-decoration: none; transition: 0.2s;
}
.share-btn:hover { transform: translateY(-2px); }
.share-btn.fb { background: #1877f2; }
.share-btn.wa { background: #25d366; }

.skeleton-title {
  height: 36px; background: #e2e8f0; border-radius: 8px;
  margin-bottom: 20px; animation: shimmer 1.4s infinite;
}
.skeleton-body {
  height: 280px; background: #e2e8f0; border-radius: 8px;
  animation: shimmer 1.4s infinite;
}
@keyframes shimmer {
  0%, 100% { opacity: 0.6; }
  50%       { opacity: 1; }
}
.detail-error { text-align: center; padding: 80px 20px; }
.detail-error i { font-size: 3rem; color: #cbd5e0; margin-bottom: 16px; display: block; }
.detail-error h2 { font-size: 1.4rem; color: var(--primary); margin-bottom: 10px; }
.detail-error p  { color: var(--text-muted); margin-bottom: 24px; }
</style>
