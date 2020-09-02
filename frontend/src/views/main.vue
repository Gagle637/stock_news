<template>
  <div>
    <!-- <p v-for="(value, name, idx) in logos" :key="idx">{{ value }} {{ name }}</p> -->
    <img v-for="(value, name, idx) in logos" :key="idx" @click="goStockNews(name)" :src="value" alt="">
  </div>
</template>

<script>
  import { useRoute, useRouter } from 'vue-router'

  export default {
    data: () => {
      return {
        logos: {
          "삼성전자": require("@/assets/삼성전자.png"),
          "애플": require("@/assets/애플.png")
        }
      }
    },
    methods: {
      goStockNews(company) {
        // console.log(require("@/assets/삼성전자.png"))
        this.$router.push({name:'stockNews', params:{company:company}})
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>