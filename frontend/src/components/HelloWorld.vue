<template>
  <div>
    <h1>Hello World ! ! !</h1>
    <div id="myModal" class="modal">
      <div class="modal-content">
        <p class="loading">
          Now Loading
        </p>
      </div>
    </div>
    <button @click="getNews">click</button>
    <canvas id="chart" @on-receive="click"></canvas>
    <div v-for="(dayNews, idx) in news" :key="idx">
      <p>{{ dayNews.title }}</p>
      <p>{{ dayNews.date }}</p>
      <p>{{ dayNews.link }}</p>
      <p>{{ dayNews.description }}</p>
      <!-- <p>{{ dayNews.company }}</p> -->
    </div>
  </div>
</template>

<script>
  import Chart from 'chart.js'
  import axios from 'axios'
  var d3 = require("d3")
  

  export default {
    data: () => {
      return {
        news: []
      }
    },
    mounted() {
      this.stock()
    },
    methods: {
      async getNews() {
        document.getElementById("myModal").style.display = "block"
        await axios.get("articles/news/")
          .then(res => {
            this.news = res.data.data
            console.log(res.data.data)
          })
          .catch(err => {
            console.log(err)
          })
        document.getElementById("myModal").style.display = ""
      },
      async stock() {
        let data = await d3.csv("/dataset/samsung.csv")
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
            ],
          },
        })

        document.getElementById("chart").onclick = function(evt){
          var activePoints = chart.getElementsAtEvent(evt)
          var firstPoint = activePoints[0]
          var label = chart.data.labels[firstPoint._index]
          var value = chart.data.datasets[firstPoint._datasetIndex].data[firstPoint._index]
          alert(label + ": " + value)
        }
      }
    }
  }
</script>

<style>
  .modal {
    display: None; 
    position: fixed;
    z-index: 1;
    left: 0;
    top: 0;
    width: 100%; 
    height: 100%; 
    overflow: auto; 
    background-color: rgb(0,0,0); 
    background-color: rgba(0,0,0,0.4); 
    overflow: hidden;
  }

  /* Modal Content/Box */
  .modal-content {
    background-color: rgba(0,0,0,0);
    margin: 20% auto;
    width: 10em; /* Could be more or less, depending on screen size */
    height: 10em;
    vertical-align: middle;
  }

  .modal-content::after {
    content: '';
    width: 10em;
    height: 10em;
    left: -2em;
    top: -2em;
    border: 2em solid #f3f3f3; /* Light grey */
    border-top: 2em solid #3498db; /* Blue */
    border-radius: 50%;
    animation: spin 2s linear infinite;
    display: block;
    position: relative;
  }
  
  .loading {
    margin: 0;
    width: 160px;
    height: 160px;
    font-size: 1.5em;
    color: #f3f3f3;
    line-height: 160px;
    position: absolute;
    text-align: center;
    font-weight: bolder;
    text-shadow: -1px 0 black, 0 2px black, 1px 0 black, 0 -1px black;
  }

  @keyframes spin {
    0% { transform: rotate(0deg); }
    100% { transform: rotate(360deg); }
  }

</style>