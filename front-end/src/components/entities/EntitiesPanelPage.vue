<template>
    <div id="Entities_forms">
        <div v-if="user_type == 'doctor'" class="flex justify-end w-full fixed">
            <router-link to="/doctor-panel">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>
        <div
            v-else-if="user_type == 'clerk'"
            class="flex justify-end w-full fixed"
        >
            <router-link to="/clerk-panel">
                <div
                    class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                >
                    Back
                </div>
            </router-link>
        </div>

        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 md-10">Update {{ title }}</p>
                <div class="flex flex-col items-center pt-10 w-full mt-10 mb-4">
                    <table
                        class="w-full ml-auto md: mr-auto md:w-3/4 2xl:w-1/2 mb-3 rounded-b-none shadow-lg"
                    >
                        <thead>
                            <tr>
                                <th
                                    class="text-lg text-black bg-blue-500 rounded-tl-2xl border-teal border-b-2 border-r-2 px-4"
                                    colspan="3"
                                >
                                    <input
                                        class="border border-blue-700 mb-2 mt-2 p-1 rounded-lg"
                                        type="text"
                                        placeholder="Search"
                                        name="entity_name"
                                        v-model="entity_name"
                                        v-on:keyup="search_entities()"
                                    />
                                </th>
                                <th
                                    class="text-lg text-white w-1/12 bg-blue-500 rounded-tr-2xl border-teal border-b-2 border-l-2"
                                >
                                    <router-link
                                        :to="{
                                            name: 'add-new-entity',
                                            params: {
                                                entity_type: entity_type,
                                                user_type: user_type,
                                                create_mode: true,
                                                query_string: query_string,
                                            },
                                        }"
                                        class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-green-700 hover:bg-green-500 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6"
                                    >
                                        <span>Add</span>
                                    </router-link>
                                </th>
                            </tr>
                        </thead>

                        <tbody>
                            <tr>
                                <td
                                    class="border-teal border-2 bg-blue-500 text-white"
                                >
                                    <b>Name</b>
                                </td>
                                <!-- Medications -->
                                <template v-if="entity_type == 'medication'">
                                    <td
                                        class="border-teal border-2 bg-blue-500 text-white"
                                    >
                                        <b>Prescr.</b>
                                    </td>
                                    <td
                                        class="border-teal border-2 bg-blue-500 text-white"
                                    >
                                        <b>Side Effects</b>
                                    </td>
                                </template>
                                <!-- Illnesses -->
                                <template v-if="entity_type == 'illness'">
                                    <td
                                        class="border-teal border-2 bg-blue-500 text-white"
                                    >
                                        <b>System</b>
                                    </td>
                                    <td
                                        class="border-teal border-2 bg-blue-500 text-white"
                                    >
                                        <b>Symptoms</b>
                                    </td>
                                </template>
                                <!-- Symptoms -->
                                <template v-if="entity_type == 'symptom'">
                                    <td
                                        class="border-teal border-2 bg-blue-500 text-white"
                                        colspan="2"
                                    >
                                        <b>Illnesses</b>
                                    </td>
                                </template>
                                <td
                                    class="border-teal border-2 bg-blue-500 text-white"
                                >
                                    <b></b>
                                </td>
                            </tr>

                            <tr
                                class="bg-blue-100"
                                v-for="(entity, i) in entity_list"
                                :key="`${i}-${entity}`"
                            >
                                <!-- Medications -->
                                <template v-if="entity_type == 'medication'">
                                    <td class="border-blue-400 border-2">
                                        {{ entity.Name }}
                                    </td>
                                    <td
                                        v-if="entity.Is_prescription == 1"
                                        class="border-teal-500 border-2 bg-green-300"
                                    >
                                        YES
                                    </td>
                                    <td
                                        v-else
                                        class="border-teal-300 border-2 bg-red-300"
                                    >
                                        NO
                                    </td>
                                    <td class="border-blue-400 border-2">
                                        <ul class="list-disc text-left pl-5">
                                            <li
                                                v-for="(
                                                    effect, i
                                                ) in entity.Effects"
                                                :key="`${i}-${effect}`"
                                            >
                                                {{ effect }}
                                            </li>
                                        </ul>
                                    </td>
                                </template>

                                <!-- Illnesses -->
                                <template v-else-if="entity_type == 'illness'">
                                    <td class="border-blue-400 border-2">
                                        {{ entity.Name }}
                                    </td>
                                    <td class="border-blue-400 border-2">
                                        {{ entity.Organ_system }}
                                    </td>
                                    <td class="border-blue-400 border-2">
                                        <ul class="list-disc text-left pl-5">
                                            <li
                                                v-for="(
                                                    effect, i
                                                ) in entity.Effects"
                                                :key="`${i}-${effect}`"
                                            >
                                                {{ effect }}
                                            </li>
                                        </ul>
                                    </td>
                                </template>

                                <!-- Symptoms -->
                                <template v-else-if="entity_type == 'symptom'">
                                    <td class="border-blue-400 border-2">
                                        {{ entity.Symptom_name }}
                                    </td>
                                    <td
                                        class="border-blue-400 border-2"
                                        colspan="2"
                                    >
                                        <ul class="list-disc text-left pl-5">
                                            <li
                                                v-for="(
                                                    effect, i
                                                ) in entity.Effects"
                                                :key="`${i}-${effect}`"
                                            >
                                                {{ effect }}
                                            </li>
                                        </ul>
                                    </td>
                                </template>

                                <td class="border-blue-400 border-2 p-2">
                                    <router-link
                                        :to="{
                                            name: 'add-new-entity',
                                            params: {
                                                entity_type: entity_type,
                                                user_type: user_type,
                                                create_mode: false,
                                                entity_name: entity.Name,
                                                Organ_system:
                                                    entity.Organ_system,
                                                is_presc:
                                                    entity.Is_prescription,
                                                effects: entity.Effects,
                                                query_string: query_string,
                                            },
                                        }"
                                        class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-blue-600 hover:bg-yellow-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-1 px-4 m-6"
                                    >
                                        <span>Edit</span>
                                    </router-link>
                                </td>
                            </tr>
                            <tr class="shadow-2xl">
                                <td
                                    class="border-teal-500 border-0 text-white bg-blue-500 rounded-b-2xl h-7"
                                    colspan="4"
                                />
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
            title: "",
            query_string: "",

            user_type: "",
        };
    },

    created() {
        this.entity_type = this.$route.params.entity_type;
        this.user_type = this.$route.params.user_type;
        this.entity_name = this.$route.params.query_string;
        if (
            typeof this.entity_type == "undefined" ||
            typeof this.user_type == "undefined"
        ) {
            this.$router.go(-1);
        }
        this.init_entity();
        this.search_entities();
    },

    methods: {
        init_entity() {
            if (this.entity_type == "medication") {
                this.entity_attr = "Side Effects";
                this.entity_post = "medication";
                this.title = "Medications";
            } else if (this.entity_type == "illness") {
                this.entity_attr = "Organ Type and Symptoms";
                this.entity_post = "illness";
                this.title = "Illnesses";
            } else {
                this.entity_attr = "Illness";
                this.entity_post = "symptom";
                this.title = "Symptoms";
            }
        },

        search_entities() {
            this.query_string = this.entity_name;
            axios
                .post(
                    "entities/forms",
                    {
                        entity_type: this.entity_post,
                        method: "query",
                        query_string: this.entity_name,
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
                    this.entity_list = response.data.results;
                })
                .catch((e) => {
                    console.log(e);
                });
        },
    },
};
</script>