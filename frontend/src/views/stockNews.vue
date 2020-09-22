<template>
  <div class="container text-center">
    <h1>{{ title }}</h1>
    <div id="myModal" class="my-modal" :class="{'now-loading': loading}">
      <div class="my-modal-content">
        <p class="loading">
          Now Loading
        </p>
      </div>
    </div>
    <div class="range">
      <input type="date" class="chartStart">
      <input type="date" class="mx-3 chartEnd">
      <button class="btn btn-primary update-chart">초기화</button>
    </div>
    <canvas id="chart" @on-receive="click"></canvas>
    <div class="card mb-3 border" v-for="(dayNews, idx) in news" :key="idx">
      <a :href="dayNews.link" class="card-body py-2 news" target="_blank">
        <p class="m-0">{{ dayNews.title }}</p>
        <p class="m-0">{{ dayNews.date }}</p>
      </a>
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
        news: [],
        page: 1,
        date: '',
        loading: false,
      }
    },
    created() {
      document.addEventListener('scroll', this.vue_scroll)
    },
    beforeRouteLeave() {
      document.removeEventListener('scroll', this.vue_scroll)
    },
    mounted() {
      this.title = this.$route.params.company
      this.stock()
    },
    methods: {
      vue_scroll(evt) {
        if (document.documentElement.scrollTop + window.innerHeight >= document.body.scrollHeight && this.news.length != 0) {
          this.getNews(this.date)
        }
      },
      async getNews(date) {
        this.date = date
        if (this.loading === false) {
          this.loading = true
          await axios.get(`articles/news/${this.title}/${date}/${this.page}/`)
            .then(res => {
              console.log(res)
              res.data.data.forEach(value => {
                this.news.push(value)
              });
              this.page = res.data.page
            })
            .catch(err => {
              console.log(err)
            })
          this.loading = false
        }        
      },
      async stock() {
        this.page = 1
        this.news = []
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
            this.news = []
            this.page = 1
            this.getNews(label.replace(/-/gi, '.'))
          }
        }
      }
    }
  }
</script>

<style>
  .news:link {text-decoration: none; color: black;}
  .news:visited {text-decoration: none; color: black;}
  .news:active {text-decoration: none; color: black;}
  .news:hover {text-decoration: none; color: black;}

  .now-loading {
    display: block !important;
  }

  .range {
    float: right;
  }

  .my-modal {
    display: none;
    /* display: block !important; */
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
  .my-modal-content {
    background-color: rgba(0,0,0,0);
    margin: 20% auto;
    width: 15em; /* Could be more or less, depending on screen size */
    height: 15em;
  }

  .my-modal-content::after {
    content: '';
    width: 15em;
    height: 15em;
    left: 0em;
    top: 0em;
    border: 2em solid #f3f3f3; /* Light grey */
    border-top: 2em solid #3498db; /* Blue */
    border-radius: 50%;
    animation: spin 2s linear infinite;
    display: block;
    position: relative;
  }
  
  .loading {
    margin: 0;
    width: 10em;
    height: 10em;
    font-size: 1.5em;
    color: #f3f3f3;
    line-height: 10em;
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