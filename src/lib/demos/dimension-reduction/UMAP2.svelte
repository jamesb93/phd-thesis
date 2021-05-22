<script>
    import * as d3 from 'd3';
    import * as THREE from "three";
    import { onMount } from 'svelte';
    import Slider from '$lib/components/Slider.svelte';
    import Container from '$lib/components/Container.svelte';
    let container;
    let height = 600;
    let width = 450;
    // Animation Code
    let camera, scene, renderer;
    let raycaster, mouse;
    let INTERSECTED;
    let group;
    let pointsGeometry, pointCloud;
    const pointSize = 2.0;
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
            color: new THREE.Color(0.1, 0.3, 0.4, 1.0),
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

    function intersector() {
        const attributes = pointsGeometry.attributes;

        const intersects = raycaster.intersectObject( pointCloud );
        if (intersects.length > 0){
            if (INTERSECTED != intersects[0].index) {
                // attributes.size.array[INTERSECTED] = params.baseParticleSize;
                INTERSECTED = intersects[0].index;
                console.log(INTERSECTED)
                // attributes.size.array[INTERSECTED] = params.baseParticleSize * 4;
                // attributes.size.needsUpdate = true;
            }
        } else if (INTERSECTED !== null) {
            // attributes.size.array[INTERSECTED] = params.baseParticleSize;
            // attributes.size.needsUpdate = true;
            INTERSECTED = null;
        }
    }
    
    function animate() {
        requestAnimationFrame( animate );
        render()
    }

    function render() {
        intersector();
        renderer.render( scene, camera );
    }

</script>

<Container zoom={false}>
    <div id="main">
        <Slider showValue={ false } showMin={ false } showMax={ false } bind:value={ interp } inFunc={ () => update(false) } min={0.0} max={3.0} step={0.005} />
        <div id="view" bind:this={container} bind:offsetHeight={height} bind:offsetWidth={width}></div>
    </div>
</Container>


<style>
    #view {
        height: 600px;
        width: 100%;
    }

    #main {
        display: flex;
        flex-direction: column;
    }
</style>