<template>
    <div id="Entities_forms">
        <div v-if="user_type == 'doctor'" class="flex justify-end w-full fixed">
            <router-link to="/doctor-panel">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>
        <div v-if="user_type == 'clerk'" class="flex justify-end w-full fixed">
            <router-link to="/clerk-panel">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>
        <!-- Parameter will specify which Entity form DIVS to load between med, illness, and symptoms-->
        <!-- STARTING WITH MEDICATION DIV FORMS -->
        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-24">Forms</p>
                <div class="w-1/2">
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="w-3/4 border-black border-2">
                                    Search Patients: 
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg"
                                        type="text"
                                        name="PatientName"
                                        v-model="form.patientName"
                                        v-on:keyup="searchPatients()"
                                    />
                                </th>
                                <th class="w-1/4 border-black border-2">
                                    <p class="text-3xl mb-4">Reports</p>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="(patient, i) in patientList"
                                :key="`${i}-${patient}`"
                            >
                                <td class="border-black border-2">
                                    {{ patient.Lname }}, {{ patient.Fname }}
                                </td>
                                <td class="border-black border-2">
                                    <router-link
                                        :to="{
                                            name: 'view-reports',
                                            params: { id: patient.P_SSN },
                                        }"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            View
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
    name: "DoctorFormPage",

    data() {
        return {
            logged_in: true,
            user_type: "",
            patientList: [],
            form: {
                thePatientName: "" 
            }
        };
    },

    created() {
        this.getForms();
    },

    methods: {
        searchPatients() {
            axios.post(`http://localhost:5000/doctor/forms`,
                {
                    action_type: "get_form",
                    form_type: "patient_search",
                    thePatientName: this.form.patientName
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            )
            .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;
                    this.patientList = response.data.patients;
                })
                .catch((e) => {
                    console.log(e);
                });
        },

        getForms() {
            axios
                .get(`http://localhost:5000/doctor/forms`, {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                })
                .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;

                    this.patientList = response.data.patients;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>