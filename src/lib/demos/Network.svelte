

<script>

    // TODO https://www.chartjs.org/docs/latest/general/responsive.html
    import * as THREE from "three";
    import * as d3 from "d3";
    import {onMount} from "svelte";
    let container;

    onMount(() => {
        const scene = new THREE.Scene();
        const raycaster = new THREE.Raycaster()
        const hoverContainer = new THREE.Object3D()
        const renderer = new THREE.WebGLRenderer();
        const circle_sprite = new THREE.TextureLoader().load(
            "/circle-sprite.png"
        )   

        let pointSize = 1;
        var points;
        let width = container.offsetWidth;
        let height = window.offsetHeight;
        renderer.setSize(width, height);
        let viz_width = width;
        // Camera Parameters
        let fov = 40;
        let near = 10;
        let far = 7000;
        let radius = 2000;

        raycaster.params.Points.threshold = 10;
        const camera = new THREE.PerspectiveCamera(
            fov,
            width/height,
            near,
            far
        );

        window.addEventListener('resize', () => {
            width = window.innerWidth;
            viz_width = width;
            height = window.innerHeight;
            
            renderer.setSize(width, height);
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
        })

        container.appendChild(renderer.domElement);

        // Zooming
        let zoom = d3.zoom()
        .scaleExtent([getScaleFromZ(far), getScaleFromZ(near)])
        .on('zoom', () =>  {
            var d3_transform = d3.event.transform;
            zoomHandler(d3_transform);
        });

        let view = d3.select(renderer.domElement);
        function setUpZoom() {
            view.call(zoom);    
            let initial_scale = getScaleFromZ(far);
            var initial_transform = d3.zoomIdentity.translate(viz_width/2, height/2).scale(initial_scale);    
            zoom.transform(view, initial_transform);
            camera.position.set(0, 0, far);
        }
        setUpZoom();

        var data;
        function loadData(json) {
            data = json.data;
            console.log(data);
            init();
            animate();
        }

        fetch("/plots/plot.json")
            .then(response => response.json())
            .then(json => loadData(json));

        function init(json) {
            var colors = new Float32Array(data.length * 2);
            var coords = new Float32Array(data.length * 2);
            var sizes  = new Float32Array(data.length * 2);

            for (var i=0; i < data.length; i++) {
                coords[i*2 + 0] = (data[i].x * radius) - (radius * 0.5)
                coords[i*2 + 1] = (data[i].y * radius) - (radius * 0.5)
                sizes[i] = pointSize;
                if (coords[i*2 +0] == NaN || coords[i*2+1] == NaN) {
                    console.log(coords[i*2+0]);
                    console.log(coords[i*2+1]);
                }
                var color = new THREE.Color();
                color.setHSL(0.5, 0.5, 0.7);
                color.toArray(colors, i*2)
            };
            // let pointsGeometry = new THREE.Geometry();
            var pointsGeometry = new THREE.BufferGeometry();
            pointsGeometry.setAttribute( 'position', new THREE.BufferAttribute(coords, 2));
            pointsGeometry.setAttribute( 'customColor', new THREE.BufferAttribute(colors, 3));
            pointsGeometry.setAttribute( 'size', new THREE.BufferAttribute(sizes, 1));
            
            // let colors = [];
            // for (var datum of data_points) {
            //     // Set vector coordinates from data
            //     var vertex = new THREE.Vector3(datum.position[0], datum.position[1], 0);
            //     pointsGeometry.vertices.push(vertex);
            //     var color = new THREE.Color(color_array[datum.group]);
            //     colors.push(color);
            // }
            // pointsGeometry.colors = colors;
            
            var pointsMaterial = new THREE.PointsMaterial({
                size: 8,
                sizeAttenuation: false,
                vertexColors: THREE.VertexColors,
                map: circle_sprite,
                transparent: true
            });
            
            points = new THREE.Points(pointsGeometry, pointsMaterial);
            
            scene.add(points);
        }
        scene.background = new THREE.Color(0xefefef);
        scene.add(hoverContainer);

        function onWindowResize() {
            camera.aspect = width / height;
            camera.updateProjectionMatrix();
            renderer.setSize(width, height);
        }

        // Three.js render loop
        function animate() {
            requestAnimationFrame(animate);
            render()
        }

        function render() {
            renderer.render(scene, camera);
        }
        animate();

        function zoomHandler(d3_transform) {
            let scale = d3_transform.k;
            let x = -(d3_transform.x - viz_width/2) / scale;
            let y = (d3_transform.y - height/2) / scale;
            let z = getZFromScale(scale);
            camera.position.set(x, y, z);
        }

        function getScaleFromZ (camera_z_position) {
            let half_fov = fov/2;
            let half_fov_radians = toRadians(half_fov);
            let half_fov_height = Math.tan(half_fov_radians) * camera_z_position;
            let fov_height = half_fov_height * 2;
            let scale = height / fov_height; // Divide visualization height by height derived from field of view
            return scale;
        }

        function getZFromScale(scale) {
            let half_fov = fov/2;
            let half_fov_radians = toRadians(half_fov);
            let scale_height = height / scale;
            let camera_z_position = scale_height / (2 * Math.tan(half_fov_radians));
            return camera_z_position;
        }

        function toRadians (angle) {
            return angle * (Math.PI / 180);
        }

        // Hover and tooltip interaction
        function sortIntersectsByDistanceToRay(intersects) {
            return _.sortBy(intersects, "distanceToRay");
        }

        function checkIntersects(mouse_position) {
            var mouse_vector = mouseToThree(...mouse_position);
            raycaster.setFromCamera(mouse_vector, camera);
            var intersects = raycaster.intersectObject(points);
            
            if (intersects[0]) {
                let sorted_intersects = sortIntersectsByDistanceToRay(intersects);
                let intersect = sorted_intersects[0];
                let index = intersect.index;
                let datum = data_points[index];
                highlightPoint(datum);
                showTooltip(mouse_position, datum);
            } else {
                removeHighlights();
                hideTooltip();
            }
        }

        view.on("mousemove", () => {
            let [mouseX, mouseY] = d3.mouse(view.node());
            let mouse_position = [mouseX, mouseY];
            checkIntersects(mouse_position);
        });

        function mouseToThree(mouseX, mouseY) {
            return new THREE.Vector3(
                mouseX / viz_width * 2 - 1,
                -(mouseY / height) * 2 + 1,
                1
            );
        }

        function highlightPoint(datum) {
            removeHighlights();
            
            let geometry = new THREE.Geometry();
            geometry.vertices.push(
                new THREE.Vector3(
                    datum.position[0],
                    datum.position[1],
                    0
                )
            );
            geometry.colors = [ new THREE.Color(color_array[datum.group]) ];
            
            let material = new THREE.PointsMaterial({
                size: 26,
                sizeAttenuation: false,
                vertexColors: THREE.VertexColors,
                map: circle_sprite,
                transparent: true
            });
            
            let point = new THREE.Points(geometry, material);
            hoverContainer.add(point);
        }

        function removeHighlights() {
            hoverContainer.remove(...hoverContainer.children);
        }

        view.on("mouseleave", () => {
            removeHighlights()
        });

        // Initial tooltip state
        let tooltip_state = { display: "none" }

        let tooltip_template = document.createRange().createContextualFragment(`<div id="tooltip" style="display: none; position: absolute; pointer-events: none; font-size: 13px; width: 120px; text-align: center; line-height: 1; padding: 6px; background: white; font-family: sans-serif;">
            <div id="point_tip" style="padding: 4px; margin-bottom: 4px;"></div>
            <div id="group_tip" style="padding: 4px;"></div>
        </div>`);
        document.body.append(tooltip_template);

        let $tooltip = document.querySelector('#tooltip');
        let $point_tip = document.querySelector('#point_tip');
        let $group_tip = document.querySelector('#group_tip');

        function updateTooltip() {
            $tooltip.style.display = tooltip_state.display;
            $tooltip.style.left = tooltip_state.left + 'px';
            $tooltip.style.top = tooltip_state.top + 'px';
            $point_tip.innerText = tooltip_state.name;
            $point_tip.style.background = color_array[tooltip_state.group];
            $group_tip.innerText = `Group ${tooltip_state.group}`;
        }

        function showTooltip(mouse_position, datum) {
            let tooltip_width = 120;
            let x_offset = -tooltip_width/2;
            let y_offset = 30;
            tooltip_state.display = "block";
            tooltip_state.left = mouse_position[0] + x_offset;
            tooltip_state.top = mouse_position[1] + y_offset;
            tooltip_state.name = datum.name;
            tooltip_state.group = datum.group;
            updateTooltip();
        }

        function hideTooltip() {
            tooltip_state.display = "none";
            updateTooltip();
        }

    })
</script>

<div bind:this={container}></div>