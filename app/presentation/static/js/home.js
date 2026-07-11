const estadoPie = document.getElementById("estadoPie");
console.log(estadoPie);

if (estadoPie) {


    const optimas = Number(estadoPie.dataset.optimas);
    const observacion = Number(estadoPie.dataset.observacion);
    const criticas = Number(estadoPie.dataset.criticas);

    new Chart(estadoPie, {

        type: "doughnut",

        data: {

            labels: [
                "Óptimas",
                "Observación",
                "Críticas"
            ],

            datasets: [{
                data: [
                    optimas,
                    observacion,
                    criticas
                ],

                backgroundColor: [
                    "#52B788",
                    "#F4A261",
                    "#E76F51"
                ],

                borderWidth: 0,

                hoverOffset: 8

            }]

        },

        options: {

            responsive: true,

            maintainAspectRatio: false,

            cutout: "70%",

            plugins: {

                legend: {

                    position: "bottom",

                    labels: {

                        usePointStyle: true,
                        pointStyle: "circle",
                        padding: 20

                    }

                }

            }

        }

    });

}

const distribution = document.getElementById("gardenDistribution");

if (distribution) {

    const labels = JSON.parse(
        distribution.dataset.labels
    );

    const values = JSON.parse(
        distribution.dataset.values
    );

    new Chart(distribution, {

        type: "bar",

        data: {

            labels,

            datasets: [

                {

                    label: "Plantas",

                    data: values,

                    borderRadius: 8,

                    backgroundColor: "#52B788"

                }

            ]

        },

        options: {

            indexAxis: "y",

            responsive: true,

            maintainAspectRatio: false,

            plugins: {

                legend: {

                    display: false

                }

            },

            scales: {

                x: {

                    beginAtZero: true,

                    grid: {

                        display: false

                    }

                },

                y: {

                    grid: {

                        display: false

                    }

                }

            }

        }

    });

}