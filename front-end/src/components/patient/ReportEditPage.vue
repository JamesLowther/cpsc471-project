<template>
    <div id="report-edit">
        <div class="flex justify-end w-full fixed">
            <router-link to="/patient-panel/forms">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col text-4xl lg:text-5xl">
                <p v-if="create_mode" class="mt-20">
                    Create New Report
                </p>
                <p v-else class="mt-20">Edit Report {{ this.$route.params.id }}</p>
            </div>
            <div class="flex flex-col items-start mt-10 w:4/5 lg:w-2/5 mx-auto px-8">
                <div class="w-full mb-6 text-white bg-blue-500 rounded-t-2xl rounded-b-2xl border-teal border-r-0 pb-4 px-1">
                    <p class="text-xl">Chief Complaint</p>
                    <textarea
                        class="text-black border border-black mb-2 p-1 rounded-lg w-full text-xl shadow-2xl"
                        type="text"
                        name="email"
                        v-model="form.Complaint"
                    />
                    <p class="text-xl mx-auto text-red-300">
                        {{ complaint_error }}
                    </p>
                </div>
                <div v-if="!create_mode" class="w-full">
                    <div class="w-full mb-6">
                        <p class="text-xl">Assigned Doctor</p>
                        <p class="text-lg font-bold">
                            {{
                                this.form.Fname +
                                    " " +
                                    this.form.Initial +
                                    ". " +
                                    this.form.Lname
                            }}
                        </p>
                    </div>
                    <div class="w-full mb-6">
                        <p class="text-xl mb-1">Diagnosis</p>
                        <table class="table-fixed w-full mb-10">
                            <thead>
                                <th class="w-1/4 text-white bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-r-2">Illness</th>
                                <th class="w-1/4 text-white bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2">Organ System</th>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="illness in form.Illness"
                                    :key="illness.Name"
                                    class="bg-blue-100"
                                >
                                    <td class="border-blue-300 border-2">
                                        {{ illness.Name }}
                                    </td>
                                    <td class="border-blue-300 border-2">
                                        {{ illness.Organ_system }}
                                    </td>
                                </tr>
                                <tr class=" shadow-2xl">
                                    <td class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl h-6" colspan="2"></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="w-full mb-6">
                        <p class="text-xl mb-1">Medications</p>
                        <table class="table-fixed w-full mb-10">
                            <thead>
                                <th class="w-1/4 text-white bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-r-2">Name</th>
                                <th class="w-1/4 text-white bg-blue-500 border-teal border-b-2">Prescription</th>
                                <th class="w-2/4 text-white bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2">Side Effects</th>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="medication in form.Medications"
                                    :key="medication.Name"
                                    class="bg-blue-100"
                                >
                                    <td class="border-blue-300 border-2">
                                        {{ medication.Name }}
                                    </td>
                                    <td class="border-blue-300 border-2">
                                        {{ medication.Is_prescription }}
                                    </td>
                                    <td class="border-blue-300 border-2">
                                        <ul class="pl-5 list-disc text-left">
                                            <li v-for="effect in medication.Effects" :key="effect">
                                                {{ effect }}
                                            </li>
                                        </ul>
                                    </td>
                                </tr>
                                <tr class=" shadow-2xl">
                                    <td class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl h-6" colspan="3"></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                    <div class="w-full mb-6">
                        <p class="text-xl mb-1">Medical Centres</p>
                        <table class="table-fixed w-full mb-10">
                            <thead>
                                <th class="w-1/4 text-white bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-r-2">Name</th>
                                <th class="w-1/4 text-white bg-blue-500 border-teal border-b-2">Type</th>
                                <th class="w-2/4 text-white bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2">Address</th>
                            </thead>
                            <tbody>
                                <tr
                                    v-for="medical_centre in form.Medical_centres"
                                    :key="medical_centre.Name"
                                    class="bg-blue-100"
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
                                </tr>
                                <tr class=" shadow-2xl">
                                    <td class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl h-6" colspan="3"></td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
                <div v-if="create_mode" class="w-full">
                    <p class="text-xl">Medical Centre</p>
                    <select
                        class="bg-gray-300 rounded py-1 px-10 mb-3"
                        id="select"
                        v-model="medical_centre"
                    >
                        <option
                            v-for="centre in medical_centres"
                            :key="centre.Name"
                            :value="centre.Name"
                        >
                            {{ centre.Name }}
                        </option>
                    </select>
                    <p class="text-xl mx-auto text-red-600">
                        {{ medical_centre_error }}
                    </p>
                </div>
            </div>
            <button
                v-if="create_mode"
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postCreateReportForm()"
            >
                Create
            </button>
            <button
                v-else
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postReportForm()"
            >
                Save
            </button>
            <p class="text-xl text-center text-red-600">{{ post_error }}</p>
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
    props: {
        isClerk: Boolean,
        pssn: Number,
    },

    data() {
        return {
            logged_in: true,
            create_mode: true,
            medical_centres: [],
            medical_centre: "",
            form: {
                Complaint: "",
                Fname: "",
                Initial: "",
                Lname: "",
                Illnesses: [],
                Medications: [],
                Medical_centres: []
            },
            complaint_error: "",
            medical_centre_error: "",
            post_error: "",
        };
    },

    created() {
        if (typeof this.$route.params.id != "undefined") {
            this.create_mode = false;
            this.getForm();
        } else {
            this.getNewFormData();
        }
    },

    methods: {
        getForm() {
            axios
                .post(
                    "patient/forms",
                    {
                        action_type: "get_form",
                        form_type: "report",
                        report_id: this.$route.params.id,
                        p_ssn: this.pssn,
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

                    this.form = response.data.form;
                })
                .catch(e => {
                    console.log(e);
                });
        },
        postCreateReportForm() {

            if (![this.checkComplaint(), this.checkMedicalCentre()].every((x) => {return x === true})) return

            axios.post(
                "patient/forms",
                {
                    action_type: "submit_form",
                    form_type: "report",
                    new_form: 1,
                    p_ssn: this.pssn,
                    form: {
                        Complaint: this.form.Complaint,
                        medical_centre: this.medical_centre
                    }
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt")
                    }
                }
            )
            .then((response) => {
                if (response.data.successful != 1) {
                    this.post_error =
                        "There was an issue with your request.";
                } else {
                    this.post_error = "";
                    this.$router.push("/patient-panel/forms");
                }

            })
        },
        postReportForm() {
            if (!this.checkComplaint()) {
                return;
            } 

            axios.post(
                "patient/forms",
                {
                    action_type: "submit_form",
                    form_type: "report",
                    report_id: this.$route.params.id,
                    p_ssn: this.pssn,
                    form: {
                        Complaint: this.form.Complaint
                    }
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt")
                    }
                }
            ).then((response) => {
                if (response.data.successful != 1) {
                    this.post_error =
                        "There was an issue with your request.";
                } else {
                    this.post_error = "";
                }
            });
        },
        getNewFormData() {
            axios
                .post(
                    "keys",
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
        checkComplaint() {
            if (this.form.Complaint === "") {
                this.complaint_error = "Chief complaint can not be empty.";
                return false;
            }
            this.complaint_error = "";
            return true;
        },
        checkMedicalCentre() {
            if (this.medical_centre === "") {
                this.medical_centre_error = "Please choose a medical center."
                return false;
            }
            this.medical_centre_error = "";
            return true;
        }
    }
};
</script>
