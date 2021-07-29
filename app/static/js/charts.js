$(document).ready(function() {
    for (let i = 0; i < 10; i++) {
        var ctx = document.getElementById('track-chart-' + i).getContext('2d');
        var myChart = new Chart(ctx, {
            type: 'line',
            data: {
            labels: ['Sun.', 'Mon.', 'Tue.', 'Wed.', 'Thu.', 'Fri.', 'Sat.'],
            datasets: [{
                data: [
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0,
                0.0
                ],
                backgroundColor: [
                'rgba(14, 235, 92, 0.2)'
                ],
                borderColor: [
                'rgba(14, 235, 92, 1)'
                ],
                borderWidth: 1,
                tension: 0.3,
                fill: {
                target: 'origin',
                }
            }]
            },
            options: {
            plugins: {
                legend: {
                display: false
                },
                tooltip: {
                displayColors: false,
                callbacks: {
                    label: function(context) {
                    var label = [context.dataset.label || '', 'n Times'];
    
                    if (context.parsed.y !== null) {
                        label[0] += new Intl.NumberFormat("en-US", {
                        style: 'percent',
                        minimumFractionDigits: 1
                        }).format(context.parsed.y);
                    }
    
                    return label;
                    }
                }
                }
            },
            scales: {
                y: {
                beginAtZero: true,
                grid: {
                    drawBorder: false,
                },
                ticks: {
                    color: "white",
                    font: {
                        size: 12,
                        family: "'Open Sans', sans-serif",
                    },
                    callback: function(value, index, values) {
                    return (value * 100).toFixed(0) + '%';
                    }
                }
                },
                x: {
                    ticks: {
                        color: "white",
                        font: {
                            size: 12,
                            family: "'Open Sans', sans-serif",
                        }
                    }
                }
            }
            }
        });
    }
});