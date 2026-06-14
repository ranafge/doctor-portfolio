<template>
  <RouterView />
</template>

<script setup>
import { onMounted } from "vue"
import { useDoctorStore } from "@/stores/doctor"

const store = useDoctorStore()
onMounted(() => store.fetchAll())
</script>
