<script>
    import * as d3 from 'd3';
    import * as THREE from "three";
    import { onMount } from 'svelte';
    import Slider from '$lib/components/Slider.svelte';
    import Container from '$lib/components/Container.svelte';
    export let title = 'UMAP parameters effect on the projection.';
    export let caption='DEMO 1';
    export let id = 'demo1'

    let container;
    let height = 600;
    let width = 450;
    // Animation Code
    let camera, scene, renderer;
    let raycaster, mouse;
    let INTERSECTED;
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

        const buffer = new ArrayBuffer(data.data.length * 3 * 4);
        const positions = new Float32Array(buffer)
        if (!init) {
            data.data.forEach((d, i) => {
                positions.set([
                    d.x * r - (r / 2), 
                    d.y * r - (r / 2), 
                    0
                ], i * 3)
            })
            pointsGeometry.setAttribute('position', new THREE.BufferAttribute( positions, 3))
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
    })

    function init() {
        camera = new THREE.PerspectiveCamera(90, width / height, 1, r * 2);
        camera.position.z = 5000;
        mouse = new THREE.Vector2();
        raycaster = new THREE.Raycaster();
        raycaster.setFromCamera(mouse, camera)
        
        scene = new THREE.Scene();
        group = new THREE.Group();
        scene.add(group);

        const pointsMaterial = new THREE.PointsMaterial({
            color: new THREE.Color('#0d47a1'),
            size: pointSize,
            transparent: true,
            sizeAttenuation: false,
        })

        pointsGeometry = new THREE.BufferGeometry();
        const buffer = new ArrayBuffer(data.data.length * 3 * 4);
        const color_buffer = new ArrayBuffer(data.data.length * 3 * 4);
        const positions = new Float32Array(buffer)
        const colors = new Float32Array(color_buffer);

        data.data.forEach((d, i) => {
            positions.set([
                d.x * r - (r / 2), 
                d.y * r - (r / 2), 
                0
            ], i * 3)
            colors.set([0, 0, 1], i * 3)
        })
        let sizes = data.data.map(d => 1.0);
        sizes = Float32Array.from(sizes)
        pointsGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
        pointsGeometry.setAttribute('size', new THREE.BufferAttribute( sizes, 1 ))
        pointsGeometry.setAttribute('position', new THREE.BufferAttribute( positions, 3))

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
        render()
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
        <span id='instructions'>Move the slider to adjust the UMAP parameters!</span>
        <Slider showValue={ false } showMin={ false } showMax={ false } bind:value={ interp } inFunc={ () => update(false) } min={0.0} max={3.0} step={0.005} />
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
    }

    #title {
        font-weight: bold;
    }

    #caption {
        font-style: italic;
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