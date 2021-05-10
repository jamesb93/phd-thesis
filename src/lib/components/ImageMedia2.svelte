<script>
    import Container from '$lib/components/Container.svelte';
    import marked from 'marked';
    export let url = "";
    export let caption = "";
    export let figure = "";
    export let htmlCap = false;
    export let id = ""
</script>

<Container id={id}>
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
</Container>
