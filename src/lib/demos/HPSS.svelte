<script>
    import { onMount } from 'svelte';
    import * as Tone from 'tone';
    import Slider from '$lib/components/Slider.svelte';
    import PlayButton from "$lib/components/PlayButton.svelte";
    import Container from '$lib/components/Container.svelte';

    export let caption = 'DEMO 1'
    export let title = 'Interactive audition of harmonic-percussive source separation'
    export let id = 'demox'

    let harmReady = false; 
    let percReady = false;
    let harmPlayer; 
    let percPlayer;
    let percVol; let harmVol;
    let balance = 50;
    let playing = false;

    onMount(() => {
        harmVol = new Tone.Gain(1).toDestination();
        percVol = new Tone.Gain(1).toDestination();

        harmPlayer = new Tone.Player("/content-awareness/hpss/019-h.mp3", harmReady = true)
            .connect(harmVol);
        percPlayer = new Tone.Player("/content-awareness/hpss/019-p.mp3", percReady = true)
            .connect(percVol);

        harmPlayer.loop = true;
        percPlayer.loop = true;
    });

    function playback() {
        if (harmPlayer.state === 'started' || percPlayer.state === 'started') {
            playing = false;
            harmPlayer.stop();
            percPlayer.stop();
        } else {
            playing = true;
            harmPlayer.start();
            percPlayer.start();
        }
    };

    function updateVolume() {
        harmVol.gain.rampTo(balance / 100.0, 0.05);
        percVol.gain.rampTo(1 - (balance / 100.0), 0.05);
    };
</script>

<Container id={id}>
    {#if harmReady && percReady}
    <div class="demo">
        <p class="cap">{caption}: {title}</p>

        <PlayButton playFunc={playback} state={playing}/>
        <div class="volume">
            <span class="text-span">percussive</span> 
            <Slider showValue={false} min="0" max="100" showMin={false} showMax={false} inFunc={updateVolume} bind:value={balance} />
            <span class="text-span">harmonic</span>
        </div>
        <div id='instructions'>Click the play button and then adjust the balance of the harmonic and percussive components using the slider.</div>
    </div>
    {:else}
    loading...
    {/if}
</Container>
    
    

<style>
    .demo {
        display: flex;
        flex-direction: column;
        justify-content: center;
        align-items: center;
        gap: 5px;
    }

    .cap {
        width: 100%;
        font-style: italic;
        text-align: center;
    }

    #instructions {
        color: grey;
        text-align: center;
    }

    .volume {
        display: flex;
        flex-direction: row;
        padding-bottom: 10px;
        align-items: center;
    }
</style>