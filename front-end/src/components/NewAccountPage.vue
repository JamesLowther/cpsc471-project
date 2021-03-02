<template>
  <div class="new-account">
    <div class="flex fixed justify-end w-full">
      <router-link
        to="/login"
        class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
        >Login Page</router-link
      >
    </div>
    <div class="flex fixed">
      <router-link
        to="/"
        class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
        >Back</router-link
      >
    </div>
    <p class="text-center text-5xl mt-10">New Account</p>
    <div class="flex justify-center my-64">
      <div class="text-xl">
        <label class="mr-3" for="select">Type:</label>
        <select class="bg-gray-300 rounded py-1 px-10" id="select" v-model="user_type">
          <option value="patient">Patient</option>
          <option value="doctor">Doctor</option>
          <option value="clerk">Clerk</option></select
        ><br />
        <input
          class="border border-black my-4 p-1 rounded-lg"
          v-bind:class="[invalid_ssn ? 'border-red-700':'border-black']"
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
          v-bind:class="[empty_pass ? 'border-red-700':'border-black']"
          type="password"
          placeholder="Password"
          id="password"
          name="password"
          v-model="password"
          ref="pass"
        /><br /><br />
        <button
          class="text-white px-4 py-2 shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg"
          @click="loginPost()"
        >
          Create Account
        </button>
        <p class="text-red-600 mt-3">{{ error }}</p>
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
      empty_pass: false
    };
  },

  methods: {

    /* check if the input SSN fits format
     * sets boolean to true, changing class of input*/
    invalidSSN() {
      // test if the ssn matches 9 digit number
      let ssnStr = this.$refs.ssn.value;
      if (!(/^[0-9]{9}$/).test(ssnStr)) {

        //change to red border, if black
        if (!this.invalid_ssn) this.invalid_ssn = !this.invalid_ssn;
        console.log("input ssn is not 9 digit number: "+ ssnStr);
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
      if (!this.invalidSSN()) {
        this.invalid_ssn=false; 
        this.error="";
      }else return;

      if (!this.invalidPass()) {
        this.empty_pass=false;
        this.error="";
      }else return;      

      axios
        .post(`http://localhost:5000/new-account`, {
          user_type: this.user_type,
          ssn: this.ssn,
          password: this.password,
        })
        .then((response) => {
          if (response.data.successful == '1') {
            this.$router.push('login')
          } else {
            this.error = "Error creating a new account"
          }
        })
        .catch((e) => {
          console.log(e);
        });
    },
  },
};
</script>