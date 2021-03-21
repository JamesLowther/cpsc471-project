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
                    Create Covid Screen
                </p>
                <p v-else class="text-5xl mt-20">Edit Covid Screen</p>
            </div>
            <div class="flex flex-col items-start mt-10 w-1/3 mx-auto">
                <div class="text-left text-xl w-full mb-10">
                    <p class="text-3xl">Are you experiencing:</p>
                    <ul class="list-disc ml-10 mt-4">
                        <li>Difficulty breathing</li>
                        <li>Shortness of breath</li>
                    </ul>
                     <form class="ml-2 mt-2 flex justify-center">
                        <div>
                            <input type="radio" name="q0-yes" value="1" v-model="form.Shortness_breath">
                            <label for="q0-yes"> Yes</label>
                        </div>
                        <div>
                            <input type="radio" class="ml-10" name="q0-no" value="0" v-model="form.Shortness_breath">
                            <label for="q0-no"> No</label>
                        </div>
                    </form> 
                </div>
                <div class="text-left text-xl w-full mb-10">
                    <p class="text-3xl">Are you experiencing:</p>
                    <ul class="list-disc ml-10 mt-4">
                        <li>A new cough</li>
                    </ul>
                     <form class="ml-2 mt-2 flex justify-center">
                        <div>
                            <input type="radio" name="q1-yes" value="1" v-model="form.New_cough">
                            <label for="q1-yes"> Yes</label>
                        </div>
                        <div>
                            <input type="radio" class="ml-10" name="q1-no" value="0" v-model="form.New_cough">
                            <label for="q1-no"> No</label>
                        </div>
                    </form> 
                </div>
                <div class="text-left text-xl w-full mb-10">
                    <p class="text-3xl">Are you experiencing:</p>
                    <ul class="list-disc ml-10 mt-4">
                        <li>Symptoms of a fever</li>
                    </ul>
                     <form class="ml-2 mt-2 flex justify-center">
                        <div>
                            <input type="radio" name="q2-yes" value="1" v-model="form.Fever">
                            <label for="q2-yes"> Yes</label>
                        </div>
                        <div>
                            <input type="radio" class="ml-10" name="q2-no" value="0" v-model="form.Fever">
                            <label for="q2-no"> No</label>
                        </div>
                    </form> 
                </div>
                <div class="text-left text-xl w-full mb-10">
                    <p class="text-3xl">Are you experiencing:</p>
                    <ul class="list-disc ml-10 mt-4">
                        <li>A sore or scratchy throat</li>
                    </ul>
                     <form class="ml-2 mt-2 flex justify-center">
                        <div>
                            <input type="radio" name="q3-yes" value="1" v-model="form.Sore_throat">
                            <label for="q3-yes"> Yes</label>
                        </div>
                        <div>
                            <input type="radio" class="ml-10" name="q3-no" value="0" v-model="form.Sore_throat">
                            <label for="q3-no"> No</label>
                        </div>
                    </form> 
                </div>
                <div class="text-left text-xl w-full mb-10">
                    <p class="text-3xl">Are you experiencing:</p>
                    <ul class="list-disc ml-10 mt-4">
                        <li>A runny nose</li>
                    </ul>
                     <form class="ml-2 mt-2 flex justify-center">
                        <div>
                            <input type="radio" name="q4-yes" value="1" v-model="form.Runny_nose">
                            <label for="q4-yes"> Yes</label>
                        </div>
                        <div>
                            <input type="radio" class="ml-10" name="q4-no" value="0" v-model="form.Runny_nose">
                            <label for="q4-no"> No</label>
                        </div>
                    </form> 
                </div>
            </div>
            <p class="text-2xl text-red-600">{{ error }}</p>
            <button
                v-if="create_mode"
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postCreateCovidScreen()"
            >
                Create
            </button>
            <button
                v-else
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                @click="postCovidScreen()"
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
    name: "CovidScreenEditPage",

    data() {
        return {
            logged_in: true,
            create_mode: true,
            error: "",
            form: {
                Shortness_breath: null,
                New_cough: null,
                Fever: null,
                Sore_throat: null,
                Runny_nose: null,
            }
        };
    },

    created() {
        if (typeof this.$route.params.date != "undefined") {
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
                        form_type: "covid_screen",
                        screen_date: this.$route.params.date
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
        postCreateCovidScreen() {
            // Check the input.
            if (!this.checkInput()) return;

            axios.post(
                `http://localhost:5000/patient/forms`,
                {
                    action_type: "submit_form",
                    form_type: "covid_screen",
                    new_form: 1,
                    form: {
                        Shortness_breath: parseInt(this.form.Shortness_breath),
                        New_cough: parseInt(this.form.New_cough),
                        Fever: parseInt(this.form.Fever),
                        Sore_throat: parseInt(this.form.Sore_throat),
                        Runny_nose: parseInt(this.form.Runny_nose),
                    }
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt")
                    }
                }
            )
            .then(() => {
                this.$router.push("/patient-panel/forms");
            })
        },
        checkInput() {
            for (var i in this.form) {
                if (this.form[i] == null) {
                    this.error = "Please answer all of the questions."
                    return false;
                }
            }
            return true;
        },
        postCovidScreen() {
            // Check the input.
            if (!this.checkInput()) return;

            axios.post(
                `http://localhost:5000/patient/forms`,
                {
                    action_type: "submit_form",
                    form_type: "covid_screen",
                    screen_date: this.$route.params.date,
                    form: {
                        Shortness_breath: parseInt(this.form.Shortness_breath),
                        New_cough: parseInt(this.form.New_cough),
                        Fever: parseInt(this.form.Fever),
                        Sore_throat: parseInt(this.form.Sore_throat),
                        Runny_nose: parseInt(this.form.Runny_nose),
                    }
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt")
                    }
                }
            );
        },
    }
};
</script>
