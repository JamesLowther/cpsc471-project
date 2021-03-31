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
        <div class="flex flex-col">
            <p class="text-center text-5xl mt-32 my-2">Login</p>
            <div class="bg-rose-300">
                <img class="object-contain md:object-scale-down h-96 w-full ..." src="@/assets/Gregor_Mendel_login.jpeg">
            </div>
            <div class="flex justify-center my-4">
                <div class="text-xl">
                    <label class="mr-3" for="select">Type:</label>
                    <select
                        class="bg-gray-300 rounded py-1 px-10"
                        id="select"
                        v-model="user_type"
                    >
                        <option value="patient">Patient</option>
                        <option value="doctor">Doctor</option>
                        <option value="clerk">Clerk</option></select
                    ><br />
                    <input
                        class="border my-4 p-1 rounded-lg"
                        v-bind:class="[
                            invalid_ssn ? 'border-red-700' : 'border-black',
                        ]"
                        type="text"
                        pattern="[0-9]{9}"
                        placeholder="SSN"
                        id="ssn"
                        name="ssn"
                        v-model="ssn"
                        ref="ssn"
                    /><br />
                    <input
                        class="border border-black p-1 rounded-lg"
                        v-bind:class="[
                            empty_pass ? 'border-red-700' : 'border-black',
                        ]"
                        type="password"
                        placeholder="Password"
                        id="password"
                        name="password"
                        v-model="password"
                        ref="pass"
                    /><br /><br />
                    <button
                        class="text-white px-4 py-2 shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg"
                        type="submit"
                        @click="loginPost()"
                    >
                        Login
                    </button>
                    <p class="text-red-600 mt-3">{{ error }}</p>
                </div>
            </div>
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
            empty_pass: false,
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
                    `http://localhost:5000/login`,
                    {
                        user_type: this.user_type,
                        ssn: this.ssn,
                        password: this.password,
                    },
                    { withCredentials: true }
                )
                .then((response) => {
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
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>