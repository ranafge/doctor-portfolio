import { defineStore } from "pinia"
import { ref } from "vue"
import api from "@/services/api"

export const useDoctorStore = defineStore("doctor", () => {
  const profile = ref(null)
  const loading = ref(false)
  const error = ref(null)

  async function fetchProfile() {
    loading.value = true
    try {
      const res = await api.getDoctorProfile()
      profile.value = res.data
    } catch (err) {
      error.value = "প্রোফাইল লোড হয়নি"
    } finally {
      loading.value = false
    }
  }

  return { profile, loading, error, fetchProfile }
})