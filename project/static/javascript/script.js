function btn_click(data) {
    // console.log(data);

    var ctx = document.getElementById('pieChart').getContext('2d');

    var myChart = new Chart(ctx, {
        type: 'doughnut',
        data: {
            labels: ['Risk', 'No Risk'],
            datasets: [{
                label: 'Projects having risk or no risk',
                data: [data.risk, data.no_risk],
                backgroundColor: [
                    'rgba(255, 99, 132, 0.2)',
                    'rgba(54, 162, 235, 0.2)'
                ],
                borderColor: [
                    'rgba(255, 99, 132, 1)',
                    'rgba(54, 162, 235, 1)'
                ],
                borderWidth: 1
            }]
        },
        options: {
            scales: {
                yAxes: [{
                    ticks: {
                        beginAtZero: true
                    }
                }]
            }
        }
    });

}