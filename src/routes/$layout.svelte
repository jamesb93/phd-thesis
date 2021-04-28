<script>
	import StaticNav from "$lib/components/StaticNav.svelte"
	import RightToc from "$lib/components/RightToc.svelte"
	import { page } from "$app/stores";
	import '../app.css';

	let w;
	let navshow = false;
	const minWidth = 1276;
	$: navshow = (w >= minWidth);
	
	const pagesWithoutNav = ['/', '/projects', '/conclusion', '/tech'];
	
	function clickHandle(){
		navshow = !navshow
	}
	
	function backgroundClickHandle(){
		navshow = false
	}
</script>

<svelte:window bind:innerWidth={w} />

<main class="wrapper">
	{#if w < minWidth}
	<div class="btn-container">
		<button on:click={clickHandle} class="btn">
			<svg width=24 height=20>
				<line x1=0 y1=4  x2=24 y2=4/>
				<line x1=0 y1=11  x2=16 y2=11/>
				<line x1=0 y1=18 x2=24  y2=18/>
			</svg>
		</button>
	</div>
	{/if}
	
	{#if navshow || w > minWidth}
	<StaticNav bind:navshow={navshow}/>
	{/if}
	
	<article
	id="article"
	on:click={backgroundClickHandle} 
	class="content" 
	class:dim='{w < minWidth && navshow}'
	>
	<slot />
</article>

<div class="pagenav">
	{#if w > minWidth}
	{#if !pagesWithoutNav.includes($page.path)}
	<RightToc/>
	{/if}
	{/if}
</div>
</main>


<style>
	.wrapper {
		display: grid;
		grid-template-columns: auto min(80ch, 100%) auto;
		justify-content: center;
		padding-left: 0em;
		padding-right: 0em;
		max-width: 160ch;
		margin: 0 auto;
	}
	
	.wrapper > article {
		grid-column: 2;
	}
	
	.content {
		margin-top: 5em;
		justify-content: center;
		padding-left: 1em;
		height: 100%;
	}
	
	.dim {
		opacity: 0.25;
	}
	
	svg {
		min-height: 24px;
		transition: transform 0.3s ease-in-out;
	}
	
	svg line {
		stroke: darkgray;
		stroke-width: 2;
	}
	
	.btn {
		background-color: white;
		box-shadow: none;
		border-width: 0px;
	}
	
	.btn-container {
		position:fixed;
		z-index: 100;
	}
	
	.pagenav {
		display: grid;
	}
	
</style>
