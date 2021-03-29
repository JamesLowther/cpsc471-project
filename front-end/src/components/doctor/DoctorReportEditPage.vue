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
                <p class="text-5xl mt-20 bg-blue-300"><b>Edit Report</b>
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
            <div class="flex flex-col items-start mt-10 w-1/3 mx-auto">
                <div class="w-full">
                    <p class="text-xl">Chief Complaint</p>
                    <textarea
                        class="border border-black mb-6 p-1 rounded-lg w-full text-xl"
                        type="text"
                        name="email"
                        v-model="form.Complaint"
                    />
                </div>
                <button
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                    @click="updateComplaint()"
                >
                    Save
                </button>
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
                        <p class="text-xl mb-1">Diagnosis</p>
                        <!-- <table class="table-fixed w-full mb-10">
                            <thead>
                                <th class="w-1/4 border-black border-2">Illness</th>
                                <th class="w-1/4 border-black border-2">Organ System</th>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="illness in form.Diagnosis"
                                    :key="illness.Name"
                                >
                                    <td class="border-black border-2">
                                        {{ illness.Name }}
                                    </td>
                                    <td class="border-black border-2">
                                        {{ illness.Organ_system }}
                                    </td>
                                </tr>
                            </tbody>
                        </table> -->
                        <table class="table-fixed w-full mb-3">
                            <thead>
                                <tr>
                                    <th class="text-lg w-1/3 border-black border-2 bg-gray-300">
                                        Current diagnosis:
                                    </th>
                                    <th class="text-lg w-1/3 border-black border-2 bg-gray-300">
                                        Organ System:
                                    </th>
                                    <th class="w-1/3 border-black border-2 bg-gray-300"></th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="illness in form.Diagnosis"
                                    :key="illness.Name"
                                >
                                    <td class="border-black border-2">
                                        {{ illness.Name }}
                                    </td>
                                    <td class="border-black border-2">
                                        {{ illness.Organ_system }}
                                    </td>
                                    <td class="border-black border-2">
                                        <button
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 px-8 m-3"
                                            v-on:click="
                                                removeIllness(illness.Name)
                                            "
                                        >
                                            Remove
                                        </button>
                                    </td>
                                </tr>
                                <tr>
                                    <td class="border-black border-2 bg-gray-300">
                                        <b>Search Illnesses:</b>
                                    </td>
                                    <td class="border-black border-2 bg-gray-300" colspan="2">
                                        <input
                                            class="border border-black mb-2 mt-2 p-1 rounded-lg w-4/5"
                                            type="text"
                                            name="illness-search"
                                            placeholder="Search"
                                            v-model="illness_query"
                                            v-on:keyup="queryIllness()"
                                        />
                                    </td>
                                    <td class="border-black border-2 bg-gray-300">
                                    </td>
                                </tr>
                                <tr
                                    v-for="illness in illness_results"
                                    :key="illness.Name"
                                >
                                    <td class="border-black border-2">
                                        {{ illness.Name }}
                                    </td>
                                    <td class="border-black border-2">
                                        {{ illness.Organ_system }}
                                    </td>
                                    <td class="border-black border-2">
                                        <button
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-2 w-1/4 m-3"
                                            v-on:click="addNewIllness(illness.Name, illness.Organ_system)"
                                        >
                                            Add
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <p class="text-xl mx-auto text-red-600">
                            {{ diagnosed_illnesses_error }}
                        </p>
                    </div>
                    <div class="w-full mb-6">
                        <p class="text-xl mb-1">Medications</p>
                        <!-- <router-link
                                        :to="{
                                            name: 'add-med-to-reports',
                                            params: { id: report.ReportID },
                                        }"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            Add
                                        </div>
                                    </router-link> -->
                        <table class="table-fixed w-full mb-10">
                            <thead>
                                <th class="w-2/4 border-black border-2 bg-gray-300">Name</th>
                                <th class="w-1/4 border-black border-2 bg-gray-300">Prescription</th>
                                <th class="w-2/4 border-black border-2 bg-gray-300">Side Effects</th>
                                <th class="w-2/4 border-black border-2 bg-gray-300"></th>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="medication in form.Medications"
                                    :key="medication.Name"
                                >
                                    <td class="border-black border-2">
                                        {{ medication.Name }}
                                    </td>
                                    <td v-if="medication.Is_prescription == 1" class="border-black border-2 bg-green-300">
                                        YES
                                    </td>
                                    <td v-else class="border-black border-2 bg-red-300">
                                        NO
                                    </td>
                                    <td class="border-black border-2">
                                        <ul class="list-disc">
                                            <li v-for="effect in medication.Effects" :key="effect">
                                                {{ effect }}
                                            </li>
                                        </ul>
                                    </td>
                                    <td class="border-black border-2">
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
                                <tr>
                                    <td class="border-black border-2 bg-gray-300">
                                        <b>Search Medications:</b>
                                    </td>
                                    <td class="border-black border-2 bg-gray-300" colspan="3">
                                        <input
                                            class="border border-black mb-2 mt-2 p-1 rounded-lg w-4/5"
                                            type="text"
                                            name="medication-search"
                                            placeholder="Search"
                                            v-model="medication_query"
                                            v-on:keyup="queryMedications()"
                                        />
                                    </td>
                                    <td class="border-black border-2 bg-gray-300">
                                    </td>
                                </tr>
                                <tr
                                    v-for="medication in medication_results"
                                    :key="medication.Name"
                                >
                                    <td class="border-black border-2">
                                        {{ medication.Name }}
                                    </td>
                                    <td v-if="medication.Is_prescription == 1" class="border-black border-2 bg-green-300">
                                        YES
                                    </td>
                                    <td v-else class="border-black border-2 bg-red-300">
                                        NO
                                    </td>
                                        <td class="border-black border-2">
                                            <ul class="list-disc">
                                                <li v-for="effect in medication.Effect" :key="effect">
                                                    {{ effect }}
                                                </li>
                                            </ul>
                                        </td>
                                    <td class="border-black border-2">
                                        <button
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-2 w-1/4 m-3"
                                            v-on:click="addNewMedication(medication.Name, medication.Is_prescription, medication.Effect)"
                                        >
                                            Add
                                        </button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                        <p class="text-xl mx-auto text-red-600">
                            {{ add_medication_error }}
                        </p>
                    </div>
                    <div class="w-full mb-6">
                        <p class="text-xl mb-1">Medical Centres</p>
                        <table class="table-fixed w-full mb-10">
                            <thead>
                                <th class="w-1/4 border-black border-2 bg-gray-300">Name</th>
                                <th class="w-1/4 border-black border-2 bg-gray-300">Type</th>
                                <th class="w-2/4 border-black border-2 bg-gray-300">Address</th>
                                <th class="w-2/4 border-black border-2 bg-gray-300"></th>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="medical_centre in form.Medical_centres"
                                    :key="medical_centre.Name"
                                >
                                    <td class="border-black border-2">
                                        {{ medical_centre.Name }}
                                    </td>
                                    <td class="border-black border-2">
                                        {{ medical_centre.Type }}
                                    </td>
                                    <td class="border-black border-2">
                                        {{ medical_centre.Address }}
                                    </td>
                                    <td class="border-black border-2">
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
                                    <td class="border-black border-2 bg-gray-300" colspan="2">
                                        <b>Search Medical Centers:</b>
                                    </td>
                                    <td class="border-black border-2 bg-gray-300" colspan="2">
                                        <input
                                            class="border border-black mb-2 mt-2 p-1 rounded-lg w-4/5"
                                            type="text"
                                            name="med-center-search"
                                            placeholder="Search"
                                            v-model="med_center_query"
                                            v-on:keyup="queryMedCenters()"
                                        />
                                    </td>
                                </tr>
                                <tr
                                    v-for="(med_center, i) in Medical_Centers_results"
                                    :key="`${i}-${med_center}`"
                                >
                                    <td class="border-black border-2">
                                        {{ med_center.Name }}
                                    </td>
                                    <td class="border-black border-2">
                                        {{ med_center.Type }}
                                    </td>
                                    <td class="border-black border-2">
                                        {{ med_center.Address }}
                                    </td>
                                    <td class="border-black border-2">
                                        <button
                                            class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-2 w-1/4 m-3"
                                            v-on:click="addMedCenter(med_center.Name, med_center.Type, med_center.Address)"
                                        >
                                            Add
                                        </button>
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
                Complaint: "",
                Doc_Fname: "",
                Doc_Initial: "",
                Doc_Lname: "",
                Illnesses: [],
                Medications: [],
                Medical_centres: [],
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
                        Effect: Effect,
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
