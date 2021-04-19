<script>
    import { onMount } from 'svelte';
    import * as Tone from 'tone';
    import Slider from '$lib/components/Slider.svelte';

    import PlayButton from "$lib/components/PlayButton.svelte";

    let playing = false;
    let masterGain;
    let perc;
    let harm;
    let percVol;
    let harmVol;
    let balance = 100;
    let masterGainVol = 100;

    onMount(async () => {
        masterGain = new Tone.Gain(1).toDestination();
        harmVol = new Tone.Gain(1).connect(masterGain);
        percVol = new Tone.Gain(1).connect(masterGain);
        harm = new Tone.Player("/content-awareness/hpss/019-h.wav").connect(harmVol);
        perc = new Tone.Player("/content-awareness/hpss/019-p.wav").connect(percVol);
        harm.loop = true;
        perc.loop = true;
    });

    const playback = () => {
        playing = !playing;
        if (playing) {
            perc.start();
            harm.start();
        } else {
            perc.stop();
            harm.stop();
        }
    };

    const updateVolume = () => {
        harmVol.gain.rampTo(balance / 100.0, 0.05);
        percVol.gain.rampTo(1 - (balance / 100.0), 0.05);
    };

    const updateMasterGain = () => {
        masterGain.gain.rampTo(masterGainVol / 100.0, 0.05);
    }
</script>

<div class="meta">
    <div class="demo">
        <div class="play-explanation">
            <p>Press the play button and move the slider to change the balance between harmonic and percussive.</p>
            <PlayButton state={playing} playFunc={playback}/>
        </div>
    
        <div class="volume">
            <span class="text-span">percussive</span> 
            <Slider min="0" max="100" func={updateVolume} bind:value={balance} />
            <span class="text-span">harmonic</span>
        </div>
    </div>
    <div class="masterGain">
        <input type="range" min=0 max=100 on:input={updateMasterGain} bind:value={masterGainVol} />
    </div>
</div>



<style>

    p {text-align: center}

    .meta {
        display: flex;
        flex-direction: row; 
        border: 1px solid grey;
        border-radius: 3px;
        max-width: 50%;
        margin-left: 25%;
        margin-right: 25%;
        max-width: 50%;
        margin-top: 30px;
        margin-bottom: 30px;

    }

    .demo {
        display: flex;
        flex-direction: column;

    }

    .play-explanation {
        display: flex;
        flex-direction: column;
        padding: 10px;
        align-self: center;
    }

    .volume {
        display: flex;
        flex-direction: row;
        padding-bottom: 10px;
        align-self: center;
        justify-content: center;
    }



    .text-span {
        padding-left: 8px;
        padding-right: 8px;
        flex-grow: 1;
        text-align: center;
    }
</style>