<!-- 
    Two Streams of audio simultaneously playing with waveform visualisation
    can mute/unmute separate streams
    they both start unmuted
 -->

 <script>
    import { onMount } from "svelte";
    import Container from '$lib/components/Container.svelte';
    import Button from '$lib/components/Button.svelte';
    export let title = "Separation of transients in residual in sys.ji_"
    export let caption = 'DEMO 1';
    export let id = 'DEMO 1';

    let selectedComponent = 'transient'
    const prefix = '/tech-reacoma/'
    const transient = 'sysji-transient'
    const residual = 'sysji-residual'
    const summed = 'sysji-ramp'

    const sounds = {
        transient: {
            audio: prefix + transient + '.mp3',
            peaks: prefix + transient + '.dat',
            instance: null,
            overview: null,
            audioElement: null
        },
        residual: {
            audio: prefix + residual + '.mp3',
            peaks: prefix + residual + '.dat',
            instance: null,
            overview: null,
            audioElement: null
        },
        summed: {
            audio: prefix + summed + '.mp3',
            peaks: prefix + summed + '.dat',
            instance: null,
            overview: null,
            audioElement: null
        }
    }

    let Peaks;

    onMount ( async () => {
        const module = await import("peaks.js");
        Peaks = module.default;

        for ( const [key, component] of Object.entries(sounds)) {
            const options = {
                containers: {
                    overview: component.overview
                },
                dataUri: { 
                    arraybuffer: component.peaks
                },
                mediaElement: component.audioElement,
                overviewWaveformColor: 'rgba(0, 15, 100, 0.3)',
                overviewHighlightColor: 'grey',
                playheadColor: 'rgba(0, 0, 0, 1)',
                playheadTextColor: '#aaa',
                showPlayheadTime: false,
                pointMarkerColor: '#FF0000',
                axisGridlineColor: '#ccc',
                axisLabelColor: '#aaa',
                randomizeSegmentColor: true,
            }
            sounds[key].instance = Peaks.init(options, (err, p) => {
                if (err) {
                    console.log(err)
                } else {
                    sounds[key].instance = p
                    sounds[key].instance.views.getView('overview').fitToContainer();
                    if (key === 'transient') {
                        const view = sounds[key].instance.views.getView('overview');
                        view.setWaveformColor('#0d47a1');
                    } else {
                        sounds[key].audioElement.volume = 0.0;
                    }
                }
            });
        }
    });

    let playState = false;
    $: playStateText = playState === false ? 'play' : 'pause'

    function playStateHandler() {

        if (playState) {
            sounds.transient.instance.player.pause();
            sounds.residual.instance.player.pause();
            sounds.summed.instance.player.pause();
        } else {
            sounds.transient.instance.player.play();
            sounds.residual.instance.player.play();
            sounds.summed.instance.player.play();
        }

        playState = !playState
    }

    function handleClick(component) {
        sounds.transient.instance.player.play();
        sounds.residual.instance.player.play();
        sounds.summed.instance.player.play();
        playState = true;
        const sel = '#0d47a1';
        const nosel = 'rgba(0, 15, 100, 0.3)';
        const currentTime = sounds[component].instance.player.getCurrentTime();

        selectedComponent = component

        for (const [name, c] of Object.entries(sounds)) {    
            if (name === component) {
                c.audioElement.volume = 1.0;
                c.instance.views.getView('overview').setWaveformColor(sel);
            } else {
                c.audioElement.volume = 0.0;
                c.instance.views.getView('overview').setWaveformColor(nosel);
                c.instance.player.seek(currentTime);
            }
        } 
    }
</script>

<Container id={id}>
    <div class="horizontal">
        <span id="title">{title}</span>
        <span id="caption">{caption}</span>
        { selectedComponent }
    </div>

    <Button 
    clickHandler={ playStateHandler }
    text={ playStateText }
    />
    <div class="vis">
        <div 
        id='residual-overview' 
        class='overview' 
        bind:this={sounds.residual.overview} 
        on:mousedown={ () => handleClick('residual') }
        on:mouseup={ () => handleClick('residual') }
        />

        <div 
        id='transient-overview' 
        class='overview' 
        bind:this={sounds.transient.overview} 
        on:mousedown={ () => handleClick('transient') }
        on:mouseup={ () => handleClick('transient') }
        />

        <div 
        id='summed-overview' 
        class='overview' 
        bind:this={sounds.summed.overview} 
        on:mousedown={ () => handleClick('summed') }
        on:mouseup={ () => handleClick('summed') }
        />
    </div>


    <audio bind:this={sounds.transient.audioElement}>
        <source src={sounds.transient.audio} type="audio/mp3">
    </audio>

    <audio bind:this={sounds.residual.audioElement}>
        <source src={sounds.residual.audio} type="audio/mp3">
    </audio>

    <audio bind:this={sounds.summed.audioElement}>
        <source src={sounds.summed.audio} type="audio/mp3">
    </audio>
</Container>

<style>
    
    #title {
        text-align: left;
        font-weight: bold;
    }

    .overview {
        height: 50px;
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
        gap: 10%;
        padding-bottom: 15px;
    }
    
    .vis {
        padding-bottom: 5px;
        display: flex;
        flex-direction: column;
        gap: 5px;
    }
</style>


    