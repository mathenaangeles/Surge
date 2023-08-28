import { createApp } from 'vue'
import { createRouter, createWebHistory } from "vue-router";
import App from './App.vue'
import Homepage from "./components/Homepage.vue"
import Answerpage from "./components/Answerpage.vue"

import "bootstrap/dist/css/bootstrap.min.css";
import "bootstrap";

const routes = [
    { path: '/', component: Homepage },
    { path: '/conversation', component: Answerpage },
]

const router = createRouter({
    history: createWebHistory(),
    routes
})

createApp(App).use(router).mount('#app')
