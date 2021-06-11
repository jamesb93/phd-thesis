<script>

    import { afterUpdate, onDestroy, onMount } from 'svelte';
    import { page } from '$app/stores';
    let visibility;
    let observer = null;
    let ready = false;
    let contents = [];
    let thisPage = null;
    let tempIntersect;
    $: thisPage = contents[$page.path];

    console.log($page.path)
    
    function handleIntersect(entries, observer) {
        let lowest = Infinity;
        entries = entries.filter(entry => entry.isIntersecting);
        if (entries.length > 0) {
            entries.forEach(entry => {
                const y = entry.boundingClientRect.y;
                if (y < lowest) {
                    lowest = y;
                    tempIntersect = entry.target.id; // hold the value for now
                }
            })    
        }
        visibility = tempIntersect;
    }


    function clipLinks(t, maxLen) {
        return t.length >= maxLen ? t.substr(0, maxLen)+'...' : t 
    }
    async function makeObserver() {
        if (observer)
            observer.disconnect();
        observer = new IntersectionObserver(handleIntersect, {rootMargin: '0px'});

        if (thisPage) {
            thisPage.forEach(c => {
                let element = document.getElementById(c.url);
                if (element)
                    observer.observe(element);
            })
            ready = true;
        }
    }

    onMount(async () => {
        await fetch('/structure.json')
            .then(response => response.json())
            .then(data => contents = data);

        await makeObserver();
    })

    afterUpdate(async()=> {
        ready = false;
        await makeObserver();
    })

    onDestroy(() => {
        if (observer) {
            observer.disconnect();
        }
    })


</script>


<div class='container'>
    {#if ready === true}
        {#if thisPage}
            {#each thisPage as section}
                    <a 
                    class="link depth-{section.indent}" 
                    href="{$page.path}#{section.url}"
                    class:shown={visibility === section.url}
                    on:click={ visibility = section.url } 
                    > 
                        { clipLinks(section.heading, 40) }
                    </a>
            {/each}
        {/if}
    {/if}
</div>



<style>
    .container {
        display: flex;
        flex-direction: column;
        /* z-index: 99; */
		height: 100%;
        position: fixed;
        line-height: 1.8em;
        font-size: 11px;
        padding-top: 13px;
        margin-left: 15px;
        padding-left: 5px;
        overflow: hidden;
    }

    .shown {
        font-weight:bold;
    }

    .depth-1 {margin-left: 0em}
    .depth-2 {margin-left: 1.5em}
    .depth-3 {margin-left: 3em}
    .depth-4 {margin-left: 4.5em}

</style>