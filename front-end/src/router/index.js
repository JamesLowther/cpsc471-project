import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/Index.vue'
import Login from '../views/Login.vue'
import NewAccount from '../views/NewAccount.vue'
import PatientPanel from '../views/PatientPanel.vue'

Vue.use(VueRouter)

const routes = [
  {
    path: '/',
    name: 'index',
    component: Index
  },
  {
    path: '/login',
    name: 'login',
    component: Login
  },
  {
    path: '/new-account',
    name: 'new-account',
    component: NewAccount
  },
  {
    path: '/patient-panel',
    name: 'patient-panel',
    component: PatientPanel
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router