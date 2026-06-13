<template>
  <nav :class="{ scrolled: isScrolled }">
    <a href="#home" class="nav-brand">
      {{ t("প্রফেসর ডা.", "Prof. Dr.") }} <span>{{ t("শরীফ আহমেদ জোনায়েদ", "Sharif Ahmed Jonayed") }}</span>
    </a>

    <ul class="nav-links">
      <li><a href="#about" :class="{ active: activeSection === 'about' }">{{ t("সম্পর্কে", "About") }}</a></li>
      <li><a href="#services" :class="{ active: activeSection === 'services' }">{{ t("সেবা", "Services") }}</a></li>
      <li><a href="#chamber" :class="{ active: activeSection === 'chamber' }">{{ t("চেম্বার", "Chamber") }}</a></li>
      <li><a href="#publications" :class="{ active: activeSection === 'publications' }">{{ t("গবেষণা", "Research") }}</a></li>
      <li><a href="#awards" :class="{ active: activeSection === 'awards' }">{{ t("পুরস্কার", "Awards") }}</a></li>
      <li><a href="#news" :class="{ active: activeSection === 'news' }">{{ t("সংবাদ", "News") }}</a></li>
      <li><a href="#blog" :class="{ active: activeSection === 'blog' }">{{ t("ব্লগ", "Blog") }}</a></li>
      <li><a href="#videos" :class="{ active: activeSection === 'videos' }">{{ t("ভিডিও", "Videos") }}</a></li>
      <li><a href="#gallery" :class="{ active: activeSection === 'gallery' }">{{ t("গ্যালারি", "Gallery") }}</a></li>
      <li><a href="#contact" class="btn-appt">{{ t("অ্যাপয়েন্টমেন্ট", "Appointment") }}</a></li>
    </ul>

    <div class="lang-toggle">
      <button class="lang-btn" :class="{ active: lang === 'bn' }" @click="setLang('bn')">বাং</button>
      <span class="lang-sep"></span>
      <button class="lang-btn" :class="{ active: lang === 'en' }" @click="setLang('en')">EN</button>
    </div>

    <!-- Hamburger -->
    <div class="hamburger" @click="toggleMenu">
      <span :style="menuOpen ? 'transform:rotate(45deg) translate(5px,5px)' : ''"></span>
      <span :style="menuOpen ? 'opacity:0' : ''"></span>
      <span :style="menuOpen ? 'transform:rotate(-45deg) translate(5px,-5px)' : ''"></span>
    </div>
  </nav>

  <!-- Mobile Menu -->
  <div class="mobile-menu" :class="{ open: menuOpen }">
    <a href="#about"        @click="closeMenu">{{ t("সম্পর্কে", "About") }}</a>
    <a href="#services"     @click="closeMenu">{{ t("সেবা", "Services") }}</a>
    <a href="#chamber"      @click="closeMenu">{{ t("চেম্বার", "Chamber") }}</a>
    <a href="#publications" @click="closeMenu">{{ t("গবেষণা", "Research") }}</a>
    <a href="#awards"       @click="closeMenu">{{ t("পুরস্কার", "Awards") }}</a>
    <a href="#news"         @click="closeMenu">{{ t("সংবাদ", "News") }}</a>
    <a href="#blog"         @click="closeMenu">{{ t("ব্লগ", "Blog") }}</a>
    <a href="#videos"       @click="closeMenu">{{ t("ভিডিও", "Videos") }}</a>
    <a href="#gallery"      @click="closeMenu">{{ t("গ্যালারি", "Gallery") }}</a>
    <a href="#contact"      @click="closeMenu" style="color:var(--gold)!important;font-weight:700!important;">
      {{ t("অ্যাপয়েন্টমেন্ট", "Appointment") }}
    </a>
  </div>
</template>

<script setup>
import { ref, onMounted, onUnmounted } from "vue"
import { storeToRefs } from "pinia"
import { useI18nStore } from "@/stores/i18n"

const i18nStore = useI18nStore()
const { lang } = storeToRefs(i18nStore)
const { setLang, t } = i18nStore

const isScrolled = ref(false)
const activeSection = ref("home")

function updateActiveSection() {
  const sections = ["home", "about", "qualifications", "services", "chamber", "publications", "awards", "news", "blog", "videos", "gallery", "contact"]
  for (const id of [...sections].reverse()) {
    const el = document.getElementById(id)
    if (el && window.scrollY >= el.offsetTop - 100) {
      activeSection.value = id
      break
    }
  }
}
const menuOpen = ref(false)

function handleScroll() { isScrolled.value = window.scrollY > 50; updateActiveSection() }
function toggleMenu() { menuOpen.value = !menuOpen.value }
function closeMenu() { menuOpen.value = false }

onMounted(() => window.addEventListener("scroll", handleScroll))
onUnmounted(() => window.removeEventListener("scroll", handleScroll))
</script>