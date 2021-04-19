<style>
    .container {
        text-align: center;
        padding-top: 10px;
    }

    .caption :global(p) {
        font-style: italic;
        text-align: center;
    }

    span {
        color: red;
        font-weight: 700;
    }
</style>

<div class="container">
    <slot name="media">
        <span>There should be media content here. If there isn't there is a problem.</span>
    </slot>
    <div class="caption">
        <slot name="caption">
            <span>There should be a caption or attribution here.</span>
        </slot>
    </div>
</div>

