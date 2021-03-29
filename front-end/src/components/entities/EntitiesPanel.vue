<template>
    <div id="Entities_forms">
        <button @click="$router.go(-1)" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
            <span >Back</span>
        </button>
        <!-- Parameter will specify which Entity form DIVS to load between med, illness, and symptoms-->
        <!-- STARTING WITH MEDICATION DIV FORMS -->
        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-24">{{ entity_type }}</p>
                <div class="w-1/2">
                    <table class="table-fixed w-full mb-10">
                        <thead>
                            <tr>
                                <th class="width: 75% border-black border-2">
                                    Search {{ entity_type }}: 
                                    <input
                                        class="border border-black mb-2 mt-2 p-1 rounded-lg"
                                        type="text"
                                        name="entity_name"
                                        v-model="form.entity_name"
                                        v-on:keyup="search_entities()"
                                    />
                                </th>
                                <th class="width: 0%">
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
                                   <b>Side Effects</b>
                                </td>
                                <td class="border-black border-2">
                                </td>
                            </tr>
                            <tr v-for="entity in entity_list" :key="entity">
                                <td class="border-black border-2">
                                    {{ entity.Name }}
                                </td>
                                <td class="border-black border-2">
                                    {{ entity.Effect}}
                                </td>
                                <td class="border-black border-2">
                                <!-- to change -->
                                    <router-link
                                        :to="{
                                            name: 'view-reports',
                                            params: { id: entity_list.Name },
                                        }"
                                    >
                                        <div
                                            class="text-white my-2 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-blue-600 rounded-lg py-2 px-1 mx-6 my-1"
                                        >
                                            Edit
                                        </div>
                                    </router-link>
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
            form: {
                entity_name: "" 
            }
        };
    },

    created() {
        this.entity_type = this.$route.params.entity_type;
    },

    methods: {
        search_entities() {

            let e_type = "";
            if (this.entity_type == "Medications") e_type = "medication";
            else e_type = "illness";

            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: e_type,
                    method: "query",
                    query_string: this.form.entity_name
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