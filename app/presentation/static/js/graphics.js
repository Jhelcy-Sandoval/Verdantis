// Grafico Planta

document.addEventListener('DOMContentLoaded', function() {
    const chartDataDiv = document.getElementById('chart-data');
    if (chartDataDiv) {
        const labels = JSON.parse(chartDataDiv.getAttribute('data-labels'));
        const values = JSON.parse(chartDataDiv.getAttribute('data-values'));

        // Create the chart for plant conditions
        const ctx = document.getElementById('myChart').getContext('2d');
        new Chart(ctx, {
            type: 'pie',
            data: {
                labels: labels,
                datasets: [{
                    data: values,
                    backgroundColor: ['#FF6384', '#36A2EB', '#FFCE56', '#FF5733', '#C70039', '#900C3F']
                }]
            },
            options: {
                responsive: true,
                plugins: {
                    legend: {
                        position: 'top',
                    },
                    tooltip: {
                        callbacks: {
                            label: function(context) {
                                return `${context.label}: ${context.raw}`;
                            }
                        }
                    }
                }
            }
        });
    }
});


// Grafico general
document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-dos');
  
    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  
  
  try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);
  
        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }
  
        const ctx = document.getElementById('myChartdos').getContext('2d');
  
        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Datos de Plantas',
                    data: values,
                    backgroundColor: 'rgba(108, 191, 85, 0.2)',
                    borderColor: 'rgba(108, 191, 85, 1)',
                    borderWidth: 1
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
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
  });

//Gráfico de desarrollo
document.addEventListener('DOMContentLoaded', function() {
    const chartDataDiv = document.getElementById('chart-data-tres');
    const labels = JSON.parse(chartDataDiv.getAttribute('data-labels'));
    const values = JSON.parse(chartDataDiv.getAttribute('data-values'));

    const datasets = labels.map((label, index) => ({
        label: label,
        data: values[index],
        borderColor: `hsl(${Math.random() * 360}, 100%, 50%)`,
        backgroundColor: `hsl(${Math.random() * 360}, 100%, 80%)`,
        fill: false,
        tension: 0.1
    }));

    const ctx = document.getElementById('myCharttres').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: values[0].map((_, i) => `Mes ${i + 1}`), 
            datasets: datasets
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.raw}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Meses'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Desarrollo (%)'
                    },
                    beginAtZero: true
                }
            }
        }
    });
});

// Grafico temperatura
document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-cuarto');

    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  

    try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);  

        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }

        const ctx = document.getElementById('myChartCuarto').getContext('2d');

        const myChart = new Chart(ctx, {
            type: 'line',
            data: {
                labels: labels,
                datasets: [{
                    label: 'temperatura (%)',
                    data: values,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
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
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
});

// Grafico humedad
document.addEventListener('DOMContentLoaded', function() {
    const chartDataElement = document.getElementById('chart-data-quinto');

    const labelsRaw = chartDataElement.dataset.labels || '[]';  
    const valuesRaw = chartDataElement.dataset.values || '[]';  

    try {
        const labels = JSON.parse(labelsRaw);
        const values = JSON.parse(valuesRaw);  

        if (!labels.length || !values.length) {
            console.warn('Los datos de las plantas están vacíos o no fueron pasados correctamente.');
            return; 
        }

        const ctx = document.getElementById('myChartQuinto').getContext('2d');

        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: labels,
                datasets: [{
                    label: 'Humedad (%)',
                    data: values,
                    backgroundColor: 'rgba(75, 192, 192, 0.2)',
                    borderColor: 'rgba(75, 192, 192, 1)',
                    borderWidth: 1
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
    } catch (e) {
        console.error('Error al parsear los datos JSON:', e);
    }
}); 

// estadistica clave 
document.addEventListener('DOMContentLoaded', function() {
    const chartDataDiv = document.getElementById('chart-data-seis');
    const labelsd = JSON.parse(chartDataDiv.getAttribute('data-labels'));
    const valuesd = JSON.parse(chartDataDiv.getAttribute('data-values'));

    const datasets = labelsd.map((label, index) => ({
        label: label,
        data: valuesd[index],
        borderColor: `hsl(${Math.random() * 360}, 100%, 50%)`,
        backgroundColor: `hsl(${Math.random() * 360}, 100%, 80%)`,
        fill: false,
        tension: 0.1
    }));

    const ctx = document.getElementById('myChartseis').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: valuesd[0].map((_, i) => `Mes ${i + 1}`), 
            datasets: datasets
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.raw}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Meses'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Valor'
                    },
                    beginAtZero: true
                }
            }
        }
    });

    const chartDataStatDiv = document.getElementById('chart-data-stat');
    const labels_stat = JSON.parse(chartDataStatDiv.getAttribute('data-labels'));
    const values_stat = JSON.parse(chartDataStatDiv.getAttribute('data-values'));

    const datasetsStat = labels_stat.map((label, index) => ({
        label: label,
        data: values_stat[index],
        borderColor: `hsl(${Math.random() * 360}, 100%, 50%)`,
        backgroundColor: `hsl(${Math.random() * 360}, 100%, 80%)`,
        fill: false,
        tension: 0.1
    }));

    const ctxStat = document.getElementById('myChartStat').getContext('2d');
    new Chart(ctxStat, {
        type: 'line',
        data: {
            labels: values_stat[0].map((_, i) => `Mes ${i + 1}`),
            datasets: datasetsStat
        },
        options: {
            responsive: true,
            plugins: {
                legend: {
                    position: 'top',
                },
                tooltip: {
                    callbacks: {
                        label: function(context) {
                            return `${context.dataset.label}: ${context.raw}`;
                        }
                    }
                }
            },
            scales: {
                x: {
                    title: {
                        display: true,
                        text: 'Meses'
                    }
                },
                y: {
                    title: {
                        display: true,
                        text: 'Valor'
                    },
                    beginAtZero: true
                }
            }
        }
    });
});

