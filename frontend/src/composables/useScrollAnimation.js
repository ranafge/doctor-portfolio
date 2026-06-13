import { onMounted, onUnmounted, watch, nextTick } from "vue"

export function useScrollAnimation(watchSource = null) {
  let observer = null

  function setupObserver() {
    if (observer) observer.disconnect()

    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible")
          }
        })
      },
      { threshold: 0.05, rootMargin: "0px 0px -30px 0px" }
    )

    nextTick(() => {
      const elements = document.querySelectorAll(".fade-up, .fade-left, .fade-right")
      elements.forEach(el => observer.observe(el))
    })
  }

  onMounted(() => {
    setupObserver()
    // dynamic content এর জন্য MutationObserver
    const mutationObserver = new MutationObserver(() => {
      setupObserver()
    })
    mutationObserver.observe(document.body, { childList: true, subtree: true })
  })

  onUnmounted(() => {
    if (observer) observer.disconnect()
  })
}