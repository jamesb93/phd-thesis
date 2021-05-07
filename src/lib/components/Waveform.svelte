<script>
    import { onMount } from "svelte";
    import { browser } from "$app/env";
    import Button from '$lib/components/Button.svelte';

    export let segments;
    export let title = "title";
    export let caption = null;
    export let file;
    export let peaks;
    export let id = "";

    let Peaks;
    let instance, overview, zoom, audio, controls;
    let peaksControls;

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
</script>

<div class="audio-box" id={id}>
    <div class="horizontal overview">
        <span id="title">{title}</span>
        {#if caption}
        <span id="caption">{caption}</span>
        {/if}
        <div bind:this={controls} class="audio-controls">
            <Button clickHandler={ () => instance.zoom.zoomOut() } text="+" />
            <Button clickHandler={ () => instance.zoom.zoomIn() } text="-" />
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
                <a on:click={ () => instance.player.seek(segment.startTime) }>
                    {convert(segment.startTime)} - {convert(segment.endTime)} | {segment.labelText}
                </a>
            </li>
        {/each}
    </ul>
    {/if}
</div>

<style>
 .audio-box {
        padding-top: 20px;
        margin-top: 20px;
        margin-bottom: 20px;
        padding-bottom: 20px;
        border-radius: 12px;
        border: 3px solid rgba(128, 128, 128, 0.575);
        transition: border .5s;
        padding-left: 20px;
        padding-right: 20px;

    }
    
    .audio-box:hover {
        border: 3px solid #2b5aa1a2;
        transition: border .5s;
        gap: 3px;
    }
    
    .audio-controls {
        display: flex;
        flex-direction: row;
        gap : 5px;
    }
    
    #title {
        font-style: italic;
        font-size: 16px;
        text-align: center;
        display: inline-block;
    }
    
    #caption{
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
    
    #timecodes {
        font-weight: bold;
    }

    ul li {
        display: block;
    }

    a { 
        color: black;
    }

    .segments {
        padding-top: 5px;
        margin: 1em auto;
        margin-right: 3em;
    }
</style>


    