<script>
    import * as Tone from 'tone';
    import { onMount } from 'svelte';
    const urlBase = "/preoccupations/isn/isn_0";
    let readyState = false;
    let playState = false;
    let players;
    onMount(() => {
        players = new Tone.Players({
            '0' : urlBase + 1 + '.mp3',
            '1' : urlBase + 2 + '.mp3',
            '2' : urlBase + 3 + '.mp3',
            '3' : urlBase + 4 + '.mp3',
            '4' : urlBase + 5 + '.mp3',
            '5' : urlBase + 6 + '.mp3',
            '6' : urlBase + 7 + '.mp3',
            '7' : urlBase + 8 + '.mp3',
            '8' : urlBase + 9 + '.mp3'
        }, () => {
            for (let i=0; i < 9; i++) {
                players.player(i).loop = true;
            }
            readyState = true
        }).toDestination();
    })


    function togAll() {
        if (players.state === 'started') {
            for (let i=0; i < 9; i++) {
                players.player(i).stop();
            }
         } else {
            for (let i=0; i < 9; i++) {
                players.player(i).start();
            }
        }
    }

    function mute(x) {
        let c = players.player(x).volume.value;
        players.player(x).volume.value = c === 0 ? -144 : 0;
    }
</script>
HI!
{#if readyState}
<button on:click={ togAll }>toggle all</button>
<div class="btn-array">
    {#each {length: 9} as _, i}
    <button on:click={ () => mute(i) }>Toggle {i} </button>
    {/each}
</div>
{:else}
Loading...
{/if}


<style>
    .btn-array {
        display: flex;
        flex-direction: column;
    }
</style>