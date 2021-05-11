<script>
    import { onMount } from "svelte";
    import { browser } from "$app/env";
    import Button from '$lib/components/Button.svelte';
    import Container from '$lib/components/Container.svelte';
    import PlayPause from '$lib/components/PlayPause.svelte';

    export let id = "";
    export let tracks = [];

    let Peaks, instance, audio;
    let title = "";
    let selectedTrack = 0;
    let overview;
    let playState = false;
    let fakeAudio = new Array(tracks.length).fill(null);

    onMount (async()=>{
        console.log(fakeAudio)
        if (browser) {
            const module = await import("peaks.js");
            Peaks = module.default;
            const options = {
                    containers: {
                    overview: overview
                },
                dataUri: { arraybuffer: tracks[0].peaks },
                mediaElement: audio,
                height: 80,
                segmentStartMarkerColor: '#a0a0a0',
                segmentEndMarkerColor: '#a0a0a0',
                zoomWaveformColor: 'rgba(0, 30, 128, 0.61)',
                overviewWaveformColor: '#0d47a1',
                overviewHighlightColor: 'grey',
                playheadColor: 'rgba(0, 0, 0, 1)',
                playheadTextColor: '#aaa',
                showPlayheadTime: false,
                pointMarkerColor: '#FF0000',
                axisGridlineColor: '#ccc',
                axisLabelColor: '#aaa',
            }

            instance = Peaks.init(options, (err, p) => {
                if (err) {
                    console.log(err)
                } else {
                    instance = p
                }
            })
        }
    });

    function clickHandler() {
        if (audio.paused) {
            audio.play();
            playState = true;
        } else {
            audio.pause();
            playState = false;
        }
    }

    function setSource(i) {
        if (i !== selectedTrack) {
            audio.pause();
            playState = false;
            selectedTrack = i;
            const options = {
                mediaUrl: tracks[i].audio,
                dataUri: { arraybuffer: tracks[i].peaks },
            };
            instance.setSource(options, err => {
                if (err) console.log(err)
            });
        }
    }

    function convertTime(time) {
        const date = new Date(time * 1000).toISOString().substr(11, 8)
        return date.toString().substr(3);
    }

</script>
<Container id={id}>
    <div class="inner">
        <div class='title'>{title}</div>
        <div class="vis">
            <button on:click={ clickHandler }>
                { playState === true ? 'stop' : 'play' }
            </button>
            <div class="overview" bind:this={ overview } />
        </div>
        <div class="peaks-controls">
            <audio bind:this={audio}>
                <source src={tracks[0].audio} type="audio/mp3">
                <track kind="captions">
            </audio>
        </div>

        <div class='track-list'>
            {#each tracks as track, i}
                <audio src={track.audio} bind:this={ fakeAudio[i] } />
                <div on:click={ () => setSource(i) } class='track-selector' class:selected={ selectedTrack === i} >
                    {i+1}. {track.name} 
                    <div class='duration'>
                    {#if fakeAudio[i] !== null}
                        { convertTime(fakeAudio[i].duration) }
                    {/if}
                    </div>
                </div>
            {/each}
        </div>
    </div>
</Container>

<style>
    .inner {
        padding: 10px;
    }
    .vis {
        display:flex;
        flex-direction: row;
        gap: 10px;
        padding-top: 10px;
        padding-bottom: 10px;
    }

    .overview {
        width: 90%;
        margin: 0 auto;
        height: 80px;
    }

    .track-list {
        display: flex;
        flex-direction: column;
    }

    .track-selector {
        border-top: 1px rgb(197, 197, 197) solid;
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .track-selector:hover {
        background-color: rgb(240, 240, 240);
    }

    .selected {
        font-weight: bold;
    }

    .duration {
        color: grey;
    }

    button {
        height: 30px;
        border-radius: 0;
        width: 76px;
        align-self: center;
    }
</style>