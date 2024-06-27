import Main from "@/pages/Main.vue";
import { createWebHistory, createRouter } from "vue-router";
import control from "@/control.js";

function denyIfUnauthenticated() {
    if (!control.check_auth())
        return "/login";
}

const routes = [
    {
        path: "/",
        name: "Main",
        component: Main,
    },
    {
        path: "/error",
        name: "Error",
        component: () =>
            import ("@/pages/404.vue"),
    },
    {
        path: "/login",
        name: "Login",
        component: () =>
            import ("@/pages/login.vue"),
    },
    {
        path: "/reg",
        name: "Registaration",
        component: () =>
            import ("@/pages/reg.vue"),
    },
    {
        path: "/crm",
        name: "Crm",
        component: () =>
            import ("@/pages/crm.vue"),
    },
];

const router = new createRouter({
    history: createWebHistory(),
    routes,
});

export default router;