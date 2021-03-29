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
                <p class="text-5xl mt-20 mb-24 bg-blue-300">Patient Report Records:</p>
            </div>
            <div class="flex flex-col items-center">
                <div class="w-1/2">
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="w-2/4 border-black border-2">
                                    Search Patient Reports: 
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg"
                                        type="text"
                                        name="PatientName"
                                        v-model="form.patientName"
                                        v-on:keyup="searchPatients()"
                                    />
                                </th>
                                <th class="w-1/4 border-black border-2">
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
                                    Report #: {{ patient.Report_ID }}
                                </td>
                                <td class="border-black border-2">

                                    <!-- Dropdown selector for Reports ordered by date -->
                                    <!-- <div class="relative inline-block text-left">
                                        <div>
                                            <button type="button" class="inline-flex justify-center w-full rounded-md border border-gray-300 shadow-sm px-4 py-2 bg-white text-sm font-medium text-gray-700 hover:bg-gray-50 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-offset-gray-100 focus:ring-indigo-500" id="options-menu" aria-expanded="true" aria-haspopup="true" @click="dropdown = !dropdown">
                                              Options -->
                                              <!-- Heroicon name: solid/chevron-down -->
                                  <!--             <svg class="-mr-1 ml-2 h-5 w-5" xmlns="http://www.w3.org/2000/svg" viewBox="0 0 20 20" fill="currentColor" aria-hidden="true">
                                                <path fill-rule="evenodd" d="M5.293 7.293a1 1 0 011.414 0L10 10.586l3.293-3.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 010-1.414z" clip-rule="evenodd" />
                                              </svg>
                                            </button>
                                        </div>

                                        <div :class="`origin-top-right absolute right-0 mt-2 w-56 rounded-md shadow-lg bg-white ring-1 ring-black ring-opacity-5 focus:outline-none transition ease-${dropdown ? 'out' : 'in'} duration-${dropdown ? '100' : '75'} transform opacity-${dropdown ? '100' : '0'} scale-${dropdown ? '100' : '95'}`" role="menu" aria-orientation="vertical" aria-labelledby="options-menu" >
                                            <div class="py-1" role="none">
                                              <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">Account settings</a>
                                              <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">Support</a>
                                              <a href="#" class="block px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">License</a>
                                              <form method="POST" action="#" role="none">
                                                <button type="submit" class="block w-full text-left px-4 py-2 text-sm text-gray-700 hover:bg-gray-100 hover:text-gray-900" role="menuitem">
                                                  Sign out
                                                </button>
                                              </form>
                                            </div>
                                        </div>
                                    </div> -->

                                    <router-link
                                        :to="{
                                            name: 'doctor-edit-report',
                                            params: { p_ssn: patient.P_SSN, id: patient.Report_ID },
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
            axios.post(`http://localhost:5000/doctor/forms`,
                {
                    action_type: "get_form",
                    form_type: "patient_search",
                    p_ssn: -1,
                    thePatientName: this.form.patientName,
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