<script>
	import { slide } from 'svelte/transition';
	
	export let caption = "The description of the code";
    export let figure = "CODE N";
    export let id = 'coden';
	
	let expanded = true;

	function clickHandler(e) {
		expanded = !expanded
	}
</script>


<div class='container' id={id}>
	<button id='top-bar' on:click={ clickHandler }>
		<div id='figure'>{figure}</div>
		<div id='top-cap'>
			<div id='caption'>{caption}</div>
			<div id='status'>
				{#if expanded}
					-
				{:else}
					+
				{/if}
			</div>
		</div>
	</button>

	{#if expanded}
		<div id='content' 
		in:slide={ {duration: 200 } }
		out:slide={ {duration: 200 } }
		>	
			<slot/>
		</div>
	{/if}
</div>	

<style>

	#status {
		padding-left: 15px;
		width: 20px;
		margin-top: 6px;
	}
	#figure {
		font-style: italic;
		min-width: 80px;
	}
	
	#caption {
		text-align: justify;
	}

	#caption, #figure {
		margin-top: 8px;
		margin-bottom: 8px;
	}

	#top-cap {
		display: flex;
		flex-direction: row;
	}

	.container {
		display: flex;
		flex-direction: column;
	}

	#top-bar {
		display: flex;
		font-size: 15px;
		min-height: 40px;
		flex-direction: row;
		justify-content: space-between;
		border: 1px solid #eeeeee;
		background: #ededed;
		box-shadow: none;
		border-radius: 0px;
	}

	#top-bar:hover {
		background-color: #f7f7f7;
	}

</style>