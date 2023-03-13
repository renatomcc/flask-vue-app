import { createRouter, createWebHistory, RouteRecordRaw } from "vue-router";
import Collaborators from "../components/Collaborators.vue";

const routes: Array<RouteRecordRaw> = [
  {
    path: "/",
    name: "Collaborators",
    component: Collaborators,
  },
];

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes,
});

export default router;
