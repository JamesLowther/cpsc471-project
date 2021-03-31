<template>
    <div id="Entities_forms">
        <button @click="$router.go(-1)" class="text-white mt-5 shadow-lg transition duration-300 ease-in-out bg-gray-700 hover:bg-red-600 transform hover:-translate-y-1 hover:scale-110 rounded-lg py-2 px-8 m-6">
            <span >Back</span>
        </button>
        <div v-if="logged_in">
            <div class="flex flex-col items-center">
                <p class="text-5xl mt-20 mb-24">Add New {{ entity_type }}</p>
                <div class="w-3/4">
                    main content
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

    data() {
        return {
            logged_in: true,
            entity_type: "", // Medication, illness or symptom
            entity_post: "", //the formatted string to send in POST
            entity_name: "", //name of tuple/row
        };
    },

    created() {
        this.entity_type = this.$route.params.entity_type;
        this.init_entity();
    },

    methods: {

        add_new() {
            axios.post(`http://localhost:5000/entities/forms`,
                {
                    entity_type: this.entity_post,
                    method: "add",
                    med_name: "test",
                },
                {
                    headers: {
                        Authorization: "Bearer " + localStorage.getItem("jwt"),
                    },
                }
            );
            


        },

        init_entity() {
            if (this.entity_type == "Medications") {
                this.entity_attr = "Side Effects";
                this.entity_post = "medication";
            }
            else if (this.entity_type == "Illnesses") {
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