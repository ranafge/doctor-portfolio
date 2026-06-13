<template>
  <section id="videos">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">{{ t("ভিডিও", "Videos") }}</span>
        <h2 class="section-title">{{ t("শিক্ষামূলক ভিডিও", "Educational Videos") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div v-if="featured" class="video-featured">
        <div class="video-featured-inner">
          <div class="video-main-frame">
            <iframe :src="featured.embed_url" :title="featured.title_en" allowfullscreen></iframe>
          </div>
          <div class="video-main-info">
            <span class="v-badge">{{ t("বিশেষ ভিডিও", "FEATURED") }}</span>
            <h3>{{ t(featured.title_bn, featured.title_en) }}</h3>
            <p>{{ t(featured.description_bn, featured.description_en) }}</p>
            <div class="video-meta">
              <span><i class="fas fa-clock"></i> {{ featured.duration }}</span>
              <span><i class="fas fa-eye"></i> {{ featured.views }} {{ t("বার দেখা হয়েছে", "views") }}</span>
            </div>
          </div>
        </div>
      </div>

      <div class="video-grid-title">
        <i class="fas fa-play-circle"></i>
        {{ t("আরও ভিডিও", "More Videos") }}
      </div>

      <div class="videos-grid">
        <div v-for="v in otherVideos" :key="v.id" class="video-card" @click="openModal(v)">
          <div class="video-thumb">
            <iframe :src="v.embed_url + '?mute=1'" :title="t(v.title_bn, v.title_en)" allowfullscreen></iframe>
            <div class="play-overlay">
              <div class="play-btn"><i class="fas fa-play"></i></div>
            </div>
            <span class="video-duration">{{ v.duration }}</span>
          </div>
          <div class="video-card-body">
            <div class="video-category">{{ t(v.category_bn, v.category_en) }}</div>
            <h5>{{ t(v.title_bn, v.title_en) }}</h5>
            <p>{{ t(v.description_bn, v.description_en) }}</p>
          </div>
          <div class="video-card-footer">
            <span><i class="fas fa-eye"></i> {{ v.views }}</span>
            <a href="#" @click.prevent="openModal(v)">{{ t("দেখুন", "Watch") }} <i class="fas fa-play"></i></a>
          </div>
        </div>
      </div>

      <div class="video-cta">
        <a href="https://youtube.com" target="_blank" class="btn-youtube">
          <i class="fab fa-youtube"></i>
          {{ t("YouTube চ্যানেলে সব ভিডিও দেখুন", "Watch All Videos on YouTube") }}
        </a>
      </div>
    </div>

    <div class="video-modal" :class="{ active: modalActive }" @click.self="closeModal">
      <div class="modal-inner">
        <button class="modal-close" @click="closeModal"><i class="fas fa-times"></i></button>
        <iframe v-if="activeVideo" :src="activeVideo.embed_url + '?autoplay=1'" allowfullscreen></iframe>
      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted } from "vue"
import { useI18nStore } from "@/stores/i18n"
import api from "@/services/api"

const { t } = useI18nStore()
const videos = ref([])
const modalActive = ref(false)
const activeVideo = ref(null)

const featured = computed(() => videos.value.find(v => v.is_featured))
const otherVideos = computed(() => videos.value.filter(v => !v.is_featured))

onMounted(async () => {
  try {
    const res = await api.getVideos()
    videos.value = res.data
  } catch (e) {
    console.error("Videos error:", e)
  }
})

function openModal(v) {
  activeVideo.value = v
  modalActive.value = true
  document.body.style.overflow = "hidden"
}

function closeModal() {
  modalActive.value = false
  activeVideo.value = null
  document.body.style.overflow = ""
}
</script>