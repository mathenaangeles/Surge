export const salesChartData = {
    type: "line",
    data: {
      labels: ["2015", "2016", "2017", "2018", "2019"],
      datasets: [
        {
          label: "Unilever",
          data: [53.3, 52.7, 53.7, 50.9, 52],
          backgroundColor: "transparent",
          borderColor: "#1E2F97",
          borderWidth: 3
        },
        {
          label: "Procter & Gamble",
          data: [76.3, 65.3, 65.1, 66.8, 67.7],
          backgroundColor: "transparent",
          borderColor: "#FFA500",
          borderWidth: 3
        }
      ]
    },
    options: {
      responsive: true,
      lineTension: 1,
      legend: {
        display: true,
        labels: {
            fontSize: 16
        }
      },
      scales: {
        yAxes: [
          {
            scaleLabel: {
                display: true,
                labelString: 'Yearly sales in billion euro',
                fontSize: 16
            },
            ticks: {
                beginAtZero: false,
                suggestedMin: 30,
                padding: 20,
                fontSize: 16
            },
          }
        ],
        xAxes : [
          {
            ticks: {
                fontSize: 16
            }
          }
        ],
      },
    }
  };
  
  export default salesChartData;