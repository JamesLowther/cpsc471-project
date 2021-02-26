<template>
  <div id="index">
    <div class="flex flex-col h-screen">
      <p class="text-5xl mt-20">Homepage</p>
      <div class="flex flex-row w-full justify-around items-center text-white h-full text-3xl">  
        <router-link class="w-1/6" to="login">
          <div class="shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg px-20 py-10">Login to an account</div>
        </router-link>
        <router-link class="w-1/6" to="new-account">
          <div class="shadow-lg transition duration-300 ease-in-out bg-purple-600 hover:bg-purple-700 transform hover:-translate-y-1 hover:scale-105 rounded-lg px-20 py-10">Create an account</div>
        </router-link>
      </div>
    </div>
  </div>
</template>

<script>

export default {
  name: "IndexPage",
};
</script>