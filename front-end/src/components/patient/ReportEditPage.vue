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
            <div class="flex flex-col">
                <p v-if="create_mode" class="text-5xl mt-20">
                    Create New Report
                </p>
                <p v-else class="text-5xl mt-20">Edit Report</p>
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
                <div v-if="!create_mode" class="w-full">
                    <p class="text-xl">Assigned Doctor</p>
                    <p class="text-lg font-bold">{{ this.form.Fname + " " + this.form.Initial + ". " + this.form.Lname }}</p>
                </div>
                <div v-if="create_mode" class="w-full">
                    <p class="text-xl">Medical Center</p>
                    <select class="bg-gray-300 rounded py-1 px-10" id="select" v-model="medical_centre">
                        <option
                            v-for="centre in medical_centres"
                            :key="centre.Name"
                            :value="centre.Name"
                        >
                            {{ centre.Name }}
                        </option>
                    </select>
                </div>
            </div>
            <button
                v-if="create_mode"
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postCreateReportForm()"
            >
                Save
            </button>
            <button
                v-else
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postReportForm()"
            >
                Save
            </button>
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
            create_mode: true,
            medical_centres: [],
            medical_centre: "",
            form: {
                Complaint: "",
                Fname: "",
                Initial: "",
                Lname: "",
            },
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
                    `http://localhost:5000/patient/forms`,
                    {
                        action_type: "get_form",
                        form_type: "report",
                        report_id: this.$route.params.id,
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

                    this.form = response.data.form;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        postCreateReportForm() {
            axios.post(
                `http://localhost:5000/patient/forms`,
                {
                    action_type: "submit_form",
                    form_type: "report",
                    new_form: 1,
                    form: {
                        Complaint: this.form.Complaint,
                        medical_centre: this.medical_centre
                    },
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            );
        },
        postReportForm() {
            axios.post(
                `http://localhost:5000/patient/forms`,
                {
                    action_type: "submit_form",
                    form_type: "report",
                    report_id: this.$route.params.id,
                    form: {
                        Complaint: this.form.Complaint
                    },
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
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
                                "Bearer " + localStorage.getItem("jwt"),
                        },
                    }
                )
                .then((response) => {
                    this.medical_centres = response.data.result;
                })
                .catch((e) => console.log(e));
        },
    },
};
</script>