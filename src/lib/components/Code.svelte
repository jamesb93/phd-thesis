<script>
    export let caption = ""
    export let figure = "CODE"
    export let id='code'
</script>

<div id={id}>
    <div class='sub-container'>
        <slot />
    </div>
    
    <div class='caption'>
        {figure} : {caption}
    </div>
</div>


<style>
    .sub-container {
        padding-left: 10px;
        padding-right: 10px;
    }

    .caption {
        font-style: italic;
        text-align: center;
        width: 80%;
        margin: 0 auto;
    }
</style>