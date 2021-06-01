<script>
    import { onMount } from "svelte";
    import Container from '$lib/components/Container.svelte';

    export let title = "title";
    export let id = "";

    let sounds = {
        pre : {
            file: '/ss/sage-pre.mp3',
            peaks: '/ss/sage-pre.dat',
            overview: null,
            instance: null,
            audioElement : null,
            slices : '/ss/pre.json'
        },
        post : {
            file: '/ss/sage-post.mp3',
            peaks: '/ss/sage-pre.mp3',
            overview: null,
            instance: null,
            audioElement : null,
            slices : '/ss/post.json'
        },
    }

    let Peaks, peaksControls;

    onMount (async()=>{

        // Fetch data
        
        const module = await import("peaks.js");
        Peaks = module.default;
    
        for ( const [key, wf] of Object.entries(sounds)) {
            const options = {
                containers: {
                    overview: wf.overview
                },
                dataUri: { 
                    arraybuffer: wf.peaks
                },
                mediaElement: wf.audioElement,
                overviewWaveformColor: 'rgba(0, 15, 100, 0.3)',
                overviewHighlightColor: 'grey',
                playheadColor: 'rgba(0, 0, 0, 1)',
                playheadTextColor: '#aaa',
                showPlayheadTime: false,
                pointMarkerColor: '#FF0000',
                axisGridlineColor: '#ccc',
                axisLabelColor: '#aaa',
                randomizeSegmentColor: false,
                segments: wf.segments
            }

            wf.instance = Peaks.init(options, (error, instance) => {
                if (error) {
                    console.log(error)
                } else {
                    wf.instance = instance
                }
            })
        }
    });


</script>

<Container id={id}>
    <div class="vis">
        <div class="overview" bind:this={sounds.pre.overview} />
        <div class="overview" bind:this={sounds.post.overview} />
    </div>
    <div class="peaks-controls" bind:this={peaksControls}>
        <audio controls bind:this={sounds.pre.audioElement}>
            <source src={sounds.pre.file} type="audio/mp3">
            <track kind="captions">
        </audio>
        <audio controls bind:this={sounds.post.audioElement}>
            <source src={sounds.post.file} type="audio/mp3">
            <track kind="captions">
        </audio>
    </div>
</Container>


<style>
    .overview {
        margin-left: 3em;
        margin-right: 3em;
    }

    #title {
        font-style: italic;
        font-size: 16px;
        text-align: center;
        display: inline-block;
    }

    .vis {
        padding-bottom: 5px;
        margin: 0 auto;
    }

    .peaks-controls {
        display: flex;
        flex-direction: column;
        justify-content: center;
        padding-top: 3px;
        width: 80%;
        margin: 0 auto;
    }
</style>


    