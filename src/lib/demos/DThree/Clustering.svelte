<!-- Demonstates clustering at multiple levels of specificity -->

<script>
    // TODO finish me with colouring and interactivity
    import { onMount } from "svelte";
    import { clip } from "./clip.js"
    import * as d3 from 'd3';

    let container;
    let height;
    let width;
    let pos = 200
    let nodes = new Array(100).fill();

    function constructDots() {
        for (let i=0; i < nodes.length; i++) {
        let x = (Math.random() * 300) + 50;
        let y = (Math.random() * 300) + 50;
        nodes[i] = {'x': x, 'y': y}
        }
    }

    // $: nodes = [
    //     {x: pos, y: pos},
    //     {x: pos, y: pos}
    // ]

    onMount(() => {
        constructDots();
        createDots();
    });

    function createDots() {
        let svg = d3.select(container);
        let node = svg.append('g')
            .attr('stroke', '#fff')
            .attr('stroke-width', 1.5)
            .selectAll('circle')
            .data(nodes)
            .join('circle')
            .attr('r', 5)
            .attr('fill', d3.color(d3.schemeCategory10))
            .attr('cx', d => clip(d.x, 0, width))
            .attr('cy', d => clip(d.y, 0, height))
    }

    function update() {
        d3.select('g').remove();
        createDots();
    }   
</script>

<input type="range" min="0" max="400" bind:value={pos} on:input={update}/>
<div class="box" bind:offsetHeight={height} bind:offsetWidth={width}>
<svg bind:this={container} class="d3-container"></svg>
</div>
<p class="caption">DEMO 2: A network of actions and outputs. Observing different outputs can lead to more direct creative action or lead back to further computational exploration and new outputs to be made.</p>

<style>
    .box {
        height: 400px;
    }
    .d3-container {
        display: block;
        margin: auto;
        width: 100%;
        height: 100%;
    }

    .caption {
        font-style: italic;
        text-align: center;
    }
</style>