import { defineStore } from "pinia"
import { ref } from "vue"
import api from "@/services/api"

export const useDoctorStore = defineStore("doctor", () => {
  const profile      = ref(null)
  const services     = ref([])
  const chambers     = ref([])
  const publications = ref([])
  const awards       = ref([])
  const news         = ref([])
  const blog         = ref([])
  const videos       = ref([])
  const photos       = ref([])
  const loading      = ref(false)
  const error        = ref(null)

  async function fetchAll() {
    loading.value = true
    error.value   = null

    const results = await Promise.allSettled([
      api.getDoctorProfile(),
      api.getServices(),
      api.getChambers(),
      api.getPublications(),
      api.getAwards(),
      api.getNews(),
      api.getBlogPosts(),
      api.getVideos(),
      api.getPhotos(),
    ])

    if (results[0].status === "fulfilled") profile.value      = results[0].value.data
    if (results[1].status === "fulfilled") services.value     = results[1].value.data
    if (results[2].status === "fulfilled") chambers.value     = results[2].value.data
    if (results[3].status === "fulfilled") publications.value = results[3].value.data
    if (results[4].status === "fulfilled") awards.value       = results[4].value.data
    if (results[5].status === "fulfilled") news.value         = results[5].value.data
    if (results[6].status === "fulfilled") blog.value         = results[6].value.data
    if (results[7].status === "fulfilled") videos.value       = results[7].value.data
    if (results[8].status === "fulfilled") photos.value       = results[8].value.data

    results.forEach((r, i) => {
      if (r.status === "rejected") {
        console.warn(`API [${i}] failed:`, r.reason?.message)
      }
    })

    loading.value = false
  }

  return {
    profile, services, chambers, publications,
    awards, news, blog, videos, photos,
    loading, error,
    fetchAll,
  }
})
