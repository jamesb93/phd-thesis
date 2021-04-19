<script>
	export let segment;
</script>

<style>
	nav {
		border-bottom: 1px solid rgba(47, 134, 255, 0.1);
		font-weight: 300;
		padding: 0 1em;
	}

	ul {
		margin: 0;
		padding: 0;
	}

	/* clearfix */
	ul::after {
		content: '';
		display: block;
		clear: both;
	}

	li {
		display: block;
		float: left;
	}

	[aria-current] {
		position: relative;
		display: inline-block;
	}

	[aria-current]::after {
		position: absolute;
		content: '';
		width: calc(100% - 1em);
		height: 2px;
		background-color: rgb(32, 110, 255);
		display: block;
		bottom: -1px;
	}

	a {
		color: rgb(127, 127, 127);
		text-decoration: none;
		padding: 1em 0.5em;
		display: block;
	}

	@media (prefers-color-scheme: dark) {
		a {
			color: rgba(256, 256, 256, 0.8)
		}

		nav {
			border-bottom: 1px solid rgba(193, 193, 193, 0.5);
		}
	}
</style>

<nav>
	<ul>
		<li><a rel=prefetch aria-current="{segment === 'thesis' ? 'page' : undefined}" href="thesis">thesis</a></li>
		<li><a rel=prefetch aria-current="{segment === 'appendix' ? 'page' : undefined}" href="appendix">appendix</a></li>
	</ul>
</nav>
