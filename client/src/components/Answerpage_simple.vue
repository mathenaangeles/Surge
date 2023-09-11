<template>
    <div class="main-wrapper h-100">
      <div class="area-containers mx-5 question-area">
        <span style="font-family: 'ShillingM';">Question: </span><br>
        <!--SAMPLE QUESTION: SIMPLE-->
        <span>
            What were the main drivers of Unilever's sales growth in 2017?
        </span>
        <br><br>
        <button @click="toggleRefined" class="btn btn-warning refined-btn" ref="btnToggle">Show refined question</button>
        <div class="refined-q mt-3" v-show="showRefined">
          Factors driving Unilever sales growth in 2017 OR Main drivers of Unilever's revenue increase in 2017 OR What caused Unilever's sales to grow in 2017? AND Unilever annual report AND competitor analysis
        </div>
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
              [1] Unilever_2017_Annual_Report-19.pdf
            </span>
            <span class="source">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [2] Unilever_2017_Annual_Report-11.pdf
            </span>
          </div>
        </div>
        <div class="mt-4">
          According to the Unilever 2017 Annual Report<sup class="inline-source">[1]</sup>, 
          the main drivers of Unilever's sales growth in 2017 were underlying sales growth of 3.1% and underlying operating margin growth of 110 basis points to 17.5%. 
          Additionally, Unilever increased dividends by 12%, which reflects the company's confidence in future profit growth and cash generation. 
          The Unilever 2017 Annual Report <sup class="inline-source">[2]</sup> also notes that the company's strategy and business model continue to deliver consistent, competitive, profitable, and responsible growth. 
          Between 2009 and 2017, Unilever delivered underlying sales growth of 4.3% per year, while operating margin expanded by 390 basis points to 16.5%.
          <br><br>
          Based on this information, it appears that Unilever's focus on consistent and responsible growth, as well as its ability to increase operating margins, were key drivers of its sales growth in 2017. 
          Additionally, the company's confidence in future profit growth and cash generation, as reflected by its increased dividends, suggests that Unilever is well-positioned for continued growth in the future.
          <br>
          <hr/>
          <br>
          <img src="@/assets/img/lightbulb.png" height="50">
          <span class="related-header">You might want to explore...</span><br>
          <div class="row">
            <router-link :to="{ path: '/' }">
            <button class="btn related-q">What was the percentage change in Unilever's sales from the previous year?</button>
            </router-link>
            <router-link :to="{ path: '/' }">
            <button class="btn related-q">What were the main drivers of Unilever's sales growth in 2019?</button>
            </router-link>
            <router-link :to="{ path: '/' }">
            <button class="btn related-q">How do Unilever's sales compare to its competitors in the industry?</button>
            </router-link>
            <br><br><br><br><br><br>
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
    return { showRefined: false, showSrc: false}
  },
  methods: {
    toggleRefined: function(){
      this.showRefined = !this.showRefined;
      this.$refs.btnToggle.innerText = this.showRefined?'Hide refined question':'Show refined question';
    },
    toggleSources: function(){
      this.showSrc = !this.showSrc;
      this.$refs.srcToggle.innerText = this.showSrc?'Hide':'View more sources';
    }
  }
}
</script>

<style scoped>
#answer-chart{
  padding: 50px;
}

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

.refined-btn{
  font-size: 13px;
}

.refined-q{
  font-size: 13px;
  font-style: italic;
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

.inline-source{
  color:#0070E0;
}

.btn-source{
  font-size: 12px;
  font-style: oblique;
  text-decoration: underline;
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
  text-align: left !important;
}
.related-q:hover{
  background-color: #c4e9f8;
}

</style>