<template>
  <div>
    <!-- <h1 class="pt-5 text-center">Stock News</h1> -->
    <div class="container">
      <img class="col-12 m-auto" src="@/assets/mainpage.png" alt="main">
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Aut molestiae molestias aperiam! Nobis, quae ducimus distinctio, necessitatibus ipsa, ratione natus illo perferendis iusto non magnam quas. Quas minima minus doloribus.</p>
      <br>
      <p>Lorem ipsum dolor sit amet consectetur adipisicing elit. Veritatis placeat dolorem molestias, expedita iusto amet sapiente, quis accusamus possimus in, eveniet quibusdam ab voluptas nisi! Tenetur distinctio quaerat magnam ullam.</p>
      <div class="row justify-content-center">
        <div @click="goStockNews(name)" class="col-sm-5 col-6 col-md-3 p-0 m-3 border logos" style="height: 15em" v-for="(value, name, idx) in logos" :key="idx">
          <div class="w-100 m-0 row justify-content-center" style="height: 10em">
            <img class="h-100" :src="value" :alt="name" >
          </div>
          <p class="w-100 company">{{ name }}</p>
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
          "삼성전자4": require("@/assets/삼성전자.png"),
          "애플4": require("@/assets/애플.png"),
          "삼성전자5": require("@/assets/삼성전자.png"),
          "애플5": require("@/assets/애플.png"),
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

<style scoped>
  .logos {
    box-shadow: 0 3px 6px rgba(0,0,0,0.16), 0 3px 6px rgba(0,0,0,0.23);
    cursor: pointer;
  }
  .company {
    position: absolute;
    text-align: center;
    bottom: 0;
    -moz-user-select: none;
    -webkit-user-select: none;
    font-size: 3em;
    font-family: 'Dokdo', cursive;
    margin: 0;
  }
</style>