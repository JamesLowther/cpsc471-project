<template>
    <div id="form-edit">
        <div class="flex justify-end w-full fixed">
            <button
                @click="$router.go(-1)"
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
            >
                Back
            </button>
        </div>
        <div v-if="logged_in">
            <div class="flex flex-col">
                <p v-if="create_mode" class="text-4xl lg:text-5xl mt-20">
                    Create Medical History Form
                </p>
                <p v-else class="text-4xl lg:text-5xl mt-20">
                    Edit Medical History Form
                </p>
            </div>
            <div class="flex flex-col items-start mt-10 w-5/6 lg:w-1/2 mx-auto">
                <div class="w-full mb-10">
                    <p class="font-bold text-3xl text-left">Pregnancy Info:</p>
                    <p class="text-left text-lg mb-2">
                        Leave values set to 0 if not applicable
                    </p>
                    <div
                        class="flex flex-row justify-around items-center w-full h-36 mx-auto bg-blue-500 rounded-2xl border-teal border-2"
                    >
                        <div
                            class="w-1/4 p-3 flex flex-col justify-between h-full"
                        >
                            <p class="text-xl text-white">Total births:</p>
                            <input
                                class="border border-blue-700 mb-6 p-1 rounded-lg text-right w-full shadow-2xl"
                                type="number"
                                min="0"
                                value="0"
                                pattern="[0-9]+"
                                name="total_births"
                                v-model="form.TPAL_total"
                            />
                        </div>
                        <div
                            class="w-1/4 p-3 flex flex-col justify-between h-full"
                        >
                            <p class="text-xl text-white">Preterm births:</p>
                            <input
                                class="border border-blue-700 mb-6 p-1 rounded-lg text-right w-full shadow-2xl"
                                type="number"
                                min="0"
                                value="0"
                                pattern="[0-9]+"
                                name="preterm_births"
                                v-model="form.TPAL_preterm"
                            />
                        </div>
                        <div
                            class="w-1/4 p-3 flex flex-col justify-between h-full"
                        >
                            <p class="text-xl text-white">Aborted:</p>
                            <input
                                class="border border-blue-700 mb-6 p-1 rounded-lg text-right w-full shadow-2xl"
                                type="number"
                                min="0"
                                value="0"
                                pattern="[0-9]+"
                                name="aborted"
                                v-model="form.TPAL_aborted"
                            />
                        </div>
                        <div
                            class="w-1/4 p-3 flex flex-col justify-between h-full"
                        >
                            <p class="text-xl text-white">Living children:</p>
                            <input
                                class="border border-blue-700 mb-6 p-1 rounded-lg text-right w-full shadow-2xl"
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
                    <table class="table-auto w-full mb-3">
                        <thead>
                            <tr>
                                <th
                                    class="text-lg w-1/3 text-white bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-r-2"
                                >
                                    Past Illnesses:
                                </th>
                                <th
                                    class="text-lg w-1/3 text-white bg-blue-500 border-teal border-b-2"
                                >
                                    Age of Onset:
                                </th>
                                <th
                                    class="w-1/3 text-white bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2"
                                ></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="illness in form.Past_illnesses"
                                :key="illness.Illness_name"
                                class="bg-blue-100"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ illness.Illness_name }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    {{ illness.Age_of_onset }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="w-3/4 text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 px-2 m-3"
                                        v-on:click="
                                            removeIllness(illness.Illness_name)
                                        "
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr class="bg-blue-100">
                                <td class="border-blue-300 border-2">
                                    <input
                                        class="border border-blue-700 mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="illness-search"
                                        placeholder="Search"
                                        v-model="illness_query"
                                        v-on:keyup="queryIllness()"
                                    />
                                </td>
                                <td class="border-blue-300 border-2">
                                    <input
                                        class="border border-blue-700 mb-2 mt-2 p-1 rounded-lg w-4/5 text-right"
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
                                class="bg-blue-100"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ illness.Name }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="w-3/4 text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-2 px-2 w-1/4 m-3"
                                        v-on:click="addNewIllness(illness.Name)"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                            <tr class="shadow-2xl">
                                <td
                                    class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl h-7 "
                                    colspan="2"
                                ></td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ past_illnesses_error }}
                    </p>
                </div>
                <div class="w-full mb-10">
                    <p class="font-bold text-3xl mb-1 text-left">Allergies:</p>
                    <table class="table-auto w-full mb-3">
                        <thead>
                            <tr>
                                <th
                                    class="text-lg w-1/3 text-white bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-r-2"
                                >
                                    Allergy:
                                </th>
                                <th
                                    class="w-1/3 text-white bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2"
                                ></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="allergy in form.Allergies"
                                :key="allergy"
                                class="bg-blue-100"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ allergy }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="w-3/4 text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 px-2 w-1/4 m-3"
                                        v-on:click="removeAllergy(allergy)"
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr class="bg-blue-100">
                                <td class="border-blue-300 border-2">
                                    <input
                                        class="border border-blue-700 mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="new-allergy"
                                        placeholder="Allergy name"
                                        v-model="new_allergy"
                                    />
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="w-3/4 text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:scale-105 rounded-lg py-2 px-2 w-1/4 m-3"
                                        v-on:click="addNewAllergy()"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                            <tr class="shadow-2xl">
                                <td
                                    class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl h-7 "
                                    colspan="2"
                                ></td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ allergies_error }}
                    </p>
                </div>
                <div class="w-full mb-5">
                    <p class="font-bold text-3xl mb-1 text-left">
                        Immunizations:
                    </p>
                    <table class="table-auto w-full mb-3">
                        <thead>
                            <tr>
                                <th
                                    class="text-lg w-1/3 text-white bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-r-2"
                                >
                                    Immunization:
                                </th>
                                <th
                                    class="w-1/3 text-white bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2"
                                ></th>
                            </tr>
                        </thead>
                        <tbody>
                            <tr
                                v-for="immunization in form.Immunizations"
                                :key="immunization"
                                class="bg-blue-100"
                            >
                                <td class="border-blue-300 border-2">
                                    {{ immunization }}
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="w-3/4 text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:scale-105 rounded-lg py-2 px-2 w-1/4 m-3"
                                        v-on:click="
                                            removeImmunization(immunization)
                                        "
                                    >
                                        Remove
                                    </button>
                                </td>
                            </tr>
                            <tr class="bg-blue-100">
                                <td class="border-blue-300 border-2">
                                    <input
                                        class="border border-blue-700 mb-2 mt-2 p-1 rounded-lg w-4/5"
                                        type="text"
                                        name="new-immunization"
                                        placeholder="Immunization name"
                                        v-model="new_immunization"
                                    />
                                </td>
                                <td class="border-blue-300 border-2">
                                    <button
                                        class="w-3/4 text-white shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 transform hover:scale-105 rounded-lg py-2 px-2 w-1/4 m-3"
                                        v-on:click="addNewImmunization()"
                                    >
                                        Add
                                    </button>
                                </td>
                            </tr>
                            <tr class="shadow-2xl">
                                <td
                                    class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl h-7 "
                                    colspan="2"
                                ></td>
                            </tr>
                        </tbody>
                    </table>
                    <p class="text-xl mx-auto text-red-600">
                        {{ immunization_error }}
                    </p>
                </div>
            </div>
            <button
                class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 mb-2"
                @click="postForm()"
            >
                <div v-if="create_mode">Create</div>
                <div v-else>Save</div>
            </button>
            <p class="text-xl text-center text-red-600 mb-2">
                {{ post_error }}
            </p>
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
    props: {
        isClerk: Boolean,
        isEdit: Boolean
    },

    data() {
        return {
            logged_in: true,
            create_mode: true,
            form: {
                Hx_ID: "",
                P_SSN: "",
                TPAL_total: "0",
                TPAL_preterm: "0",
                TPAL_aborted: "0",
                TPAL_living: "0",
                Past_illnesses: [],
                Allergies: [],
                Immunizations: []
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
            post_error: ""
        };
    },

    created() {
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
                        form_type: "medical_history",
                        p_ssn: this.$route.params.ssn
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                )
                .then(response => {
                    if (response.data.logged_in != "1") {
                        this.logged_in = false;
                        return;
                    }

                    this.logged_in = true;

                    this.form = response.data.form;
                })
                .catch(e => {
                    console.log(e);
                });
        },
        postForm() {
            if (!this.checkTPAL()) {
                return;
            }

            axios
                .post(
                    "patient/forms",
                    {
                        action_type: "submit_form",
                        form_type: "medical_history",
                        p_ssn: this.$route.params.ssn,
                        form: this.form
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                )
                .then(response => {
                    if (response.data.successful != 1) {
                        this.post_error =
                            "There was an issue with your request.";
                    } else {
                        this.post_error = "";

                        if (this.create_mode) {
                            if (this.isClerk) {
                                this.$router.push("/clerk-panel/forms");
                            } else {
                                this.$router.push("/patient-panel/forms");
                            }
                        }
                    }
                });
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
                    "entities/forms",
                    {
                        entity_type: "illness",
                        method: "query",
                        query_string: this.illness_query
                    },
                    {
                        headers: {
                            Authorization:
                                "Bearer " + localStorage.getItem("jwt")
                        }
                    }
                )
                .then(response => {
                    if (response.data.logged_in != "1") {
                        this.logged_in = false;
                        return;
                    }

                    this.logged_in = true;
                    this.illness_results = response.data.results;
                })
                .catch(e => {
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
                Age_of_onset: this.new_age_of_onset
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
            if (!this.new_allergy.trim()) return;

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
            if (!this.new_immunization.trim()) return;

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
        }
    }
};
</script>
