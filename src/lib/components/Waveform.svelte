<script>
    import { onMount } from "svelte";
    import { browser } from "$app/env";

    export let segments;
    export let title = "title";
    export let file;
    export let peaks;
    export let id = "";

    let Peaks;
    let instance;
    let overview;
    let zoom;
    let audio;
    let controls;
    let peaksControls;
    let zoomIn;
    let zoomOut;

    function handleZoomIn () {instance.zoom.zoomIn()}
    function handleZoomOut () {instance.zoom.zoomOut()}
    function handleMouseEnter() {hovered = true}
    function handleMouseLeave() {hovered = false}

    const convert = (time) => {
        const date = new Date(time * 1000).toISOString().substr(11, 8)
        return date.toString().substr(3);
    }

    onMount (async()=>{
        if (browser) {
            const module = await import("peaks.js");
            Peaks = module.default;

            instance = Peaks.init({
                containers: {
                    zoomview: zoom,
                    overview: overview
                },
                dataUri: { 
                    arraybuffer: peaks 
                },
                mediaElement: audio,
                height: 60,
                segmentStartMarkerColor: '#a0a0a0',
                segmentEndMarkerColor: '#a0a0a0',
                zoomWaveformColor: 'rgba(0, 30, 128, 0.61)',
                overviewWaveformColor: 'rgba(0, 15, 100, 0.3)',
                overviewHighlightColor: 'grey',
                segmentColor: 'rgba(255, 161, 39, 1)',
                playheadColor: 'rgba(0, 0, 0, 1)',
                playheadTextColor: '#aaa',
                showPlayheadTime: false,
                pointMarkerColor: '#FF0000',
                axisGridlineColor: '#ccc',
                axisLabelColor: '#aaa',
                randomizeSegmentColor: true,
                segments: segments
            })
        }
    });


</script>

<style>
    .audio-box {
        padding-top: 20px;
        margin-top: 20px;
        padding-bottom: 20px;
        border-radius: 12px;
        border: 3px solid rgba(128, 128, 128, 0.575);
        transition: border .5s;
    }

    .audio-box:hover {
        border: 3px solid #2b5aa1a2;
        transition: border .5s;
        gap: 3px;
    }

    .audio-controls {
        display: grid;
        grid-template-columns: auto auto auto;
        gap : 5px;
    }

    .btn {
        position: relative;
        width: 2em;
        height: 2em;
        padding: 5px;
        font-size: 15px;
        overflow: hidden;
        border-width: 0;
        outline: none;
        border-radius: 1px;
        box-shadow: 0 1px 4px rgba(0, 0, 0, .6);    
        color: #ecf0f1;
        transition: background-color .25s;
    }

    .btn:before {
        content: "";
        
        position: absolute;
        top: 50%;
        left: 50%;
        
        display: block;
        width: 0;
        padding-top: 0;
        
        border-radius: 100%;
        
        background-color: rgba(236, 240, 241, .3);
        
        -webkit-transform: translate(-50%, -50%);
        -moz-transform: translate(-50%, -50%);
        -ms-transform: translate(-50%, -50%);
        -o-transform: translate(-50%, -50%);
        transform: translate(-50%, -50%);
    }
    
    .btn:active:before {
        width: 120%;
        padding-top: 120%;
        
        transition: width .2s ease-out, padding-top .2s ease-out;
    }

    .zoom {
        background-color: darkcyan;
        font-weight: bold;
        font-size: 15px;
        width: 2em;
    }
    .zoom:hover, .zoom:focus {
        background-color: rgb(2, 196, 196);
    }

    .overview {
        margin-left: 3em;
        margin-right: 3em;
    }

    #title {
        font-style: italic;
        font-size: 16px;
        text-align: center;
        display: inline-block;
    }

    .horizontal {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        height: 10%;
        padding-bottom: 15px;
    }

    .vis {
        padding-bottom: 5px;
        margin: 0 auto;
    }

    .peaks-controls {
        display: flex;
        justify-content: center;
        padding-top: 3px;
    }

    ul li {
        display: block;
    }

    a { 
        color: black;
    }

    #timecodes {
        font-weight: bold;
    }

    .segments {
        padding-top: 5px;
        margin: 1em auto;
        margin-right: 3em;
    }
</style>

<div class="audio-box" id={id}>
    <div class="horizontal overview">
        <span id="title">{title}</span>
        <div bind:this={controls} class="audio-controls">
            <button bind:this={zoomIn} on:click={handleZoomIn} class="btn zoom">+</button>
            <button bind:this={zoomOut} on:click={handleZoomOut} class="btn zoom">-</button>
        </div>
    </div>
    <div class="vis">
        <div class="overview" bind:this={overview} />
        <div class="overview" bind:this={zoom} />
    </div>
    <div class="peaks-controls" bind:this={peaksControls}>
        <audio controls bind:this={audio}>
            <source src={file} type="audio/mp3">
            <track kind="captions">
        </audio>
    </div>
    {#if segments}
    <ul class="segments">
        <span id="timecodes">List of referenced time codes</span>
        <hr>
        {#each segments as segment}
            <li>
                <a on:click={() => instance.player.seek(segment.startTime)}>
                    {convert(segment.startTime)} - {convert(segment.endTime)} | {segment.labelText}
                </a>
            </li>
        {/each}
    </ul>
    {/if}
</div>


    