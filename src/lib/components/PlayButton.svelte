<script>
export let playFunc;
export let state;
</script>

<button 
on:click={playFunc} 
class:playing="{state === true}"
class:stopped="{state === false}"
class="btn" 
>
{#if state} 
    stop 
{:else} 
    play 
{/if}
</button>

<style>
    button {
        border: none;
        color: white;
        padding: 5px;
        text-align: center;
        text-decoration: none;
        font-size: 16px;
        width: 25%;
        height: 30px;
        align-self: center;
    }

    .stopped {
        background-color: #4CAF50;
    }
    .stopped:hover {
        background-color: #38803a;
    }

    .playing {
        background-color:tomato
    }

    .playing:hover {
        background-color: rgb(194, 75, 54)
    }
</style>