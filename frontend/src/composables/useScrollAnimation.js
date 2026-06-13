import { onMounted, onUnmounted } from "vue"

export function useScrollAnimation() {
  let observer = null

  function observe() {
    const elements = document.querySelectorAll(".fade-up, .fade-left, .fade-right")
    elements.forEach(el => {
      if (observer) observer.observe(el)
    })
  }

  onMounted(() => {
    observer = new IntersectionObserver(
      (entries) => {
        entries.forEach(entry => {
          if (entry.isIntersecting) {
            entry.target.classList.add("visible")
            observer.unobserve(entry.target)
          }
        })
      },
      { threshold: 0.1 }
    )

    // initial observe
    observe()

    // dynamic content এর জন্য — 500ms, 1s, 2s পরে আবার observe
    setTimeout(observe, 500)
    setTimeout(observe, 1000)
    setTimeout(observe, 2000)
  })

  onUnmounted(() => {
    if (observer) observer.disconnect()
  })
}