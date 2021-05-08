<script>
    export let url = "";
    export let figure = "";
    export let caption = "";
    export let id = figure;
</script>

<div class="container" id={id}>
    <video controls loop>
        <source src={url} type="video/mp4">
        <track kind="captions" />
        <p>Your browser doesn't support HTML5 video. Here is a <a href={url}>link to the video</a> instead.</p> 
        </video>
    <div class="caption">{figure}: {caption}</div>
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

    .caption {
        font-style: italic;
        text-align: center;
        width: 80%;
        margin: 0 auto;
    }

    .container :global(video) {
        width: 80%;
        display: block;
        margin: 0 auto;
    }

    .container :global(iframe) {
        width: 80%;
        display: block;
        margin: 0 auto;
    }
</style>