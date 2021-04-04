<template>
    <div id="forms">
        <div class="flex justify-end w-full fixed">
            <router-link to="/clerk-panel/forms">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-24">Register New Patients</p>
                
                <div class="w-1/2">
                    <p class="text-3xl mb-4">Unregistered Patients</p>
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="w-3/4 border-black border-2">
                                    Patient SSN
                                </th>
                                <th class="w-1/4 border-black border-2">
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="form in existingPatients"
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
                                            to: create form
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
    name: "ClerkNewAppForm",

    data() {
        return {
            logged_in: false,
            existingPatients: [],
        };
    },
    created() {
        this.getExistingPatients();
    },

    methods: {
        getExistingPatients() {
            axios.post(
                "clerk/forms", 
                {
                    form_type: "new_applicant_form",
                    action_type: "get_form"
                },
                {
                    headers: 
                    {
                        Authorization: "Bearer " + localStorage.getItem("jwt")
                    }
                }
            )
            .then((response) => {
                if (response.data.logged_in != "1") return;

                this.logged_in = true;
                this.existingPatients = response.data.existingPatients;

            })
            .catch((e) => {
                console.log(e);
            });
        },
    },
};
</script>