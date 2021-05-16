<script>
    import * as d3 from 'd3';
    import { onMount } from 'svelte';
    import { CanvasSpace, Pt } from 'pts';
    import Container from '$lib/components/Container.svelte';
    import plot1 from './umap7-0.1.json';
    import plot2 from './umap15-0.75.json';
    import plot3 from './umap15-0.1.json';
    import plot4 from './umap30-0.1.json';

    let interp = 0.0;
    const blend1 = d3.interpolateObject(plot1, plot2);
    const blend2 = d3.interpolateObject(plot2, plot3);
    const blend3 = d3.interpolateObject(plot3, plot4);
    let canvas, anchor, mousedown
    let config = 100;
    let d = plot1;

    function update() {
        // Band the interpolation
        if (interp <= 1.0 && interp >= 0.0) {
            d = blend1(interp);
            config = 'config dasdsadas'
        }

        if (interp <= 2.0 && interp > 1.0 ) {
            d = blend2(interp-1.0);
            config = 'config 2'
        }


        if (interp <= 3.0 && interp > 2.0) {
            d = blend3(interp-2.0);
            config = 'config 3'
        } 
    };

    onMount(async() => {
        update();
        let space = new CanvasSpace('#sketch').setup({ bgcolor: '#fff' });
        let form = space.getForm();
        space.add({
            animate: (time, ftime, space) => {
                d.data.forEach(z => {
                    form.fillOnly('grey').point( 
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

<h1>Points</h1>
<Container>
    { config }
    <input type='range' bind:value={ interp } on:input={ update } min=0.0 max=3.0 step=0.001 />
    <canvas id='sketch' bind:this={ canvas } />
</Container>

<style>
    #sketch {
        width: 100%;
        height: 600px;
    }
</style>

