<template>
    <div class="main-wrapper h-100">
      <div class="area-containers mx-5 question-area">
        <span style="font-family: 'ShillingM';">Question: </span><br>
        <!--SAMPLE QUESTION: COMPLEX-->
        <span>I am looking for a comprehensive analysis of Unilever's sales 
          performance from 2015 to 2019. Please provide the following information:
          1. Yearly sales figures for Unilever from 2015 to 2019.
          2. A brief analysis of Unilever's sales growth during this period.
          3. Yearly sales figures for Procter & Gamble (P&G) from 2015 to 2019.
          4. A brief analysis of P&G's sales growth during this period.
          5. A comparison of Unilever's and P&G's sales growth and performance from 2015 to 2019.
          6. Any notable factors or events that influenced the sales growth of both companies during this period. Please provide the information in a clear and concise manner, using bullet points and tables where appropriate.
        </span>
      </div>
      <div class="area-containers mx-5 p-4 answer-area" style="margin-bottom: 50px;">
        <div>
          <span style="font-family: 'ShillingM'; font-size: 14px;">Source/s</span> <br>
          <div class="source-list">
            <span class="source">
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              Unilever_2012_Annual_Report-25.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              Unilever_2012_Annual_Report-23.pdf 
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              Procter&Gamble_2015_AnnualReport-23.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              Unilever_2019_Annual_Report-23.pdf 
            </span>
          </div>
        </div>
        <div class="mt-4">
          <VueWriter :array="arr1" :typeSpeed="10" :iterations='1'/>
          <div style="margin-left: 18px;">
          <VueWriter :array="arr2" :typeSpeed="10" :iterations='1' :start="500"/>
          <VueWriter :array="arr3" :typeSpeed="10" :iterations='1' :start="1000"/>
          <VueWriter :array="arr4" :typeSpeed="10" :iterations='1' :start="1500"/>
          <VueWriter :array="arr5" :typeSpeed="10" :iterations='1' :start="2000"/>
          <VueWriter :array="arr5" :typeSpeed="10" :iterations='1' :start="2500"/>
          <VueWriter :array="arr6" :typeSpeed="10" :iterations='1' :start="3000"/>
          </div>
          <br>
          <VueWriter :array="arr7" :typeSpeed="10" :iterations='1' :start="3500"/>
          <div style="margin-left: 18px;">
          <VueWriter :array="arr8" :typeSpeed="10" :iterations='1' :start="4000"/>
          </div>
          <br>
          <VueWriter :array="arr9" :typeSpeed="10" :iterations='1' :start="5000"/>
          <div style="margin-left: 18px;">
          <VueWriter :array="arr10" :typeSpeed="10" :iterations='1' :start="5500"/>
          <VueWriter :array="arr11" :typeSpeed="10" :iterations='1' :start="6000"/>
          <VueWriter :array="arr12" :typeSpeed="10" :iterations='1' :start="6500"/>
          <VueWriter :array="arr13" :typeSpeed="10" :iterations='1' :start="7000"/>
          <VueWriter :array="arr14" :typeSpeed="10" :iterations='1' :start="7500"/>
          </div>
          <br>
          <VueWriter :array="arr15" :typeSpeed="10" :iterations='1' :start="8000"/>
          <div style="margin-left: 18px;">
          <VueWriter :array="arr16" :typeSpeed="10" :iterations='1' :start="9000"/>
          </div>
          <br>
          <VueWriter :array="arr17" :typeSpeed="10" :iterations='1' :start="10000"/>
          <div style="margin-left: 18px;">
          <VueWriter :array="arr18" :typeSpeed="10" :iterations='1' :start="11000"/>
          </div>
          <br>
          <VueWriter :array="arr19" :typeSpeed="10" :iterations='1' :start="14000"/>
          <div style="margin-left: 18px;">
          <VueWriter :array="arr20" :typeSpeed="10" :iterations='1' :start="15000"/>
          </div>
          <br><br>
          <hr/>
          <br>
          <img src="@/assets/img/lightbulb.png" height="50">
          <span class="related-header">You might want to explore...</span><br>
          <div class="row">
            <span class="related-q">What were the major currency fluctuations and economic/political uncertainties that affected Unilever's sales growth during this period?</span>
            <span class="related-q">What were the major changes in consumer preferences and behaviors that affected Unilever's and P&G's sales growth during this period?</span>
            <span class="related-q">What strategies did Unilever and P&G implement to address the factors that affected their sales growth during this period?</span>
          </div>
          <br>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Answerpage',
  data(){
    const arr1 = ["1. Yearly sales figures for Unilever from 2015 to 2019:"];
    const arr2 = ["- 2015: €53.3 billion [Unilever_2019_Annual_Report-25.pdf]"];
    const arr3 = ["- 2016: €52.7 billion [Unilever_2019_Annual_Report-25.pdf]"];
    const arr4 = ["- 2017: €53.7 billion [Unilever_2019_Annual_Report-25.pdf]"];
    const arr5 = ["- 2018: €50.9 billion [Unilever_2019_Annual_Report-25.pdf]"];
    const arr6 = ["- 2019: €52.0 billion [Unilever_2019_Annual_Report-25.pdf]"];

    const arr7 = ["2. A brief analysis of Unilever's sales growth during this period:"];
    const arr8 = ["- Unilever's sales showed a fluctuating trend from 2015 to 2019, with a peak in 2017 and a dip in 2019."];
   
    const arr9 = ["3. Yearly sales figures for Procter & Gamble (P&G) from 2015 to 2019:"];
    const arr10 = ["- 2015: €76.3 billion [Procter&Gamble_2015_AnnualReport-23.pdf]"];
    const arr11 = ["- 2016: €65.3 billion [Procter&Gamble_2015_AnnualReport-23.pdf]"];
    const arr12 = ["- 2017: €65.1 billion [Procter&Gamble_2015_AnnualReport-23.pdf]"];
    const arr13 = ["- 2018: €66.8 billion [Procter&Gamble_2015_AnnualReport-23.pdf]"];
    const arr14 = ["- 2019: €67.7 billion [Procter&Gamble_2015_AnnualReport-23.pdf]"];

    const arr15 = ["4. A brief analysis of P&G's sales growth during this period: "];
    const arr16 = ["- P&G's sales showed a declining trend from 2015 to 2016, followed by a slight increase in 2017 and a further increase in 2018 and 2019."];
    
    const arr17 = ["5. A comparison of Unilever's and P&G's sales growth and performance from 2015 to 2019:"];
    const arr18 = ["- Unilever's sales showed a fluctuating trend, with a peak in 2017 and a dip in 2018, while P&G's sales showed a declining trend in 2015 to 2016, followed by a slight increase in 2017 and a further increase in 2018 and 2019."];
   
    const arr19 = ["6. Any notable factors or events that influenced the sales growth of both companies during this period:"];
    const arr20 = ["The sources do not provide information on notable factors or events that influenced the sales growth of both companies during this period."];
    return { arr1, arr2, arr3, arr4, arr5, arr6, arr7, arr8, arr9, arr10, arr11, arr12, arr13, arr14, arr15, arr16, arr17, arr18, arr19, arr20 }
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