<template>
    <div class="main-wrapper h-100">
      <div class="area-containers mx-5 question-area">
        <span style="font-family: 'ShillingM';">Question: </span><br>
        <!--SAMPLE QUESTION: SIMPLE-->
        <span>
            What is Unilever's sales in 2019?
        </span>
      </div>
      <div class="area-containers mx-5 p-4 answer-area">
        <div>
          <span style="font-family: 'ShillingM'; font-size: 14px;">Source/s</span> <br>
          <div class="source-list">
            <span class="source">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              Unilever_2019_Annual_Report-25.pdf
            </span>
          </div>
        </div>
        <div class="mt-4">
          <VueWriter :array="arr" :typeSpeed="10" :iterations='1'/>
          <br>
          <hr/>
          <br>
          <img src="@/assets/img/lightbulb.png" height="50">
          <span class="related-header">You might want to explore...</span><br>
          <div class="row">
            <span class="related-q">What was the percentage change in Unilever's sales from the previous year?</span>
            <span class="related-q">What were the main drivers of Unilever's sales growth in 2019?</span>
            <span class="related-q">How do Unilever's sales compare to its competitors in the industry?</span>
          </div>
          <br>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Answerpage_simple',
  data(){
    const arr = ["Unilever's sales in 2019 were €52.0 billion. [Unilever_2019_Annual_Report-25.pdf]"];
    return { arr }
  }
}
</script>

<style scoped>
.area-containers{
  border-radius: 10px;
}
.question-area{
  background-color:aliceblue;
  margin-top: 20px;
  font-size: 16px;
  padding-top: 40px;
  padding-left: 40px;
  padding-bottom: 40px;
  padding-right: 50px;
}

.answer-area{
  margin-top:10px;
  background-color: #F5F5F5;
}

.source{
  background-color: #e4e4e4;
  padding: 10px;
  border-radius: 10px;
  margin-right: 10px;
  margin-top: 5px;
  display: inline-block;
  font-size: 14px;
  color: #0070E0;
  text-decoration: underline;
  font-family: 'ShillingM';
}

.source-icon{
  margin-top: -5px;
  margin-right: 2px;
  color: black;
}

.related-header{
  font-family: 'ShillingM';
  margin-left: 15px;
  font-size: 20px;
}

.related-q{
  background-color: #9bdffd;
  border-radius: 20px;
  padding: 12px;
  padding-left: 18px;
  margin-top: 12px;
  margin-left: 60px;
  width: 75%;
}

</style>