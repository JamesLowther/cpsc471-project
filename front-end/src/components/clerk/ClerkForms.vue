<template>
    <div id="forms">
        <div class="flex justify-end w-full fixed">
            <button class="justify-self-end" @click="$router.go(-1)">
                <div class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                    Back
                </div>
            </button>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-24">Clerk Workstation</p>
                
                <div class="w-full lg:w-4/5">
                    <p class="text-3xl mb-4"></p>
                    <table class="shadow-2xl table-auto w-full h-full mb-10 border-black">
                        <thead>
                            <tr class="h-14">
                                <th class="text-white bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-l-2">
                                    Patient SSN
                                </th>
                                <th class="text-white bg-blue-500 border-teal border-b-2 border-l-2">
                                    Patient Name
                                </th>
                                <th class="text-white bg-blue-500 border-teal border-b-2 border-l-2">
                                    New Application Status
                                </th>
                                <th class="text-white bg-blue-500 border-teal border-b-2 border-l-2">
                                    Medical History
                                </th>
                                <th class="text-white bg-blue-500 border-teal border-b-2 border-l-2">
                                    Covid Screen Date
                                </th>
                                <th class="text-white bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2">
                                    Report ID
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="patient in forms" v-bind:key="patient.P_SSN" class="h-10">
                                <td class="bg-blue-100 border-blue-300 border-2">
                                    {{ patient.P_SSN }}
                                </td>
                                <td class="bg-blue-100 border-blue-300 border-2">
                                    <div v-if="patient.Lname">{{ patient.Lname}}, {{ patient.Fname}}</div>
                                    <div v-else class="bg-red-200 w-2/3 inline-block m-2 rounded">N/A</div>    
                                </td>
                                
                                <!-- New Applicant Forms -->
                                <td class="bg-blue-100 border-blue-300 border-2">

                                    <!--Applicant is Approved: link to existing form-->
                                    <div v-if="patient.Is_approved==1" class="flex flex-wrap items-center justify-around"> 
                                        <p class="bg-green-300 lg:w-2/5 px-1 py-1 rounded">Approved</p>
                                        <router-link class="lg:w-2/5" :to="{name: 'approve-applicant',params: { ssn: patient.P_SSN, isClerk: true, isEdit: true }}">
                                            <div class="text-white px-1 py-1 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-600 hover:bg-blue-500 rounded-lg">
                                                View/Edit
                                            </div>
                                        </router-link>
                                    </div>
                                    
                                    <!--Applicant is Pending: link to existing form-->
                                    <div v-else-if="patient.Is_approved==0" class="flex flex-wrap items-center justify-around"> 
                                        <p class="bg-yellow-300 lg:w-2/5 px-1 py-1 rounded">Pending</p>
                                        <router-link class="lg:w-2/5" :to="{name: 'approve-applicant',params: { ssn: patient.P_SSN, isClerk: true, isEdit: true }}">
                                            <div class="text-white px-1 py-1 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-600 hover:bg-yellow-500 rounded-lg">
                                                View & Approve
                                            </div>
                                        </router-link>
                                    </div>

                                    <!--Applicant has not submitted: link to create new form-->
                                    <div v-else class="flex flex-wrap items-center justify-around">
                                    <p class="bg-red-300 lg:w-2/5 px-1 py-1 rounded">Not Submitted</p>
                                        <router-link class="lg:w-2/5" :to="{name: 'approve-applicant',params: { ssn: patient.P_SSN, isClerk: true, isEdit: false }}">
                                            <div class="text-white px-1 py-1 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-600 hover:bg-green-500 rounded-lg">
                                                Create New
                                            </div>
                                        </router-link>
                                    </div>

                                </td>


                                <!-- Medical Histories -->
                                <td class="bg-blue-100 border-blue-300 border-2">

                                <!-- Medical history has been submitted, link to view-->
                                    <div v-if="patient.TPAL_total != null"> 
                                        <router-link :to="{name: 'view-patient-history',params: { ssn: patient.P_SSN, isClerk: true, isEdit: true }}">
                                            <div class="w-4/5 mx-auto my-2 mx-1 shadow-lg transition duration-300 ease-in-out bg-green-300 hover:bg-blue-500 rounded-lg py-1 px-1">
                                                View/Edit
                                            </div>
                                        </router-link>
                                    </div>

                                    <!--Applicant has not submitted: link to create new form-->
                                    <div v-else>
                                        <router-link :to="{name: 'view-patient-history',params: { ssn: patient.P_SSN, isClerk: true, isEdit: false }}">
                                            <div class="w-4/5 mx-auto my-2 mx-1 shadow-lg transition duration-300 ease-in-out bg-red-200 hover:bg-green-500 rounded-lg py-1 px-1">
                                                Create New
                                            </div>
                                        </router-link>
                                    </div>
                                
                                </td>


                                <!-- Covid Screens -->
                                <td class="bg-blue-100 border-blue-300 border-2">

                                    <!-- Patient has submitted a covid screen -->
                                    <div v-if="patient.dates.length" class="flex flex-wrap items-center justify-around">
                                        <!-- use drop down for multiple screens -->
                                            <select
                                                class="bg-green-300 lg:w-2/5 px-1 py-1 rounded"
                                                id="dates"
                                                v-model="param_date"
                                            >
                                                <option disabled value=null>select one</option>
                                                <option value="New">New</option>
                                                <option v-for="date in patient.dates" 
                                                        v-bind:key="date"
                                                        v-bind:value="date">
                                                    {{date}}
                                                </option>
                                            </select>
                                            <button @click="go_to_covid(param_date,patient.P_SSN)"
                                                    class="lg:w-2/5 px-1 py-1 my-2 shadow-lg transition duration-300 ease-in-out text-white bg-gray-600 hover:bg-blue-500 rounded-lg">
                                                <p v-if="param_date == 'New'">Create New</p>
                                                <p v-else>View/Edit</p>
                                            </button>
                                    </div>

                                    <!-- No covid screens exist -->
                                    <div v-else class="flex flex-wrap items-center justify-around">
                                        <p class="bg-red-200 lg:w-2/5 px-1 py-1 rounded">N/A</p>
                                        <button @click="go_to_covid('New',patient.P_SSN)"
                                        class="lg:w-2/5 px-1 py-1 my-2 shadow-lg transition duration-300 ease-in-out text-white bg-gray-600 hover:bg-green-500 rounded-lg">
                                            Create New
                                        </button>
                                    </div>

                                </td>

                                <!-- Doctor Reports -->
                                <td class="bg-blue-100 border-blue-300 border-2">

                                    <!-- Patient has submitted a report -->
                                    <div v-if="patient.dates.length" class="flex flex-wrap items-center justify-around">
                                        <!-- use drop down for multiple reports -->
                                            <select
                                                class="bg-green-300 lg:w-2/5 px-1 py-1 rounded"
                                                id="reports"
                                                v-model="report_id"
                                            >
                                                <option disabled value=null>select one</option>
                                                <option value="New">New</option>
                                                <option v-for="r_id in patient.reports" 
                                                        v-bind:key="r_id"
                                                        v-bind:value="r_id">
                                                    {{r_id}}
                                                </option>
                                            </select>
                                            <button @click="go_to_report(report_id,patient.P_SSN)"
                                                    class="lg:w-2/5 px-1 py-1 my-2 shadow-lg transition duration-300 ease-in-out text-white bg-gray-600 hover:bg-blue-500 rounded-lg">
                                                <p v-if="report_id == 'New'">Create New</p>
                                                <p v-else>View/Edit</p>
                                            </button>
                                    </div>

                                    <!-- No reports exist -->
                                    <div v-else class="flex flex-wrap items-center justify-around">
                                        <p class="bg-red-200 lg:w-2/5 px-1 py-1 rounded">N/A</p>
                                        <button @click="go_to_report('New',patient.P_SSN)"
                                        class="lg:w-2/5 py-1 px-1 my-1px-1 py-1 my-2 shadow-lg transition duration-300 ease-in-out text-white bg-gray-600 hover:bg-green-500 rounded-lg">
                                            Create New
                                        </button>
                                    </div>

                                </td>
                            </tr>
                            <tr class="shadow-2xl">
                                <td
                                    class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl h-7"
                                    colspan="6"
                                ></td>
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
    name: "ClerkFormPage",

    data() {
        return {
            param_date: null, // Covid Screen date to send as a parameter
            report_id: null,

            logged_in: false,
            forms: []
        };
    },

    created() {
        this.get_forms();
    },

    methods: {

        go_to_report(r_id,ssn){

            // r_id is null when no option is selected from the drop down list
            if (r_id == null) {console.log("00000\n\n");return;}
            
            // Create a new covid screen
            else if (r_id == "New") {
                this.$router.push ({
                    name:'view-patient-report',
                    params: { 
                        pssn: ssn, 
                        isClerk: true 
                    }
                });
            }
            // View existing covid Screen
            else {
                this.$router.push ({
                    name:'view-patient-report',
                    params: { 
                        id: r_id,
                        pssn: ssn, 
                        isClerk: true 
                    }
                });
            }


            this.$router.push ({
                name:'view-patient-report',
                params: { 
                    id: r_id,
                    pssn: ssn, 
                    isClerk: true 
                }
            });

        },

        // Go the edit covid screen page
        go_to_covid(date, ssn) {
            
            // date is null when no option is selected from the drop down list
            if (date == null) {return;}
            
            // Create a new covid screen
            else if (date == "New") {
                this.$router.push ({
                    name:'view-patient-covid-screen',
                    params: { 
                        pssn: ssn, 
                        isClerk: true 
                    }
                });
            }
            // View existing covid Screen
            else {
                this.$router.push ({
                    name:'view-patient-covid-screen',
                    params: { 
                        date: date, 
                        pssn: ssn, 
                        isClerk: true 
                    }
                });
            }
        },

        get_forms() {
            axios
                .get("clerk/forms", {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                })
                .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;
                    this.forms = response.data.forms;

                    console.log(this.forms);
                    
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>