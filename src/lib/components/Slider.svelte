<script>
    export let value;
    export let min = 0;
    export let max = 100;
    export let func = () => {return};
</script>

<input type="range" min="{min}" max="{max}" on:input={func} bind:value={value} class="slider"> 

<style>
    /* .slider {
        -webkit-appearance: none;
        height: 25px;
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        -webkit-transition: .2s;
        transition: opacity .2s;
    }
    
    .slider:hover {
        opacity: 1;
    }
    
    .slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 10px;
        height: 25px;
        background: #4CAF50;
        cursor: pointer;
    }
    
    .slider::-moz-range-thumb {
        width: 10px;
        height: 25px;
        background: #4CAF50;
        cursor: pointer;
    } */
</style>