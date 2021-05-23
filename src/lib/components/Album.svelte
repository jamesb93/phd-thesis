<script>
    import { onMount } from "svelte";
    import { browser } from "$app/env";
    import Container from '$lib/components/Container.svelte';
    import { cloudPrefix, noext } from '$lib/utility/paths.js';

    export let id = "";
    export let tracks = [];
    export let title = "";
    export let figure = "";

    let Peaks, instance, audio, overview;
    let selectedTrack = 0;
    let playState = false;
    let fakeAudio = new Array(tracks.trackData.length).fill(null);
    let loading = true;

    onMount (async()=>{
        if (browser) {
            const module = await import("peaks.js");
            Peaks = module.default;
            const options = {
                    containers: {
                    overview: overview
                },
                dataUri: { arraybuffer: tracks.prefix + tracks.trackData[0].peaks },
                mediaElement: audio,
                height: 75,
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
                    loading = false;
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
                mediaUrl: tracks.prefix + tracks.trackData[i].audio,
                dataUri: { arraybuffer: tracks.prefix + tracks.trackData[i].peaks },
            };
            instance.setSource(options, err => {
                if (err) console.log(err)
            });
            audio.play();
            playState = true;
        }
    }

    function convertTime(time) {
        if (time !== null && !Number.isNaN(time)) {
            const date = new Date(time * 1000).toISOString().substr(11, 8)
            return date.toString().substr(3);
        }
        return 'Invalid Time Format'
    }

</script>
<Container id={id}>
    <div class="inner">
        <div class='top-text'>
            <span class='title'>{title}</span>
            <span class='figure'>{figure}</span>
        </div>
        <div class="vis">
            {#if !loading}
            <button on:click={ clickHandler }>
                { playState === true ? 'stop' : 'play' }
            </button>
            {/if}
            <div class="overview" bind:this={ overview } />
        </div>
        <div class="peaks-controls">
            <audio bind:this={audio} on:ended={ ()=>playState=false }>
                <source src={ tracks.prefix + tracks.trackData[0].audio } type="audio/mp3">
                <track kind="captions">
            </audio>
        </div>

        <div class='track-list'>
            {#if loading}Loading...{/if}
            {#each tracks.trackData as track, i}
                <audio src={tracks.prefix + track.audio} bind:this={ fakeAudio[i] }>
                    <track kind="captions">
                </audio>
                {#if !loading}
                <div on:click={ () => setSource(i) } class='track-selector'>
                    <div id='name-time' class:selected={ selectedTrack === i}>
                        <span>{i+1}. {track.name}</span>
                        <div class='duration'>
                        {#if fakeAudio[i] !== null && fakeAudio[i].duration !== NaN}
                            { convertTime(fakeAudio[i].duration) }
                        {/if}
                        </div>
                    </div>
                    <div id='single-lossless' >
                        <a rel='external' href={ cloudPrefix + tracks.prefix + noext(track.audio) + '.wav'}>Download Lossless Version</a>
                    </div>
                </div>
                {/if}
            {/each}
        </div>
        
        <!-- { cloudPrefix + (tracks.prefix).slice(0, -1) + '.zip' } -->
        
    </div>
</Container>

<style>
    :root {
        --text-margin: 10px;
    }

    #name-time {
        display: flex;
        flex-direction: row;
        gap: 10px;
    }

    #single-lossless {
        font-style: italic;
        font-size: 12px;
    }

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
    .top-text {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }
    .title {
        font-weight: bold;
    }
    .figure {
        font-style: italic;
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
        margin-left: var(--text-margin);
    }

    .track-selector:hover {
        background-color: rgb(240, 240, 240);
    }

    .selected {
        font-weight: bold;
    }

    .duration {
        color: grey;
        margin-right: var(--text-margin);
    }

    button {
        height: 30px;
        border-radius: 0;
        width: 76px;
        align-self: center;
    }
</style>