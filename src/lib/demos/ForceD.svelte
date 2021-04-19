<script>
    import { onMount } from 'svelte';
    import * as d3 from 'd3';
    var data;
    let h = 300
    let w = 300
    let container;
    let url = "http://localhost:8000/query";

    onMount(() => {
        function dragstarted(d) {
            if (!d3.event.active) simulation.alphaTarget(0.3).restart();
            d.fx = d.x;
            d.fy = d.y;
        }

        function dragged(d) {
            d.fx = d3.event.x;
            d.fy = d3.event.y;
        }

        function dragended(d) {
            if (!d3.event.active) simulation.alphaTarget(0);
            d.fx = null;
            d.fy = null;
        }

        d3.json(url)
            .then(function(graph) {
                console.log(graph)
                var svg = d3.select(container)
                var width={w};
                var height={h};
                var color = d3.scaleOrdinal(d3.schemeCategory10);
                var simulation = d3.forceSimulation()
                    .force("link", d3.forceLink().id(function(d) { return d.id; }))
                    .force("charge", d3.forceManyBody())
                    .force("center", d3.forceCenter(width / 2, height / 2));
                var link = svg.append("g")
                    .attr("class", "links")
                    .selectAll("line")
                    .data(graph.links)
                    .enter().append("line")
                    .attr("stroke-width", function(d) { return Math.sqrt(d.value); });
                var node = svg.append("g")
                    .attr("class", "nodes")
                    .selectAll("g")
                    .data(graph.nodes)
                    .enter().append("g")
                        
                var circles = node.append("circle")
                    .attr("r", 5)
                    .attr("fill", function(d) { return color(d.group); })
                    .call(d3.drag()
                        .on("start", dragstarted)
                        .on("drag", dragged)
                        .on("end", dragended));

                var lables = node.append("text")
                    .text(function(d) {
                        return d.id;
                    })
                    .attr('x', 6)
                    .attr('y', 3);

                node.append("title")
                    .text(function(d) { return d.id; });

                simulation
                    .nodes(graph.nodes)
                    .on("tick", ticked);

                simulation.force("link")
                    .links(graph.links);
                function ticked() {
                    link
                        .attr("x1", function(d) { return d.source.x; })
                        .attr("y1", function(d) { return d.source.y; })
                        .attr("x2", function(d) { return d.target.x; })
                        .attr("y2", function(d) { return d.target.y; });

                    node
                        .attr("transform", function(d) {
                            return "translate(" + d.x + "," + d.y + ")";
                        })
                }
                
            })
	});
</script>

<style>
	.chart :global(div) {
		font: 10px sans-serif;
		background-color: steelblue;
		text-align: right;
		padding: 3px;
		margin: 1px;
		color: white;
	}
</style>

<svg bind:this={container} class="chart"></svg>
