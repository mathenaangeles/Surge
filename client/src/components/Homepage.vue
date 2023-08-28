<template>
  <div class="main-wrapper container-fluid">
  <div class="main row">
    <div class="landing my-auto">
      <div class="landing-text-group">
      <img src="@/assets/img/chat.png" height="100">
      <p style="font-family: 'ShillingM';font-size: 50px;">Hello, U!</p>
      <p style="margin-top:-10px; line-height: 20px;">Need some help getting started? <br> Here are some questions you can ask:</p>
      </div>
      <div class="row suggested-group mx-auto">
      <div class="col">
        <div class="suggested">Suggested Question 1</div>
        <div class="suggested mt-2">Suggestion Question 2</div>
      </div>
      <div class="col">
        <div class="suggested">Suggested Question 3</div>
        <div class="suggested mt-2">Suggestion Question 4</div>
      </div>
      </div>
    </div>
  </div>
  </div>
</template>

<script>
export default {
  name: 'Homepage'
}
</script>
