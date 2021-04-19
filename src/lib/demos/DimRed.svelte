<script>
    import { onMount } from "svelte";

    let container;
    let chart;
    import { UMAP } from "umap-js"
    const umap = new UMAP({
        nComponents: 2,
        nNeighbors: 4,
        epochNumber: 10
    });
    let data = [
        [1, 2, 3, 4],
        [2, 3, 4, 5],
        [3, 2, 3, 4],
        [1, 2, 3, 1],
        [4, 1, 2, 3],
        [1, 4, 2, 3]
    ];
    let points = [];

    function marshallPoints(arr) {
        var temp = []
        for (let i=0; i < arr.length; i++) {
            temp.push({
                "x": arr[i][0],
                "y": arr[i][1]
            })
        }
        return temp
    }
    onMount(() => {
        const nEpochs = umap.initializeFit(data);
        let embedding = umap.getEmbedding();
        points = marshallPoints(embedding);
        var ctx = container.getContext('2d');
        chart = new Chart(ctx, {
            type: 'scatter',
            data: {
                datasets: [{
                    pointRadius: 4.0,
                    data: points,
                    pointBackgroundColor: "#000000"
                }]
            },
            options: {
                title: {
                    display: true,
                    text: "My Title"
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
    function clickHandler() {
        umap.step();
        points = marshallPoints(umap.getEmbedding());
        chart.options.title.text = "foooo!";
        chart.update();
    }



</script>

<style>
    canvas {
        border: 1px solid grey;
    }
    div {
        padding-top: 1em;
        padding-bottom: 1em;
    }
</style>
<div>
    <button on:click={clickHandler} on>compute!</button>
    <canvas bind:this={container} height=300></canvas>
</div>