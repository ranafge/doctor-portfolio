import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useI18nStore = defineStore('i18n', () => {
  const lang = ref(localStorage.getItem('lang') || 'bn')

  function setLang(newLang) {
    lang.value = newLang
    localStorage.setItem('lang', newLang)
  }

  function t(field_bn, field_en) {
    return lang.value === 'bn' ? field_bn : field_en
  }

  return { lang, setLang, t }
})
