<template>
  <div id="app">
    <navbar></navbar>
    <hr>
    <router-view></router-view>
  </div>
</template>

<script>
import navbar from '@/components/navbar.vue'

export default {
  name: 'App',
  components: {
    navbar
  }
}
</script>

<style>
html, body {
  height: 100%;
  background-color: #f8f9fa !important;
}
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #2c3e50;
  height: auto;
}
</style>
