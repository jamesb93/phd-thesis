<script>
    export let id = "";
    export let zoom = true;
</script>

<div class='container' id={id} class:zoomable={ zoom === true }>
    <slot />
</div>

<style>
    :root {
        --width: 87%
    }
    .container {
        position: relative;
        max-width: var(--width);
        min-width: var(--width);
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
        padding: 10px;
        text-align: left;
    }

    .zoomable:hover {
        --scale: 1.03;
        -webkit-transform: scale(var(--scale), var(--scale));
        transform: scale(var(--scale), var(--scale));
    }

    .zoomable::after {
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

    .zoomable::hover::after {
        opacity: 1;
    }

    .container :global(img) {
        max-width: 90%;
        text-align: center; 
        margin-left: auto;
        margin-right: auto;
        display: block;
    }

    :global(video), :global(iframe) {
        width: 93%;
        display: block;
        margin: 0 auto;
    }

    :global(iframe) {
        height: 400px;
    }

    .container :global(.caption) {
        font-style: italic;
        text-align: center;
        width: 80%;
        margin: 0 auto;
    }

</style>