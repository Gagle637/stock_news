<template>
  <div>
    <h1 class="pt-5">Stock News</h1>
    <div class="container">
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut molestiae molestias aperiam! Nobis, quae ducimus distinctio, necessitatibus ipsa, ratione natus illo perferendis iusto non magnam quas. Quas minima minus doloribus.</p>
      <br>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis placeat dolorem molestias, expedita iusto amet sapiente, quis accusamus possimus in, eveniet quibusdam ab voluptas nisi! Tenetur distinctio quaerat magnam ullam.</p>
      <div class="card d-inline-block px-3 m-2" style="width: 20rem;" v-for="(value, name, idx) in logos" :key="idx">
        <div class="w-100 d-flex" style="height: 18rem">
          <img class="card-img-top m-auto" :src="value" :alt="name">
        </div>
        <div class="card-body">
          <h5 class="card-title">{{ name }}</h5>
          <p class="btn btn-primary" @click="goStockNews(name)">GO</p>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
  import { useRoute, useRouter } from 'vue-router'

  export default {
    data: () => {
      return {
        logos: {
          "삼성전자": require("@/assets/삼성전자.png"),
          "애플": require("@/assets/애플.png"),
          "삼성전자2": require("@/assets/삼성전자.png"),
          "애플2": require("@/assets/애플.png"),
          "삼성전자3": require("@/assets/삼성전자.png"),
          "애플3": require("@/assets/애플.png"),
        }
      }
    },
    methods: {
      goStockNews(company) {
        this.$router.push({name:'stockNews', params:{company:company}})
      }
    }
  }
</script>

<style lang="scss" scoped>

</style>