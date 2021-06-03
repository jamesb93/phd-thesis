<script>

    import { afterUpdate, onDestroy, onMount } from 'svelte';
    import { page } from '$app/stores';
    let visibility;
    let observer = null;
    let ready = false;
    let contents = [];
    let thisPage = null;
    let nodes = ["H1", "H2", "H3", "H4"];
    let tempIntersect;

    const options = {
        rootMargin: "0px",
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
        let element = document.getElementById("article");
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

    function clipLinks(t, maxLen) {
        return t.length >= maxLen ? t.substr(0, maxLen)+'...' : t 
    }

    function makeObserver() {
        iteratePage();
        observer = new IntersectionObserver(handleIntersect, options);
        if (contents) {
            contents.forEach((c) => {
                let element = document.getElementById(c.url)
                observer.observe(element);
            })
        }
    }

    onMount(async() => {
        await fetch('/structure.json')
        .then(response => response.json())
        .then(data => contents = data)
        thisPage = contents[$page.path]
        ready = true;
    })

    afterUpdate(()=> {
        thisPage = contents[$page.path]
    })

    onDestroy(() => {
        if (observer) {
            observer.disconnect();
        }
    })


</script>


<div class='container'>
        {#if ready === true}
            {#each thisPage as section}
                        <a 
                        class="link depth-{section.indent}" 
                        href="{$page.path}#{section.url}"
                        class:shown={visibility === section.url} 
                        > 
                            { clipLinks(section.heading, 40) }
                        </a>
            {/each}
        {/if}
    </div>



<style>

    .container {
        display: flex;
        flex-direction: column;
        z-index: 99;
		height: 100%;
        position: fixed;
        line-height: 1.8em;
        font-size: 11px;
        padding-top: 13px;
        padding-left: 20px;
        white-space: nowrap;
        overflow: hidden;
        text-overflow: ellipsis;
    }

    .shown {
        font-weight:bold;
    }

    .depth-1 {margin-left: 0em}
    .depth-2 {margin-left: 1.5em}
    .depth-3 {margin-left: 3em}
    .depth-4 {margin-left: 4.5em}

</style>