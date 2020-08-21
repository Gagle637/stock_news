<template>
  <div>
    <h1>Hello World ! ! !</h1>
    <button @click="stock()">d3</button>
    <canvas id="chart"></canvas>
  </div>
</template>

<script>
  import Chart from 'chart.js';
  var d3 = require("d3");


  export default {
    methods: {
      async stock() {
        let data = await d3.csv("/dataset/samsung.csv");
        let labels = data.map(function(d) {return d.Date})
        let stockData = data.map(function(d) {return d.Close})
        
        var ctx = document.getElementById('chart')
        var chart = new Chart(ctx, {
          type: 'line',
          options: {
            legend: {
              display: false
            },
            elements: {
              point:{
                radius: 2
              }
            },
            scales: {
              xAxes: [{
                gridLines: {
                  display:false
                },
                ticks: {
                  display: false
                }
              }]
            }
          },
          data: {
            labels: labels,
            datasets: [
              {
                fill: false,
                borderColor: 'rgb(255, 99, 132)',
                data: stockData
              }
            ]
          }
        })
        chart
      }
    }
  }
</script>

<style>

</style>