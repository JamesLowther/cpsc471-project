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
        <div v-else-if="user_type == 'clerk'" class="flex justify-end w-full fixed">
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
        <div v-if="logged_in && (entity_type == 'medication')">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-24">Medications</p>
                <div class="w-1/2">
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="width: 75% border-black border-2">
                                    Search Medications: 
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg"
                                        type="text"
                                        name="MedicationName"
                                        v-model="form.medicationName"
                                        v-on:keyup="searchMedications()"
                                    />
                                </th>
                                <th class="width: 0%">
                                </th>
                                <th class="width: 25% border-black border-2">
                                    <p class="text-3xl mb-4">Modify</p>
                                </th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr>
                                <td class="border-black border-2">
                                    <b>Name</b>
                                </td>
                                <td class="border-black border-2">
                                   <b>Side Effects</b>
                                </td>
                                <td class="border-black border-2">
                                </td>
                            </tr>
                            <tr
                                v-for="(medication, i) in medicationList"
                                :key="`${i}-${medication}`"
                            >
                                <td class="border-black border-2">
                                    {{ medication.Name }}
                                </td>
                                <td class="border-black border-2">
                                    {{ medication.Effect}}
                                </td>
                                <td class="border-black border-2">
                                    <router-link
                                        :to="{
                                            name: 'view-reports',
                                            params: { id: medicationList.Name },
                                        }"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            Edit
                                        </div>
                                    </router-link>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                </div>
            </div>
        </div>
        <!-- STARTING WITH ILLNESSES DIV FORMS -->
        <div v-else-if="logged_in && (entity_type == 'illness')">
        </div>
        <!-- STARTING WITH SYMPTOMS DIV FORMS -->
        <div v-else-if="logged_in && (entity_type == 'symptoms')">
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
            user_type: "doctor",
            entity_type: "medication",
            medicationList: [],
            form: {
                theMedicationName: "" 
            }
        };
    },

    created() {
        this.searchMedications();
    },

    methods: {
        searchMedications() {
            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: "medication",
                    method: "query",
                    query_string: this.form.medicationName
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
                    this.medicationList = response.data.results;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>