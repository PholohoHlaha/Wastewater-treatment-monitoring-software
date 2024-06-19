const total_sales_chart = document.getElementById("total-sales-chart");
const waste_flow_chart = document.getElementById("waste-flow-chart");
const waste_quality = document.getElementById("Water-quality-data-chart");

new Chart(total_sales_chart, {
    type: 'line',
    data: {
        labels: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
        datasets: [{
            label: '# of votes',
            data: [1245, 19512, 37897, 24574, 20564, 44547],
            borderWidth: 1  // Corrected typo from borderwidth to borderWidth
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});

const wasteFlowChart = new Chart(waste_flow_chart, {  // Renamed variable to wasteFlowChart
    type: 'line',
    data: {
        labels: ['Aug', 'Sep', 'Oct', 'Nov', 'Dec', 'Jan'],
        datasets: [{
            label: '# of votes',
            data: [1245, 19512, 37897, 24574, 20564, 44547],
            borderWidth: 1  // Corrected typo from borderwidth to borderWidth
        }]
    },
    options: {
        scales: {
            y: {
                beginAtZero: true
            }
        }
    }
});
