<template>
  <div>
    <h1>{{ title }}</h1>
    <div id="myModal" class="modal">
      <div class="modal-content">
        <p class="loading">
          Now Loading
        </p>
      </div>
    </div>
    <input type="date" class="chartStart">
    <input type="date" class="chartEnd">
    <button class="update-chart">초기화</button>
    <canvas id="chart" @on-receive="click"></canvas>
    <div v-for="(dayNews, idx) in news" :key="idx">
      <p>{{ dayNews.title }}</p>
      <p>{{ dayNews.date }}</p>
      <p>{{ dayNews.link }}</p>
      <!-- <p>{{ dayNews.description }}</p> -->
      <!-- <p>{{ dayNews.company }}</p> -->
    </div>
  </div>
</template>

<script>
  import Chart from 'chart.js'
  import axios from 'axios'
  var d3 = require('d3')
  

  export default {
    data: () => {
      return {
        dataset: {
          '삼성전자': 'samsung',
          '애플': 'apple'
        },
        title: '',
        news: []
      }
    },
    mounted() {
      this.title = this.$route.params.company
      this.stock()
    },
    methods: {
      async getNews(date) {
        document.getElementById('myModal').style.display = 'block'
        await axios.get(`articles/news/${this.title}/${date}/`)
          .then(res => {
            this.news = res.data.data
          })
          .catch(err => {
            console.log(err)
          })
        document.getElementById('myModal').style.display = ''
      },
      async stock() {
        let data = await d3.csv(`/dataset/${this.dataset[this.$route.params.company]}.csv`)
        let labels = data.map(function(d) {return d.Date})
        let stockData = data.map(function(d) {return d.Close})
        var ctx = document.getElementById('chart')
        var chart = new Chart(ctx, {
          type: 'line',
          options: {
            tooltips: {
              mode: 'index',
              intersect: false
            },
            legend: {
              display: false
            },
            elements: {
              point:{
                radius: 0,
                hoverRadius: 0
              }
            },
            scales: {
              xAxes: [{
                type: 'time',
                time: {
                  unit: 'year'
                },
                gridLines: {
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
        
        document.querySelector(".chartStart").addEventListener('change', evt => {
          chart.options.scales.xAxes[0].ticks.min = document.querySelector(".chartStart").value
          chart.update()
        })

        document.querySelector(".chartEnd").addEventListener('change', evt => {
          chart.options.scales.xAxes[0].ticks.max = document.querySelector(".chartEnd").value
          chart.update()
        })

        document.querySelector('.update-chart').addEventListener('click', evt => {
          document.querySelector(".chartEnd").value = ''
          document.querySelector(".chartStart").value = ''
          chart.options.scales.xAxes[0].ticks.min = ''
          chart.options.scales.xAxes[0].ticks.max = ''
          chart.update()
        })

        document.getElementById('chart').onclick = evt => {
          var activePoints = chart.getElementsAtXAxis(evt)
          var firstPoint = activePoints[0]
          var label = chart.data.labels[firstPoint._index]
          var value = chart.data.datasets[firstPoint._datasetIndex].data[firstPoint._index]
          if (confirm(label + ': ' + value)) {
            this.getNews(label.replace(/-/gi, '.'))
          }
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