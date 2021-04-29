<script>

    import * as Tone from 'tone';
    import { browser } from '$app/env';
    let ready = false;
    let sampler, loop;
    if (browser) {
        sampler = new Tone.Sampler({
            urls: {
                A1: "58.mp3",
                A2: "95.mp3",
                A3: "659.mp3",
                A4: "1569.mp3",
                A5: "1780.mp3",
                A6: "1904.mp3"
            },
            baseUrl: "/ss/z12/",
            onLoad: () => {ready = true}
        }).toDestination();

        loop = new Tone.Loop(time => {
            step(time)
        }, "0.05").start(0);
    }



    const table = ["A1", "A2", "A3", "A4", "A5", "A6"]

    let probs = new Array(6).fill(0.5);
    let probArray = [];
    let overflowArray = [];

    $: {
        overflowArray = new Array(probs.length).fill(0);

        let probSum = probs.reduce((accum, current) => accum + current);
        let normFactor = 1.0 / probSum;

        probArray = probs.map(v => v * normFactor)
    }

    function step(time) {
        overflowArray = probArray.map((v, i) => v + overflowArray[i]) // add probArray to overflowArray
        const maxIndex =  overflowArray.reduce((iMax, x, i, arr2) => x > arr2[iMax] ? i : iMax, 0);
        overflowArray[maxIndex] = overflowArray[maxIndex] - 1.0;
        sampler.triggerAttackRelease(table[maxIndex], 1.0, time);
    }

    function play() {
        Tone.start();
        Tone.Transport.start();
        loop.start();
    }

    function stop() {
        Tone.Transport.stop();
        loop.stop();
    }

</script>

<div class="container">
    <button on:click={play}>play</button>
    <button on:click={stop}>stop</button>
    <button on:click={step}>step</button>

    Change the probability of each potential outcome by modifying the slider's value.
    Observe how different ordering of samples can be created by changing the probabilities.
    <div id="probs">
        {#each probs as i, x}
            <input type="range" step="0.1" min="0.0" max="1.0" bind:value={probs[x]}/>
        {/each}
    </div>
    <div id="notifiers">
        {#each probs as i, x}
            <button></button>
        {/each}
    </div>
</div>

<style>
    .container {
        display: flex;
        flex-direction: column;
        border-radius: 12px;
        border: 3px solid rgba(128, 128, 128, 0.575);
        transition: border .5s;
        padding: 20px;
    }
    #probs {
        display: flex;
        flex-direction: column;
        max-width: 30%;
    }

    input {
        padding: 3px;
    }
</style>





