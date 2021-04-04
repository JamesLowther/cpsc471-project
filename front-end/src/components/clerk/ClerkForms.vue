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
                
                <div class="mx-36">
                    <p class="text-3xl mb-4"></p>
                    <table class="table-fixed w-full h-full mb-10 border-black">
                        <thead>
                            <tr class="h-14">
                                <th class="w-1/12 border-black border-2">
                                    Patient SSN
                                </th>
                                <th class="w-1/12 border-black border-2">
                                    Patient Name
                                </th>
                                <th class="w-3/12 border-black border-2">
                                    New Application Status
                                </th>
                                <th class="w-3/12 border-black border-2">
                                    Covid Screen Date
                                </th>
                                <th class="w-3/12 border-black border-2">
                                    Report ID
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr v-for="patient in forms" v-bind:key="patient.P_SSN" class="h-10">
                                <td class="border-black border-2">
                                    {{ patient.P_SSN }}
                                </td>
                                <td class="border-black border-2">
                                    <div v-if="patient.Lname">{{ patient.Lname}}, {{ patient.Fname}}</div>
                                    <div v-else class="bg-red-200 w-1/3 inline-block m-2 rounded">N/A</div>    
                                </td>
                                
                                <!-- New Applicant Forms -->
                                <td class="border-black border-2">

                                    <!--Applicant is Approved: link to existing form-->
                                    <div v-if="patient.Is_approved==1"> 
                                        <p class="bg-green-300 w-1/3 inline-block m-2 rounded">Approved</p>
                                        <router-link :to="{name: 'approve-applicant',params: { ssn: patient.P_SSN, isClerk: true, isEdit: true }}">
                                            <div class="inline-block w-1/3 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-300 hover:bg-blue-500 rounded-lg py-1 px-1 mx-6 my-1">
                                                View/Edit
                                            </div>
                                        </router-link>
                                    </div>
                                    
                                    <!--Applicant is Pending: link to existing form-->
                                    <div v-else-if="patient.Is_approved==0"> 
                                        <p class="bg-yellow-300 w-1/3 inline-block m-2 rounded">Pending</p>
                                        <router-link :to="{name: 'approve-applicant',params: { ssn: patient.P_SSN, isClerk: true, isEdit: true }}">
                                            <div class="inline-block w-1/3 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-300 hover:bg-yellow-500 rounded-lg py-1 px-1 mx-6 my-1">
                                                View & Approve
                                            </div>
                                        </router-link>
                                    </div>

                                    <!--Applicant has not submitted: link to create new form-->
                                    <div v-else>
                                    <p class="bg-red-300 w-1/3 inline-block m-2 rounded">Not Submitted</p>
                                        <router-link :to="{name: 'approve-applicant',params: { ssn: patient.P_SSN, isClerk: true, isEdit: false }}">
                                            <div class="inline-block w-1/3 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-300 hover:bg-green-500 rounded-lg py-1 px-1 mx-6 my-1">
                                                Create New
                                            </div>
                                        </router-link>
                                    </div>

                                </td>

                                <!-- Covid Screens -->
                                <td class="border-black border-2">

                                    <!-- Patient has submitted a covid screen -->
                                    <template v-if="patient.dates.length">
                                        <!-- use drop down for multiple screens -->
                                            <select
                                                class="p-1 bg-green-300 w-1/3 inline-block m-2 rounded"
                                                id="dates"
                                                v-model="param_date"
                                            >
                                                <option disabled value="">select one</option>
                                                <option value="New">New</option>
                                                <option v-for="date in patient.dates" 
                                                        v-bind:key="date"
                                                        v-bind:value="date">
                                                    {{date}}
                                                </option>
                                            </select>
                                            <button @click="go_to_covid(param_date,patient.P_SSN)"
                                                    class="inline-block w-1/3 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-300 hover:bg-blue-500 rounded-lg py-1 px-1 mx-6 my-1">
                                                <p v-if="param_date == 'New'">Create New</p>
                                                <p v-else>View/Edit</p>
                                            </button>
                                    </template>

                                    <!-- No covid screens exist -->
                                    <template v-else>
                                        <p class="bg-red-200 w-1/3 inline-block m-2 rounded">N/A</p>
                                        <router-link :to="{name:'view-patient-covid-screen',params: { pssn:patient.P_SSN, isClerk: true }}"
                                        class="inline-block w-1/3 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-300 hover:bg-green-500 rounded-lg py-1 px-1 mx-6 my-1">
                                            Create New
                                        </router-link>
                                    </template>

                                </td>

                                <!-- Doctor Reports -->
                                <td class="border-black border-2">
                                    <div v-if="patient.Report_ID" class="bg-green-300 w-1/3 inline-block m-2 rounded">{{ patient.Report_ID}}</div>
                                    <div v-else class="bg-red-200 w-1/3 inline-block m-2 rounded">N/A</div>
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
    name: "ClerkFormPage",

    data() {
        return {
            param_date: "", // Covid Screen date to send as a parameter

            logged_in: false,
            forms: []
        };
    },

    created() {
        this.get_forms();
    },

    methods: {

        // Go the edit covid screen page
        go_to_covid(date, ssn) {
            
            // date is "" when no option is selected from the drop down list
            if (date == "") {return;}
            
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