<template>
  <section id="contact">
    <div class="container">
      <div class="section-header">
        <span class="section-eyebrow">{{ t("যোগাযোগ", "Contact") }}</span>
        <h2 class="section-title">{{ t("অ্যাপয়েন্টমেন্ট নিন", "Book Appointment") }}</h2>
        <div class="section-divider"></div>
      </div>

      <div class="contact-grid">

        <!-- বাম: যোগাযোগ তথ্য -->
        <div class="contact-info">
          <h3>{{ t("যোগাযোগের তথ্য", "Contact Information") }}</h3>

          <div class="contact-item">
            <div class="contact-icon"><i class="fas fa-map-marker-alt"></i></div>
            <div>
              <div class="c-label">{{ t("প্রাইভেট চেম্বার", "Private Chamber") }}</div>
              <div class="c-val">{{ t("১০ মেইন রোড, কল্যাণপুর বাস স্ট্যান্ড, ঢাকা-১২১৬", "10 Main Road, Kalyanpur Bus Stand, Dhaka-1216") }}</div>
              <div class="c-val">{{ t("বিকাল ৫টা – রাত ৯টা (শুক্রবার বন্ধ)", "5:00 PM – 9:00 PM (Closed Friday)") }}</div>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon"><i class="fas fa-hospital"></i></div>
            <div>
              <div class="c-label">{{ t("ঢাকা মেডিকেল কলেজ", "Dhaka Medical College") }}</div>
              <div class="c-val">{{ t("সকাল ৮টা – দুপুর ২টা", "8:00 AM – 2:00 PM") }}</div>
              <div class="c-val">{{ t("রবি, মঙ্গল ও বৃহস্পতিবার", "Sun, Tue & Thu") }}</div>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon"><i class="fas fa-phone"></i></div>
            <div>
              <div class="c-label">{{ t("ফোন", "Phone") }}</div>
              <div class="c-val">+880 1977-063412</div>
            </div>
          </div>

          <div class="contact-item">
            <div class="contact-icon"><i class="fas fa-envelope"></i></div>
            <div>
              <div class="c-label">{{ t("ইমেইল", "Email") }}</div>
              <div class="c-val">dr.jonayed@gmail.com</div>
            </div>
          </div>

          <!-- সোশ্যাল -->
          <div class="contact-social">
            <a href="#" class="social-btn"><i class="fab fa-facebook-f"></i></a>
            <a href="#" class="social-btn"><i class="fab fa-youtube"></i></a>
            <a href="#" class="social-btn whatsapp"><i class="fab fa-whatsapp"></i></a>
          </div>
        </div>

        <!-- ডান: ফর্ম -->
        <div class="contact-form-wrap">
          <!-- সাফল্য বার্তা -->
          <div v-if="submitted" class="form-success">
            <i class="fas fa-check-circle"></i>
            <h4>{{ t("অ্যাপয়েন্টমেন্ট সফলভাবে জমা হয়েছে!", "Appointment submitted successfully!") }}</h4>
            <p>{{ t("আমরা শীঘ্রই আপনার সাথে যোগাযোগ করব।", "We will contact you soon.") }}</p>
            <button class="btn-primary" @click="submitted = false; resetForm()">
              {{ t("নতুন অ্যাপয়েন্টমেন্ট", "New Appointment") }}
            </button>
          </div>

          <!-- ফর্ম -->
          <div v-else>
            <h3>{{ t("অ্যাপয়েন্টমেন্ট ফর্ম", "Appointment Form") }}</h3>
            <div v-if="formError" class="form-error-box">
              <i class="fas fa-exclamation-circle"></i> {{ formError }}
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>{{ t("রোগীর নাম *", "Patient Name *") }}</label>
                <input v-model="form.name" type="text" :placeholder="t('আপনার পূর্ণ নাম', 'Your full name')" @input="validateName" :class="{'input-error': errors.name, 'input-ok': form.name && !errors.name}" />
                <span class="err" v-if="errors.name">{{ errors.name }}</span>
              </div>
              <div class="form-group">
                <label>{{ t("ফোন নম্বর *", "Phone Number *") }}</label>
                <input v-model="form.phone" type="tel" placeholder="01XXXXXXXXX" @input="validatePhone" :class="{'input-error': errors.phone, 'input-ok': form.phone && !errors.phone}" maxlength="11" />
                <span class="err" v-if="errors.phone">{{ errors.phone }}</span>
              </div>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>{{ t("ইমেইল", "Email") }}</label>
                <input v-model="form.email" type="email" :placeholder="t('আপনার ইমেইল', 'Your email')" @input="validateEmail" :class="{'input-error': errors.email, 'input-ok': form.email && !errors.email}" />
              </div>
              <div class="form-group">
                <label>{{ t("বয়স *", "Age *") }}</label>
                <input v-model="form.age" type="number" :placeholder="t('বয়স লিখুন', 'Enter age')" @input="validateAge" :class="{'input-error': errors.age, 'input-ok': form.age && !errors.age}" min="0" max="120" />
                <span class="err" v-if="errors.age">{{ errors.age }}</span>
              </div>
            </div>

            <div class="form-group">
              <label>{{ t("চেম্বার *", "Chamber *") }}</label>
              <select v-model="form.chamber">
                <option value="">{{ t("চেম্বার বেছে নিন", "Select Chamber") }}</option>
                <option value="প্রাইভেট চেম্বার, কল্যাণপুর">{{ t("প্রাইভেট চেম্বার, কল্যাণপুর", "Private Chamber, Kalyanpur") }}</option>
                <option value="ঢাকা মেডিকেল কলেজ">{{ t("ঢাকা মেডিকেল কলেজ", "Dhaka Medical College") }}</option>
              </select>
              <span class="err" v-if="errors.chamber">{{ errors.chamber }}</span>
            </div>

            <div class="form-row">
              <div class="form-group">
                <label>{{ t("পছন্দের তারিখ *", "Preferred Date *") }}</label>
                <input v-model="form.preferred_date" type="date" :min="today" />
                <span class="err" v-if="errors.preferred_date">{{ errors.preferred_date }}</span>
              </div>
              <div class="form-group">
                <label>{{ t("পছন্দের সময় *", "Preferred Time *") }}</label>
                <select v-model="form.preferred_time">
                  <option value="">{{ t("সময় বেছে নিন", "Select Time") }}</option>
                  <option value="সকাল ৮-১০টা">{{ t("সকাল ৮-১০টা", "8:00 AM - 10:00 AM") }}</option>
                  <option value="সকাল ১০-১২টা">{{ t("সকাল ১০-১২টা", "10:00 AM - 12:00 PM") }}</option>
                  <option value="বিকাল ৫-৭টা">{{ t("বিকাল ৫-৭টা", "5:00 PM - 7:00 PM") }}</option>
                  <option value="রাত ৭-৯টা">{{ t("রাত ৭-৯টা", "7:00 PM - 9:00 PM") }}</option>
                </select>
                <span class="err" v-if="errors.preferred_time">{{ errors.preferred_time }}</span>
              </div>
            </div>

            <!-- Honeypot — bot trap, human দেখবে না -->
            <div style="display:none;">
              <input v-model="form.honeypot" type="text" name="website" autocomplete="off" />
            </div>

            <div class="form-group">
              <label>{{ t("সমস্যার বিবরণ *", "Problem Description *") }}</label>
              <textarea v-model="form.problem" rows="4" :placeholder="t('আপনার সমস্যা বিস্তারিত লিখুন', 'Describe your problem in detail')"></textarea>
              <span class="err" v-if="errors.problem">{{ errors.problem }}</span>
            </div>

            <button class="btn-primary" :disabled="loading" @click="submitForm">
              <i class="fas fa-calendar-check"></i>
              {{ loading ? t("পাঠানো হচ্ছে...", "Submitting...") : t("অ্যাপয়েন্টমেন্ট নিন", "Book Appointment") }}
            </button>
          </div>
        </div>

      </div>
    </div>
  </section>
</template>

<script setup>
import { ref, reactive, computed } from "vue"
import { useScrollAnimation } from "@/composables/useScrollAnimation"
import { useI18nStore } from "@/stores/i18n"
import api from "@/services/api"

const { t } = useI18nStore()
useScrollAnimation()
const loading = ref(false)
const submitted = ref(false)
const formError = ref("")

const today = computed(() => new Date().toISOString().split("T")[0])

const form = reactive({
  name: "", phone: "", email: "",
  age: "", chamber: "",
  preferred_date: "", preferred_time: "",
  problem: "",
  honeypot: ""
})

const errors = reactive({})

function validate() {
  Object.keys(errors).forEach(k => delete errors[k])
  formError.value = ""
  // honeypot check — bot হলে সাথে সাথে false return
  if (form.honeypot) return false
  if (!form.name)           errors.name = t("নাম আবশ্যক", "Name is required")
  if (!form.phone) {
    errors.phone = t("ফোন নম্বর আবশ্যক", "Phone is required")
  } else if (!/^[0-9]{11}$/.test(form.phone)) {
    errors.phone = t("১১ সংখ্যার ফোন নম্বর দিন", "Enter 11 digit phone number")
  }
  if (!form.age)            errors.age = t("বয়স আবশ্যক", "Age is required")
  if (!form.chamber)        errors.chamber = t("চেম্বার বেছে নিন", "Select a chamber")
  if (!form.preferred_date) errors.preferred_date = t("তারিখ আবশ্যক", "Date is required")
  if (!form.preferred_time) errors.preferred_time = t("সময় বেছে নিন", "Select a time")
  if (!form.problem)        errors.problem = t("সমস্যার বিবরণ আবশ্যক", "Problem description is required")
  return Object.keys(errors).length === 0
}

function validateName() {
  delete errors.name
  const nameRegex = /^[a-zA-Zঀ-৿\s]+$/
  if (!form.name) {
    errors.name = t("নাম আবশ্যক", "Name is required")
  } else if (!nameRegex.test(form.name)) {
    errors.name = t("শুধু বাংলা বা ইংরেজি অক্ষর দিন", "Only Bengali or English letters allowed")
  }
}

function validatePhone() {
  delete errors.phone
  if (!form.phone) {
    errors.phone = t("ফোন নম্বর আবশ্যক", "Phone is required")
  } else if (!/^[0-9]{11}$/.test(form.phone)) {
    errors.phone = t("১১ সংখ্যার ফোন নম্বর দিন", "Enter 11 digit phone number")
  }
}

function validateEmail() {
  delete errors.email
  if (form.email && !/^[^@]+@[^@]+\.[^@]+$/.test(form.email)) {
    errors.email = t("সঠিক ইমেইল দিন", "Enter a valid email")
  }
}

function validateAge() {
  delete errors.age
  if (!form.age) {
    errors.age = t("বয়স আবশ্যক", "Age is required")
  } else if (parseInt(form.age) < 0 || parseInt(form.age) > 120) {
    errors.age = t("বয়স ০ থেকে ১২০ এর মধ্যে হতে হবে", "Age must be between 0 and 120")
  }
}

function resetForm() {
  Object.keys(form).forEach(k => form[k] = "")
}

async function submitForm() {
  if (!validate()) return
  loading.value = true
  try {
    // XSS protection
    function sanitize(str) {
      return String(str).replace(/[<>"']/g, "")
    }
    const payload = {
      name: sanitize(form.name),
      phone: form.phone,
      email: form.email || "",
      age: parseInt(form.age),
      chamber: form.chamber,
      preferred_date: form.preferred_date,
      preferred_time: form.preferred_time,
      problem: sanitize(form.problem),
    }
    console.log("Sending:", payload)
    const res = await api.submitAppointment(payload)
    console.log("Response:", res.data)
    submitted.value = true
    resetForm()
  } catch (err) {
    console.error("Error:", err.response?.data)
    const errData = err.response?.data
    if (errData?.errors) {
      const msgs = Object.values(errData.errors).flat().join(" | ")
      formError.value = msgs
    } else {
      formError.value = t("কিছু একটা ভুল হয়েছে। আবার চেষ্টা করুন।", "Something went wrong.")
    }
  } finally {
    loading.value = false
  }
}
</script>