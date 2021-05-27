import { writable, get } from 'svelte/store';

export const durations = writable({});


async function getDurations() {
    try {
        const response = await fetch('/durations.json')
        durations.set(await response.json())
    } catch(e) {
        console.log(e)
    }
}

getDurations()



