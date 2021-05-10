<script>
    import Container from '$lib/components/Container.svelte';
    export let url = "";
    export let title = "";
    export let figure = "";
    export let caption = title;
    export let id = "";
    export let width = 560;
    export let height = 315;
</script>

<Container id={id}>
    <iframe title={title} width={width} height={height} src={url} frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen />
    <div class="caption">
        <p>{figure}: {caption}</p>
    </div>
</Container>

<style>
    iframe {
        max-width: 100%;
        margin: 0 auto;
        display: block;
    }

    .caption :global(p) {
        font-style: italic;
        text-align: center;
        width: 80%;
        margin: 0 auto;
    }
</style>