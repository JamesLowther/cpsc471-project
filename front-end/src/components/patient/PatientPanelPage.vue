<template>
    <div id="index">
        <div class="flex justify-end w-full fixed">
            <button
                @click="logout()"
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
            >
                <span v-if="logged_in">Logout</span>
                <span v-else>Back</span>
            </button>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col">
                <p class="text-5xl mt-20">Patient Panel</p>
                <p class="text-3xl mt-4">SSN: {{ ssn }}</p>
            </div>
            <div class="flex flex-wrap items-center justify-center mt-48">
                <router-link to="patient-panel/forms">
                    <div
                        class="text-white shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-8 px-4"
                    >
                        Reports, Forms, and Screens
                    </div>
                </router-link>
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
    name: "PatientPanelPage",

    data() {
        return {
            logged_in: false,
            ssn: "",
        };
    },

    created() {
        this.patientGet();
    },

    methods: {
        patientGet() {
            axios
                .get("patient", {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                })
                .then((response) => {
                    if (response.data.logged_in != "1") {
                        return;
                    }

                    this.logged_in = true;

                    this.ssn = response.data.ssn;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        logout() {
            localStorage.removeItem("jwt");
            this.$router.push("/");
        },
    },
};
</script>