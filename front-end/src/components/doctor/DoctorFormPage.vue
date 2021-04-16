<template>
    <div id="Doctor_forms">
        <div class="flex justify-end w-full fixed">
            <router-link to="/doctor-panel">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col">
                <p class="text-3xl md:text-4xl lg:text-5xl mt-20 bg-blue-300">
                    Doctor Panel
                </p>
                <p class="text-2xl md:text-3xl lg:text-4xl mt-4 bg-blue-300">
                    Patient Reports
                </p>
            </div>
            <div class="flex flex-col items-center pt-10 w-full mt-16 mb-4">
                <table
                    class="w-full ml-auto md: mr-auto md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg"
                >
                    <thead>
                        <tr>
                            <th
                                class="text-lg text-black w-full bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-r-2"
                            >
                                <input
                                    class="border border-blue-700 w-3/4 mb-2 mt-2 p-1 rounded-lg"
                                    type="text"
                                    name="PatientName"
                                    placeholder="Search Reports"
                                    v-model="form.patientName"
                                    v-on:keyup="searchPatients()"
                                />
                            </th>
                            <th
                                class="text-lg text-white bg-blue-500 border-b-2 p-2 pb-0"
                            >
                                Report-#
                            </th>
                            <th
                                class="text-lg text-white bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2 px-8"
                            ></th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr
                            class="bg-blue-100"
                            v-for="(patient, i) in patientList"
                            :key="`${i}-${patient}`"
                        >
                            <td class="border-blue-300 border-2">
                                {{ patient.Lname }}, {{ patient.Fname }}
                            </td>
                            <td class="border-blue-300 border-2">
                                {{ patient.Report_ID }}
                            </td>
                            <td class="border-blue-300 border-2">
                                <router-link
                                    :to="{
                                        name: 'doctor-edit-report',
                                        params: {
                                            p_ssn: patient.P_SSN,
                                            id: patient.Report_ID
                                        }
                                    }"
                                >
                                    <div
                                        class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-1 px-4 mx-6 my-1"
                                    >
                                        View
                                    </div>
                                </router-link>
                            </td>
                        </tr>
                        <tr class=" shadow-2xl">
                            <td
                                class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl  h-7"
                                colspan="3"
                            />
                        </tr>
                    </tbody>
                </table>
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
            dropdown: false,
            logged_in: true,
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
            axios
                .post(
                    "doctor/forms",
                    {
                        action_type: "get_form",
                        form_type: "patient_search",
                        p_ssn: -1,
                        thePatientName: this.form.patientName
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                )
                .then(response => {
                    if (response.data.logged_in != "1") {
                        this.logged_in = false;
                        return;
                    }

                    this.logged_in = true;
                    this.patientList = response.data.patients;
                })
                .catch(e => {
                    console.log(e);
                });
        },

        getForms() {
            axios
                .get("doctor/forms", {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt")
                    }
                })
                .then(response => {
                    if (response.data.logged_in != "1") {
                        this.logged_in = false;
                        return;
                    }

                    this.logged_in = true;

                    this.patientList = response.data.patients;
                })
                .catch(e => {
                    console.log(e);
                });
        }
    }
};
</script>
