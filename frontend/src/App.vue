<template>
  <div id="app">
    <img alt="Vue logo" src="./assets/logo.png">
    <button @click="stock()">d3</button>
    <router-view></router-view>
  </div>
</template>

<script>
// import dataset from "./samsung.csv";
var d3 = require("d3");

export default {
  name: 'App',
  methods: {
    async stock() {
      let data = await d3.csv("/dataset/samsung.csv");
      console.log(data)
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 60px;
}
</style>
