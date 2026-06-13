import axios from "axios"
const api = axios.create({
  baseURL: "http://127.0.0.1:8000/api",
  timeout: 10000,
})
export default {
  getDoctorProfile()      { return api.get("/doctor/profile/") },
  getServices()           { return api.get("/services/") },
  getChambers()           { return api.get("/chambers/") },
  getPublications()       { return api.get("/publications/") },
  getAwards()             { return api.get("/awards/") },
  getNews()               { return api.get("/news/") },
  getBlogPosts()          { return api.get("/blog/") },
  getVideos()             { return api.get("/gallery/videos/") },
  getPhotos()             { return api.get("/gallery/photos/") },
  submitAppointment(data) { return api.post("/appointments/", data) },
}