<script>
    export let url = "";
    export let title = "";
    export let figure = "";
    export let caption = title;
    export let id = "";
    export let width = 560;
    export let height = 315;
</script>

<div class="container" id={id}>
    <iframe title={title} width={width} height={height} src={url} frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
    <div class="caption">
        <p>{figure}: {caption}</p>
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

    .container > iframe {
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