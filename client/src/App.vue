<template>
  <div>
  <!-- NAVIGATION BAR -->
  <nav class="navbar navbar-expand-lg navbar-dark u-navbar">
    <div class="container-fluid">
      <router-link :to="{ path: '/' }">
        <img src="@/assets/img/logo.png" height="40" style="padding:5px">
      </router-link>
    </div>
  </nav>
  <div style = "display: flex; justify-content:flex-end;">
  <!--VISUALIZATION MODAL-->
  <Modal v-if="modalActive" :toggleModal= "() => toggleModal()">
    <div v-if="area == 'General'" class="d-flex align-items-center h-100 w-100">
      <img src="@/assets/img/visualizations/general.png" style="object-fit:cover;width:100%">
    </div>
    <div v-if="area == 'Financials'" class="d-flex align-items-center h-100 w-100">
      <img src="@/assets/img/visualizations/financials.png" style="object-fit:cover;width:100%">
    </div>
    <div v-if="area == 'E-Commerce'" class="d-flex align-items-center h-100 w-100">
      <img src="@/assets/img/visualizations/e-commerce.png" style="object-fit:cover;width:100%">
    </div>
    <div v-if="area == 'Sustainability'" class="d-flex align-items-center h-100 w-100">
      <img src="@/assets/img/visualizations/sustainability.png" style="object-fit:cover;width:100%">
    </div>
    <div v-if="area == 'R&D'" class="d-flex align-items-center h-100 w-100">
      <img src="@/assets/img/visualizations/r&d.png" style="object-fit:cover;width:100%">
    </div>
    <div v-if="area == 'MAStrategy'" class="d-flex align-items-center h-100 w-100">
      <img src="@/assets/img/visualizations/m&a.png" style="object-fit:cover;width:100%">
    </div>
  </Modal>
  </div>
  <!-- AT A GLANCE BUTTON -->
  <div style = "display: flex; justify-content:flex-end;">
    <button @click="() => toggleModal()" class="vis-button"><p>At A Glance</p></button>
  </div>
  <!-- PROMPT AREA -->
  <div class="prompt-area fixed-bottom">
    <div class="mt-3 container-lg prompt-bar p-2">
      <form @submit.prevent="submitForm()">
        <div class="d-flex flex-row">
          <div class="custom-dropdown">
            <select v-model="area" @change="() => closeModal()" class="form-select text-light">
              <option value="General">General</option>
              <option value="Financials">Financials</option>
              <option value="E-Commerce">E-Commerce</option>
              <option value="Sustainability">Sustainability</option>
              <option value="R&D">R&D</option>
              <option value="MAStrategy">M&A, Strategy</option>
            </select>
          </div>
          <div class="custom-promptbox">
            <input v-model="question" @keydown.enter.prevent="fetchAnswer()" type="text" class="form-control" id="prompt" placeholder="What do you want to know?">
            <button type="submit" class="btn btn-warning btn-circle btn-sm">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="bi bi-arrow-up" viewBox="0 0 16 16">
                <path fill-rule="evenodd" d="M8 15a.5.5 0 0 0 .5-.5V2.707l3.146 3.147a.5.5 0 0 0 .708-.708l-4-4a.5.5 0 0 0-.708 0l-4 4a.5.5 0 1 0 .708.708L7.5 2.707V14.5a.5.5 0 0 0 .5.5z"/>
              </svg>
            </button>
          </div>
        </div>
      </form>
    </div>
  </div>
  <!-- TO RENDER HOMEPAGE UPON APP START -->
  <RouterView />
  </div>
</template>

<script>
import { ref } from 'vue';
import Modal from './components/Modal.vue'

export default {
  name: "App",
  components: {
    "Modal": Modal,
  },
  data() {
    return {
        histories: [''],
    }
  },
  setup(){
    const question = ref('');
    const area = ref('General');
    const fetchAnswer = () => {
      // console.log("QUESTION: " + question.value);
      // console.log("AREA: " + area.value);
      question.value = '';
    }
    const modalActive = ref(false);
    const toggleModal = () => {
      modalActive.value = !modalActive.value
    }
    const closeModal = () => {
      modalActive.value = false;
    }
    return { question, area, modalActive, toggleModal, closeModal, fetchAnswer };
  },
  methods: {
    async getData() {
        try {
            const response = await this.$http.get('http://localhost:8000/chatbot/histories/');
            this.histories = response.data; 
        } catch (error) {
            console.log(error);
        }
    },
    async submitForm(){
      try {
        const history = {
          user: this.question,
          bot: ""
        }
        const response = await this.$http.post('http://localhost:8000/chatbot/histories/', {
            conversation: history,
        });
        this.histories.push(response.data);
        this.question = ref('');
      } catch (error) {
        console.log(error);
      }
  }
  },
}
</script>

<style>
  @import './assets/style.css';
</style>
