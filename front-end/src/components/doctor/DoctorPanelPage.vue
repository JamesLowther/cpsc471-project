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
                <p class="text-3xl md:text-4xl lg:text-5xl mt-20 bg-blue-300">Doctor Panel</p>
                <p class="text-2xl md:text-3xl lg:text-4xl mt-4 bg-blue-300">SSN: {{ ssn }}</p>
            </div>
            <div class="flex flex-wrap items-center justify-center mt-16 md:mt-24 lg:mt-48">
                <div class="w-full sm:w-1/3 lg:w-1/4 mb-10">
                    <p class="text-2xl md:text-3xl lg:text-4xl mt-2 mb-2">Patient Reports:</p>

                    <router-link to="doctor-panel/forms">
                        <div
                            class="text-white shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-4 md:py-8 px-4 m-2 text-1xl md:text-2xl"
                        >
                            Search
                        </div>
                    </router-link>

                    <p class="text-2xl md:text-3xl lg:text-4xl mt-2 mb-2">Update Database:</p>

                    <router-link :to="{name: 'entities-panel',params: { entity_type: 'medication', user_type:'doctor' }}">
                        <div class="text-white shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-4 md:py-8 px-4 m-2 text-1xl md:text-2xl">
                            Medications
                        </div>
                    </router-link>

                    <router-link :to="{name: 'entities-panel',params: { entity_type: 'illness', user_type:'doctor' }}">
                        <div class="text-white shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-4 md:py-8 :py-8 px-4 m-2 text-1xl md:text-2xl">
                            Illnesses
                        </div>
                    </router-link>

                    <router-link :to="{name: 'entities-panel',params: { entity_type: 'symptom', user_type:'doctor' }}">
                        <div class="text-white shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-4 md:py-8 px-4 m-2 text-1xl md:text-2xl">
                            Symptoms
                        </div>
                    </router-link>
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
    name: "DoctorPanelPage",

    data() {
        return {
            logged_in: false,
            ssn: "",
        };
    },

    created() {
        this.doctorGet();
    },

    methods: {
        doctorGet() {
            axios
                .get("doctor", {
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