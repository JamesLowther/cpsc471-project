import Vue from 'vue'
import VueRouter from 'vue-router'
import Index from '../views/Index.vue'
import Login from '../views/Login.vue'
import NewAccount from '../views/NewAccount.vue'
import PatientPanel from '../views/PatientPanel.vue'

import PatientPanelPage from '../components/patient/PatientPanelPage.vue'
import FormPage from '../components/patient/FormPage.vue'
import ReportEditPage from '../components/patient/ReportEditPage.vue'
import NewApplicantEditPage from '../components/patient/NewApplicantEditPage.vue'

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
    component: PatientPanel,
    children: [
      {
        path: '/',
        component: PatientPanelPage
      },
      {
        path: 'forms',
        component: FormPage
      },
      {
        path: 'forms/edit-report/:id?',
        name: 'edit-report',
        props: true,
        component: ReportEditPage
      },
      {
        path: 'forms/edit-new-applicant/:email?',
        name: 'edit-new-applicant',
        component: NewApplicantEditPage
      }
    ]
  }
]

const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router