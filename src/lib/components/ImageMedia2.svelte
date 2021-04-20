<script>
    export let url = "";
    export let caption = "";
    export let figure = "";
</script>

<div class="container">
    {#if url !== ""}
    <a href={url} target="_blank">
        <img src={url} alt={caption}>
    </a>
    {:else}
    Set a URL for an image or there is another problem...
    {/if}

    <div class="caption">
        <p>{figure}: {caption}</p>
    </div>
</div>

<style>
    .container :global(img) {
        max-width: 80%;
        border-radius: 1%;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        display: block;
        margin-top: 30px;

    }
    .container {
        position: relative;
        display: inline-block;
        width: 100%;
        background-color: #fff;
        border-radius: 5px;
        box-shadow: 0 1px 2px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
        -webkit-transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
        transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
    }

    .container:hover {
        -webkit-transform: scale(1.05, 1.05);
        transform: scale(1.05, 1.05);
    }

    .container::after {
        content: "";
        border-radius: 5px;
        position: absolute;
        z-index: -1;
        top: 0;
        left: 0;
        width: 100%;
        box-shadow: 0 5px 15px rgba(0, 0, 0, 0.3);
        opacity: 0;
        -webkit-transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
        transition: all 0.4s cubic-bezier(0.165, 0.84, 0.44, 1);
    }

    .container::hover::after {
        opacity: 1;
    }
    
    .caption :global(p) {
        font-style: italic;
        text-align: center;
        width: 80%;
        margin: 0 auto;
    }
    
</style>
