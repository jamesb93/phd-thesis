<script>
    export let value;
    export let min= "0";
    export let max = "100";
    export let title = "";
    export let step = "any";
    export let inFunc;
    export let chFunc;
    export let showValue = true;
    export let showMin = true;
    export let showMax = true;
    export let focused = false;
</script>

<div class="pad">
    <span class="text title">{title}</span>
    <div class="container">
        <span class:hidden={showMin === false} class="text min">{min}</span>
        <input 
        type=range
        on:mousedown={ ()=>focused=true } 
        on:mouseup  ={ ()=>focused=false } 
        class="slider" 
        min={min} max={max} step={step} 
        bind:value={value} on:input={inFunc} on:change={chFunc} 
        />
        <span class:hidden={showMax === false} class="text max">{max}</span>
    </div>
    {#if showValue}
        <span class="text value">{value}</span>
    {/if}
</div>


<style>
    .pad {
        padding-top: 10px;
        padding-bottom: 10px;
    }
    .container {
        display: flex;
        flex-direction: row;
        justify-content: center;
        align-items: center;
    }

    .title {
        text-align: center;
    }
    
    .text {
        font-size: 10px;
        color: grey;
    }
    .min {
        text-align: right;
        padding-right: 2px;
    }
    .max {
        text-align: left;
        padding-left: 2px;
    }
    
    .slider {
        -webkit-appearance: none;
        width: 75%;
        height: 10px;
        border-radius: 5px;   
        background: #d3d3d3;
        outline: none;
        opacity: 0.7;
        /* -webkit-transition: .2s;
        transition: opacity .2s; */
    }
    
    .slider::-webkit-slider-thumb {
        -webkit-appearance: none;
        appearance: none;
        width: 17px;
        height: 17px;
        border-radius: 10%; 
        background: #4c87af;
        cursor: pointer;
    }
    
    .slider::-moz-range-thumb {
        width: 17px;
        height: 17px;
        border-radius: 50%;
        background: #4c87af;
        cursor: pointer;
    }

    .hidden {
        display: none;
    }
</style>