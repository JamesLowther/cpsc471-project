<template>
    <div id="Doctor_reports">
        <div class="flex justify-end w-full fixed">
            <router-link to="/doctor-panel/forms">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col">
                <p class="text-3xl md:text-4xl lg:text-5xl mt-20 bg-blue-300">Doctor Panel</p>
                <p class="text-2xl md:text-3xl lg:text-4xl mt-4 bg-blue-300"><b>Edit Report</b>
                <br />Patient SSN: {{ p_ssn }}
                <br />Patient Name: {{
                                        this.form.Fname +
                                        " " +
                                        this.form.Initial +
                                        ". " +
                                        this.form.Lname
                                    }}
                                </p>
            </div>
            <div class="flex flex-col items-center justify-center w-full p-5">
                
                <p class="text-xl"><b><i>COVID SCREEN STATUS:</i></b></p>
                    <svg v-if="this.form.Has_passed" class="w-20 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="green">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <svg v-else class="w-20 mx-auto" xmlns="http://www.w3.org/2000/svg" fill="none" viewBox="0 0 24 24" stroke="red">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>

            </div>
                <table class="w-full ml-auto md: mr-auto md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg">
                    <thead>
                        <tr>
                            <th class="text-lg w-full text-white bg-blue-500 rounded-t-2xl border-teal border-r-0"> 
                                Chief Complaint
                                <textarea
                                    class="border border-black text-black mb-2 p-1 rounded-lg w-full text-xl h-40 shadow-2xl"
                                    type="text"
                                    name="email"
                                    v-model="form.Complaint"
                                />
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr>
                            <td class="border-blue-300 border-0 bg-blue-500 rounded-b-2xl pb-0">
                                <button
                                    class="text-white mt-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                                    @click="updateComplaint()"
                                >
                                    Save
                                </button>
                            </td>
                        </tr>
                    </tbody>
                </table>
            <div class="w-full mb-6 mt-12">
                <table class="w-full ml-auto md: mr-auto md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg">
                    <thead>
                        <tr>
                            <th class="text-lg text-white w-full bg-blue-500 rounded-t-2xl border-teal border-r-0" colspan="3">
                                Patients Medical History
                            </th>
                            <th />
                            <th />
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="bg-blue-300">
                            <td class="border-blue-300 border-0 border-l-0">
                                <b>Age:</b> {{ this.form.Age }}
                            </td>
                            <td class="border-blue-300 border-0">
                                <b>Gender:</b> {{ this.form.Gender }}
                            </td>
                            <td class="border-blue-300 border-2 border-l-0">
                                <b>Sex:</b> {{ this.form.Sex }}
                            </td>
                        </tr>
                        <tr>
                            <td class="bg-blue-500 border-blue-300 border-2 border-r-0 border-l-0 text-white">
                                <b>Allergies:</b>
                            </td>
                            <td class="border-blue-300 border-2 border-l-0 bg-blue-100" colspan="2">
                                <ul class="list-disc text-left pl-5">
                                    <li v-for="allergy in form.allergies" :key="allergy.Allergy">
                                        {{ allergy.Allergy }}
                                    </li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="bg-blue-500 border-blue-300 border-2 border-r-0 border-l-0 text-white">
                                <b>Immunizations:</b>
                            </td>
                            <td class="border-blue-300 border-2 border-l-0 bg-blue-100" colspan="2">
                                <ul class="list-disc text-left pl-5">
                                    <li v-for="immunization in form.immunizations" :key="immunization.Immunization">
                                        {{ immunization.Immunization }}
                                    </li>
                                </ul>
                            </td>
                        </tr>
                        <tr>
                            <td class="bg-blue-500 border-blue-300  border-b-0 border-r-0 border-l-0 border-2 text-white">
                                <b>Past Illnesses:</b><br />[Age of Onset]
                            </td>
                            <td class="border-blue-300 border-2 border-b-0 border-l-0 bg-blue-100" colspan="2">
                                <ul class="list-disc text-left pl-5">
                                    <li v-for="past_illness in form.past_illnesses" :key="past_illness.Illness_name">
                                        <b>{{ past_illness.Illness_name }}</b> [{{ past_illness.Age_of_onset }}]
                                    </li>
                                </ul>

                            </td>
                        </tr>
                        <tr class=" shadow-2xl">
                            <td class="border-teal-500 border-0 text-white bg-blue-300 rounded-b-2xl" colspan="4">
                                .
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>
            <div class="w-full">
                <div class="w-full mb-6">
                    <p class="text-xl">Assigned Doctor</p>
                    <p class="text-lg font-bold">
                        {{
                                this.form.Doc_Fname +
                                " " +
                                this.form.Doc_Initial +
                                ". " +
                                this.form.Doc_Lname
                        }}
                    </p>
                </div>
                <div class="w-full mb-6">
                    <table class="w-full ml-auto md: mr-auto md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg">
                        <thead>
                            <tr>
                                <th class="text-lg text-white w-1/2 bg-blue-500 rounded-tl-2xl border-teal border-r-2">
                                    Current diagnosis:
                                </th>
                                <th class="text-lg text-white w-1/2 bg-blue-500 ">
                                    Organ System:
                                </th>
                                <th class="text-lg text-white bg-blue-500 rounded-tr-2xl border-teal border-l-2 px-8"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr class="bg-blue-100"
                                v-for="illness in form.Diagnosis"
                                :key="illness.Name"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ illness.Name }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    {{ illness.Organ_system }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-1 px-8 m-2"
                                        v-on:click="
                                            removeIllness(illness.Name)
                                        "
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr class="border-t-2">
                                <td class="border-teal-500 border-0 border-b-2 bg-blue-400 " colspan="1">
                                    <input
                                        class="border border-blue-700 mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="illness-search"
                                        placeholder="Search Illnesses"
                                        v-model="illness_query"
                                        v-on:keyup="queryIllness()"
                                    />
                                </td>
                                <td class="border-teal-500 border-0 border-b-2 text-white bg-blue-400 " colspan="2" />
                            </tr>
                            <tr class="bg-blue-100"
                                v-for="illness in illness_results"
                                :key="illness.Name"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ illness.Name }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    {{ illness.Organ_system }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-1 px-5 m-2"
                                        v-on:click="addNewIllness(illness.Name, illness.Organ_system)"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                            <tr class=" shadow-2xl">
                                <td class="border-teal-500 border-0 text-white bg-blue-400 rounded-b-2xl" colspan="3">
                                    .
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ diagnosed_illnesses_error }}
                    </p>
                </div>
                <br />
                <div class="w-full mb-6">
                <table class="w-full ml-auto md: mr-auto md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg">
                        <thead>
                            <th class="text-lg text-white w-full bg-blue-500 rounded-tl-2xl border-teal border-r-2 p-2 pb-0">Treatment</th>
                            <th class="text-lg text-white bg-blue-500 p-2 pb-0 border-r-2">Prescription</th>
                            <th class="text-lg text-white bg-blue-500 p-2 pb-0">Side_Effects</th>
                            <th class="text-lg text-white bg-blue-500 rounded-tr-2xl border-teal border-l-2 px-8"></th>
                        </thead>
                        <tbody>
                            <tr class="bg-blue-100"
                                v-for="medication in form.Medications"
                                :key="medication.Name"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ medication.Name }}
                                </td>
                                <td v-if="medication.Is_prescription == 1" class="border-teal-500 border-2 bg-green-300">
                                    YES
                                </td>
                                <td v-else class="border-teal-300 border-2 bg-red-300">
                                    NO
                                </td>
                                <td class="border-blue-300 border-2">
                                    <ul class="list-disc text-left pl-5">
                                        <li v-for="effect in medication.Effects" :key="effect">
                                            {{ effect }}
                                        </li>
                                    </ul>
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 px-8 m-3"
                                        v-on:click="
                                            removeMedication(medication.Name)
                                        "
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr class="border-t-2">
                                <td class="border-teal-500 border-b-2 bg-blue-400" colspan="1">
                                    <input
                                        class="border border-blue-700 mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="medication-search"
                                        placeholder="Search Medications"
                                        v-model="medication_query"
                                        v-on:keyup="queryMedications()"
                                    />
                                </td>
                                <td class="border-teal-500 border-b-2 bg-blue-400" colspan="3">
                                </td>
                            </tr>
                            <tr class="bg-blue-100"
                                v-for="medication in medication_results"
                                :key="medication.Name"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ medication.Name }}
                                </td>
                                <td v-if="medication.Is_prescription == 1" class="border-teal-500 border-2 bg-green-300">
                                    YES
                                </td>
                                <td v-else class="border-teal-500 border-2 bg-red-300">
                                    NO
                                </td>
                                    <td class="border-blue-300 border-2">
                                        <ul class="list-disc text-left pl-5">
                                            <li v-for="effect in medication.Effects" :key="effect">
                                                {{ effect }}
                                            </li>
                                        </ul>
                                    </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-1 px-5 m-2"
                                        v-on:click="addNewMedication(medication.Name, medication.Is_prescription, medication.Effects)"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                            <tr class=" shadow-2xl">
                                <td class="border-teal-500 border-0 text-white bg-blue-400 rounded-b-2xl" colspan="4">
                                    .
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ add_medication_error }}
                    </p>
                </div>
                <br />
                <div class="w-full mb-6">
                    <table class="w-full ml-auto md: mr-auto md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg">
                        <thead>
                            <th class="text-lg text-white w-1/2 bg-blue-500 rounded-tl-2xl border-teal border-r-2">Med. Center Name</th>
                            <th class="text-lg text-white bg-blue-500 p-2 pb-0 border-teal border-r-2">Type</th>
                            <th class="text-lg text-white w-1/2 bg-blue-500 p-2 pb-0">Address</th>
                            <th class="text-lg text-white bg-blue-500 rounded-tr-2xl border-teal border-l-2 px-8"></th>
                        </thead>
                        <tbody>
                            <tr class="bg-blue-100"
                                v-for="medical_centre in form.Medical_centres"
                                :key="medical_centre.Name"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ medical_centre.Name }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    {{ medical_centre.Type }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    {{ medical_centre.Address }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 px-8 m-3"
                                        v-on:click="
                                            removeMedCenter(medical_centre.Name)
                                        "
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr>
                                <td class="border-teal-500 border-2 border-r-0 border-l-0 bg-blue-400" colspan="2">
                                    <input
                                        class="border border-blue-700 mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="med-center-search"
                                        placeholder="Search Medical Centers"
                                        v-model="med_center_query"
                                        v-on:keyup="queryMedCenters()"
                                    />
                                </td>
                                <td class="border-teal-500 border-2 bg-blue-400 border-r-0 border-l-0 " colspan="2">
                                </td>
                            </tr>
                            <tr class="bg-blue-100"
                                v-for="(med_center, i) in Medical_Centers_results"
                                :key="`${i}-${med_center}`"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ med_center.Name }}
                                </td>
                                <td class="border-blue-300 border-2 px-2">
                                    {{ med_center.Type }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    {{ med_center.Address }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-1 px-5 m-2"
                                        v-on:click="addMedCenter(med_center.Name, med_center.Type, med_center.Address)"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                            <tr class=" shadow-2xl">
                                <td class="border-teal-500 border-0 text-white bg-blue-400 rounded-b-2xl" colspan="4">
                                    .
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ medCenter_error }}
                    </p>
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
    name: "FormEditPage",

    data() {
        return {
            logged_in: true,
            p_ssn: "",
            id: "",
            form: {
                Fname: "",
                Initial: "",
                Lname: "",
                Gender: "",
                Sex: "",
                Age: "",
                Complaint: "",
                Doc_Fname: "",
                Doc_Initial: "",
                Doc_Lname: "",
                Illnesses: [],
                Medications: [],
                Medical_centres: [],
                TPAL: "",
                past_illnesses: [],
                allergies: [],
                immunizations: [],
                Has_passed: "",
            },
            illness_query: "",
            illness_results: [],
            medication_query: "",
            medication_results: [],
            med_center_query: "",
            Medical_Centers_results: [],
            diagnosed_illnesses_error: "",
            medCenter_error: "",
            add_medication_error: "",
        };
    },

    created() {
        if (typeof this.$route.params.p_ssn != "undefined") {
            this.p_ssn = this.$route.params.p_ssn;
            this.getForm();
        } else {
            this.getNewFormData();
        }
    },

    methods: {
        getForm() {
            axios
                .post(
                    `http://localhost:5000/doctor/forms`,
                    {
                        action_type: "get_form",
                        form_type: "report",
                        p_ssn: this.$route.params.p_ssn,
                        id: this.$route.params.id,
                        form: this.form,
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                )
                .then(response => {
                    if (response.data.logged_in != "1") return;

                    this.id = this.$route.params.id;
                    this.form = response.data.form;
                })
                .catch(e => {
                    console.log(e);
                });
        },
        updateComplaint() {
            axios.post(
                `http://localhost:5000/doctor/forms`,
                {
                    action_type: "update_complaint",
                    form_type: "report",
                    p_ssn: this.$route.params.p_ssn,
                    id: this.$route.params.id,
                    complaint: this.form.Complaint,
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt")
                    }
                }
            );
        },
        getNewFormData() {
            axios
                .post(
                    `http://localhost:5000/keys`,
                    { entity: "medical_centre" },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                )
                .then(response => {
                    this.medical_centres = response.data.result;
                })
                .catch(e => console.log(e));
        },
        queryIllness() {
            axios
                .post(
                    `http://localhost:5000/entities/forms`,
                    {
                        entity_type: "illness",
                        method: "query",
                        query_string: this.illness_query,
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt"),
                        },
                    }
                )
                .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;
                    this.illness_results = response.data.results;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        addNewIllness(illness, Organ_system) {
            // Check for a duplicate illness insert and abort if there is one
            for (let i = 0; i < this.form.Diagnosis.length; i++) {
                if (this.form.Diagnosis[i].Name == illness) {
                    this.diagnosed_illnesses_error =
                        "You have already added that illness to the Diagnosis.";
                    return;
                }
            }

            axios.post(
                `http://localhost:5000/doctor/forms`,
                {
                    action_type: "add_illness",
                    form_type: "report",
                    illness_to_add: illness,
                    id: this.id,
                    p_ssn: this.p_ssn,
                },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                    )
                    .then(response => {
                        if (response.data.logged_in != "1") return;


                    // Update the html list of Diagnosed illnesses
                    this.diagnosed_illnesses_error = "";

                    this.form.Diagnosis.push({
                        Name: illness,
                        Organ_system: Organ_system,
                    });


                    })
                    .catch(e => {
                        console.log(e);
                    }
            );
        },
        removeIllness(illness) {

            axios.post(
                `http://localhost:5000/doctor/forms`,
                {
                    action_type: "remove_illness",
                    form_type: "report",
                    illness_to_remove: illness,
                    id: this.id,
                    p_ssn: this.p_ssn,
                },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                    )
                    .then(response => {
                        if (response.data.logged_in != "1") return;

                    //If successful then update the html form to reflect the removal
                    let temp_array = this.form.Diagnosis;
                    this.form.Diagnosis = [];

                    for (let i = 0; i < temp_array.length; i++) {
                        if (temp_array[i].Name != illness) {
                            this.form.Diagnosis.push(temp_array[i]);
                        }
                    }

                    })
                    .catch(e => {
                        console.log(e);
                    }
            );
        },
        queryMedications() {
            axios
                .post(
                    `http://localhost:5000/entities/forms`,
                    {
                        entity_type: "medication",
                        method: "query",
                        query_string: this.medication_query,
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt"),
                        },
                    }
                )
                .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;
                    this.medication_results = response.data.results;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        addNewMedication(medication, Is_prescription, Effect) {
            // Check for a duplicate illness insert and abort if there is one
            for (let i = 0; i < this.form.Medications.length; i++) {
                if (this.form.Medications[i].Name == medication) {
                    this.add_medication_error =
                        "You have already added that medication to the Patients Report.";
                    return;
                }
            }

            axios.post(
                `http://localhost:5000/doctor/forms`,
                {
                    action_type: "add_medication",
                    form_type: "report",
                    medication_to_add: medication,
                    id: this.id,
                    p_ssn: this.p_ssn,
                },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                    )
                    .then(response => {
                        if (response.data.logged_in != "1") return;


                    // Update the html list of Diagnosed illnesses
                    this.add_medication_error = "";

                    this.form.Medications.push({
                        Name: medication,
                        Is_prescription: Is_prescription,
                        Effects: Effect,
                    });


                    })
                    .catch(e => {
                        console.log(e);
                    }
            );
        },
        removeMedication(medication) {

            axios.post(
                `http://localhost:5000/doctor/forms`,
                {
                    action_type: "remove_medication",
                    form_type: "report",
                    medication_to_remove: medication,
                    id: this.id,
                    p_ssn: this.p_ssn,
                },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                    )
                    .then(response => {
                        if (response.data.logged_in != "1") return;

                    })
                    .catch(e => {
                        console.log(e);
                    }
            );


            let temp_array = this.form.Medications;
            this.form.Medications = [];

            for (let i = 0; i < temp_array.length; i++) {
                if (temp_array[i].Name != medication) {
                    this.form.Medications.push(temp_array[i]);
                }
            }
        },
        queryMedCenters() {
            axios
                .post(
                    `http://localhost:5000/keys`,
                    {
                        entity: "medical_centre",
                        query_string: this.med_center_query,
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt"),
                        },
                    }
                )
                .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;
                    this.Medical_Centers_results = response.data.result;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        addMedCenter(MedCenter_Name, type, address) {
            // Check for a duplicate illness insert and abort if there is one
            for (let i = 0; i < this.form.Medical_centres.length; i++) {
                if (this.form.Medical_centres[i].Name == MedCenter_Name) {
                    this.medCenter_error =
                        "You have already added that Medical Center to the report.";
                    return;
                }
            }

            axios.post(
                `http://localhost:5000/doctor/forms`,
                {
                    action_type: "add_medCenter",
                    form_type: "report",
                    medCenter_to_add: MedCenter_Name,
                    id: this.id,
                    p_ssn: this.p_ssn,
                },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                    )
                    .then(response => {
                        if (response.data.logged_in != "1") return;


                    // Update the html list of Diagnosed illnesses
                    this.medCenter_error = "";

                    this.form.Medical_centres.push({
                        Name: MedCenter_Name,
                        Type: type,
                        Address: address,
                    });


                    })
                    .catch(e => {
                        console.log(e);
                    }
            );
        },
        removeMedCenter(MedCenter_Name) {

            axios.post(
                `http://localhost:5000/doctor/forms`,
                {
                    action_type: "remove_medCenter",
                    form_type: "report",
                    medCenter_to_remove: MedCenter_Name,
                    id: this.id,
                    p_ssn: this.p_ssn,
                },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                    )
                    .then(response => {
                        if (response.data.logged_in != "1") return;

                    //If successful then update the html form to reflect the removal
                    let temp_array = this.form.Medical_centres;
                    this.form.Medical_centres = [];

                    for (let i = 0; i < temp_array.length; i++) {
                        if (temp_array[i].Name != MedCenter_Name) {
                            this.form.Medical_centres.push(temp_array[i]);
                        }
                    }

                    })
                    .catch(e => {
                        console.log(e);
                    }
            );
        },
    }
};
</script>
