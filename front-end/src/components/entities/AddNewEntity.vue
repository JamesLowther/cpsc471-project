<template>
    <div id="Entities_forms">
        <router-link :to="{name: 'entities-panel',params: { entity_type: entity_type, user_type: user_type }}">
        <button class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
            <span >Back</span>
        </button>
        </router-link>
        <div v-if="logged_in">
            <div class="flex flex-col items-center ">
                <p class="text-5xl mt-20 mb-24">Add New {{ entity_type }}</p>

                    <!-- Add a new medication, specifying prescription/non -->
                    <template v-if="entity_type == 'medication'" class="m-4">
                        <b class="text-xl">{{ entity_type }} Name</b>
                        <input
                            class="border border-black m-4 p-1 rounded-lg"
                            type="text"
                            name="entity_name"
                            v-model="entity_name"
                        />
                        <div class="flex">
                            <b class="text-lg">Is it a prescription drug?</b>

                            <input type="radio" name="pre-yes" value="1" v-model="Is_prescription" class="mx-2">
                            <label for="pre-yes">Yes</label>

                            <input type="radio" name="pre-no" value="0" v-model="Is_prescription" class="mx-2">
                            <label for="pre-no">No</label>
                        </div>
                        
                    </template>

                    <!-- Add a new illness, choosing an organ system and a set of symptoms -->
                    <template v-if="entity_type == 'illness'">
                        <b class="text-xl">{{ entity_type }} Name</b>
                        <input
                            class="border border-black mb-2 mt-2 p-1 rounded-lg"
                            type="text"
                            name="entity_name"
                            v-model="entity_name"
                        />
                        <div class="flex">
                            <b class="text-lg mx-4">Organ System:</b>
                            <div class="bg-red-200 rounded-lg p-2">
                                <input type="radio" name="resp" value="Respiratory" v-model="Organ_system" class="mx-2">
                                <label for="resp">Respiratory</label>
                            </div>

                            <div class="bg-yellow-200 rounded-lg p-2">
                            <input type="radio" name="card" value="Cardiovascular" v-model="Organ_system" class="mx-2">
                            <label for="card">Cardiovascular</label>
                            </div>       
                            
                            <div class="bg-green-300 rounded-lg p-2">
                            <input type="radio" name="psych" value="Psychiatric" v-model="Organ_system" class="mx-2">
                            <label for="psych">Psychiatric</label>
                            </div>

                            <div class="bg-blue-200 rounded-lg p-2">
                            <input type="radio" name="gas" value="Gastrointestinal" v-model="Organ_system" class="mx-2">
                            <label for="gas">Gastrointestinal</label>
                            </div>

                            <div class="bg-purple-200 rounded-lg p-2">   
                            <input type="radio" name="endo" value="Endocrine" v-model="Organ_system" class="mx-2">
                            <label for="endo">Endocrine</label>
                            </div>

                        </div>
                        
                    </template>

                    
                    <div class="bg-gray-300 rounded-lg p-2 m-4">
                            <input
                                class="border border-black mb-2 mt-2 p-1 rounded-lg"
                                type="text"
                                name="effect"
                                v-model="effect"
                            />
                            <label v-if="entity_type == 'medication'" for="effect" class="m-2">Add Symptom(s) (optional)</label>
                            <label v-if="entity_type == 'illness'" for="effect" class="m-2">Add Symptom(s) (optional)</label>
                            

                            <ul class="list-disc text-left pl-5">
                                <li v-for="effect in effects" :key="effect">
                                    {{ effect }}
                                </li>
                            </ul>
                            <button @click="rm_effect()" class="rounded-lg text-white px-1 mx-4 bg-gray-700">remove</button>
                            <button @click="add_effect()" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                                <span >add</span>
                            </button>
                        </div>

                    <button @click="add_new()" class="text-white text-xl mt-5 shadow-lg transition duration-300 ease-in-out bg-blue-600 hover:bg-green-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                        <span>Submit</span>
                    </button>

                    <b v-if="status=='0'">error</b>
                    <b v-if="status=='1'">success</b>

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
            user_type: "",
            status: null,

            entity_type: "", // Medication, illness or symptom
            entity_post: "", //the formatted string to send in POST
            entity_name: "", //name of added entity

            Is_prescription: null,
            Organ_system: null,

            effect: "", // Either a symptom (illness) or side-effect (medication)
            effects: [],
        };
    },

    created() {
        this.entity_type = this.$route.params.entity_type;
        this.user_type = this.$route.params.user_type;
        this.init_entity();
    },

    methods: {
        
        rm_effect() {this.effects.pop(this.effect);},
        add_effect() {this.effects.push(this.effect);},

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
        add_ill() {
            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: this.entity_post,
                    method: "add",
                    ill_name: this.entity_name,
                    org_sys: this.Organ_system,
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


        add_new() {

            if (this.entity_type == 'medication') this.add_med();
            else if (this.entity_type == 'illness') this.add_ill();
            
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