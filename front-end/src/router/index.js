import Vue from "vue";
import VueRouter from "vue-router";
import Index from "../views/Index.vue";
import Login from "../views/Login.vue";
import NewAccount from "../views/NewAccount.vue";
import PatientPanel from "../views/PatientPanel.vue";
import DoctorPanel from "../views/DoctorPanel.vue";
import ClerkPanel from "../views/ClerkPanel.vue";
import EntitiesPanel from "../views/EntitiesPanel.vue";

import DoctorPanelPage from "../components/doctor/DoctorPanelPage.vue";
import DoctorFormPage from "../components/doctor/DoctorFormPage.vue";
import DoctorReportEditPage from "../components/doctor/DoctorReportEditPage.vue";

import EntitiesPanelPage from "../components/entities/EntitiesPanelPage.vue";
import AddNewEntity from "../components/entities/AddNewEntity.vue";

import PatientPanelPage from "../components/patient/PatientPanelPage.vue";
import FormPage from "../components/patient/FormPage.vue";
import ReportEditPage from "../components/patient/ReportEditPage.vue";
import NewApplicantEditPage from "../components/patient/NewApplicantEditPage.vue";
import CovidScreenEditPage from "../components/patient/CovidScreenEditPage.vue";
import MedicalHistoryEditPage from "../components/patient/MedicalHistoryEditPage.vue";

import ClerkPanelPage from "../components/clerk/ClerkPanelPage.vue";
import ClerkForms from "../components/clerk/ClerkForms.vue";

Vue.use(VueRouter);

const routes = [
    {
        path: "/",
        name: "index",
        component: Index,
        meta: {
            title: "Home - RPD Symptom Analyser"
        }
    },
    {
        path: "/login",
        name: "login",
        component: Login,
        meta: {
            title: "Login - RPD Symptom Analyser"
        }
    },
    {
        path: "/new-account",
        name: "new-account",
        component: NewAccount,
        meta: {
            title: "Register - RPD Symptom Analyser"
        }
    },

    {
        path: "/clerk-panel",
        name: "clerk-panel",
        component: ClerkPanel,
        meta: {
            title: "Clerk - RPD Symptom Analyser"
        },
        children: [
            {
                path: "/",
                component: ClerkPanelPage,
                meta: {
                    title: "Clerk - RPD Symptom Analyser"
                }
            },
            {
                path: "forms",
                name: "clerk-form-home-page",
                component: ClerkForms,
                meta: {
                    title: "Clerk - RPD Symptom Analyser"
                }
            },
            {
                path: "forms/edit-new-applicant/:ssn?",
                name: "approve-applicant",
                props: true,
                component: NewApplicantEditPage,
                meta: {
                    title: "Clerk - RPD Symptom Analyser"
                }
            },
            {
                path: "forms/view-patient-covid-screen/:date?",
                name: "view-patient-covid-screen",
                props: true,
                component: CovidScreenEditPage,
                meta: {
                    title: "Clerk - RPD Symptom Analyser"
                }
            },
            {
                path: "forms/view-patient-report/:id?",
                name: "view-patient-report",
                props: true,
                component: ReportEditPage,
                meta: {
                    title: "Clerk - RPD Symptom Analyser"
                }
            },
            {
                path: "forms/view-patient-history/:ssn?",
                name: "view-patient-history",
                props: true,
                component: MedicalHistoryEditPage,
                meta: {
                    title: "Clerk - RPD Symptom Analyser"
                }
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
                component: PatientPanelPage,
                meta: {
                    title: "Patient - RPD Symptom Analyser"
                }
            },
            {
                path: "forms",
                component: FormPage,
                meta: {
                    title: "Patient - RPD Symptom Analyser"
                }
            },
            {
                path: "forms/edit-report/:id?",
                name: "edit-report",
                props: true,
                component: ReportEditPage,
                meta: {
                    title: "Patient - RPD Symptom Analyser"
                }
            },
            {
                path: "forms/edit-new-applicant/:ssn?",
                name: "edit-new-applicant",
                props: true,
                component: NewApplicantEditPage,
                meta: {
                    title: "Patient - RPD Symptom Analyser"
                }
            },
            {
                path: "forms/edit-covid-screen/:date?",
                name: "edit-covid-screen",
                props: true,
                component: CovidScreenEditPage,
                meta: {
                    title: "Patient - RPD Symptom Analyser"
                }
            },
            {
                path: "forms/edit-medical-history/:ssn?",
                name: "edit-medical-history",
                props: true,
                component: MedicalHistoryEditPage,
                meta: {
                    title: "Patient - RPD Symptom Analyser"
                }
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
                component: DoctorPanelPage,
                meta: {
                    title: "Doctor - RPD Symptom Analyser"
                }
            },
            {
                path: "forms",
                name: "view-patients",
                component: DoctorFormPage,
                meta: {
                    title: "Doctor - RPD Symptom Analyser"
                }
            },
            {
                path: "forms",
                name: "doctor-edit-report",
                component: DoctorReportEditPage,
                meta: {
                    title: "Doctor - RPD Symptom Analyser"
                }
            }
        ]
    },

    {
        path: "/entities-panel",
        props: true,
        component: EntitiesPanel,
        children: [
            {
                path: "/",
                props: true,
                name: "entities-panel",
                component: EntitiesPanelPage,
                meta: {
                    title: "Entities - RPD Symptom Analyser"
                }
            },
            {
                path: "add-new-entity",
                name: "add-new-entity",
                props: true,
                component: AddNewEntity,
                meta: {
                    title: "Entities - RPD Symptom Analyser"
                }
            }
        ]
    }
];

const router = new VueRouter({
    mode: "history",
    base: process.env.BASE_URL,
    routes
});

// Allows page titles to properly update.
// Taken from https://stackoverflow.com/questions/45462687/how-to-change-page-title-according-to-route-links-vuejs
router.beforeEach((to, from, next) => {
    document.title = to.meta.title;

    next();
});

export default router;
