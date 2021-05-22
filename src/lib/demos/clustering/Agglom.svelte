<script>
    import * as d3 from 'd3';
    import * as THREE from "three";
    import { onMount } from 'svelte';
    import Container from '$lib/components/Container.svelte';
    export let title = 'Agglomerative Clustering with different levels of granularity';
    export let caption='DEMO 2';
    export let id = 'demo1'

    let ready = false;
    let needsUpdate = false;
    let container;
    let height = 600;
    let width = 450;
    // Animation Code
    let camera, scene, renderer;
    let group;
    let pointsGeometry, pointCloud;
    const pointSize = 8.0;
    const r = 9500;

    let d, data;
    let cluster = 0;
    let clusterValues = [2, 4, 8];
    $: key = clusterValues[cluster];
    const colourScale = d3.scaleOrdinal(d3.schemeSet1).domain([0.0, 1.0])

    // Buffers
    let positionBuffer, colorBuffer, positions, colors;


    function update(init) {
        data = d[key];
        if (!init) {
            data.forEach((point, i) => {
                positions.set([
                    point.coords[0] * r - (r / 2), 
                    point.coords[1] * r - (r / 2), 
                    0
                ], i * 3)
                let col = colourScale(point.cluster / Object.entries(data).length);
                const hex = d3.color(col);
                colors.set([hex.r/255, hex.g/255, hex.b/255], i * 3)
            })
            pointsGeometry.setAttribute('color', new THREE.BufferAttribute(colors, 3));
            pointsGeometry.setAttribute('position', new THREE.BufferAttribute( positions, 3))
        }
        needsUpdate = true;
    };
    
    onMount(async() => {
        await fetch('/re/cluster-data.json')
            .then(response => response.json())
            .then(data => d = data)

        update(true)
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
        positionBuffer = new ArrayBuffer(data.length * 3 * 4);
        colorBuffer = new ArrayBuffer(data.length * 3 * 4);
        positions = new Float32Array(positionBuffer)
        colors = new Float32Array(colorBuffer);

        data.forEach((point, i) => {
            positions.set([
                point.coords[0] * r - (r / 2), 
                point.coords[1] * r - (r / 2), 
                0
            ], i * 3)
            const col = colourScale(point.cluster / Object.entries(data).length);
            const hex = d3.color(col);
            colors.set([hex.r/255, hex.g/255, hex.b/255], i * 3)
        })
        const sizes = Float32Array.from(new Array(data.length).fill(1.0))
        pointsGeometry.setAttribute('color', new THREE.BufferAttribute( colors, 3 ));
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
        // Only render if the slider is focused to conserve idle CPU.
        if (needsUpdate) {
            render()
            needsUpdate = false
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
                <span id='instructions'>
                    Change the number of clusters on the right hand radio group.
                </span>
            </div>
            <div id='parameters'>
                <label>
                    <input type=radio bind:group={ cluster } on:change={ ()=>update(false) } value={0} />
                    2 Clusters
                </label>
            
                <label>
                    <input type=radio bind:group={ cluster } on:change={ ()=>update(false) } value={1} />
                    4 Clusters
                </label>
            
                <label>
                    <input type=radio bind:group={ cluster } on:change={ ()=>update(false) } value={2} />
                    8 Clusters
                </label>
            </div>
        </div>

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
        display: flex;
        flex-direction: column;
        text-align: right;
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
        color: grey;
    }

    #main {
        display: flex;
        flex-direction: column;
    }
</style>