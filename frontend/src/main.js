// Vue
import { createApp } from "vue";

// Toast
import Toast, { POSITION } from "vue-toastification";
import "vue-toastification/dist/index.css";

// App
import App from "./App.vue";
import Router from "./router/Router";
import "./App.css";

const app = createApp(App);

app.use(Router);
app.use(Toast, {
  position: POSITION.BOTTOM_RIGHT,
});

app.mount("#app");
