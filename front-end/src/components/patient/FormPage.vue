<template>
    <div id="forms">
        <div class="flex justify-end w-full fixed">
            <router-link to="/patient-panel">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-14">Forms</p>
                <div class="w-1/2 mb-10">
                    <p class="text-3xl mb-4">Reports</p>
                    <table class="table-fixed w-full">
                        <thead>
                            <tr class="text-lg">
                                <th class="w-3/4 border-black border-2">
                                    Report ID
                                </th>
                                <th class="w-1/4 border-black border-2">
                                    <router-link :to="{ name: 'edit-report' }">
                                        <div
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 transform hover:scale-105 hover:bg-green-600 rounded-lg py-1 px-1 mx-6 my-1"
                                        >
                                            New
                                        </div>
                                    </router-link>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="report in reports"
                                :key="report.Report_ID"
                            >
                                <td class="border-black border-2">
                                    {{ report.Report_ID }}
                                </td>
                                <td class="border-black border-2">
                                    <router-link
                                        :to="{
                                            name: 'edit-report',
                                            params: { id: report.Report_ID },
                                        }"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 transform hover:scale-105 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            View
                                        </div>
                                    </router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="w-1/2 mb-10">
                    <p class="text-3xl mb-4">New Applicant Forms</p>
                    <table class="table-fixed w-full">
                        <thead>
                            <tr class="text-lg">
                                <th class="w-3/5 border-black border-2">
                                    Email
                                </th>
                                <th class="w-1/5 border-black border-2">
                                    Approved
                                </th>
                                <th class="w-1/5 border-black border-2">
                                    <router-link
                                        :to="{ name: 'edit-new-applicant' }"
                                        v-if="new_applicant.length == 0"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 transform hover:scale-105 hover:bg-green-600 rounded-lg py-1 px-1 mx-6 my-1"
                                        >
                                            New
                                        </div>
                                    </router-link>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="report in new_applicant"
                                :key="report.Email"
                            >
                                <td class="border-black border-2">
                                    {{ report.Email }}
                                </td>
                                <td class="border-black border-2">
                                    <svg v-if="report.Is_approved" class="w-1/4 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="green">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                    <svg v-else class="w-1/4 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="red">
                                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                                    </svg>
                                </td>
                                <td class="border-black border-2">
                                    <router-link
                                        :to="{
                                            name: 'edit-new-applicant',
                                            params: { email: report.Email },
                                        }"
                                    >
                                        <div
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 transform hover:scale-105 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            Edit
                                        </div>
                                    </router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="w-1/2 mb-10">
                    <p class="text-3xl mb-4">Covid Screens</p>
                    <table class="table-fixed w-full">
                        <thead>
                            <tr class="text-lg">
                                <th class="w-3/4 border-black border-2">
                                    Date
                                </th>
                                <th class="w-1/4 border-black border-2">
                                    <router-link
                                        :to="{ name: 'edit-covid-screen' }"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 transform hover:scale-105 hover:bg-green-600 rounded-lg py-1 px-1 mx-6 my-1"
                                        >
                                            New
                                        </div>
                                    </router-link>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="report in covid_screen"
                                :key="report.date"
                            >
                                <td class="border-black border-2">
                                    {{ report.Date }}
                                </td>
                                <td class="border-black border-2">
                                    <router-link
                                        :to="{
                                            name: 'edit-covid-screen',
                                            params: { date: report.Date },
                                        }"
                                    >
                                        <div
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 transform hover:scale-105 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            Edit
                                        </div>
                                    </router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="w-1/2 mb-10">
                    <p class="text-3xl mb-4">Medical History</p>
                    <table class="table-fixed w-full">
                        <thead>
                            <tr class="text-lg">
                                <th class="w-3/4 border-black border-2">
                                    SSN
                                </th>
                                 <th class="w-1/4 border-black border-2">
                                    <router-link
                                        :to="{ name: 'edit-medical-history' }"
                                        v-if="medical_history.length == 0"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 transform hover:scale-105 hover:bg-green-600 rounded-lg py-1 px-1 mx-6 my-1"
                                        >
                                            New
                                        </div>
                                    </router-link>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="report in medical_history"
                                :key="report.P_SSN"
                            >
                                <td class="border-black border-2">
                                    {{ report.P_SSN }}
                                </td>
                                <td class="border-black border-2">
                                    <router-link
                                        :to="{
                                            name: 'edit-medical-history',
                                            params: { id: report.P_SSN },
                                        }"
                                    >
                                        <div
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 transform hover:scale-105 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            Edit
                                        </div>
                                    </router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <div v-else class="flex flex-col">
            <p class="text-5xl mt-20">Forbidden</p>
            <p class="text-3xl mt-4">You're not logged in</p>
        </div>
    </div>
</template>

<script>
import axios from "axios";
export default {
    name: "FormPage",

    data() {
        return {
            logged_in: false,
            reports: [],
            new_applicant: [],
            covid_screen: [],
            medical_history: [],
        };
    },

    created() {
        this.getForms();
    },

    methods: {
        getForms() {
            axios
                .get(`http://localhost:5000/patient/forms`, {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                })
                .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;

                    this.reports = response.data.reports;
                    this.new_applicant = response.data.new_applicant;
                    this.covid_screen = response.data.covid_screen;
                    this.medical_history = response.data.medical_history;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>