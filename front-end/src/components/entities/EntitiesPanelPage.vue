<template>
    <div id="Entities_forms">
        <div v-if="user_type == 'doctor'" class="flex justify-end w-full fixed">
            <router-link to="/doctor-panel">
                <div class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                    Back
                </div>
            </router-link>
        </div>
        <div v-else-if="user_type == 'clerk'" class="flex justify-end w-full fixed">
            <router-link to="/clerk-panel">
                <div class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                    Back
                </div>
            </router-link>
        </div>


        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-24">{{ entity_type }}</p>
                <div class="w-3/4">
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="width: 75% border-black border-2">
                                    Search {{ entity_type }}: 
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg"
                                        type="text"
                                        name="entity_name"
                                        v-model="entity_name"
                                        v-on:keyup="search_entities()"
                                    />
                                </th>
                                <!-- include "add new" button only for med and ill -->
                                <th v-if="entity_type == 'medication' || entity_type == 'illness'" 
                                class="width: 25% border-black border-2">
                                    <router-link :to="{name: 'add-new-entity',params: { entity_type: entity_type, user_type:user_type }}"
                                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-green-700 hover:bg-green-500 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                                        <span >Add New {{entity_type}}</span>
                                    </router-link>
                                </th>
                                <th v-else></th>
                                
                                <th class="width: 25% border-black border-2">
                                    <p class="text-3xl mb-4">Modify</p>
                                </th>
                            </tr>
                        </thead>


                        <tbody>
                            <tr>
                                <td class="border-black border-2">
                                    <b>Name</b>
                                </td>
                                <td class="border-black border-2">
                                    <b>{{entity_attr}}</b>
                                </td>
                                <td class="border-black border-2">
                                    <b></b>
                                </td>
                            </tr>
                            
                            <tr v-for="entity in entity_list" :key="entity">

                                <!-- Medications -->
                                <template v-if="entity_type == 'medication'">
                                    <td class="border-black border-2">
                                        {{entity.Name}}
                                    </td>
                                    <td class="border-black border-2">
                                        <ul class="list-disc text-left pl-5">
                                            <li v-for="effect in entity.Effects" :key="effect">
                                                {{ effect }}
                                            </li>
                                        </ul>
                                    </td>
                                </template>

                                <!-- Illnesses -->
                                <template v-else-if="entity_type == 'illness'">
                                    <td class="border-black border-2">
                                        {{entity.Name}}
                                    </td>
                                    <td class="border-black border-2">
                                    {{entity.Organ_system}}
                                        <ul class="list-disc text-left pl-5">
                                            <li v-for="effect in entity.Effects" :key="effect">
                                                {{ effect }}
                                            </li>
                                        </ul>
                                    </td>
                                </template>

                                <!-- Symptoms -->
                                <template v-else-if="entity_type == 'symptom'">
                                    <td class="border-black border-2">
                                        {{entity.Symptom_name}}
                                    </td>
                                    <td class="border-black border-2">
                                        {{entity.Illness_name}}
                                    </td>
                                </template>

                                <td class="border-black border-2">
                                    <button @click="$router.go(-1)" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-blue-600 hover:bg-yellow-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                                        <span >Edit</span>
                                    </button>
                                </td>

                        
                                
                            </tr>
                        </tbody>
                    </table>
                </div>
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
    name: "EntitiesPanelPage",

    data() {
        return {
            logged_in: true,
            entity_type: "", // Medication, illness or symptom
            entity_post: "", //the formatted string to send in POST
            entity_list: [],
            entity_name: "", //name of tuple/row
            entity_attr: "", //attribute specific to that entity

            user_type:"",
        };
    },

    created() {
        this.entity_type = this.$route.params.entity_type;
        this.user_type = this.$route.params.user_type;
        this.init_entity();
    },

    methods: {
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


        search_entities() {
            axios.post("entities/forms",
                {
                    entity_type: this.entity_post,
                    method: "query",
                    query_string: this.entity_name
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            )
            .then((response) => {
                    if (response.data.logged_in != "1") return;

                    this.logged_in = true;
                    this.entity_list = response.data.results;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>