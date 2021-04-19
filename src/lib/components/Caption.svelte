<style>
    .caption {
        text-align: center;
        margin-left: auto;
        margin-right: auto;
        display: block;
    }

    .caption :global(p) {
        font-style: italic;
        text-align: center;
    }

    .error {
        color: red;
        font-weight: 700;
    }
</style>

<div class="caption">
    <slot name="text">
        <span class="error">
            There should be a caption or attribution here inside a p tag
        </span>
    </slot>

</div>

