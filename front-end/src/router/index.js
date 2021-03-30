import Vue from "vue";
import VueRouter from "vue-router";
import Index from "../views/Index.vue";
import Login from "../views/Login.vue";
import NewAccount from "../views/NewAccount.vue";
import PatientPanel from "../views/PatientPanel.vue";
import DoctorPanel from "../views/DoctorPanel.vue";

import DoctorPanelPage from "../components/doctor/DoctorPanelPage.vue";
import DoctorFormPage from "../components/doctor/DoctorFormPage.vue";
import DoctorReportEditPage from "../components/doctor/DoctorReportEditPage.vue";

import EntitiesPanel from "../components/entities/EntitiesPanel.vue";
//import EntitiesFormPage from "../components/entities/EntitiesFormPage.vue";

import PatientPanelPage from "../components/patient/PatientPanelPage.vue";
import FormPage from "../components/patient/FormPage.vue";
import ReportEditPage from "../components/patient/ReportEditPage.vue";
import NewApplicantEditPage from "../components/patient/NewApplicantEditPage.vue";
import CovidScreenEditPage from "../components/patient/CovidScreenEditPage.vue";
import MedicalHistoryEditPage from "../components/patient/MedicalHistoryEditPage.vue";

import ClerkPanel from "../views/ClerkPanel.vue";
import ClerkPanelPage from '../components/clerk/ClerkPanelPage.vue'
import ClerkForms from '../components/clerk/ClerkForms.vue'

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "index",
        component: Index
    },
    {
        path: "/login",
        name: "login",
        component: Login
    },
    {
        path: "/new-account",
        name: "new-account",
        component: NewAccount
    },

    {
        path: "/clerk-panel",
        name: "clerk-panel",
        component: ClerkPanel,
        children: [
            {
                path: "/",
                component: ClerkPanelPage
            },
            {
                path: "forms",
                name: "clerk-form-home-page",
                component: ClerkForms
            },
            {
                path: "forms/edit-new-applicant/:ssn?",
                name: "approve-applicant",
                props: true,
                component: NewApplicantEditPage,
            },
            {   path: "forms/view-patient-covid-screen/:date?",
                name: "view-patient-covid-screen",
                props: true,
                component: CovidScreenEditPage
        }
        ]
    },

    {
        path: "/patient-panel",
        name: "patient-panel",
        component: PatientPanel,
        children: [
            {
                path: "/",
                component: PatientPanelPage
            },
            {
                path: "forms",
                component: FormPage
            },
            {
                path: "forms/edit-report/:id?",
                name: "edit-report",
                props: true,
                component: ReportEditPage
            },
            {
                path: "forms/edit-new-applicant/:ssn?",
                name: "edit-new-applicant",
                props: true,
                component: NewApplicantEditPage,
            },
            {
                path: "forms/edit-covid-screen/:date?",
                name: "edit-covid-screen",
                props: true,
                component: CovidScreenEditPage
            },
            {
                path: "forms/edit-medical-history/:ssn?",
                name: "edit-medical-history",
                props: true,
                component: MedicalHistoryEditPage
            }
        ]
    },

    {
        path: "/doctor-panel",
        name: "doctor-panel",
        component: DoctorPanel,
        children: [
            {
                path: "/",
                component: DoctorPanelPage
            },
            {
                path: "forms",
                name: "view-patients",
                component: DoctorFormPage
            },
            {
                path: "forms",
                name: "doctor-edit-report",
                component: DoctorReportEditPage
            }
        ]
    },

    {
        path: "/entities-panel",
        name: "entities-panel",
        props: true,
        component: EntitiesPanel,
        
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;
