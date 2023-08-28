<template>
    <div class="visual-modal">
        <button @click="toggleModal()" type="button" class="close close-btn"><span aria-hidden="true">&times;</span></button>
        <div class="modal-inner">
            <slot />
        </div>
    </div>
</template>

<script>
export default {
    props: ['toggleModal']
}
</script>

<style scoped>
.visual-modal{
    background-color: #FF544F;
    position: absolute;
    margin-top: 50px;
    height: 75%;
    width: 90%;
    z-index: 99;
    padding: 15px;
}

.modal-inner{
    background-color: white;
    height: 100%;
    width: 95%;
}

.close-btn{
    margin-top: -20px;
    float: right;
    border: none;
    font-size:40px;
    background-color: transparent;
    color: white;
}


</style>