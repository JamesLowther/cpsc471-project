<template>
    <div id="Entities_forms">
        <button @click="$router.go(-1)" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
            <span >Back</span>
        </button>
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
                                <th class="width: 25% border-black border-2">
                                    <button class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-green-700 hover:bg-green-500 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
                                        <span >Add New {{entity_type}}</span>
                                    </button>
                                </th>
                                
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
                                <template v-if="entity_type == 'Medications'">
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
                                <template v-else-if="entity_type == 'Illnesses'">
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
                                <template v-else-if="entity_type == 'Symptoms'">
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
    name: "EntitiesPanel",

    data() {
        return {
            logged_in: true,
            entity_type: "",
            entity_list: [],
            entity_name: "",
            entity_attr: ""
        };
    },

    created() {
        this.entity_type = this.$route.params.entity_type;

        if (this.entity_type == "Medications") this.entity_attr = "Side Effects";
        else if (this.entity_type == "Illnesses") this.entity_attr = "Organ Type and Symptoms";
        else this.entity_attr = "Illness";
    },

    methods: {
        search_entities() {

            // POST either medication, illness or symptom
            let e_type = "";
            if (this.entity_type == "Medications") e_type = "medication";
            else if (this.entity_type == "Illnesses") e_type = "illness";
            else e_type = "symptom";

            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: e_type,
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