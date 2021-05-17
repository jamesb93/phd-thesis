<script>
    import { onMount } from "svelte";
    import { browser } from "$app/env";
    import Container from '$lib/components/Container.svelte';
    import Button from '$lib/components/Button.svelte';

    export let segments;
    export let title = "title";
    export let caption = "";
    export let file;
    export let peaks;
    export let id = "";

    let Peaks;
    let instance, overview, zoom, audio, controls;
    let peaksControls;
    let lastSelected = 0;

    const convert = (time) => {
        const date = new Date(time * 1000).toISOString().substr(11, 8)
        return date.toString().substr(3);
    }

    onMount (async()=>{
        if (browser) {
            const module = await import("peaks.js");
            Peaks = module.default;
            const options = {
                containers: {
                    zoomview: zoom,
                    overview: overview
                },
                dataUri: { 
                    arraybuffer: peaks 
                },
                mediaElement: audio,
                height: 60,
                zoomWaveformColor: 'rgba(0, 30, 128, 0.61)',
                overviewWaveformColor: 'rgba(0, 15, 100, 0.3)',
                overviewHighlightColor: 'grey',
                playheadColor: 'rgba(0, 0, 0, 1)',
                playheadTextColor: '#aaa',
                showPlayheadTime: false,
                pointMarkerColor: '#FF0000',
                axisGridlineColor: '#ccc',
                axisLabelColor: '#aaa',
                randomizeSegmentColor: true,
                segments: segments
            }
            instance = Peaks.init(options, (err, p) => {
                if (err) {
                    console.log(err)
                } else {
                    instance = p
                }
            })
        }
    });

    function clickHandler(segment, i) {
        instance.player.seek(segment.startTime)
        lastSelected = i
    }
</script>

<Container id={id}>
    <div class="horizontal overview">
        <span id="title">{title}</span>
        <span id="caption">{caption}</span>

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
        <div bind:this={controls} class="audio-controls">
            <Button clickHandler={ () => instance.zoom.zoomIn() } text="+" />
            <Button clickHandler={ () => instance.zoom.zoomOut() } text="-" />
        </div>
    </div>
    {#if segments}
    <ul class="segments">
        <span id="timecodes">List of referenced time codes</span>
        {#each segments as segment, i}
            <li>
                    <a class:selected={ lastSelected === i } class='timecode' on:click={ () => clickHandler(segment, i) }>
                        <span>{convert(segment.startTime)} - {convert(segment.endTime)}</span>
                        <span id="label">{segment.labelText}</span>
                    </a>
            </li>
        {/each}
    </ul>
    {/if}
</Container>

<style>
    
    .audio-controls {
        display: flex;
        flex-direction: row;
    }
    
    #title {
        text-align: left;
        font-weight: bold;
    }
    
    #caption{
        display: inline-block;
        font-style: italic;
        min-width: max-content;
    }
    
    .horizontal {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding-bottom: 15px;
    }
    
    .vis {
        padding-bottom: 5px;
        margin: 0 auto;
    }
    
    .peaks-controls {
        display: flex;
        justify-content: space-between;
        padding-top: 3px;
    }
    
    #timecodes {
        font-weight: bold;
    }

    ul li {
        display: block;
        border-top: 1px rgb(197, 197, 197) solid;
    }

    ul li:hover {
        background-color: rgb(240, 240, 240);
    }

    a { 
        color: black
    }

    a:hover {
        background-color: inherit;
        text-decoration: none;
    }

    .timecode {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        margin-right: 10px;
    }

    .selected {
        font-weight: bold;
    }

    #label {
        color: grey;
    }

    .segments {
        padding-top: 5px;
        margin: 1em auto;
        margin-right: 3em;
        border-top: 1px rgb(197, 197, 197) solid;
        justify-content: space-between;
    }
</style>


    