<template>
    <div id="form-edit">
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
                    Create Medical History Form
                </p>
                <p v-else class="text-5xl mt-20">Edit Medical History Form</p>
            </div>
            <div class="flex flex-col items-start mt-10 w-1/3 mx-auto">
                <div>
                    <p class="text-xl">Email</p>
                    <input
                        class="border border-black mb-6 p-1 rounded-lg"
                        type="text"
                        name="email"
                        v-model="form.Email"
                    />
                </div>
                <div class="flex flex-row">
                    <div class="mr-4">
                        <p class="text-xl">First Name</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="fname"
                            v-model="form.Fname"
                        />
                    </div>
                    <div class="mr-4">
                        <p class="text-xl">Initial</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="initial"
                            v-model="form.Initial"
                        />
                    </div>
                    <div>
                        <p class="text-xl">Last Name</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="lname"
                            v-model="form.Lname"
                        />
                    </div>
                </div>
                <div class="flex flex-row">
                    <div class="mr-4">
                        <p class="text-xl">Gender</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="gender"
                            v-model="form.Gender"
                        />
                    </div>
                    <div>
                        <p class="text-xl">Sex</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="sex"
                            v-model="form.Sex"
                        />
                    </div>
                </div>
                <div>
                    <p class="text-xl">Date of Birth</p>
                    <input
                        class="border border-black mb-6 p-1 rounded-lg"
                        type="text"
                        name="dob"
                        v-model="form.DoB"
                    />
                </div>
                <div>
                    <p class="text-xl">Phone</p>
                    <input
                        class="border border-black mb-6 p-1 rounded-lg"
                        type="text"
                        name="phone"
                        v-model="form.Phone"
                    />
                </div>
                <div class="flex flex-row">
                    <div class="mr-4">
                        <p class="text-xl">HCN</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="healthcare_no"
                            v-model="form.Healthcare_no"
                        />
                    </div>
                    <div class="mr-4">
                        <p class="text-xl">HCN Expiry</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="hcn_expiry"
                            v-model="form.HCN_expiry"
                        />
                    </div>
                    <div class="mr-4">
                        <p class="text-xl">HCN Province</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="hcn_provice"
                            v-model="form.HCN_province"
                        />
                    </div>
                </div>
            </div>
            <button
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postForm()"
            >
                <div v-if="create_mode">
                    Create
                </div>
                <div v-else>
                    Save
                </div>
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
    name: "MedicalHistoryEditPage",

    data() {
        return {
            logged_in: true,
            create_mode: true,
            form: {
                Email: "",
                Fname: "",
                Initial: "",
                Lname: "",
                Gender: "",
                Sex: "",
                DoB: "",
                Phone: "",
                Healthcare_no: "",
                HCN_expiry: "",
                HCN_province: "",
            }
        };
    },

    created() {
        if (typeof this.$route.params.email != "undefined") {
            this.create_mode = false;
            this.getForm();
        }
    },

    methods: {
        getForm() {
            axios
                .post(
                    `http://localhost:5000/patient/forms`,
                    {
                        action_type: "get_form",
                        form_type: "new_applicant_form",
                        applicant_form: this.$route.params.email,
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
        postForm() {
            let email_data = this.$route.params.email;
            console.log(email_data)

            if (this.create_mode) {
                email_data = this.form.Email;
            }

            console.log(this.create_mode);
            console.log(email_data);

            axios.post(
                `http://localhost:5000/patient/forms`,
                {
                    action_type: "submit_form",
                    form_type: "new_applicant_form",
                    form: {
                        email: email_data,
                        fname: this.form.Fname,
                        initial: this.form.Initial,
                        lname: this.form.Lname,
                        gender: this.form.Gender,
                        sex: this.form.Sex,
                        dob: this.form.DoB,
                        phone: this.form.Phone,
                        healthcare_no: this.form.Healthcare_no,
                        hcn_expiry: this.form.HCN_expiry,
                        hcn_province: this.form.HCN_province,
                    },
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            )
            .then(() => {
                if (this.create_mode) {
                    this.$router.push("/patient-panel/forms")
                }
            });
        },
    },
};
</script>
