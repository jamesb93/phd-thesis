<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';
    import { browser } from '$app/env';
    import { CanvasSpace, Pt } from 'pts';
    import Container from '$lib/components/Container.svelte';
    import Slider from '$lib/components/Slider.svelte';
    import plot1 from './umap7-0.1.json';
    import plot2 from './umap15-0.75.json';
    import plot3 from './umap15-0.1.json';
    import plot4 from './umap30-0.1.json';

    export let title = 'title'
    export let caption = 'DEMO'
    export let id = ''
    let interp = 0.0;
    let blend1, blend2, blend3;
    let canvas;
    let neighbours = plot1.parameters.neighbours;
    let mindist = plot2.parameters.mindist
    let d = plot1;

    function update() {
        // Band the interpolation
        if (interp <= 1.0 && interp >= 0.0)
            d = blend1(interp);

        if (interp <= 2.0 && interp > 1.0 )
            d = blend2(interp-1.0);

        if (interp <= 3.0 && interp > 2.0)
            d = blend3(interp-2.0);
        
        neighbours = d.parameters.neighbours;
        mindist = d.parameters.mindist;
        // if (interp <= 0.5 && interp >= 0.0) {
        //     neighbours = plot1.parameters.neighbours;
        //     mindist = plot1.parameters.mindist;
        // }

        // if (interp <= 1.5 && interp > 0.5) {
        //     neighbours = plot2.parameters.neighbours;
        //     mindist = plot2.parameters.mindist;
        // }

        // if (interp <= 2.5 && interp > 1.5) {
        //     neighbours = plot3.parameters.neighbours;
        //     mindist = plot3.parameters.mindist;
        // }

        // if (interp <= 4.0 && interp > 2.5) {
        //     neighbours = plot4.parameters.neighbours;
        //     mindist = plot4.parameters.mindist;
        // }
    };

    onMount(async() => {
        blend1 = d3.interpolateObject(plot1, plot2);
        blend2 = d3.interpolateObject(plot2, plot3);
        blend3 = d3.interpolateObject(plot3, plot4);
        update();
        let space = new CanvasSpace('#sketch').setup({ bgcolor: '#fff' });
        let form = space.getForm();
        space.add({
            animate: (time, ftime, space) => {
                d.data.forEach(z => {
                    form.fillOnly('#0d47a1').point( 
                        new Pt(
                            z.x*space.width*0.95, 
                            z.y*space.height* 0.95
                        ), 0.6, 'square' 
                    );
                })
            }
        });
        space.play().bindMouse();
    })
</script>

<Container zoom={false} id={id}>
    <div id='top-text'>
        <div id='info'>
            <span id='title'>{title}</span>
            <span id='caption'>{caption}</span>
        </div>
        <div id='parameters'>
            <span>
                Neighbours: { parseFloat(neighbours).toFixed(2) }
            </span>
            <span>
                Minimum Distance: { parseFloat(mindist).toFixed(2) }
            </span>
        </div>
    </div>
    <Slider showValue={ false } showMin={ false } showMax={ false } bind:value={ interp } inFunc={ update } min={0.0} max={3.0} step={0.005} />
    <canvas id='sketch' bind:this={ canvas } />
</Container>

<style>
    #sketch {
        width: 100%;
        height: 600px;
    }

    #top-text {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    #info {
        display: flex;
        flex-direction: column;
    }

    #title {
        font-weight: bold;
    }

    #caption {
        font-style: italic;
    }

    #parameters {
        display: flex;
        flex-direction: column;
        text-align: right;
    }
</style>

