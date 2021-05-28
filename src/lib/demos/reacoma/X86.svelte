<script>
    import { onMount } from 'svelte';
    import Button from '$lib/components/Button.svelte';
    import Container from '$lib/components/Container.svelte';
    export let id = "";
    export let title = "";
    export let caption = ""
    
    const rAudio = '/reacoma/x86/residu.mp3'
    const tAudio = '/reacoma/x86/transi.mp3'
    const rData = '/reacoma/x86/residu.dat'
    const tData = '/reacoma/x86/transi.dat' 
    
    let instance, Peaks;
    let zoom, overview, controls, audio, controller;
    let whichSource = 'residual';
    
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

            instance.player.play();
        }
    }
    
    
    onMount(async() => {
        const options = {
            containers: {
                zoomview: zoom,
                overview: overview
            },
            dataUri: { arraybuffer: rData },
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
    <div id='top-text'>
        <span id="title">{title}</span>
        <span id="caption">{caption}</span>
    </div>
    <div id='comment'>
        Choose either the transient and residual components by clicking the respective button. Playback will be paused between selections.
    </div>
    <div class="horizontal">
        <div>
            <Button selected={ whichSource === 'residual' } clickHandler={ () => setSource(rAudio, rData, 'residual') } text="Residual Component" />
            <Button selected={ whichSource === 'transient' } clickHandler={ () => setSource(tAudio, tData, 'transient') } text="Transient Component" />
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
            <source bind:this={controller} src={rAudio} type="audio/mp3">
            <track kind="captions">
        </audio>
    </div>
</Container>

        
<style>
    
    .audio-controls {
        display: flex;
        flex-direction: row;
        gap : 5px;
    }

    #top-text {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    
    #title {
        font-weight: bold;
    }
    
    #caption{
        font-style: italic;
        font-size: 16px;
        text-align: center;
        display: inline-block;
    }

    #comment {
        padding-top: 10px;
        padding-bottom: 20px;
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
        