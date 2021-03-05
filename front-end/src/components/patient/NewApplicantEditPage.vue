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
                    Create New Applicant Form
                </p>
                <p v-else class="text-5xl mt-20">Edit New Applicant Form</p>
            </div>
            <div class="flex flex-col items-start mt-10 w-1/3 mx-auto">
                <div>
                    <p class="text-xl">Email</p>
                    <input
                        class="border border-black mb-6 p-1 rounded-lg"
                        type="text"
                        name="email"
                        v-model="email"
                    />
                </div>
                <div class="flex flex-row">
                    <div class="mr-4">
                        <p class="text-xl">First Name</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="fname"
                            v-model="fname"
                        />
                    </div>
                    <div class="mr-4">
                        <p class="text-xl">Initial</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="initial"
                            v-model="initial"
                        />
                    </div>
                    <div>
                        <p class="text-xl">Last Name</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="lname"
                            v-model="lname"
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
                            v-model="gender"
                        />
                    </div>
                    <div>
                        <p class="text-xl">Sex</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="sex"
                            v-model="sex"
                        />
                    </div>
                </div>
                <div>
                    <p class="text-xl">Date of Birth</p>
                    <input
                        class="border border-black mb-6 p-1 rounded-lg"
                        type="text"
                        name="dob"
                        v-model="dob"
                    />
                </div>
                <div>
                    <p class="text-xl">Phone</p>
                    <input
                        class="border border-black mb-6 p-1 rounded-lg"
                        type="text"
                        name="phone"
                        v-model="phone"
                    />
                </div>
                <div class="flex flex-row">
                    <div class="mr-4">
                        <p class="text-xl">HCN</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="healthcare_no"
                            v-model="healthcare_no"
                        />
                    </div>
                    <div class="mr-4">
                        <p class="text-xl">HCN Expiry</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="hcn_expiry"
                            v-model="hcn_expiry"
                        />
                    </div>
                    <div class="mr-4">
                        <p class="text-xl">HCN Province</p>
                        <input
                            class="border border-black mb-6 p-1 rounded-lg"
                            type="text"
                            name="hcn_provice"
                            v-model="hcn_province"
                        />
                    </div>
                </div>
            </div>
            <button
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postForm()"
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
    name: "NewApplicantEditPage",

    data() {
        return {
            logged_in: true,
            create_mode: true,
            email: "",
            fname: "",
            initial: "",
            lname: "",
            gender: "",
            sex: "",
            dob: "",
            phone: "",
            healthcare_no: "",
            hcn_expiry: "",
            hcn_province: "",
        };
    },

    created() {
        console.log(typeof this.$route.params.email != "undefined");
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

                    this.email = response.data.form.Email;
                    this.fname = response.data.form.Fname;
                    this.initial = response.data.form.Initial;
                    this.lname = response.data.form.Lname;
                    this.gender = response.data.form.Gender;
                    this.sex = response.data.form.Sex;
                    this.dob = response.data.form.DoB;
                    this.phone = response.data.form.Phone;
                    this.healthcare_no = response.data.form.Healthcare_no;
                    this.hcn_expiry = response.data.form.HCN_expiry;
                    this.hcn_province = response.data.form.HCN_province;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        postForm() {
            let email_data = this.$route.params.email;

            if (this.create_mode) {
                email_data = this.email;
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
                        fname: this.fname,
                        initial: this.initial,
                        lname: this.lname,
                        gender: this.gender,
                        sex: this.sex,
                        dob: this.dob,
                        phone: this.phone,
                        healthcare_no: this.healthcare_no,
                        hcn_expiry: this.hcn_expiry,
                        hcn_province: this.hcn_province,
                    },
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            );
        },
    },
};
</script>
