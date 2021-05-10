
<script>
    import Container from '$lib/components/Container.svelte';
    export let id = ""
</script>

<Container id={id}>
    <slot name="media">
        <span>There should be media content here. If there isn't there is a problem.</span>
    </slot>
    <div class="caption">
        <slot name="caption">
            <span class="error">There should be a caption or attribution here.</span>
        </slot>
    </div>
</Container>