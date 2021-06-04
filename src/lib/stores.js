import { writable } from 'svelte/store';
import { browser } from '$app/env';

// Durations for all audio files in the thesis
export const durations = writable({});
async function getDurations() {
    try {
        const response = await fetch('/durations.json')
        durations.set(await response.json())
    } catch(e) {
        console.log(e)
    }
}

if (browser)
    getDurations()

// export const directory = readable({
//     intro : '/introduction',
//     preoc : '/preoccupations',
//     ca : '/content-awareness',
//     proj : '/projects',
//     ss : '/projects/stitch-strata',
//     as : '/projects/annealing-strategies',
//     rt : '/projects/refracted-touch',
//     re : '/projects/reconstruction-error',
//     em : '/projects/electromagnetic',
//     emname: 'Interferences',
//     conc : '/conclusion',
//     ti : '/tech',
//     mosh : '/tech/mosh',
//     reacoma : '/tech/reacoma',
//     ftis : '/tech/ftis',
//     ref : '/references',
//     biom : 'https://www.jamesbradbury.xyz/projects/biomimicry',
//     anchors: 'anchors',
//     eee: 'eee'
// }) 



