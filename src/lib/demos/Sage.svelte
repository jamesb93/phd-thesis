<script>
    import { onMount } from "svelte";
    import { browser } from "$app/env";


    export let title = "title";
    export let file1;
    export let file2
    export let peaks1;
    export let peaks2;
    export let segs1;
    export let segs2;
    export let id = "";

    let Peaks;
    let unshuffled;
    let shuffled;
    let unshuffledOverview;
    let shuffledOverview;
    let audio1;
    let audio2;
    let peaksControls;

    onMount (async()=>{
        if (browser) {
            try {
                const module = await import("peaks.js");
                Peaks = module.default;
    
                unshuffled = Peaks.init({
                    containers: {overview: unshuffledOverview},
                    dataUri: {arraybuffer: peaks1},
                    mediaElement: audio1,
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
                    segments: segs1
                })
    
                shuffled = Peaks.init({
                    containers: {overview: shuffledOverview},
                    dataUri: {arraybuffer:  peaks2},
                    mediaElement: audio2,
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
                    segments: segs2
                })
            } catch (err) {
                console.error(err);
            }
        }
    });


</script>

<div class="audio-box" id={id}>
    <div class="vis">
        <div class="overview" bind:this={unshuffledOverview} />
        <div class="overview" bind:this={shuffledOverview} />
    </div>
    <div class="peaks-controls" bind:this={peaksControls}>
        <audio controls bind:this={audio1}>
            <source src={file1} type="audio/mp3">
            <track kind="captions">
        </audio>
        <audio controls bind:this={audio2}>
            <source src={file2} type="audio/mp3">
            <track kind="captions">
        </audio>
    </div>
</div>

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

    .vis {
        padding-bottom: 5px;
        margin: 0 auto;
    }

    .peaks-controls {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 3px;
        width: 80%;
        margin: 0 auto;
    }
</style>


    