<script>
    import { onMount } from "svelte";
    import { dragNetwork } from "./dragNetwork.js"
    import { clip } from "./clip.js"
    import * as d3 from 'd3';

    let container;
    let simulation;
    let height;
    let width;
    let connections = [
        {
            'Content-Aware Program Output' : [
                'JSON Data', 
                'Audio Outputs', 
                'Data Visualisation'
            ]
        },
        {
            'JSON Data' : [
                'Max Facilitated Exploration', 
                'Return to Generating Outputs', 
                'REAPER Scripting', 
                'Manual Composing'
            ]
        },
        {
            'Max Facilitated Exploration' : [
                'Return to Generating Outputs', 
                'REAPER Scripting', 
                'Manual Composing'
            ]
        },
        {
            'Return to Generating Outputs' : ['Content-Aware Program Output']
        },
        {
            'REAPER Scripting' : [
                'Manual Composing', 
                'Return to Generating Outputs',
                'Audio Outputs'
            ]
        },
        {
            'Audio Outputs' : [
                'Manual Composing', 
                'Return to Generating Outputs',
            ]
        },
        {
            'Manual Composing' : ['Return to Generating Outputs']
        },
        {
            'Data Visualisation' : [
                'Return to Generating Outputs',
                'Manual Composing',
                'REAPER Scripting'
            ]
        }
    ]

    let nodes = []
    let links = []
    connections.forEach((d) => {
        for (var k in d) {
            nodes.push({'id' : k})
            d[k].forEach(l => {
                links.push({
                    'source' : k, 'target' : l
                })
            })
        }
    })
    // TODO: weighted nodes, so there can be more importance on content-aware program output
    onMount(() => {
        let svg = d3.select(container)
        simulation = d3.forceSimulation(nodes)
            .force('link', d3.forceLink(links).id((d) => {
                return d.id
            }))
            .force('charge', d3.forceManyBody()
                .strength(-1200)
                .distanceMin(-5)
            )
            .force('center', d3.forceCenter(width / 2.74, height / 2));

        let link = svg.append('g')
            .attr('id', 'markers')
            .attr('stroke', '#999')
            .attr('stroke-opacity', 0.9)
            .selectAll('line')
            .data(links)
            .join('line')
            .attr('stroke-width', 1)

        let node = svg.append('g')
            .attr('stroke', '#fff')
            .attr('stroke-width', 1.5)
            .selectAll('circle')
            .data(nodes)
            .join('circle')
            .attr('r', 5)
            .attr('fill', d3.color(d3.schemeCategory10))
            .call(dragNetwork(simulation));
        
        let text = svg.append('g')
            .attr('class', 'labels')
            .selectAll('text')
            .data(nodes)
            .enter().append('text').attr('text-left', 'middle')
            .attr('transform', 'translate(15, 0)')
            .text((d) => { return d.id });

        simulation.on('tick', () => {
            link
                .attr('x1', d => clip(d.source.x, 0, width))
                .attr('y1', d => clip(d.source.y, 0, height))
                .attr('x2', d => clip(d.target.x, 0, width))
                .attr('y2', d => clip(d.target.y, 0, height))
    
            node
                .attr('cx', d => clip(d.x, 0, width))
                .attr('cy', d => clip(d.y, 0, height))

            text
                .attr('dx', d => clip(d.x, 0, width))
                .attr('dy', d => clip(d.y, 0, height))
        });
    });
        
</script>
<div class="box" bind:offsetHeight={height} bind:offsetWidth={width}>
<svg bind:this={container} class="d3-container"></svg>
</div>
<p class="caption">DEMO 1: A network of actions and outputs. Observing different outputs can lead to more direct creative action or lead back to further computational exploration and new outputs to be made.</p>

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