import { createRouter, createWebHistory } from "vue-router"
import Home from "@/views/HomeView.vue"

const routes = [
  {
    path: "/",
    component: Home,
  },
  {
    path: "/blog/:id",
    name: "blog-detail",
    component: () => import("@/views/BlogDetailView.vue"),
  },
  {
    path: "/news/:id",
    name: "news-detail",
    component: () => import("@/views/NewsDetailView.vue"),
  },
  {
    path: "/:pathMatch(.*)*",
    redirect: "/",
  },
]

export default createRouter({
  history: createWebHistory(),
  routes,
  scrollBehavior(to) {
    if (to.hash) return { el: to.hash, behavior: "smooth" }
    return { top: 0 }
  },
})
