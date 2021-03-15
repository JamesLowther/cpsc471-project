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
import EntitiesFormPage from "../components/entities/EntitiesFormPage.vue";

import PatientPanelPage from "../components/patient/PatientPanelPage.vue";
import FormPage from "../components/patient/FormPage.vue";
import ReportEditPage from "../components/patient/ReportEditPage.vue";
import NewApplicantEditPage from "../components/patient/NewApplicantEditPage.vue";

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
                component: ClerkForms
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
                path: "forms/edit-new-applicant/:email?",
                name: "edit-new-applicant",
                component: NewApplicantEditPage
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
                name: "view-reports",
                component: DoctorReportEditPage
            }
        ]
    },

    {
        path: "/entities-panel",
        name: "entities-panel",
        component: EntitiesPanel,
        children: [
            {
                path: "medications",
                name: "search-medications",
                component: EntitiesFormPage
            },
            {
                path: "medications/:name?",
                name: "edit-medications",
                component: EntitiesFormPage
            },
            {
                path: "illnesses",
                name: "search-illnesses",
                component: EntitiesFormPage
            },
            {
                path: "illnesses/:illness_name?",
                name: "edit-illnesses",
                component: EntitiesFormPage
            },
        ]
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

export default router;
