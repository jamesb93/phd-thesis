<script>
    import Chart from "chart.js"
    import { onMount } from "svelte";
    export let title = "title";
    
    let container;
    onMount(() => {
        fetch("plots/umap7-1.json")
            .then(res => res.json())
            .then(json => {
                var ctx = container.getContext('2d');
                var scatterChart = new Chart(ctx, {
                    type: 'scatter',
                    data: {
                        datasets: [{
                            pointRadius: 0.5,
                            data: json.data,
                            pointBackgroundColor: "#000000"
                        }]
                    },
                    options: {
                        title: {
                            display: true,
                            text: title
                        },
                        tooltip: {
                            enabled: false
                        },
                        legend: {
                            display: false
                        },
                        animation: false,
                        responsive: true,
                        scales: {
                            yAxes: [{
                                gridLines: {
                                    drawBorder: false,
                                    display: false
                                },
                                ticks: {
                                    display: false
                                }
                            }],
                            xAxes: [{
                                gridLines: {
                                    display: false
                                },
                                ticks: {
                                    display: false
                                }
                            }]
                        }
                    }
                });
            });


    })
    
</script>

<style>
    canvas {
        border: 1px solid grey;
    }
</style>

<canvas bind:this={container} height=300></canvas>