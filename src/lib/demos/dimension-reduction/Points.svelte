<script>
    import * as d3 from 'd3';
    import * as THREE from "three";
    import { onMount } from 'svelte';
    import Slider from '$lib/components/Slider.svelte';
    import Container from '$lib/components/Container.svelte';
    export let title = 'The effect of UMAP parameters on the projection characteristics';
    export let caption='DEMO 1';
    export let id = 'demo1'

    let ready = false;
    let container;
    let height = 600;
    let width = 450;
    // Animation Code
    let camera, scene, renderer;
    let focused;
    let group;
    let pointsGeometry, pointCloud;
    const pointSize = 1.5;
    const r = 9500;

    // Interplation
    let interp = 0.0;
    let plot1, plot2, plot3, plot4;
    let blend1, blend2, blend3;
    let data;
    let neighbours, mindist;

    // Buffers
    let positionBuffer, colorBuffer, positions, colors;

    function update(init) {
        // Band the interpolation
        if (interp <= 1.0 && interp >= 0.0)
            data = blend1(interp);

        if (interp <= 2.0 && interp > 1.0 )
            data = blend2(interp-1.0);

        if (interp <= 3.0 && interp > 2.0)
            data = blend3(interp-2.0);
        
        neighbours = data.parameters.neighbours;
        mindist = data.parameters.mindist;

        if (!init) {
            data.data.forEach((d, i) => {
                positions.set([
                    d.x * r - (r / 2), 
                    d.y * r - (r / 2), 
                    0
                ], i * 3)
            })
            pointsGeometry.setAttribute('position', new THREE.BufferAttribute( positions, 3));
        }
    };
    
    onMount(async() => {
        await fetch('/plots/umap7-0.1.json')
            .then(response => response.json())
            .then(data => plot1 = data)

        await fetch('/plots/umap15-0.1.json')
            .then(response => response.json())
            .then(data => plot2 = data)

        await fetch('/plots/umap15-0.75.json')
            .then(response => response.json())
            .then(data => plot3 = data)
            
        await fetch('/plots/umap30-0.1.json')
            .then(response => response.json())
            .then(data => plot4 = data)
        
        blend1 = d3.interpolateObject(plot1, plot2);
        blend2 = d3.interpolateObject(plot2, plot3);
        blend3 = d3.interpolateObject(plot3, plot4);
        
        update(true);
        init();
        animate();
        render();
        ready = true;
    })

    function init() {
        camera = new THREE.PerspectiveCamera(90, width / height, 1, r * 2);
        camera.position.z = 5000;
        
        scene = new THREE.Scene();
        group = new THREE.Group();
        scene.add(group);

        const pointsMaterial = new THREE.PointsMaterial({
            vertexColors: true,
            size: pointSize,
            sizeAttenuation: false,
        })

        pointsGeometry = new THREE.BufferGeometry();
        positionBuffer = new ArrayBuffer(data.data.length * 3 * 4);
        colorBuffer = new ArrayBuffer(data.data.length * 3 * 4);
        positions = new Float32Array(positionBuffer)
        colors = new Float32Array(colorBuffer);

        data.data.forEach((d, i) => {
            positions.set([
                d.x * r - (r / 2), 
                d.y * r - (r / 2), 
                0
            ], i * 3)

            colors.set([d.x, d.y, 0.5], i * 3)
        })
        let sizes = data.data.map(d => 1.0);
        sizes = Float32Array.from(sizes)
        pointsGeometry.setAttribute('size', new THREE.BufferAttribute( sizes, 1 ));
        pointsGeometry.setAttribute('position', new THREE.BufferAttribute( positions, 3));
        pointsGeometry.setAttribute('color', new THREE.BufferAttribute( colors, 3 ));

        // particles/points
        pointCloud = new THREE.Points( pointsGeometry, pointsMaterial );
        group.add( pointCloud );

        // Renderer
        renderer = new THREE.WebGLRenderer({ antialias: true, alpha: true });
        renderer.setPixelRatio( window.devicePixelRatio );
        renderer.setSize( width, height );
        container.appendChild( renderer.domElement );
    }
    
    function animate() {
        requestAnimationFrame( animate );
        if (focused) {
            render()
        }
    }

    function render() {
        renderer.render( scene, camera );
    }

</script>

<svelte:window />

<Container id={id} zoom={false}>
    <div id="main">
        <div id='top-text'>
            <div class='vertical'>
                <span id='title'>{title}</span>
                <span id='caption'>{caption}</span>
            </div>
            <div class='vertical' id='parameters'>
                <span>
                    Neighbours: { parseFloat(neighbours).toFixed(2) }
                </span>
                <span>
                    Minimum Distance: { parseFloat(mindist).toFixed(2) }
                </span>
            </div>
        </div>
        <span id='instructions'>Move the slider to adjust the UMAP parameters</span>
        <Slider bind:focused={ focused } showValue={ false } showMin={ false } showMax={ false } bind:value={ interp } inFunc={ () => update(false) } min={0.0} max={3.0} step={0.005} />
        <span id='status'>{#if !ready}Loading... {/if}</span>
        <div id="view" bind:this={container} bind:offsetHeight={height} bind:offsetWidth={width}></div>
    </div>
</Container>


<style>
    #view {
        height: 600px;
        width: 100%;
    }

    #top-text {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    #parameters { 
        text-align: right;
        white-space: nowrap;
    }

    #title {
        font-weight: bold;
    }

    #caption {
        font-style: italic;
    }

    #status {
        text-align: center;
    }

    .vertical {
        display: flex;
        flex-direction: column;
    }

    #instructions {
        text-align: center;
        color: grey;
    }

    #main {
        display: flex;
        flex-direction: column;
    }
</style>