// Libs
import { createRouter, createWebHistory } from "vue-router";

// Pages
import Home from "@/pages/Home.vue";
import Dashboard from "@/pages/Dashboard.vue";
import Profile from "@/pages/Profile.vue";
import EditJob from "@/pages/EditJob.vue";
import CreateJob from "@/pages/CreateJob.vue";
import Register from "@/pages/Register.vue";
import { getTokenFromLocalStorage } from "../helpers/local-storage";

const routes = [
  {
    path: "/",
    name: "Home",
    component: Home,
  },
  {
    path: "/dashboard",
    name: "Dashboard",
    component: Dashboard,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/profile",
    name: "Profile",
    component: Profile,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/edit/:id",
    name: "EditJob",
    component: EditJob,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/create",
    name: "CreateJob",
    component: CreateJob,
    meta: {
      requiresAuth: true,
    },
  },
  {
    path: "/register",
    name: "Register",
    component: Register,
  },
];

const Router = createRouter({
  history: createWebHistory(),
  routes,
});

Router.beforeEach((to, from, next) => {
  const requiresAuth = to.matched.some((path) => path.meta.requiresAuth);
  const token = getTokenFromLocalStorage();

  // This is a mess, unforunately. ;(

  // If the route doesn't require auth but the
  // user is logged in, redirect to the dashboard
  if (!requiresAuth && token) {
    console.log("PRIMEIRA");
    next({ path: "/dashboard" });
  }
  // If the route requires auth and the user is
  // logged in, continue
  else if (requiresAuth && token) {
    next();
  }
  // If it doesn't requires auth, continue
  else if (!requiresAuth) {
    next();
  }
  // If it doesn't match any of the previous
  // go to the login page
  else {
    next({ path: "/" });
  }
});

export default Router;
