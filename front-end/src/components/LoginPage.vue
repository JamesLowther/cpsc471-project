<template>
    <div class="login">
        <div class="grid grid-cols-2 w-full fixed mt-5">
            <router-link
                to="/new-account"
                class="justify-self-start text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-4 ml-6"
                >Create Account</router-link
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
                src="@/assets/Gregor_Mendel_login.jpeg"
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
                            Login
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
                                type="submit"
                                @click="loginPost()"
                            >
                                Login
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
            error: "",
            invalid_ssn: false,
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
                if (!this.invalid_ssn) this.invalid_ssn = !this.invalid_ssn;
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
                if (!this.empty_pass) this.empty_pass = !this.empty_pass;
                console.log("Password is empty");
                this.error = "Password cannot be empty.";
                return true;
            }
            return false;
        },

        loginPost() {
            // check for proper input
            if (!this.invalidSSN()) this.invalid_ssn = false;
            else return;
            if (!this.invalidPass()) this.empty_pass = false;
            else return;

            axios
                .post(
                    "login",
                    {
                        user_type: this.user_type,
                        ssn: this.ssn,
                        password: this.password
                    },
                    { withCredentials: true }
                )
                .then(response => {
                    if (response.data.logged_in != "1") {
                        this.error = "Error logging in";
                        return;
                    }

                    localStorage.setItem("jwt", response.data.access_token);

                    if (response.data.user_type == "patient") {
                        this.$router.push("patient-panel");
                    } else if (response.data.user_type == "doctor") {
                        this.$router.push("doctor-panel");
                    } else if (response.data.user_type == "clerk") {
                        this.$router.push("clerk-panel");
                    }
                })
                .catch(e => {
                    console.log(e);
                });
        }
    }
};
</script>
