import { createApp } from 'vue'
import axios from 'axios'
import App from './App.vue'
import router from './routes'

axios.defaults.baseURL = 'http://localhost:8000'+'/api/'


createApp(App).use(router, axios).mount('#app')
