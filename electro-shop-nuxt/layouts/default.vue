<template>
    <div>
        <Navbar />
        <Nuxt />
        <TheFooter />
    </div>
  </template>

  <script>
  export default {
    mounted() {
        this.$store.dispatch('checkAuth')
    }
  }
  </script>
  