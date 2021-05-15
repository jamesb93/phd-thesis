<script>

    import { afterUpdate, onDestroy, onMount } from 'svelte';
    import { page } from '$app/stores';
    let visibility;
    let observer = null;
    let contents = [];
    let nodes = ["H1", "H2", "H3", "H4"];
    let tempIntersect;

    const options = {
        rootMargin: "0px",
        threshold : [0.1, 0.9],
    }

    function handleIntersect(entries, observer) {
        let lowest = Infinity;
        entries.forEach(entry => {
            if (entry.isIntersecting) {
                var y = entry.boundingClientRect.y;
                if (y < lowest) {
                    lowest = y;
                    tempIntersect = entry.target.id; // hold the value for now
                }
            }
        })    
        visibility = tempIntersect;
    }

    function iteratePage() {
        contents = [];
        let element = document.getElementById("article")
        let children = Array.from(element.childNodes);
        children.forEach(child => {
            if (nodes.includes(child.tagName)) {
                contents.push({
                    depth: child.tagName[1],
                    url: child.id,
                    heading: child.textContent
                })
            }
        })
    }

    const makeObserver = () => {
        iteratePage();
        observer = new IntersectionObserver(handleIntersect, options);
        if (contents) {
            contents.forEach((c) => {
                let element = document.getElementById(c.url)
                observer.observe(element);
            })
        }
    }

    onMount(() => {
        if (observer) {
            observer.disconnect();
        }
        makeObserver();
    })

    afterUpdate(()=> {
        if (observer) {
            observer.disconnect();
        }
        makeObserver();
    })

    onDestroy(() => {
        if (observer) {
            observer.disconnect();
        }
    })


</script>

<div class="container">
    {#if contents}
        <ul>
            {#each contents as section}
                    <li>
                        <a 
                        class="link depth-{section.depth}" 
                        href="{$page.path}#{section.url}"
                        class:shown={visibility === section.url} 
                        > 
                            {section.heading}
                        </a>
                    </li>
            {/each}
        </ul>
    {/if}
</div>

<style>
	.container {
        z-index: 99;
		height: 100%;
        position: fixed;
        line-height: 1.8em;
        font-size: 11px;
        padding-top: 13px;
    }

    .shown {
        font-weight:bold;
    }
    
    ul li{
        display: block;
    }

    .link {
        text-overflow: ellipsis;
        word-wrap: ellipsis;
        white-space: nowrap;
    }

    .depth-1 {margin-left: 0em}
    .depth-2 {margin-left: 1.5em}
    .depth-3 {margin-left: 3em}
    .depth-4 {margin-left: 4.5em}

</style>