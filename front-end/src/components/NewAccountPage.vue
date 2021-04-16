<template>
    <div class="new-account">
        <div class="grid grid-cols-2 w-full fixed mt-5">
            <router-link
                to="/login"
                class="justify-self-start text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-4 ml-6"
                >Login Page</router-link
            >
            <router-link
                to="/"
                class="justify-self-end text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-4 mr-6"
                >Back</router-link
            >
        </div>
        <div class="bg-rose-300">
            <img
                class="object-contain md:object-scale-down pt-10 h-96 w-full ..."
                src="@/assets/Gregor_Mendel_login2.jpeg"
            />
        </div>
        <div
            class="flex flex-col items-center ml-auto mr-auto pt-2 w-1/12 mt-3 mb-4"
        >
            <table
                class="w-full md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg"
            >
                <thead>
                    <tr>
                        <th
                            class="text-lg text-white w-full bg-blue-500 rounded-t-2xl border-teal border-b-2 border-r-2"
                        >
                            New Account
                        </th>
                    </tr>
                </thead>
                <tbody>
                    <tr class="bg-blue-100">
                        <td class="border-blue-300 border-2 py-4">
                            <label class="mr-3" for="select">Type:</label>
                            <select
                                class="bg-blue-400 text-white rounded-md py-1 px-10"
                                id="select"
                                v-model="user_type"
                            >
                                <option value="patient">Patient</option>
                                <option value="doctor">Doctor</option>
                                <option value="clerk">Clerk</option></select
                            >
                        </td>
                    </tr>
                    <tr v-if="user_type != 'patient'" class="bg-blue-100">
                        <td class="border-blue-300 border-2 px-8 py-2">
                            <input
                                class="border p-1 rounded-lg"
                                v-bind:class="[
                                    invalid_fname
                                        ? 'border-red-700'
                                        : 'border-black'
                                ]"
                                type="text"
                                placeholder="First Name"
                                id="fname"
                                name="fname"
                                v-model="Fname"
                                ref="fname"
                            />
                        </td>
                    </tr>
                    <tr v-if="user_type != 'patient'" class="bg-blue-100">
                        <td class="border-blue-300 border-2 px-8 py-2">
                            <input
                                class="border p-1 rounded-lg"
                                v-bind:class="[
                                    invalid_initial
                                        ? 'border-red-700'
                                        : 'border-black'
                                ]"
                                type="text"
                                placeholder="Initial"
                                id="initial"
                                name="initial"
                                v-model="Initial"
                                ref="initial"
                            />
                        </td>
                    </tr>
                    <tr v-if="user_type != 'patient'" class="bg-blue-100">
                        <td class="border-blue-300 border-2 px-8 py-2">
                            <input
                                class="border p-1 rounded-lg"
                                v-bind:class="[
                                    invalid_lname
                                        ? 'border-red-700'
                                        : 'border-black'
                                ]"
                                type="text"
                                placeholder="Last Name"
                                id="lname"
                                name="lname"
                                v-model="Lname"
                                ref="lname"
                            />
                        </td>
                    </tr>
                    <tr v-if="user_type != 'patient'" class="bg-blue-100">
                        <td class="border-blue-300 border-2 px-8 py-2">
                            <input
                                class="border border-black p-1 rounded-lg"
                                type="text"
                                v-bind:class="[
                                    invalid_DoB
                                        ? 'border-red-700'
                                        : 'border-black'
                                ]"
                                placeholder="Date of Birth (yyyy-mm-dd)"
                                id="dob"
                                name="dob"
                                v-model="DoB"
                                ref="dob"
                            />
                        </td>
                    </tr>
                    <tr v-if="user_type == 'doctor'" class="bg-blue-100">
                        <td class="border-blue-300 border-2 px-8 py-2">
                            <input
                                class="border p-1 rounded-lg"
                                v-bind:class="[
                                    invalid_spec
                                        ? 'border-red-700'
                                        : 'border-black'
                                ]"
                                type="text"
                                pattern="[0-9]{9}"
                                placeholder="Specialization"
                                id="specialization"
                                name="specialization"
                                v-model="Specialization"
                                ref="specialization"
                            />
                        </td>
                    </tr>
                    <tr class="bg-blue-100">
                        <td class="border-blue-300 border-2 px-8 py-2">
                            <input
                                class="border p-1 rounded-lg"
                                v-bind:class="[
                                    invalid_ssn
                                        ? 'border-red-700'
                                        : 'border-black'
                                ]"
                                type="text"
                                pattern="[0-9]{9}"
                                placeholder="SSN"
                                id="ssn"
                                name="ssn"
                                v-model="ssn"
                                ref="ssn"
                            />
                        </td>
                    </tr>
                    <tr class="bg-blue-100">
                        <td class="border-blue-300 border-2 px-8 py-2">
                            <input
                                class="border border-black p-1 rounded-lg"
                                v-bind:class="[
                                    empty_pass
                                        ? 'border-red-700'
                                        : 'border-black'
                                ]"
                                type="password"
                                placeholder="Password"
                                id="password"
                                name="password"
                                v-model="password"
                                ref="pass"
                            />
                        </td>
                    </tr>
                    <tr class="bg-blue-100">
                        <td class="border-blue-300 border-2 py-2">
                            <button
                                class="text-white px-4 py-2 shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg"
                                @click="loginPost()"
                            >
                                Create Account
                            </button>
                        </td>
                    </tr>
                    <tr class=" shadow-2xl">
                        <td
                            class="border-teal-500 border-0 text-pink-300 bg-blue-500 rounded-b-2xl h-7"
                            colspan="3"
                        >
                            {{ error }}
                        </td>
                    </tr>
                </tbody>
            </table>
        </div>
    </div>
</template>

<script>
import axios from "axios";

export default {
    name: "LoginPage",

    data() {
        return {
            user_type: "patient",
            ssn: "",
            password: "",
            Fname: "",
            Lname: "",
            Initial: "",
            DoB: "",
            Specialization: "",
            error: "",
            invalid_ssn: false,
            invalid_DoB: false,
            invalid_fname: false,
            invalid_lname: false,
            invalid_initial: false,
            invalid_spec: false,
            empty_pass: false
        };
    },

    methods: {
        /* check if the input SSN fits format
         * sets boolean to true, changing class of input*/
        invalidSSN() {
            // test if the ssn matches 9 digit number
            let ssnStr = this.$refs.ssn.value;
            if (!/^[0-9]{9}$/.test(ssnStr)) {
                //change to red border, if black
                this.invalid_ssn = true;
                console.log("input ssn is not 9 digit number: " + ssnStr);
                this.error = "Invalid ssn: must be 9 digits";
                return true;
            }
            return false;
        },

        /* check if the input password is empty
         * sets boolean to true, changing class of input*/
        invalidPass() {
            let pass = this.$refs.pass.value;
            if (!pass) {
                this.empty_pass = true;
                console.log("Password is empty");
                this.error = "Password cannot be empty.";
                return true;
            }
            return false;
        },

        invalidDoB() {
            // test if the ssn matches 9 digit number
            let dob = this.$refs.dob.value;
            if (!/^[0-9]{4}-[0-9]{2}-[0-9]{2}$/.test(dob)) {
                //change to red border, if black
                this.invalid_DoB = true;
                this.error =
                    "Please enter your date of birth in the form yyyy-mm-dd";
                return true;
            }
            return false;
        },

        invalidFname() {
            let fname = this.$refs.fname.value;
            if (!fname) {
                this.invalid_fname = true;
                this.error = "First name cannot be empty.";
                return true;
            }
            return false;
        },

        invalidLname() {
            let lname = this.$refs.lname.value;
            if (!lname) {
                this.invalid_lname = true;
                this.error = "Last name cannot be empty.";
                return true;
            }
            return false;
        },

        invalidInitial() {
            let initial = this.$refs.initial.value;
            if (!initial) {
                this.invalid_initial = true;
                this.error = "Initial cannot be empty.";
                return true;
            }
            return false;
        },

        invalidSpec() {
            let spec = this.$refs.specialization.value;
            if (!spec) {
                this.invalid_spec = true;
                this.error = "Specialization cannot be empty.";
                return true;
            }
            return false;
        },

        loginPost() {
            // check for proper input
            if (this.user_type != "patient") {
                if (!this.invalidFname()) {
                    this.invalid_fname = false;
                    this.error = "";
                } else return;

                if (!this.invalidInitial()) {
                    this.invalid_initial = false;
                    this.error = "";
                } else return;

                if (!this.invalidLname()) {
                    this.invalid_lname = false;
                    this.error = "";
                } else return;

                if (!this.invalidDoB()) {
                    this.invalid_DoB = false;
                    this.error = "";
                } else return;
            }

            if (this.user_type == "doctor") {
                if (!this.invalidSpec()) {
                    this.invalid_spec = false;
                    this.error = "";
                } else return;
            }

            if (!this.invalidSSN()) {
                this.invalid_ssn = false;
                this.error = "";
            } else return;

            if (!this.invalidPass()) {
                this.empty_pass = false;
                this.error = "";
            } else return;

            axios
                .post("new-account", {
                    user_type: this.user_type,
                    ssn: this.ssn,
                    password: this.password,
                    Fname: this.Fname,
                    Lname: this.Lname,
                    Initial: this.Initial,
                    DoB: this.DoB,
                    Specialization: this.Specialization
                })
                .then(response => {
                    if (response.data.successful == "1") {
                        this.$router.push("login");
                    } else {
                        this.error = "Error creating a new account";
                    }
                })
                .catch(e => {
                    console.log(e);
                });
        }
    }
};
</script>
