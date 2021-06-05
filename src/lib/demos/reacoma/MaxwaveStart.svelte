<script>
    import { onMount } from "svelte";
    import Container from '$lib/components/Container.svelte';
    import Button from '$lib/components/Button.svelte';
    export let title = "NMF"
    export let caption = 'DEMO 1';
    export let id = 'demox';

    const prefix = '/tech-reacoma/dotmaxwave/';
    const pre = 'unprocessed';
    const post = 'processed';

    const sel = '#0d47a1';
    const nosel = 'rgba(0, 15, 100, 0.3)';

    let lastSelected = 'pre';

    const sounds = {
        pre: {
            audio: prefix + pre + '.mp3',
            peaks: prefix + pre + '.dat',
            instance: null,
            overview: null,
            audioElement: null,
            displayName: 'Raw Source'
        },
        post: {
            audio: prefix + post + '.mp3',
            peaks: prefix + post + '.dat',
            instance: null,
            overview: null,
            audioElement: null,
            displayName: 'Processed with HPSS'
        },
    }

    let selectedComponent = sounds.pre.displayName;
    let Peaks;

    onMount (async () => {
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
                    if (key === 'pre') {
                        const view = sounds[key].instance.views.getView('overview');
                        view.setWaveformColor('#0d47a1');
                    } else {
                        sounds[key].audioElement.volume = 0.0;
                    }
                }
            });
        }
    });

    let playState = false
    $: playStateText = playState === false ? 'Play' : 'Pause'

    function playStateHandler() {

        if (playState) {
            sounds.pre.instance.player.pause();
            sounds.post.instance.player.pause();
        } else {
            sounds.pre.instance.player.play();
            sounds.post.instance.player.play();
        }
        playState = !playState
    }

    function handleClick(component) {
        lastSelected = component;
        selectedComponent = sounds[component].displayName
        const currentTime = sounds[component].instance.player.getCurrentTime();

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

    function seekView(seek, component) {
        // Check if currently selected

        if (component === lastSelected) {
            for (const [name, c] of Object.entries(sounds)) {   
                if (name != component)
                    c.instance.player.seek(seek.target.currentTime);
            } 
        }
    }
</script>

<Container id={id}>
    <div class="horizontal">
        <span id="title">{title}</span>
        <span id="caption">{caption}</span>
    </div>

    <div class="horizontal">
        <Button 
        clickHandler={ playStateHandler }
        text={ playStateText }
        />
        <span id='selected-component'>{ selectedComponent }</span>
    </div>


    <div class="vis">
        <div 
        class='overview' 
        bind:this={sounds.pre.overview} 
        on:mousedown={ () => handleClick('pre') }
        />
        
        <div 
        class='overview' 
        bind:this={sounds.post.overview} 
        on:mousedown={ () => handleClick('post') }
        />
    </div>


    <audio 
    bind:this={sounds.pre.audioElement} 
    on:ended={ () => playState = false }
    on:seeking={ (seek) => seekView(seek, 'pre') }
    >
        <source src={sounds.pre.audio} type="audio/mp3">
        <track kind='captions' />
    </audio>

    <audio 
    bind:this={sounds.post.audioElement} 
    on:ended={ () => playState = false }
    on:seeking={ (seek) => seekView(seek, 'post') }
    >
        <source src={sounds.post.audio} type="audio/mp3">
        <track kind='captions' />
    </audio>
</Container>

<style>
    
    #title {
        text-align: left;
        font-weight: bold;
    }

    .overview {
        height: 100px;
    }

    #selected-component {
        color: grey;
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
        gap: 8px;
        padding-bottom: 15px;
    }
    
    .vis {
        padding-bottom: 5px;
        display: flex;
        flex-direction: column;
        gap: 5px;
    }
</style>


    