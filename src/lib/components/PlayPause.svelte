<script>
    export let w, h;

    const WIDTH = w;
    const HEIGHT = h;

    export let state = true; // true = play, false = paused
    export let clickHandler = () => {};
</script>

<svg width={`${WIDTH}px`} height={`${HEIGHT}px`} on:click={clickHandler}>
    {#if state}
        <line x1=0 x2={WIDTH} y1=0 y2={HEIGHT / 2} />
        <line x1=0 x2={WIDTH} y1={HEIGHT} y2={HEIGHT / 2} />
        <line x1=0 x2=0 y1=0 y2={HEIGHT} />
    {/if}
</svg>

<style>
    line {
        stroke: black;
        stroke-width: 2px;
    }
</style>