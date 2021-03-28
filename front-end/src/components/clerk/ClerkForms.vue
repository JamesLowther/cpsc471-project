<template>
    <div id="forms">
        <div class="flex justify-end w-full fixed">
            <router-link to="/clerk-panel">
                <div class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                    Back
                </div>
            </router-link>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-24">Clerk Workstation</p>
                
                <div class="mx-36">
                    <p class="text-3xl mb-4"></p>
                    <table class="table-fixed w-full h-full mb-10 border-black">
                        <thead>
                            <tr class="h-14">
                                <th class="w-1/6 border-black border-2">
                                    Patient SSN
                                </th>
                                <th class="w-1/6 border-black border-2">
                                    Patient Name
                                </th>
                                <th class="w-2/6 border-black border-2">
                                    New Application Status
                                </th>
                                <th class="w-2/6 border-black border-2">
                                    Covid Screen Date
                                </th>
                                <th class="w-2/6 border-black border-2">
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
                                    <div v-else class="bg-red-300 w-1/3 inline-block m-2 rounded">N/A</div>    
                                </td>
                                
                                <td class="border-black border-2">
                                    <!--Applicant is Approved: link to existing form-->
                                    <div v-if="patient.Is_approved==1"> 
                                        <p class="bg-green-300 w-1/3 inline-block m-2 rounded">Approved</p>
                                        <router-link :to="{name: 'edit-new-applicant',params: { ssn: patient.P_SSN, isClerk: true }}">
                                            <div class="inline-block w-1/3 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-300 hover:bg-blue-500 rounded-lg py-1 px-1 mx-6 my-1">
                                                View/Edit
                                            </div>
                                        </router-link>
                                    </div>
                                    
                                    <!--Applicant is Pending: link to existing form-->
                                    <div v-else-if="patient.Is_approved==0"> 
                                        <p class="bg-yellow-300 w-1/3 inline-block m-2 rounded">Pending</p>
                                        <router-link :to="{name: 'edit-new-applicant',params: { ssn: patient.P_SSN, isClerk: true }}">
                                            <div class="inline-block w-1/3 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-300 hover:bg-yellow-500 rounded-lg py-1 px-1 mx-6 my-1">
                                                View & Approve
                                            </div>
                                        </router-link>
                                    </div>

                                    <!--Applicant has not submitted: link to create new form-->
                                    <div v-else>
                                    <p class="bg-red-300 w-1/3 inline-block m-2 rounded">Not Submitted</p>
                                        <router-link :to="{name: 'edit-new-applicant',params: { ssn: patient.P_SSN, isClerk: true }}">
                                            <div class="inline-block w-1/3 my-2 shadow-lg transition duration-300 ease-in-out bg-gray-300 hover:bg-green-500 rounded-lg py-1 px-1 mx-6 my-1">
                                                Create New
                                            </div>
                                        </router-link>
                                    </div>
                                    
                                </td>
                                <td class="border-black border-2">
                                    <div v-if="patient.Date">{{ patient.Date}}</div>
                                    <div v-else>Not Submitted</div>
                                    
                                </td>
                                <td class="border-black border-2">
                                    {{ patient.Report_ID}}
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
            forms: []
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
                    this.forms = response.data.forms;
                    
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>