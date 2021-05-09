<script>

    import * as Tone from 'tone';
    import { browser } from '$app/env';
    export let id="demo2";
    let ready = false;
    let sampler, loop, current;
    let bpm = 120;
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
        }).toDestination();

        
        Tone.loaded().then(() => ready = true);

        loop = new Tone.Loop(time => {
            step(time)
        }, "16n").start(0);
    }

    const table = ["A1", "A2", "A3", "A4", "A5", "A6"]

    let probs = new Array(6).fill(0.5);
    let probArray = [];
    let overflowArray = [];

    function updateProbs() {
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
        current = maxIndex;
    }

    function play() {
        updateProbs()
        Tone.start();
        Tone.Transport.start();
        loop.start();
    }

    function stop() {
        Tone.Transport.stop();
        loop.stop();
    }

</script>

{#if browser}
<div class="container" id={id}>
    {#if ready}
    
    Change the probability of each potential outcome by modifying the slider's value.
    Observe how different ordering of samples can be created by changing the probabilities.
    <div id='btn-array'>
        <button class='btn' on:click={play}>play</button>
        <button class='btn' on:click={stop}>stop</button>
    </div>
    <div id="probs">
        {#each probs as i, x}
            <div class='slider'>
                <input class:selected={x === current} type="range" step="0.1" min="0.0" max="1.0" bind:value={probs[x]} on:change={updateProbs} />
                <span>Probability {x}: {probs[x]}</span>
                <button class='sample-notify' class:selected={x === current}></button>
            </div>
        {/each}
    </div>
    {/if}
</div>
{/if}

<style>
    .container {
        display: flex;
        flex-direction: column;
        border-radius: 12px;
        border: 3px solid rgba(128, 128, 128, 0.575);
        transition: border .5s;
        padding: 20px;
    }

    #btn-array {
        display: flex;
        flex-direction: column;
        padding-top: 30px;
        padding-bottom: 30px;
        justify-content: center;
    }


    .btn {
        width: 35%;
        margin: 0 auto;
    }

    .sample-notify {
        width: 40px;
        height: 40px;
        border-width: 0;
        margin-top: auto;
        margin-bottom: auto;
    }

    .slider {
        display: flex;
        flex-direction: row;
        justify-content: space-around;
    }

    .selected {
        background-color: var(--blue);

    }
    #probs {
        display: grid;
        grid-template-rows: repeat(6, auto);
    }

    input {
        width: 100px;
    }
</style>





