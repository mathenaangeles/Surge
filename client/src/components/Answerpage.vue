<template>
    <div class="main-wrapper h-100">
      <div class="area-containers mx-5 question-area">
        <span style="font-family: 'ShillingM';">Question: </span><br>
        <!--SAMPLE QUESTION: COMPLEX-->
        <span>I am looking for a comprehensive analysis of Unilever's sales performance from 2015 to 2019. 
          Please provide the following information in a chart: Yearly sales figures for Unilever from 2015 to 2019, Yearly sales figures for Procter & Gamble (P&G) from 2015 to 2019. 
          Provide a written analysis comparing Unilever's and P&G's sales growth and performance from 2015 to 2019. 
          Add any notable factors or events that influenced the sales growth of both companies during this period. 
          Recommend actions that Unilever can take to continue to grow its sales. 
          Please provide the information in a clear and concise manner, using bullet points and tables where appropriate.
        </span>
        <br><br>
        <button @click="toggleRefined" class="btn btn-warning refined-btn" ref="btnToggle">Show refined question</button>
        <div class="refined-q mt-3" v-show="showRefined">
          Unilever and P&G sales performance from 2015 to 2019: <br>
          - Yearly sales figures for Unilever and P&G from 2015 to 2019 <br>
          - Comparison of Unilever's and P&G's sales growth and performance from 2015 to 2019 <br>
          - Factors/events that influenced the sales growth of Unilever and P&G from 2015 to 2019 <br>
          - Recommendations for Unilever to continue to grow its sales <br>
          - Analysis presented in clear and concise manner using bullet points and tables (if applicable) <br>
        </div>
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
              [1] Unilever_2015_Annual_Report-78.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [2] Unilever_2016_Annual_Report-53.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [3] Unilever_2017_Annual_Report-45.pdf
            </span>

            <!--TOGGLE MORE REFERENCES-->
            <div v-show="showSrc">
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [4] Unilever_2018_Annual_Report-53.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [5] Unilever_2019_Annual_Report.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [6] P&G_2015_Annual_Report-4.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [7] P&G_2016_Annual_Report-4.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [8] P&G_2017_Annual_Report-4.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [9] P&G_2018_Annual_Report-4.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [10] P&G_2019_Annual_Report-4.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [11] P&G_2019_Annual_Report-29.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [12] Unilever_2015_Annual_Report-73.pdf
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              [13] P&G_2019_Annual_Report-29.pdf
            </span>
            </div>
            <button @click="toggleSources" class="btn btn-source" ref="srcToggle">View more sources</button>
          </div>
        </div>
        <!--CHART-->
        <canvas id="answer-chart"></canvas>
        <!--ANSWER-->
          Yearly sales figures for Unilever from 2015 to 2019: <br>
          <ul>
            <li>2015: €53.3 billion<sup class="inline-source">[1]</sup></li>
            <li>2016: €52.7 billion<sup class="inline-source">[2]</sup></li>
            <li>2017: €53.7 billion<sup class="inline-source">[3]</sup></li>
            <li>2018: €50.9 billion<sup class="inline-source">[4]</sup></li>
            <li>2019: €52.0 billion<sup class="inline-source">[5]</sup></li>
          </ul><br>
          Yearly sales figures for Procter & Gamble (P&G) from 2015 to 2019: <br>
          <ul>
            <li>2015: $76.3 billion<sup class="inline-source">[6]</sup></li>
            <li>2016: $65.3 billion<sup class="inline-source">[7]</sup></li>
            <li>2017: $65.1 billion<sup class="inline-source">[8]</sup></li>
            <li>2018: $66.8 billion<sup class="inline-source">[9]</sup></li>
            <li>2019: $67.7 billion<sup class="inline-source">[10]</sup></li>
          </ul><br>
            Comparing Unilever's and P&G's sales growth and performance from 2015 to 2019: <br>
            <ul>
            <li>Unilever's sales figures fluctuated during this period, with a peak in 2017 and a dip in 2018, while P&G's sales figures remained relatively stable.</li>
            <li>Unilever's sales figures in 2019 were slightly higher than in 2015, while P&G's sales figures in 2019 were higher than in 2015 but lower than in 2016 and 2017.</li>
            <li>Unilever's underlying sales growth during this period was 3.8% per annum, while P&G's organic sales growth was 2% in 2015, 1% in 2016, 2% in 2017, 1% in 2018, and 5% in 2019<sup class="inline-source">[11]</sup>.</li>
            <li>Unilever's core operating margin improved by an average of 0.37 percentage points per year during this period<sup class="inline-source">[12]</sup>, while P&G's core gross margin increased by 1.4 percentage points from 2015 to 2019<sup class="inline-source">[13]</sup>.</li>
            </ul>
          <br>
            Notable factors or events that influenced the sales growth of both companies during this period: <br>
          <ul>
            <li>Unilever faced challenges in 2015<sup class="inline-source">[1]</sup>.</li>
            <li>P&G underwent a significant portfolio transformation during this period, divesting more than 100 brands<sup class="inline-source">[8]</sup>.</li>
          </ul><br>
            Actions that Unilever can take to continue to grow its sales: <br>
          <ul>
            <li>Consider investing in research and development to innovate and introduce new products.</li>
            <li>Explore opportunities for acquisitions or partnerships to expand into new markets or product categories.</li>
            <li>Focus on sustainability and social responsibility to appeal to consumers who prioritize these values.</li>
            <li>Continuously monitor and analyze consumer trends to stay ahead of the competition.</li>
          </ul>
          <br>
          <hr/>
          <br>
          <img src="@/assets/img/lightbulb.png" height="50">
          <span class="related-header">You might want to explore...</span><br>
          <div class="row">
            <span class="related-q">What were the main drivers of Unilever's sales growth in 2017?</span>
            <span class="related-q">How did P&G's sales growth compare to its competitors during this period?</span>
            <span class="related-q">What actions did P&G take to improve its core gross margin from 2015 to 2019?</span>
          </div>
          <br>
        </div>
      </div>
</template>

<script>
import Chart from 'chart.js'
import salesChartData from '../answer-chart.js'

export default {
  name: 'Answerpage',
  data(){
    return { showRefined: false, showSrc: false, salesChartData: salesChartData}
  },
  mounted() {
    const ctx = document.getElementById('answer-chart');
    new Chart(ctx, this.salesChartData);
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
}

</style>