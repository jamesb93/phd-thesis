<script>
    import { onMount } from "svelte";
    import { durations } from '$lib/stores.js';
    import Container from '$lib/components/Container.svelte';
    import Button from '$lib/components/Button.svelte';
    import { cloudPrefix, noext } from '$lib/utility/paths.js';

    export let id = "";
    export let tracks = [];
    export let title = "";
    export let figure = "";

    let Peaks, instance, audio, overview;
    let selectedTrack = 0;
    let playState = false;
    let loading = true;

    onMount (async () => {
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
        }
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
                <Button clickHandler={clickHandler} text={ playState === true ? 'pause' : 'play'} />
            {/if}

            <div id='overview' bind:this={ overview } />
        </div>
        <div class="peaks-controls">
            <audio bind:this={audio} on:ended={ ()=>playState=false }>
                <source src={ tracks.prefix + tracks.trackData[0].audio } type="audio/mp3">
                <track kind="captions">
            </audio>
        </div>

        <div class='track-list'>
            {#if loading}
            Loading...
            {/if}
            {#each tracks.trackData as track, i}
                {#if !loading}
                <div on:click={ () => setSource(i) } class='track-selector'>
                    <div id='name-time' class:selected={ selectedTrack === i}>
                        <span>{i+1}. {track.name}</span>
                        <div class='duration'>
                            { $durations[track.audio] } 
                        </div>
                    </div>
                    <div id='single-lossless' >
                        <a rel='external' href={ cloudPrefix + tracks.prefix + noext(track.audio) + '.wav'}>Download Lossless Version</a>
                    </div>
                </div>
                {/if}
            {/each}
        </div>
    </div>
</Container>

<style>
    :root {
        --text-margin: 10px;
    }

    .title {
        font-weight: bold;
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
        display: flex;
        flex-direction: row;
        justify-content: space-between;
        padding-top: 10px;
        padding-bottom: 10px;
    }

    #overview {
        min-width: 90%;
    }

    .top-text {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
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
</style>