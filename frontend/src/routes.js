import { createRouter, createWebHistory } from 'vue-router'
import stockNews from '@/views/stockNews.vue'
import main from '@/views/main.vue'

const history = createWebHistory()
const router = createRouter({
  history,
  routes: [
    {
      path: '/',
      name: 'main',
      component: main,
    },
    {
      path: '/stock-news/:company/',
      name: 'stockNews',
      component: stockNews,
    },
  ]
})

export default router