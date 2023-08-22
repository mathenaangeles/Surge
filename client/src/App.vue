<template>
  <!-- NAVIGATION BAR -->
  <nav class="navbar navbar-expand-lg navbar-dark u-navbar">
    <div class="container-fluid">
      <img src="@/assets/img/logo.png" height="40" style="padding:5px">
    </div>
  </nav>
  <!-- AT A GLANCE BUTTON -->
  <div style = "display: flex; justify-content:flex-end;">
    <button class="vis-button"><p>At A Glance</p></button>
  </div>
  <!-- PROMPT AREA -->
  <div class="prompt-area fixed-bottom">
    <div class="mt-3 container-lg prompt-bar p-2">
      <form>
        <div class="d-flex flex-row">
          <div class="custom-dropdown">
            <select class="form-select text-light">
              <option selected value="General">General</option>
              <option value="Financials">Financials</option>
              <option value="Technology">Technology</option>
              <option value="Sustainability">Sustainability</option>
              <option value="R&D">R&D</option>
              <option value="MAStrategy">M&A, Strategy</option>
            </select>
          </div>
          <div class="custom-promptbox">
            <input type="text" class="form-control" id="prompt" placeholder="What do you want to know?">
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
  <Homepage/>
</template>

<script>
import Homepage from './components/Homepage.vue'

export default {
  name: 'App',
  components: {
    Homepage
  }
}
</script>

<style>
  @import './assets/style.css';
</style>
