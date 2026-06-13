<template>
  <section id="gallery">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">{{ t("গ্যালারি", "Gallery") }}</span>
        <h2 class="section-title">{{ t("ছবির গ্যালারি", "Photo Gallery") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div class="gallery-filter">
        <button
          v-for="cat in categories" :key="cat.value"
          class="filter-btn"
          :class="{ active: activeCategory === cat.value }"
          @click="changeCategory(cat.value)"
        >
          {{ t(cat.label_bn, cat.label_en) }}
        </button>
      </div>

      <div class="gallery-grid">
        <div
          v-for="(photo, index) in filteredPhotos" :key="photo.id"
          class="gallery-item"
          @click="openModal(index)"
        >
          <img :src="photo.image" :alt="t(photo.title_bn, photo.title_en)" />
          <div class="gallery-overlay">
            <div class="gallery-overlay-content">
              <i class="fas fa-search-plus"></i>
              <p>{{ t(photo.title_bn, photo.title_en) }}</p>
            </div>
          </div>
        </div>
      </div>

      <div v-if="filteredPhotos.length === 0" class="gallery-empty">
        <i class="fas fa-images"></i>
        <p>{{ t("এই ক্যাটাগরিতে কোনো ছবি নেই", "No photos in this category") }}</p>
      </div>
    </div>

    <!-- Photo Modal with Navigation -->
    <div class="photo-modal" :class="{ active: modalActive }" @click.self="closeModal">
      <div class="photo-modal-inner">

        <!-- Close -->
        <button class="modal-close" @click="closeModal">
          <i class="fas fa-times"></i>
        </button>

        <!-- Left Arrow -->
        <button class="modal-arrow modal-arrow-left" @click="prevPhoto" :disabled="currentIndex === 0">
          <i class="fas fa-chevron-left"></i>
        </button>

        <!-- Image -->
        <img v-if="activePhoto" :src="activePhoto.image" :alt="t(activePhoto.title_bn, activePhoto.title_en)" />

        <!-- Right Arrow -->
        <button class="modal-arrow modal-arrow-right" @click="nextPhoto" :disabled="currentIndex === filteredPhotos.length - 1">
          <i class="fas fa-chevron-right"></i>
        </button>

        <!-- Caption -->
        <div v-if="activePhoto" class="photo-modal-caption">
          <h4>{{ t(activePhoto.title_bn, activePhoto.title_en) }}</h4>
          <span class="photo-modal-cat">{{ activePhoto.category }}</span>
          <span class="photo-counter">{{ currentIndex + 1 }} / {{ filteredPhotos.length }}</span>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, computed, onMounted, onUnmounted } from "vue"
import { useScrollAnimation } from "@/composables/useScrollAnimation"
import { useI18nStore } from "@/stores/i18n"
import api from "@/services/api"

const { t } = useI18nStore()
const photos = ref([])
const activeCategory = ref("all")
const modalActive = ref(false)
const currentIndex = ref(0)

useScrollAnimation()

const categories = [
  { value: "all",        label_bn: "সব",       label_en: "All" },
  { value: "conference", label_bn: "সম্মেলন",   label_en: "Conference" },
  { value: "award",      label_bn: "পুরস্কার",  label_en: "Award" },
  { value: "chamber",    label_bn: "চেম্বার",   label_en: "Chamber" },
  { value: "other",      label_bn: "অন্যান্য",  label_en: "Other" },
]

const filteredPhotos = computed(() => {
  if (activeCategory.value === "all") return photos.value
  return photos.value.filter(p => p.category === activeCategory.value)
})

const activePhoto = computed(() => filteredPhotos.value[currentIndex.value] || null)

onMounted(async () => {
  try {
    const res = await api.getPhotos()
    photos.value = res.data
  } catch (e) {
    console.error("Photos error:", e)
  }
  window.addEventListener("keydown", handleKey)
})

onUnmounted(() => {
  window.removeEventListener("keydown", handleKey)
})

function changeCategory(cat) {
  activeCategory.value = cat
  currentIndex.value = 0
  // scroll animation re-trigger
  setTimeout(() => {
    const elements = document.querySelectorAll(".gallery-item")
    elements.forEach(el => {
      el.classList.remove("visible")
      setTimeout(() => el.classList.add("visible"), 50)
    })
  }, 50)
}

function openModal(index) {
  currentIndex.value = index
  modalActive.value = true
  document.body.style.overflow = "hidden"
}

function closeModal() {
  modalActive.value = false
  document.body.style.overflow = ""
}

function prevPhoto() {
  if (currentIndex.value > 0) currentIndex.value--
}

function nextPhoto() {
  if (currentIndex.value < filteredPhotos.value.length - 1) currentIndex.value++
}

function handleKey(e) {
  if (!modalActive.value) return
  if (e.key === "ArrowLeft") prevPhoto()
  if (e.key === "ArrowRight") nextPhoto()
  if (e.key === "Escape") closeModal()
}
</script>