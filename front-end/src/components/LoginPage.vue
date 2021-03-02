<template>
  <div class="login">
    <div class="flex fixed justify-end w-full">
      <router-link
        to="/new-account"
        class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
        >Create Account</router-link
      >
    </div>
    <div class="flex fixed">
      <router-link
        to="/"
        class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
        >Back</router-link
      >
    </div>
    <p class="text-center text-5xl mt-10">Login</p>
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
          type="text"
          pattern="[0-9]{9}"
          placeholder="SSN"
          id="ssn"
          name="ssn"
          v-model="ssn"
        /><br />
        <input
          class="border border-black p-1 rounded-lg"
          type="password"
          placeholder="Password"
          id="password"
          name="password"
          v-model="password"
        /><br /><br />
        <button
          class="text-white px-4 py-2 shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg"
          @click="loginPost()"
        >
          Login
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
    };
  },

  methods: {
    loginPost() {
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