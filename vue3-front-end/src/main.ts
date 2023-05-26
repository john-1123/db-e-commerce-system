import { createApp } from "vue";
import App from "./App.vue";
import { registerLayouts } from "./layouts/register";
import vuetify from "./plugins/vuetify";
import router from "./router";
import "./style.css";
import { authStore } from "./store/auth.store";

const app = createApp(App);

app.use(authStore);
app.use(router);

registerLayouts(app);

app.use(vuetify);
app.mount("#app");
