<template>
  <footer id="footer">
    <div class="footer-top">
      <div class="container">
        <div class="footer-grid">

          <!-- কলাম ১: ডাক্তারের পরিচয় -->
          <div class="footer-col">
            <div class="footer-brand">
              {{ t("প্রফেসর ডা.", "Prof. Dr.") }} <span>{{ t("মো. শাহ আলম", "Md Shah Alam") }}</span>
            </div>
            <p class="footer-desc">
              {{ t("বাংলাদেশের অন্যতম বিশিষ্ট নিউরোলজি বিশেষজ্ঞ। ৩০+ বছরের অভিজ্ঞতা সম্পন্ন চিকিৎসক।", "One of Bangladesh's most distinguished neurologists with 30+ years of experience.") }}
            </p>
            <div class="footer-social">
              <a href="#"><i class="fab fa-facebook-f"></i></a>
              <a href="#"><i class="fab fa-youtube"></i></a>
              <a href="#"><i class="fab fa-linkedin-in"></i></a>
              <a href="#" class="whatsapp"><i class="fab fa-whatsapp"></i></a>
            </div>
          </div>

          <!-- কলাম ২: দ্রুত লিংক -->
          <div class="footer-col">
            <h4>{{ t("দ্রুত লিংক", "Quick Links") }}</h4>
            <ul class="footer-links">
              <li><a href="#about">{{ t("পরিচিতি", "About") }}</a></li>
              <li><a href="#qualifications">{{ t("শিক্ষাগত যোগ্যতা", "Qualifications") }}</a></li>
              <li><a href="#services">{{ t("চিকিৎসা সেবা", "Services") }}</a></li>
              <li><a href="#chamber">{{ t("চেম্বার", "Chamber") }}</a></li>
              <li><a href="#publications">{{ t("গবেষণা", "Research") }}</a></li>
              <li><a href="#awards">{{ t("পুরস্কার", "Awards") }}</a></li>
              <li><a href="#blog">{{ t("ব্লগ", "Blog") }}</a></li>
              <li><a href="#contact">{{ t("অ্যাপয়েন্টমেন্ট", "Appointment") }}</a></li>
            </ul>
          </div>

          <!-- কলাম ৩: চেম্বার -->
          <div class="footer-col">
            <h4>{{ t("চেম্বার তথ্য", "Chamber Info") }}</h4>
            <div class="footer-chamber-item">
              <div class="fci-head">
                <i class="fas fa-clinic-medical"></i>
                <span>{{ t("প্রাইভেট চেম্বার", "Private Chamber") }}</span>
              </div>
              <div class="fci-body">
                <p><i class="fas fa-map-marker-alt"></i> {{ t("১০ মেইন রোড, কল্যাণপুর, ঢাকা-১২১৬", "10 Main Road, Kalyanpur, Dhaka-1216") }}</p>
                <p><i class="fas fa-clock"></i> {{ t("বিকাল ৫টা – রাত ৯টা", "5:00 PM – 9:00 PM") }}</p>
                <p><i class="fas fa-ban"></i> {{ t("শুক্রবার বন্ধ", "Closed Friday") }}</p>
              </div>
            </div>
            <div class="footer-chamber-item">
              <div class="fci-head">
                <i class="fas fa-hospital"></i>
                <span>{{ t("ঢাকা মেডিকেল কলেজ", "Dhaka Medical College") }}</span>
              </div>
              <div class="fci-body">
                <p><i class="fas fa-calendar"></i> {{ t("রবি, মঙ্গল ও বৃহস্পতিবার", "Sun, Tue & Thu") }}</p>
                <p><i class="fas fa-clock"></i> {{ t("সকাল ৮টা – দুপুর ২টা", "8:00 AM – 2:00 PM") }}</p>
              </div>
            </div>
          </div>

          <!-- কলাম ৪: যোগাযোগ -->
          <div class="footer-col">
            <h4>{{ t("যোগাযোগ", "Contact") }}</h4>
            <div class="footer-info-item">
              <i class="fas fa-phone"></i>
              <div>
                <div class="fi-val">+880 1977-063412</div>
              </div>
            </div>
            <div class="footer-info-item">
              <i class="fas fa-envelope"></i>
              <div>
                <div class="fi-val">dr.s.alam@hotmail.com</div>
              </div>
            </div>
            <div class="footer-info-item">
              <i class="fas fa-map-marker-alt"></i>
              <div>
                <div class="fi-val">{{ t("কল্যাণপুর, ঢাকা-১২১৬", "Kalyanpur, Dhaka-1216") }}</div>
              </div>
            </div>
            <a href="#contact" class="footer-appt-btn">
              <i class="fas fa-calendar-check"></i>
              {{ t("অ্যাপয়েন্টমেন্ট নিন", "Book Appointment") }}
            </a>
          </div>

        </div>
      </div>
    </div>

    <!-- Footer Bottom -->
    <div class="footer-bottom">
      <div class="container">
        <p>© {{ year }} {{ t("প্রফেসর ডা. মো. শাহ আলম। সর্বস্বত্ব সংরক্ষিত।", "Prof. Dr. Md Shah Alam. All rights reserved.") }}</p>
      </div>
    </div>
  </footer>

  <!-- WhatsApp Floating Button -->
  <a href="https://wa.me/8801977063412" target="_blank" class="whatsapp-float" :title="t('WhatsApp এ যোগাযোগ করুন', 'Contact on WhatsApp')">
    <i class="fab fa-whatsapp"></i>
    <span class="wp-tooltip">{{ t("WhatsApp", "WhatsApp") }}</span>
  </a>

  <!-- Scroll to Top Button -->
  <button class="scroll-top" :class="{ visible: isScrolled }" @click="scrollTop" :title="t('উপরে যান', 'Go to top')">
    <i class="fas fa-chevron-up"></i>
  </button>
</template>

<script setup>
import { ref, onMounted, onUnmounted, computed } from "vue"
import { useScrollAnimation } from "@/composables/useScrollAnimation"
import { useI18nStore } from "@/stores/i18n"

const { t } = useI18nStore()
const year = new Date().getFullYear()
useScrollAnimation()
const isScrolled = ref(false)

function handleScroll() { isScrolled.value = window.scrollY > 400 }
function scrollTop() { window.scrollTo({ top: 0, behavior: "smooth" }) }

onMounted(() => window.addEventListener("scroll", handleScroll))
onUnmounted(() => window.removeEventListener("scroll", handleScroll))
</script>