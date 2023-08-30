<template>
    <div class="visual-modal">
        <div class="row h-100">
            <div class="col vis-button-modal">
                <button @click="() => toggleModal()" class="vis-button"><p>At A Glance</p></button>
            </div>
            <div class="col-11 p-3" style="background-color: #FF544F;">
                <button @click="toggleModal()" type="button" class="close close-btn"><span aria-hidden="true">&times;</span></button>
                <div class="modal-inner">
                    <slot />
                </div>
            </div>
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
    background-color: transparent;
    position: absolute;
    margin-top: 50px;
    height: 75%;
    width: 95%;
    z-index: 99;
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
.vis-button-modal{
    position: relative;
}

.vis-button{
    background-color: #FF544F;
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    border-top-right-radius: 0px;
    border-bottom-right-radius: 0px;
    border-color: transparent;
    color: white;
    font-family: 'ShillingM';
    font-size: 20px;
    height:120px;
    width: 90px;
    right: 0;
    margin-top: 0px;
    line-height: 22px;
    padding-top: 10px;
}


</style>