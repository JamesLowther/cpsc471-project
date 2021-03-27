<template>
    <div id="forms">
        <div class="flex justify-end w-full fixed">
            <router-link to="/clerk-panel">
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
                    <p class="text-3xl mb-4">New Applicant Forms</p>
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="w-3/4 border-black border-2">
                                    Patient SSN
                                </th>
                                <th class="w-1/4 border-black border-2">
                                    <router-link to="/clerk-panel/forms/new-applicant-form"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 rounded-lg py-1 px-1 mx-6 my-1"
                                        >
                                            Create a New Applicant Form
                                        </div>
                                    </router-link>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="form in new_applicant"
                                :key="form.P_SSN"
                            >
                                <td class="border-black border-2">
                                    {{ form.P_SSN }}
                                </td>
                                <td class="border-black border-2">
                                    <router-link
                                        :to="{
                                            name: 'LINK TO APPROVE APPLICANT FORMS',
                                            params: { P_SSN: form.P_SSN }
                                        }"
                                    >
                                        <div
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            to:view application and approve or reject
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
                                <th class="w-2/5 border-black border-2">
                                    Date
                                </th>
                                <th class="w-2/5 border-black border-2">
                                    Patient SSN
                                </th>
                                <th class="w-1/5 border-black border-2">
                                    View
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="form in covid_screens"
                                :key="form.Date"
                            >
                                <td class="border-black border-2">
                                    {{ form.Date }}
                                </td>
                                <td class="border-black border-2">
                                    {{ form.P_SSN }}
                                </td>
                                <td class="border-black border-2">
                                    <router-link
                                        :to="{
                                            name: 'LINK TO VIEW COVID SCREEN',
                                            params: { email: form.Email, P_ssn: form.P_SSN },
                                        }"
                                    >
                                        <div
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            to: view screen; approve or recommend action (emergency, isolate etc)
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
            new_applicant: [],
            covid_screens: [],
        };
    },

    created() {
        this.getForms();
    },

    methods: {
        getForms() {
            axios
                .get(`http://localhost:5000/clerk/forms`, {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                })
                .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;

                    this.new_applicant = response.data.new_applicant;
                    this.covid_screens = response.data.covid_screens;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>