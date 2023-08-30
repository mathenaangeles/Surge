<template>
    <div class="main-wrapper w-100 h-100">
      <div class="area-containers mx-5 p-4 question-area">
        <span style="font-family: 'ShillingM';">Question: </span>
        <span>Unilever background</span>
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
              Unilever_2012_Annual_Report-46.pdf 
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              Unilever_2012_Annual_Report-77.pdf 
            </span>
            <span class="source"> 
              <svg xmlns="http://www.w3.org/2000/svg" width="16" height="16" fill="currentColor" class="source-icon bi bi-bookmarks" viewBox="0 0 16 16">
                <path d="M2 4a2 2 0 0 1 2-2h6a2 2 0 0 1 2 2v11.5a.5.5 0 0 1-.777.416L7 13.101l-4.223 2.815A.5.5 0 0 1 2 15.5V4zm2-1a1 1 0 0 0-1 1v10.566l3.723-2.482a.5.5 0 0 1 .554 0L11 14.566V4a1 1 0 0 0-1-1H4z"/>
                <path d="M4.268 1H12a1 1 0 0 1 1 1v11.768l.223.148A.5.5 0 0 0 14 13.5V2a2 2 0 0 0-2-2H6a2 2 0 0 0-1.732 1z"/>
              </svg>
              Unilever_2012_Annual_Report-60.pdf 
            </span>
          </div>
        </div>
        <div class="mt-5">
          <span>Unilever values diversity in its workforce and Board, with a focus on gender diversity but also considering a variety of backgrounds, skills, knowledge, and nationalities.</span>
          <br><br><br>
          <hr/>
          <br>
          <img src="@/assets/img/lightbulb.png" height="50">
          <span class="related-header">You might want to explore...</span><br>
          <div class="row">
            <span class="related-q">How has Unilever's workforce diversity evolved over time?</span>
            <span class="related-q">What actions has Unilever taken to promote diversity and inclusion in its operations?</span>
            <span class="related-q">How does Unilever measure the effectiveness of its diversity initiatives?</span>
          </div>
          <br>
        </div>
      </div>
    </div>
</template>

<script>
export default {
  name: 'Answerpage'
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