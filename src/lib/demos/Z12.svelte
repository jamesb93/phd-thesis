<script>
    import * as Tone from 'tone';
    import Container from '$lib/components/Container.svelte';
    import Button from '$lib/components/Button.svelte';
    import { browser } from '$app/env';
    export let title = ''
    export let id="demo2";
    export let caption='DEMO 2'

    let ready = false;
    let sampler, loop, current;
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
        }, 0.1).start(0);
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

<Container id={id} zoom={false}>
{#if browser}
    {#if ready}
    
    <div class='top-text'>
        <div class='title'>
            {title}
        </div>
        <div class='cap'>
            {caption}
        </div>
    </div>

    <div class='desc'>
        Press play or stop to turn the demonstration on and off. Change the probability for each sound playing by modifying the slider values. Observe how changing the probabilities alters the patterning of the individual samples. You can increase or decrease the rate at which samples are played by adjusting the iteration rate slider.
    </div>

    <div id='btn-array'>
        <Button clickHandler={play} text='Play' />
        <Button clickHandler={stop} text='Stop' />
        <div class='rate'>
            <span>Iteration Rate: {loop.interval.toFixed(2)} </span>
            <input type='range' bind:value={ loop.interval } step=0.01 min=0.05 max=0.2 />
        </div>
    </div>


    <div id="probs">
        {#each probs as i, x}
            <div class='slider'>
                <div class='input'>
                    <span>Probability {x}: {probs[x]}</span>
                    <input class:selected={x === current} type="range" step="0.1" min="0.0" max="1.0" bind:value={probs[x]} on:change={updateProbs} />
                </div>
                <button class='sample-notify' class:selected={x === current}></button>
            </div>
        {/each}
    </div>
    {/if}
{/if}
</Container>


<style>
    .top-text {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .title {
        font-weight: bold;
    }

    .desc {
        padding-top: 10px;
        display: flex;
        flex-direction: column;
        max-width: 85%;
        color: grey;
    }

    .cap {
        font-style: italic;
        min-width: max-content;
    }
    .input {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    #btn-array {
        display: flex;
        flex-direction: row;
        padding-top: 30px;
        justify-content: space-around;
        width: 50%;
        margin: 0 auto;
        align-items: center;
    }

    .rate {
        display: flex;
        flex-direction: column;
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
        padding-top: 10px;
        padding-bottom: 10px;

    }

    .selected {
        background-color: var(--blue);

    }
    #probs {
        display: grid;
        grid-template-rows: repeat(6, auto);
    }

    input {
        width: 140px;
    }
</style>





