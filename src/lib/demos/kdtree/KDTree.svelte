<!-- 
    Refer to:
    https://ptsjs.org/guide/op-0400s
 -->

<script>
    import { onMount } from 'svelte';
    import { CanvasSpace, Create } from 'pts';
    import Container from '$lib/components/Container.svelte';

    export let title = 'k-d tree sample searching'
    export let caption = 'DEMO 1'
    export let id = ''

    let canvas;
    let ready = false;
    let pts;
    let mouse
    let rect;

    function getMousePos(canvas, evt) {
        // We need to do this manually otherwise when shifting the window the resize is not accounted for.
        rect = canvas.getBoundingClientRect();
        return [
            (evt.clientX - rect.left) / (rect.right - rect.left) * canvas.width,
            (evt.clientY - rect.top) / (rect.bottom - rect.top) * canvas.height
        ]
    }

    onMount(async() => {
        let space = new CanvasSpace('#sketch').setup({ bgcolor: '#fff' });
        let form = space.getForm();
        rect = canvas.getBoundingClientRect();
        space.add({
            start: () => {
                pts = Create.distributeRandom( space.innerBound, 300 );
            },
            animate: (time, ftime, space) => {
                pts.sort( (a,b) => a.$subtract(mouse).magnitude() - b.$subtract(mouse).magnitude() );
                for (let i=1; i < 10; i++) {
                    form.fillOnly("#123").points( pts.slice(0, 10), 3, "circle" );
                }
                for (let i=0; i < 10; i++) {
                    form.strokeOnly('#0d47a1', 2).line( [ pts[i], pts[0] ] );
                }
                form.fill("#f03").point( pts[0], 6, "circle" );
                form.fillOnly("#123").points( pts.slice(10), 2, "circle" );
            },
            action: (t,x,y,e) => {
                mouse = getMousePos(canvas, e)
            }
        });
        space.play().bindMouse();
        ready = true;
    })
</script>

<Container zoom={false} id={id}>
    <div id='top-text'>
        <div id='info'>
            <span id='title'>{title}</span>
            <span id='caption'>{caption}</span>
        </div>
        <div id='explanation'>
            <p>    
                Each point in this space represents an audio sample, reduced into a two-dimensional representation through analysis and dimension reduction.
            </p>
            <p>
                As you move the mouse, the nearest sample to the pointer is highlighted in red. The 10 samples closest to this have lines drawn to them and are emboldened.
            </p>
            <p>
                This method of navigating through the sample space depicts my <i>k-d approach</i> to finding sounds which are similar to a specifically selected sample within a corpus. The selected sample is represented by the highlighted red point, and the 10 most similar sounds are derived by branching out into nearby space.
            </p>
        </div>
    </div>
    <div id='drawing-zone'>        
        {#if ready === false}
        <span>Loading UMAP Data...</span>
        {/if}
        <canvas id='sketch' bind:this={ canvas } />
    </div>
</Container>

<style>
    #sketch {
        width: 100%;
        height: 600px;
    }

    #top-text {
        display: flex;
        flex-direction: column;
    }

    #info {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    #title {
        font-weight: bold;
    }

    #caption {
        font-style: italic;
    }
</style>

