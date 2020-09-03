import { createApp } from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './routes'
import 'bootstrap/dist/css/bootstrap.css'
import 'bootstrap/dist/js/bootstrap.js'

axios.defaults.baseURL = 'http://localhost:8000'+'/api/'

createApp(App).use(router, axios).mount('#app')
