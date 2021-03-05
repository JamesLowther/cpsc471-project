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
                <p class="text-5xl mt-20 mb-24">Forms</p>
                <div class="w-1/2">
                    <p class="text-3xl mb-4">Reports</p>
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="w-3/4 border-black border-2">
                                    Report ID
                                </th>
                                <th class="w-1/4 border-black border-2">
                                    <router-link :to="{ name: 'edit-report' }">
                                        <div
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 rounded-lg py-1 px-1 mx-6 my-1"
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
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            Edit
                                        </div>
                                    </router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="w-1/2">
                    <p class="text-3xl mb-4">New Applicant Forms</p>
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="w-3/4 border-black border-2">
                                    Email
                                </th>
                                <th class="w-1/4 border-black border-2">
                                    <router-link
                                        :to="{ name: 'edit-new-applicant' }"
                                        v-if="new_applicant.length == 0"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 rounded-lg py-1 px-1 mx-6 my-1"
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
                                    <router-link
                                        :to="{
                                            name: 'edit-new-applicant',
                                            params: { email: report.Email },
                                        }"
                                    >
                                        <div
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            Edit
                                        </div>
                                    </router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="w-1/2">
                    <p class="text-3xl mb-4">Covid Screens</p>
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="w-3/4 border-black border-2">
                                    Date
                                </th>
                                <th class="w-1/4 border-black border-2">
                                    Link
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="report in covid_screens"
                                :key="report.date"
                            >
                                <td class="border-black border-2">
                                    {{ report.date }}
                                </td>
                                <td class="border-black border-2">test</td>
                            </tr>
                        </tbody>
                    </table>
                </div>
                <div class="w-1/2">
                    <p class="text-3xl mb-4">Medical History</p>
                    <table class="table-fixed w-full">
                        <thead>
                            <tr>
                                <th class="w-3/4 border-black border-2">
                                    History ID
                                </th>
                                <th class="w-1/4 border-black border-2">
                                    Link
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="report in medical_history"
                                :key="report.HID"
                            >
                                <td class="border-black border-2">
                                    {{ report.HID }}
                                </td>
                                <td class="border-black border-2">test</td>
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
            covid_screens: [],
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
                    this.covid_screens = response.data.covid_screens;
                    this.medical_history = response.data.medical_history;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>