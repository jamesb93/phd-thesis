<script>
    import Container from '$lib/components/Container.svelte';
    export let url = "";
    export let figure = "";
    export let caption = "";
    export let id = figure;
</script>

<Container id={id}>
    <video controls loop>
        <source src={url+'.webm'} type="video/webm">
        <source src={url+'.mp4'} type="video/mp4">

        <p>Your browser doesn't support HTML5 video. Here is a <a href={url}>link to the video</a> instead.</p> 
    </video>
    <div class="caption">
        {figure}: {caption}
    </div>
</Container>