<script>
    import {metadata as m} from "../../routes/directory.svx"
	import { page } from "$app/stores";
	export let navshow;
	function handleClick(){
		navshow = false;
	};
</script>


<nav class="container">
	<ul>
		<li><a  on:click={handleClick} class="section" class:selected='{$page.path === "/"}'	href='.'>Home</a></li>
		
		<li><a  on:click={handleClick} class="section" class:selected='{$page.path === m.intro}' href={m.intro}>1. Introduction</a></li>
		<li><a  on:click={handleClick} class="section" class:selected='{$page.path === m.preoc}' href={m.preoc}>2. Preoccupations</a></li>
		<li><a  on:click={handleClick} class="section" class:selected='{$page.path === m.ca}' href={m.ca}>3. Content-Awareness</a></li>
		
		<li><a  on:click={handleClick} class="section" class:selected='{$page.path === m.proj}' href={m.proj}>4. Projects</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === m.ss}' href={m.ss}>4.1 Stitch/Strata</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === m.as}' href={m.as}>4.2 Annealing Strategies</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === m.rt}' href={m.rt}>4.3 Refracted Touch</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === 'interlude'}' href={'interlude'}>interlude</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === m.re}' href={m.re}>4.4 Reconstruction Error</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === m.em}' href={m.em}>4.5 ElectroMagnetic</a></li>

		<li><a  on:click={handleClick} class="section" class:selected='{$page.path === m.ti}' href="/tech">5. Technical Implementation</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === m.mosh}' href={m.mosh}>5.1 mosh</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === m.reacoma}' href={m.reacoma}>5.2 ReaCoMa</a></li>
		<li><a  on:click={handleClick} class="subsection" class:selected='{$page.path === m.ftis}' href={m.ftis}>5.3 FTIS</a></li>


		<li><a  on:click={handleClick} class="section" class:selected='{$page.path === m.conc}' href={m.conc}>6. Conclusion</a></li>
		
		<li><a  on:click={handleClick} class="section" class:selected='{$page.path === m.ref}' href={m.ref}>References and Links</a></li>

		<br>
		<li><a target="_blank" on:click={handleClick} class="faint" href="https://github.com/jamesb93/phd-sapper">source code</a></li>
	</ul>
</nav>

<style>
	.faint {
		color:rgb(178, 178, 178)
	}
	.container {
		position: fixed;
		height: 100%;
		background-color: white;
		z-index: 99;
		box-shadow: 1em;
		padding-left: 5em;
	}

	nav {
		min-width: max-content;
		max-width: max-content;
		padding-left: 0;
		transition: 0.1s;
		height: 100%;
		padding-right: 1em;
		z-index: 200;
	}

	ul {
		font-size: 12px;
		color: rgb(127, 127, 127);
		word-wrap: none;
		padding-left: 0;
		opacity: 1;
		padding-top: 5em;
	}

	ul li {
		display: block;
	}

	.selected {
		display: inline-block;
		color: rgb(0, 0, 0);
	}

	.subsection {
		margin-left: 1.5em;
	}
	
	ul li a {
		text-decoration: none;
		padding: 0.1em;
		display: block;
		
	}

	ul li a:hover {
		color: rgb(95, 95, 95)
	}
	
	a {
		color: rgb(127, 127, 127)
	}
	
	a:hover {
		color: rgb(178, 178, 178)
	}
</style>
