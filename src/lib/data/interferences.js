export const interAlbum = {
    prefix : '/pieces/inter/',
    trackData : [
        { name: 'eee', audio: 'eee.mp3', peaks: 'eee.dat' },
        { name: 'anchors', audio: 'anchors.mp3', peaks: 'anchors.dat' },
    ]
}

export const kindleModes = [
    {
        startTime : 0.0,
        endTime: 1.83,
        labelText: 'Initial static state.'
    },
    {
        startTime: 1.83,
        endTime: 119.0,
        labelText: 'Activity induced through user interaction.'
    },
    {
        startTime: 119.0,
        endTime: 127.0,
        labelText: 'Static state returns after activity ends.'
    }
]

export const xiaomiModes = [
    {
        startTime : 0.0,
        endTime: 40.0,
        labelText: 'Static state.'
    },
    {
        startTime: 40.0,
        endTime: 102.0,
        labelText: 'Active state.'
    }
]