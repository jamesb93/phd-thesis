<script>
    import { onMount } from "svelte";
    import Container from '$lib/components/Container.svelte';

    export let title = "Random recombination of voice segments";
    export let caption = "DEMO 1"
    export let id = "";

    let sounds = {
        pre : {
            file: '/ss/sage-pre.mp3',
            peaks: '/ss/sage-pre.dat',
            slices : '/ss/pre.json',
            overview: null,
            instance: null,
            audioElement : null,
            segments : []
        },
        post : {
            file: '/ss/sage-post.mp3',
            peaks: '/ss/sage-post.dat',
            slices : '/ss/post.json',
            overview: null,
            instance: null,
            audioElement : null,
            segments : []
        },
    }

    let Peaks;

    onMount (async()=>{
        for ( const [key, wf] of Object.entries(sounds)) {
            await fetch(wf.slices)
                .then(response => response.json())
                .then(data => {
                    wf.segments = data.segments.map(seg => { return {
                            startTime : seg.start / 44100,
                            endTime : seg.end / 44100,
                            color : seg.color,
                            editable: false
                        } 
                    })
                })

            const module = await import("peaks.js");
            Peaks = module.default;
            const options = {
                containers: {overview: wf.overview},
                dataUri: { arraybuffer: wf.peaks},
                mediaElement: wf.audioElement,
                height: 100,
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
            };

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
    <div class='top-text'>
        <div class='title'>{title}</div>
        <div class='cap'>{caption}</div>
    </div>
    
    <div class='vis'>
        <span class='desc'>Original Source</span>
        <div bind:this={sounds.pre.overview} />
        <audio controls bind:this={sounds.pre.audioElement}>
            <source src={sounds.pre.file} type="audio/mp3">
            <track kind="captions">
        </audio>
    </div>

    <div class='vis'>
        <span class='desc'>Segmented and Shuffled Output</span>
        <div bind:this={sounds.post.overview} />
        <audio controls bind:this={sounds.post.audioElement}>
            <source src={sounds.post.file} type="audio/mp3">
            <track kind="captions">
        </audio>
    </div>

</Container>


<style>
    .top-text {
        display: flex;
        flex-direction: row;
        justify-content: space-between;
    }

    .cap {
        max-width: max-content;
        font-style: italic;
    }

    .title {
        font-weight: bold;
    }

    .vis {
        display: flex;
        flex-direction: column;
        margin-bottom: 30px;
        margin-top: 10px;
    }

    .vis > audio {
        max-width: 50%;
        margin: 0 auto;
    }
</style>


    