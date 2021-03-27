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
            <div class="flex flex-col items-start mt-10 w-1/2 mx-auto">
                <div class="w-full mb-10">
                    <p class="font-bold text-3xl mb-1 text-left">
                        Pregnancy Info:
                    </p>
                    <div
                        class="flex flex-row justify-around items-center w-full mx-auto"
                    >
                        <div>
                            <p class="text-xl">Total births:</p>
                            <input
                                class="border border-black mb-6 p-1 rounded-lg text-right"
                                type="number"
                                min="0"
                                value="0"
                                pattern="[0-9]+"
                                name="total_births"
                                v-model="form.TPAL_total"
                            />
                        </div>
                        <div>
                            <p class="text-xl">Preterm births:</p>
                            <input
                                class="border border-black mb-6 p-1 rounded-lg text-right"
                                type="number"
                                min="0"
                                value="0"
                                pattern="[0-9]+"
                                name="preterm_births"
                                v-model="form.TPAL_preterm"
                            />
                        </div>
                        <div>
                            <p class="text-xl">Aborted:</p>
                            <input
                                class="border border-black mb-6 p-1 rounded-lg text-right"
                                type="number"
                                min="0"
                                value="0"
                                pattern="[0-9]+"
                                name="aborted"
                                v-model="form.TPAL_aborted"
                            />
                        </div>
                        <div>
                            <p class="text-xl">Living children:</p>
                            <input
                                class="border border-black mb-6 p-1 rounded-lg text-right"
                                type="number"
                                min="0"
                                value="0"
                                pattern="[0-9]+"
                                name="living_children"
                                v-model="form.TPAL_living"
                            />
                        </div>
                    </div>
                    <p class="text-xl mx-auto text-red-600">
                        {{ pregnancy_info_error }}
                    </p>
                </div>
                <div class="w-full mb-10">
                    <p class="font-bold text-3xl mb-1 text-left">
                        Past Illnesses:
                    </p>
                    <table class="table-fixed w-full mb-3">
                        <thead>
                            <tr>
                                <th class="text-lg w-1/3 border-black border-2">
                                    Past Illnesses:
                                </th>
                                <th class="text-lg w-1/3 border-black border-2">
                                    Age of Onset:
                                </th>
                                <th class="w-1/3 border-black border-2"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="illness in form.Past_illnesses"
                                :key="illness.Illness_name"
                            >
                                <td class="border-black border-2">
                                    {{ illness.Illness_name }}
                                </td>
                                <td class="border-black border-2">
                                    {{ illness.Age_of_onset }}
                                </td>
                                <td class="border-black border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 px-8 m-3"
                                        v-on:click="
                                            removeIllness(illness.Illness_name)
                                        "
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr>
                                <td class="border-black border-2">
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="illness-search"
                                        placeholder="Search"
                                        v-model="illness_query"
                                        v-on:keyup="queryIllness()"
                                    />
                                </td>
                                <td class="border-black border-2">
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg w-4/5 text-right"
                                        type="number"
                                        min="0"
                                        value="0"
                                        name="age-of-onset"
                                        v-model="new_age_of_onset"
                                    />
                                </td>
                            </tr>
                            <tr
                                v-for="illness in illness_results"
                                :key="illness.Name"
                            >
                                <td class="border-black border-2">
                                    {{ illness.Name }}
                                </td>
                                <td class="border-black border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-2 w-1/4 m-3"
                                        v-on:click="addNewIllness(illness.Name)"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ past_illnesses_error }}
                    </p>
                </div>
                <div class="w-full mb-10">
                    <p class="font-bold text-3xl mb-1 text-left">Allergies:</p>
                    <table class="table-fixed w-full mb-3">
                        <thead>
                            <tr>
                                <th class="text-lg w-1/3 border-black border-2">
                                    Allergy:
                                </th>
                                <th class="w-1/3 border-black border-2"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="allergy in form.Allergies"
                                :key="allergy"
                            >
                                <td class="border-black border-2">
                                    {{ allergy }}
                                </td>
                                <td class="border-black border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 w-1/4 m-3"
                                        v-on:click="removeAllergy(allergy)"
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr>
                                <td class="border-black border-2">
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="new-allergy"
                                        placeholder="Allergy name"
                                        v-model="new_allergy"
                                    />
                                </td>
                                <td class="border-black border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:scale-105 rounded-lg py-2 w-1/4 m-3"
                                        v-on:click="addNewAllergy()"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ allergies_error }}
                    </p>
                </div>
                <div class="w-full mb-10">
                    <p class="font-bold text-3xl mb-1 text-left">
                        Immunizations:
                    </p>
                    <table class="table-fixed w-full mb-3">
                        <thead>
                            <tr>
                                <th class="text-lg w-1/3 border-black border-2">
                                    Immunization:
                                </th>
                                <th class="w-1/3 border-black border-2"></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="immunization in form.Immunizations"
                                :key="immunization"
                            >
                                <td class="border-black border-2">
                                    {{ immunization }}
                                </td>
                                <td class="border-black border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 w-1/4 m-3"
                                        v-on:click="
                                            removeImmunization(immunization)
                                        "
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr>
                                <td class="border-black border-2">
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="new-immunization"
                                        placeholder="Immunization name"
                                        v-model="new_immunization"
                                    />
                                </td>
                                <td class="border-black border-2">
                                    <button
                                        class="text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:scale-105 rounded-lg py-2 w-1/4 m-3"
                                        v-on:click="addNewImmunization()"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ immunization_error }}
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
                Hx_ID: "",
                P_SSN: "",
                TPAL_total: "",
                TPAL_preterm: "",
                TPAL_aborted: "",
                TPAL_living: "",
                Past_illnesses: [],
                Allergies: [],
                Immunizations: [],
            },
            illness_query: "",
            illness_results: [],
            new_age_of_onset: "",
            new_allergy: "",
            new_immunization: "",
            pregnancy_info_error: "",
            past_illnesses_error: "",
            allergies_error: "",
            immunization_error: "",
        };
    },

    created() {
        if (typeof this.$route.params.id != "undefined") {
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
                        form_type: "medical_history",
                        history_id: this.$route.params.id,
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
            if (!this.checkTPAL()) {
                return;
            }

            axios.post(
                `http://localhost:5000/patient/forms`,
                {
                    action_type: "submit_form",
                    form_type: "medical_history",
                    form: this.form,
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            );
        },
        checkTPAL() {
            if (
                this.form.TPAL_total === "" ||
                this.form.TPAL_preterm === "" ||
                this.form.TPAL_aborted === "" ||
                this.form.TPAL_living === "" ||
                isNaN(this.form.TPAL_total) ||
                isNaN(this.form.TPAL_preterm) ||
                isNaN(this.form.TPAL_aborted) ||
                isNaN(this.form.TPAL_living)
            ) {
                this.pregnancy_info_error =
                    "TPAL info must be a valid integer.";
                return false;
            }

            if (
                parseInt(this.form.TPAL_total) < 0 ||
                parseInt(this.form.TPAL_preterm) < 0 ||
                parseInt(this.form.TPAL_aborted) < 0 ||
                parseInt(this.form.TPAL_living) < 0
            ) {
                this.pregnancy_info_error =
                    "TPAL info must be a positive integer.";
                return false;
            }

            this.pregnancy_info_error = "";
            return true;
        },
        checkPastIllness() {
            if (this.new_age_of_onset === "" || isNaN(this.new_age_of_onset)) {
                this.past_illnesses_error =
                    "New age of onset must be a valid integer.";
                return false;
            }

            if (parseInt(this.new_age_of_onset) < 0) {
                this.past_illnesses_error =
                    "New age of onset must be a positive integer.";
                return false;
            }

            this.past_illnesses_error = "";
            return true;
        },
        queryIllness() {
            axios
                .post(
                    `http://localhost:5000/entities/forms`,
                    {
                        entity_type: "illness",
                        method: "query",
                        query_string: this.illness_query,
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

                    this.logged_in = true;
                    this.illness_results = response.data.results;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        addNewIllness(illness) {
            if (!this.checkPastIllness()) {
                return;
            }

            for (let i = 0; i < this.form.Past_illnesses.length; i++) {
                if (this.form.Past_illnesses[i].Illness_name == illness) {
                    this.past_illnesses_error =
                        "You have already added that illness.";
                    return;
                }
            }
            this.past_illnesses_error = "";

            this.form.Past_illnesses.push({
                Illness_name: illness,
                Age_of_onset: this.new_age_of_onset,
            });

            this.new_age_of_onset = "";
        },
        removeIllness(illness) {
            let temp_array = this.form.Past_illnesses;
            this.form.Past_illnesses = [];

            for (let i = 0; i < temp_array.length; i++) {
                if (temp_array[i].Illness_name != illness) {
                    this.form.Past_illnesses.push(temp_array[i]);
                }
            }
        },
        addNewAllergy() {
            if (this.new_allergy == "") return;

            for (let i = 0; i < this.form.Allergies.length; i++) {
                if (this.form.Allergies[i] == this.new_allergy) {
                    this.allergies_error =
                        "You have already added that allergy.";
                    return;
                }
            }

            this.allergies_error = "";

            this.form.Allergies.push(this.new_allergy);
            this.new_allergy = "";
        },
        removeAllergy(allergy) {
            let temp_array = this.form.Allergies;
            this.form.Allergies = [];

            for (let i = 0; i < temp_array.length; i++) {
                if (temp_array[i] != allergy) {
                    this.form.Allergies.push(temp_array[i]);
                }
            }
        },
        addNewImmunization() {
            if (this.new_immunization == "") return;

            for (let i = 0; i < this.form.Immunizations.length; i++) {
                if (this.form.Immunizations[i] == this.new_immunization) {
                    this.immunization_error =
                        "You have already added that immunization.";
                    return;
                }
            }

            this.immunization_error = "";

            this.form.Immunizations.push(this.new_immunization);
            this.new_immunization = "";
        },
        removeImmunization(immunization) {
            let temp_array = this.form.Immunizations;
            this.form.Immunizations = [];

            for (let i = 0; i < temp_array.length; i++) {
                if (temp_array[i] != immunization) {
                    this.form.Immunizations.push(temp_array[i]);
                }
            }
        },
    },
};
</script>
