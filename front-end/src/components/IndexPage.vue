<template>
    <div id="index">
        <div class="flex flex-col h-screen">
            <div class="flex w-full justify-end opacity-25">
                <button
                    v-if="creepy_mode"
                    @click="creepy_mode = false"
                    class="text-sm w-16 border border-yellow-200 bg-yellow-200 hover:bg-transparent text-white hover:text-gray-300 m-4 rounded-lg"
                >
                    Creepy Mode
                </button>
                <button
                    v-else
                    @click="creepy_mode = true"
                    class="text-sm w-16 border border-yellow-200 hover:bg-yellow-200 text-gray-300 hover:text-white m-4 rounded-lg"
                >
                    Creepy Mode
                </button>
            </div>
            <p class="text-4xl lg:text-5xl mt-20 mb-12">
                Remote Patient - Doctor Symptom Analyser
            </p>
            <div v-if="creepy_mode" class="bg-rose-300 mb-10">
                <img
                    class="object-contain md:object-scale-down h-96 w-full ..."
                    src="@/assets/aamc_doctors_trace.jpeg"
                />
            </div>
            <div
                class="flex flex-row w-full justify-around items-center text-white h-full text-2xl lg:text-3xl"
            >
                <router-link class="w-4/12" to="login">
                    <div
                        class="shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-8 px-1"
                    >
                        Login
                    </div>
                </router-link>
                <router-link class="w-4/12" to="new-account">
                    <div
                        class="shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg py-8 px-1"
                    >
                        Register
                    </div>
                </router-link>
            </div>
            <p class="text-2xl mt-20 mb-10">
                CPSC 471 - Database Management Systems
                <br />Winter 2021 March 25
                <br />
                <br />TA: Abdelghani Guerbas
                <br />
                <br />Group No. 13
                <br />
                <br />James Lowther <br />Logan Perry-Din <br />Brody Wells
            </p>
            <div class="opacity-75">
                Icons made by
                <a
                    href="https://www.flaticon.com/authors/vectors-market"
                    title="Vectors Market"
                    >Vectors Market</a
                >
                from
                <a href="https://www.flaticon.com/" title="Flaticon"
                    >www.flaticon.com</a
                >
            </div>
        </div>
    </div>
</template>

<script>
export default {
    name: "IndexPage",
    data() {
        return {
            creepy_mode: false
        };
    }
};
</script>
