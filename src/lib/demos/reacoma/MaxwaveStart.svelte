<script>
    import { onMount } from 'svelte';
    import Button from '$lib/components/Button.svelte';
    import Container from '$lib/components/Container.svelte';
    export let id = "";
    export let title = "";
    
    const originalAudio = '/reacoma/dotmaxwave/unprocessed.mp3'
    const originalData = '/reacoma/dotmaxwave/unprocessed.dat'
    const processedAudio = '/reacoma/dotmaxwave/processed.mp3'
    const processedData = '/reacoma/dotmaxwave/processed.dat'
    
    let instance, Peaks;
    let zoom, overview, controls, audio, controller;
    let whichSource = 'original';
    
    function setSource(audio, buffer, src) {
        if (whichSource !== src) {
            whichSource = src;
            const options = {
                mediaUrl: audio,
                dataUri: { arraybuffer: buffer },
            };
            instance.setSource(options, err => {
                if (err) console.log(err)
            });
        }
    }
    
    onMount(async() => {
        const options = {
            containers: {
                zoomview: zoom,
                overview: overview
            },
            dataUri: { arraybuffer: originalData },
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
            segments: null
        }
        const module = await import("peaks.js");
        Peaks = module.default;
        
        Peaks.init(options, (err, p) => {
            if (err) {  
                console.log(err)
            } else {
                instance = p
            }
        });
    })
    
</script>

<Container id={id}>
<div class="audio-box">
    <div>
        <span id="title">{title}</span>
        <p>
            Alternate between the transient and residual components by clicking the respective button.
        </p>
    </div>
    <div class="horizontal">
        <div>
            <Button selected={whichSource === 'original'} clickHandler={ () => setSource(originalAudio, originalData, 'original') } text="Unprocessed Source" />
            <Button selected={whichSource === 'processed'} clickHandler={ () => setSource(processedAudio, processedData, 'processed') } text="HPSS Processed Source" />
        </div>
        <div bind:this={controls} class="audio-controls">
            <Button clickHandler={ () => instance.zoom.zoomOut() } text="+" />
            <Button clickHandler={ () => instance.zoom.zoomIn() } text="-" />
        </div>
    </div>
    <div class="vis">
        <div bind:this={overview} />
        <div bind:this={zoom} />
    </div>
    <div class="peaks-controls">
        <audio controls bind:this={audio}>
            <source bind:this={controller} src={originalAudio} type="audio/mp3">
            <track kind="captions">
        </audio>
    </div>
</div>
</Container>

        
<style>
    
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

</style>
        