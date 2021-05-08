<script>
    import marked from 'marked';
    export let url = "";
    export let caption = "";
    export let figure = "";
    export let htmlCap = false;
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
        {#if htmlCap === true}
            <p>{@html marked(figure+': '+caption)}</p>
        {:else}
            <p>{figure}: {caption}</p>
        {/if}
    </div>
</div>

<style>
    .container {
        position: relative;
        width: 95%;
        border-radius: 5px;
        box-shadow: 0 1px 3px 4px rgba(0, 0, 0, 0.1);
        border-radius: 5px;
        -webkit-transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
        transition: all 0.2s cubic-bezier(0.165, 0.84, 0.44, 1);
        background-color: transparent;
        margin-top: 30px;
        margin-bottom: 30px;
        margin-left: auto;
        margin-right: auto;
        padding-bottom: 20px;
        padding-top: 20px
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

    .container :global(img) {
        max-width: 80%;
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        display: block;
        height: 100%;
    }
    
</style>
