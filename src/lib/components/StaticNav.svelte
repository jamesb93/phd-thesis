<script>
    import {metadata as m} from "../../routes/directory.svx"
	import Button from '$lib/components/Button.svelte';
	import { slide } from 'svelte/transition';
	import { quintOut } from 'svelte/easing';
	import { page } from "$app/stores";
	export let navshow;
	export let value;
	function handleClick(){
		navshow = false;
	};

	function handleButton() {
		value = !value			
	}
</script>

<nav class="container" transition:slide="{{ duration: 300, easing: quintOut }}">
	<!-- <Button clickHandler={handleButton} text="toggle justification"/> -->
	<ul>
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === "/"}	href='/'>Home</a></li>
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === "/howto"}	href='/howto'>How To</a></li>
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === "/acknowledgements"} href='/acknowledgements'>Acknowledgements</a></li>
		
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === "/submission-materials"} href='/submission-materials'>Submission Materials</a></li>

		<li><a on:click={handleClick} class="link section" class:selected={$page.path === m.intro} href={m.intro}>1. Introduction</a></li>
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === m.preoc} href={m.preoc}>2. Preoccupations</a></li>
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === m.ca} href={m.ca}>3. Content-Awareness</a></li>
		
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === m.proj} href={m.proj}>4. Projects</a></li>
		<li><a on:click={handleClick} class="link subsection" class:selected={$page.path === m.ss} href={m.ss}>4.1 Stitch/Strata</a></li>
		<li><a on:click={handleClick} class="link subsection" class:selected={$page.path === m.as} href={m.as}>4.2 Annealing Strategies</a></li>
		<li><a on:click={handleClick} class="link subsection" class:selected={$page.path === m.rt} href={m.rt}>4.3 Refracted Touch</a></li>
		<li><a on:click={handleClick} class="link subsection" class:selected={$page.path === m.re} href={m.re}>4.4 Reconstruction Error</a></li>
		<li><a on:click={handleClick} class="link subsection" class:selected={$page.path === m.em} href={m.em}>4.5 Interferences</a></li>

		<li><a on:click={handleClick} class="link section" class:selected={$page.path === m.ti} href="/tech">5. Technical Implementation</a></li>
		<li><a on:click={handleClick} class="link subsection" class:selected={$page.path === m.mosh} href={m.mosh}>5.1 mosh</a></li>
		<li><a on:click={handleClick} class="link subsection" class:selected={$page.path === m.ftis} href={m.ftis}>5.2 FTIS</a></li>
		<li><a on:click={handleClick} class="link subsection" class:selected={$page.path === m.reacoma} href={m.reacoma}>5.3 ReaCoMa</a></li>

		<li><a on:click={handleClick} class="link section" class:selected={$page.path === m.conc} href={m.conc}>6. Conclusion</a></li>
		
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === m.ref} href={m.ref}>References, Links and Figures</a></li>
		<li><a on:click={handleClick} class="link section" class:selected={$page.path === "/copyright"}	href='/copyright'>Copyright</a></li>
	</ul>
</nav>

<style>
	.faint {
		color:rgb(178, 178, 178)
	}
	.container {
		background-color:white;
		position: fixed;
		height: 100%;
		box-shadow: 1em;
		min-width: max-content;
		padding-right: 1em;
		z-index: 200;
		padding-left: 100px;
		padding-top: 5px;
	}


	ul {
		font-size: 12px;
		color: rgb(2, 2, 2);
		word-wrap: none;
		padding-left: 0;
		opacity: 1;
	}

	ul li {
		display: block;
	}

	.selected {
		color: rgb(0, 0, 0);
		font-weight: bold;
	}

	.subsection {
		margin-left: 1.5em;
	}

	.link {
		color: rgb(2, 2, 2);
		text-decoration: none;
		padding: 0.1em;
	}

	.link:hover {
		color: white;
		/* background-color: rgb(2, 2, 2); */
		text-decoration: underline;
	}

</style>
