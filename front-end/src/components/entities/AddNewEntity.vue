<template>
    <div id="Entities_forms">
        <router-link :to="{name: 'entities-panel',params: { entity_type: entity_type, user_type: user_type, query_string: query_string }}"
        class="flex justify-end w-full fixed">
        <button class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
            <span >Back</span>
        </button>
        </router-link>
        <div v-if="logged_in">

            <!-- If the entity being modified is an Medication, load this table view -->
            <div v-if="entity_type == 'medication'" class="flex flex-col items-center ml-auto mr-auto pt-24 mt-3 mb-4">
                <table class="w-full md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg">
                    <thead>
                        <tr>
                            <th v-if="create_mode" class="text-lg text-white text-2xl w-full bg-blue-500 rounded-t-2xl border-teal border-b-2 border-r-2" colspan="2"> 
                                <b>Add new {{ entity_type }}</b>
                            </th>
                            <th v-else class="text-lg text-white text-2xl w-full bg-blue-500 rounded-t-2xl border-teal border-b-2 border-r-2" colspan="2"> 
                                <b>Modify {{ entity_type }}</b>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="bg-blue-100">
                            <td class="border-blue-300 border-2 py-2">
                                <b class="text-xl">{{ entity_type }} Name</b>
                            </td>
                            <td v-if="create_mode == true" class="border-blue-300 border-2 py-2">
                                <input
                                    class="border border-black mb-1 mt-1 p-1 rounded-lg"
                                    type="text"
                                    name="entity_name"
                                    placeholder="Name"
                                    v-model="entity_name"/>
                            </td>
                            <td v-else class="border-blue-300 border-2 py-2">
                                <input
                                    class="border border-black text-gray-400 mb-1 mt-2 p-1 rounded-lg"
                                    type="text"
                                    name="entity_name"
                                    placeholder="entity_name"
                                    v-model="entity_name"
                                    readonly/>
                            </td>
                        <tr class="bg-blue-100">
                            <td class="border-blue-300 border-2 py-3">
                                <b>Is it a prescription drug?</b>
                            </td>
                            <td class="border-blue-300 border-2 py-1">
                                <input type="radio" name="pre-yes" value="1" v-model="Is_prescription" class="mx-2">
                                <label for="pre-yes">Yes</label>
                                <br />
                                <input type="radio" name="pre-no" value="0" v-model="Is_prescription" class="mx-2">
                                <label for="pre-no">No</label>
                            </td>
                        </tr>
                        <tr class="bg-blue-100">
                            <td class="border-blue-300 border-2 py-2">
                                <label v-if="entity_type == 'medication'" for="effect" class="m-2">
                                    <b>Add Side-effect(s)</b> <i class="text-gray-400">(optional)</i></label>
                                <br />
                                <input
                                    class="border border-black mb-2 mt-2 p-1 rounded-lg"
                                    type="text"
                                    name="effect"
                                    v-model="effect"
                                />
                                <br />
                                <button @click="rm_effect()" class="text-white shadow-lg transition duration-300 ease-in-out bg-pink-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-1 px-4 m-1">
                                    remove
                                </button>
                                <button @click="add_effect()" class="text-white shadow-lg transition duration-300 ease-in-out bg-blue-500 hover:bg-blue-700 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-1 px-4 m-1">
                                    add
                                </button>
                            </td>
                            <td class="border-blue-300 border-2 py-2">
                                <ul class="list-disc text-left pl-5">
                                    <li v-for="(effect, i) in effects" :key="`${i}-${effect}`">
                                        {{ effect }}
                                    </li>
                                </ul>
                            </td>
                        </tr>
                        <tr class=" shadow-2xl">
                            <td class="border-teal-500 border-0 text-pink-300 bg-blue-500 rounded-b-2xl" colspan="3">
                                <button v-if="create_mode"
                                        @click="add_med()" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-green-500 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                                    <b>Add Medication</b>
                                </button>
                                <button v-else
                                        @click="update_med()" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-green-500 hover:bg-green-800 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                                    <b>Update Medication</b>
                                </button>
                                <template v-if="sys_msg.length != 0">
                                    <!-- Display error or success, depending on response from server -->
                                    <p v-if="status=='0'" class="text-red-600 text-xl">Error updating {{entity_type}}</p>
                                    <p v-else-if="status=='1'" class="text-white text-xl"><b>Success</b></p>
                                </template>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>


            <!-- If the entity being modified is an Illness, load this table view -->
            <div v-if="entity_type == 'illness'" class="flex flex-col items-center ml-auto mr-auto pt-24 mt-3 mb-4">
                <table class="w-full md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg">
                    <thead>
                        <tr>
                            <th v-if="create_mode" class="text-lg text-white text-2xl w-full bg-blue-500 rounded-t-2xl border-teal border-b-2 border-r-2" colspan="2"> 
                                <b>Add new {{ entity_type }}</b>
                            </th>
                            <th v-else class="text-lg text-white text-2xl w-full bg-blue-500 rounded-t-2xl border-teal border-b-2 border-r-2" colspan="2"> 
                                <b>Modify {{ entity_type }}</b>
                            </th>
                        </tr>
                    </thead>
                    <tbody>
                        <tr class="bg-blue-100">
                            <td class="border-blue-300 border-2 py-3">
                                <b>Name of {{ entity_type }}:</b>
                            </td>
                            <td v-if="create_mode == true" class="border-blue-300 border-2 py-2">
                                <input
                                    class="border border-black mb-1 mt-1 p-1 rounded-lg"
                                    type="text"
                                    name="entity_name"
                                    placeholder="Name"
                                    v-model="entity_name"/>
                            </td>
                            <td v-else class="border-blue-300 border-2 py-2">
                                <input
                                    class="border border-black text-gray-400 mb-1 mt-2 p-1 rounded-lg"
                                    type="text"
                                    name="entity_name"
                                    placeholder="entity_name"
                                    v-model="entity_name"
                                    readonly/>
                            </td>
                        </tr>
                        <tr class="bg-blue-100">
                            <td class="border-blue-300 border-2 py-3">
                                <label class="mr-3" for="select"><b>Organ System:</b></label>
                            </td>
                            <td class="border-blue-300 border-2 py-1">
                                <select class="bg-blue-400 text-white rounded-md py-1 px-10"
                                        id="select"
                                        v-model="organ_system">

                                    <option name="none" value="None"><i>None</i></option>
                                    <option name="resp" value="Respiratory">Respiratory</option>
                                    <option name="card" value="Cardiovascular">Cardiovascular</option>
                                    <option name="psych" value="Psychiatric">Psychiatric</option>
                                    <option name="gas" value="Gastrointestinal">Gastrointestinal</option>
                                    <option name="endo" value="Endocrine">Endocrine</option>
                                    <option name="skel" value="Skeletal">Respiratory</option>
                                    <option name="musc" value="Muscular">Muscular</option>
                                    <option name="nerv" value="Nervous">Nervous</option>
                                    <option name="skin" value="Integumentary">Integumentary</option>
                                    <option name="lymp" value="Lymphatic">Lymphatic</option>
                                    <option name="urin" value="Urinary">Urinary</option>
                                    <option name="repo" value="Reproductive">Reproductive</option>
                                </select>
                            </td>
                        </tr>
                        <tr class="bg-blue-100">
                            <td class="border-blue-300 border-2 py-4">
                                <label v-if="entity_type == 'illness'" for="effect" class="m-2">
                                    <b>Add Symptom(s)</b> <i class="text-gray-400">(optional)</i>
                                </label>
                                <br />
                                <input
                                    class="border border-black mb-2 mt-2 p-1 rounded-lg"
                                    type="text"
                                    name="effect"
                                    v-model="effect"
                                />
                                <br />
                                <button @click="rm_effect()" class="text-white shadow-lg transition duration-300 ease-in-out bg-pink-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-1 px-4 m-1">
                                    remove
                                </button>
                                <button @click="add_effect()" class="text-white shadow-lg transition duration-300 ease-in-out bg-blue-500 hover:bg-blue-700 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-1 px-4 m-1">
                                    add
                                </button>
                            </td>
                            <td class="border-blue-300 border-2 py-2">
                                <ul class="list-disc text-left pl-5">
                                    <li v-for="(effect, i) in effects" :key="`${i}-${effect}`">
                                        {{ effect }}
                                    </li>
                                </ul>
                            </td>
                        </tr>
                        <tr class=" shadow-2xl">
                            <td class="border-teal-500 border-0 text-pink-300 bg-blue-500 rounded-b-2xl" colspan="3">
                                <button v-if="create_mode"
                                        @click="add_ill()" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-green-500 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                                    <b>Add Illness</b>
                                </button>
                                <button v-else
                                        @click="update_ill()" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-green-500 hover:bg-green-800 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                                    <b>Update Illness</b>
                                </button>
                                <template v-if="sys_msg.length != 0">
                                    <!-- Display error or success, depending on response from server -->
                                    <p v-if="status=='0'" class="text-red-600 text-xl">Error updating {{entity_type}}</p>
                                    <p v-else-if="status=='1'" class="text-white text-xl"><b>Success</b></p>
                                </template>
                            </td>
                        </tr>
                    </tbody>
                </table>
            </div>

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

    data() {
        return {
            logged_in: true,
            organ_system: "None",
            user_type: "",
            query_string: "",
            status: null, // reponse from server: 0 or 1
            sys_msg: "", // Succes or Error message

            entity_type: "", // Medication, illness or symptom
            entity_post: "", //the formatted string to send in POST
            entity_name: "", //name of added entity

            Is_prescription: null,
            Organ_system: null,

            effect: "", // Either a symptom (illness) or side-effect (medication)
            effects: [],

            create_mode: true,
        };
    },

    created() {
        // Get parameters from route, and initialize data()
        this.entity_type = this.$route.params.entity_type;
        this.user_type = this.$route.params.user_type;
        this.create_mode = this.$route.params.create_mode;
        this.entity_name = this.$route.params.entity_name;
        this.query_string = this.$route.params.query_string;
        if (typeof this.entity_type == 'undefined' || typeof this.user_type == 'undefined' ) {
            console.log(this.entity_type);
            this.$router.go(-1);
        }
        if (this.entity_type == 'medication' & !this.create_mode) {
            this.Is_prescription = this.$route.params.is_presc;
            this.effects = this.$route.params.effects;
        }
        else if (this.entity_type == 'illness' && !this.create_mode) {
            this.organ_system = this.$route.params.Organ_system;
            this.effects = this.$route.params.effects;
        }
        this.init_entity();
    },

    methods: {
        
        // Push and Pop effects listed on screen before sending to server
        rm_effect() {
            this.effects.pop(this.effect);
            this.sys_msg = "";
        },
        add_effect() {
            this.effects.push(this.effect);
            this.sys_msg = "";
        },

        add_new() {
            if(!this.check_input()) return;

            if (this.entity_type == 'medication') this.add_med();
            else if (this.entity_type == 'illness') this.add_ill();
        },

        check_input() {
        // Only the input text box for entity name must be non-null
            if (this.entity_name == "") {
                this.sys_msg = "Name is Blank";
                return false;
            }
            else{
                this.sys_msg = "";
                return true;
            }
        },

        add_med() {
            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: this.entity_post,
                    method: "add",
                    med_name: this.entity_name,
                    is_pres: parseInt(this.Is_prescription),
                    effects: this.effects
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            ).then((response) => {
                    this.status = response.data.status;
                })
                .catch((e) => {
                    console.log(e);
                }
            );
        },
        update_med() {
            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: this.entity_post,
                    method: "update",
                    med_name: this.entity_name,
                    is_pres: this.Is_prescription,
                    effects: this.effects
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            ).then((response) => {
                    this.status = response.data.status;
                    this.sys_msg = response.data.sys_msg;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        add_ill() {
            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: this.entity_post,
                    method: "add",
                    ill_name: this.entity_name,
                    org_sys: this.organ_system,
                    effects: this.effects
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            ).then((response) => {
                    this.status = response.data.status;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
        update_ill() {
            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: this.entity_post,
                    method: "update",
                    ill_name: this.entity_name,
                    org_sys: this.organ_system,
                    effects: this.effects
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            ).then((response) => {
                    this.status = response.data.status;
                    this.sys_msg = response.data.sys_msg;
                })
                .catch((e) => {
                    console.log(e);
                });
        },

        init_entity() {
            if (this.entity_type == "medication") {
                this.entity_attr = "Side Effects";
                this.entity_post = "medication";
            }
            else if (this.entity_type == "illness") {
                this.entity_attr = "Organ Type and Symptoms";
                this.entity_post = "illness";
            }
            else {
                this.entity_attr = "Illness";
                this.entity_post = "symptom";
            }
            
        },
    },
};
</script>