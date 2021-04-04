import Vue from "vue";
import App from "./App.vue";
import router from "./router";
import axios from "axios";
import "./index.css";

Vue.config.productionTip = false;

axios.defaults.baseURL = process.env.VUE_APP_API_ENDPOINT;

new Vue({
    router,
    render: h => h(App)
}).$mount("#app");
