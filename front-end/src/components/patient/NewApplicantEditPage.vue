<template>
    <div id="form-edit">
        <div class="grid grid-cols-2 w-full fixed">
            <button
                v-if="isClerk"
                class="justify-self-start"
                @click="approveForm()"
            >
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-yellow-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Approve
                </div>
            </button>
            <div v-else></div>
            <button class="justify-self-end" @click="$router.go(-1)">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </button>
        </div>
        <div v-if="logged_in" class="flex flex-col items-center w-full">
            <div class="flex flex-col">
                <p v-if="create_mode" class="text-5xl mt-20">
                    Create New Applicant Form
                </p>
                <div v-else>
                    <p class="text-4xl lg:text-5xl mt-20 mb-2">Edit New Applicant Form</p>
                    <div class="flex flex-row justify-center items-center h-16">
                        <p class="text-3xl">Approved:</p>
                        <svg
                            v-if="form.Is_approved"
                            class="h-4/5"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="green"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"
                            />
                        </svg>
                        <svg
                            v-else
                            class="h-4/5"
                            xmlns="http://www.w3.org/2000/svg"
                            fill="none"
                            viewBox="0 0 24 24"
                            stroke="red"
                        >
                            <path
                                stroke-linecap="round"
                                stroke-linejoin="round"
                                stroke-width="2"
                                d="M10 14l2-2m0 0l2-2m-2 2l-2-2m2 2l2 2m7-2a9 9 0 11-18 0 9 9 0 0118 0z"
                            />
                        </svg>
                    </div>
                </div>
            </div>
            <div class="flex flex-col mt-10 mx-auto bg-blue-500 rounded-2xl border-teal border-2 p-5">
                <div class="flex flex-col items-center lg:items-start mb-6 w-full bg-blue-100 py-1 text-black rounded-2xl">
                    <div class="mx-2">
                        <p class="text-xl">Email</p>
                        <input
                            class="border border-blue-700 mb-2 p-1 rounded-lg"
                            type="text"
                            name="email"
                            v-model="form.Email"
                            placeholder="john.smith@abc.com"
                        />
                    </div>
                    <p class="w-full text-xl text-center text-red-600">
                        {{ email_error }}
                    </p>
                </div>
                <div class="mb-6 w-full bg-blue-100 py-1 text-black rounded-2xl">
                    <div class="flex flex-col lg:flex-row">
                        <div class="mx-2">
                            <p class="text-xl">First Name</p>
                            <input
                                class="border border-blue-700 mb-2 p-1 rounded-lg"
                                type="text"
                                name="fname"
                                v-model="form.Fname"
                                placeholder="John"
                            />
                        </div>
                        <div class="mx-2">
                            <p class="text-xl">Initial</p>
                            <input
                                class="border border-blue-700 mb-2 p-1 rounded-lg"
                                type="text"
                                name="initial"
                                v-model="form.Initial"
                                placeholder="A"
                            />
                        </div>
                        <div class="mx-2">
                            <p class="text-xl">Last Name</p>
                            <input
                                class="border border-blue-700 mb-2 p-1 rounded-lg"
                                type="text"
                                name="lname"
                                v-model="form.Lname"
                                placeholder="Smith"
                            />
                        </div>
                    </div>
                    <p class="text-xl text-center text-red-600">
                        {{ name_error }}
                    </p>
                </div>
                <div class="mb-6 bg-blue-100 py-1 text-black rounded-2xl">
                    <div class="flex flex-col lg:flex-row">
                        <div class="mx-2">
                            <p class="text-xl">Gender</p>
                            <input
                                class="border border-blue-700 mb-2 p-1 rounded-lg"
                                type="text"
                                name="gender"
                                v-model="form.Gender"
                            />
                        </div>
                        <div class="mx-2">
                            <p class="text-xl">Sex</p>
                            <input
                                class="border border-blue-700 mb-2 p-1 rounded-lg"
                                type="text"
                                name="sex"
                                v-model="form.Sex"
                            />
                        </div>
                    </div>
                    <p class="text-xl text-center text-red-600">
                        {{ gender_error }}
                    </p>
                </div>
                <div class="flex flex-col items-center lg:items-start mb-6 bg-blue-100 py-1 text-black rounded-2xl">
                    <div class="mx-2">
                        <p class="text-xl">Date of Birth</p>
                        <input
                            class="border border-blue-700 mb-2 p-1 rounded-lg"
                            type="text"
                            name="dob"
                            v-model="form.DoB"
                            placeholder="yyyy-mm-dd"
                        />
                    </div>
                    <p class="text-xl mx-auto text-red-600">
                        {{ DoB_error }}
                    </p>
                </div>
                <div class="flex flex-col items-center lg:items-start mb-6 bg-blue-100 py-1 text-black rounded-2xl">
                    <div class="mx-2">
                        <p class="text-xl">Phone</p>
                        <input
                            class="border border-blue-700 mb-2 p-1 rounded-lg"
                            type="text"
                            name="phone"
                            v-model="form.Phone"
                            placeholder="123-123-1234"
                        />
                    </div>
                    <p class="text-xl mx-auto text-red-600">
                        {{ phone_error }}
                    </p>
                </div>
                <div class="mb-6 bg-blue-100 py-1 text-black rounded-2xl">
                    <div class="flex flex-col lg:flex-row">
                        <div class="mx-2">
                            <p class="text-xl">HCN</p>
                            <input
                                class="border border-blue-700 mb-2 p-1 rounded-lg"
                                type="text"
                                name="healthcare_no"
                                v-model="form.Healthcare_no"
                            />
                        </div>
                        <div class="mx-2">
                            <p class="text-xl">HCN Expiry</p>
                            <input
                                class="border border-blue-700 mb-2 p-1 rounded-lg"
                                type="text"
                                name="hcn_expiry"
                                v-model="form.HCN_expiry"
                            />
                        </div>
                        <div class="mx-2">
                            <p class="text-xl">HCN Province</p>
                            <input
                                class="border border-blue-700 mb-2 p-1 rounded-lg"
                                type="text"
                                name="hcn_provice"
                                v-model="form.HCN_province"
                            />
                        </div>
                    </div>
                    <p class="text-xl text-center text-red-600">
                        {{ HCN_error }}
                    </p>
                </div>
            </div>
            <button
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postForm()"
            >
                <div v-if="create_mode">Create</div>
                <div v-else>Save</div>
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
    name: "NewApplicantEditPage",

    props: {
        isClerk: Boolean,
        isEdit: Boolean,
    },

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
                Is_approved: "",
            },
            email_error: "",
            name_error: "",
            gender_error: "",
            DoB_error: "",
            phone_error: "",
            HCN_error: "",
            post_error: "",
        };
    },

    created() {
        console.log(this.isEdit)
        if (this.isEdit) {
            this.create_mode = false;
            this.getForm();
        }
    },

    methods: {
        getForm() {
            axios
                .post(
                    "patient/forms",
                    {
                        action_type: "get_form",
                        form_type: "new_applicant_form",
                        p_ssn: this.$route.params.ssn,
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
            if (
                ![
                    this.checkEmail(),
                    this.checkName(),
                    this.checkGender(),
                    this.checkDoB(),
                    this.checkPhone(),
                    this.checkHCN(),
                ].every((x) => {
                    return x === true;
                })
            )
                return;

            axios
                .post(
                    "patient/forms",
                    {
                        action_type: "submit_form",
                        form_type: "new_applicant_form",
                        p_ssn: this.$route.params.ssn,
                        form: {
                            email: this.form.Email,
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
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt"),
                        },
                    }
                )
                .then((response) => {
                    if (this.create_mode) {
                        this.$router.push("/patient-panel/forms");
                    }

                    if (response.data.successful != 1) {
                        this.post_error =
                            "There was an issue with your request.";
                    } else {
                        this.post_error = "";
                    }

                    // Reload the data.
                    this.getForm();
                });
        },
        approveForm() {
            // This should be called by clerks.
            // Posting when logged in as a patient should not be permitted.
            axios
                .post(
                    "clerk/forms",
                    {
                        form_type: "new_application_form",
                        action_type: "submit_form",
                        P_SSN: this.$route.params.ssn,
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt"),
                        },
                    }
                )
                .then(() => {
                    // Reload the form data after the post.
                    this.getForm();
                });
        },
        checkEmail() {
            // I just found this regex from https://codepen.io/CSWApps/pen/MmpBjV
            // Since email validation is no joke.
            if (
                !/^(([^<>()[\]\\.,;:\s@"]+(\.[^<>()[\]\\.,;:\s@"]+)*)|(".+"))@((\[[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}\.[0-9]{1,3}])|(([a-zA-Z\-0-9]+\.)+[a-zA-Z]{2,24}))$/.test(
                    this.form.Email
                )
            ) {
                this.email_error = "Please enter a valid email.";
                return false;
            }
            this.email_error = "";
            return true;
        },
        checkName() {
            if (
                this.form.Fname === "" ||
                this.form.Initial === "" ||
                this.form.Lname === ""
            ) {
                this.name_error = "Please fill out all of the fields.";
                return false;
            }
            this.name_error = "";
            return true;
        },
        checkGender() {
            if (this.form.Gender === "" || this.form.Sex === "") {
                this.gender_error = "Please fill out all of the fields.";
                return false;
            }
            this.gender_error = "";
            return true;
        },
        checkDoB() {
            let regex = new RegExp("^[0-9]{4}-[0-9]{2}-[0-9]{2}$");
            if (!regex.test(this.form.DoB)) {
                this.DoB_error =
                    "Please enter your date of birth in the form yyyy/mm/dd.";
                return false;
            }
            this.DoB_error = "";
            return true;
        },
        checkPhone() {
            // Taken from https://stackoverflow.com/questions/16699007/regular-expression-to-match-standard-10-digit-phone-number.
            let regex = new RegExp("^[0-9]{3}-[0-9]{3}-[0-9]{4}$");
            if (!regex.test(this.form.Phone)) {
                this.phone_error =
                    "Please enter your phone in the form 123-123-1324.";
                return false;
            }
            this.phone_error = "";
            return true;
        },
        checkHCN() {
            if (
                this.form.Healthcare_no === "" ||
                this.form.HCN_expiry === "" ||
                this.form.HCN_province === ""
            ) {
                this.HCN_error = "Please fill out all of the fields.";
                return false;
            }
            this.HCN_error = "";
            return true;
        },
    },
};
</script>
