export const classifier = {
    prefix : '/inter/classifier/',
    trackData : [
        { name: 'Kindle_02_1.wav (Active)', audio: 'A_Kindle_02_1.mp3', peaks: 'A_Kindle_02_1.dat' },
        { name: 'Xiamo_Note 4X_01_1.wav (Active)', audio: 'A_Xiamo_Note 4X_01_1.mp3', peaks: 'A_Xiamo_Note 4X_01_1.dat' },
        { name: 'Kindle_02_2.wav (Active)', audio: 'A_Kindle_02_2.mp3', peaks: 'A_Kindle_02_2.dat' },
        { name: 'Kindle_04_9.wav (Passive)', audio: 'P_Kindle_04_9.mp3', peaks: 'P_Kindle_04_9.dat' },
        { name: 'Mouse_01_1.wav (Passive)', audio: 'P_Mouse_01_1.mp3', peaks: 'P_Mouse_01_1.dat' },
        { name: 'RME_Face_Panel_01_1.wav (Passive)', audio: 'P_RME_Face_Panel_01_1.mp3', peaks: 'P_RME_Face_Panel_01_1.dat' },
        { name: 'Xiamo Note 4X_01_0.wav (Passive)', audio: 'P_Xiamo Note 4X_01_0.mp3', peaks: 'P_Xiamo Note 4X_01_0.dat' },

    ]
}

export const xboxModes = [
    {
        startTime: 0.0,
        endTime: 3.4,
        labelText: 'Static'
    },
    {
        startTime : 3.4,
        endTime: 4.65,
        labelText: 'Active',
    },
    {
        startTime : 4.65,
        endTime: 9.08,
        labelText: 'Static',
    },
    {
        startTime : 9.08,
        endTime: 10.235,
        labelText: 'Active',
    },
    {
        startTime : 10.235,
        endTime: 12.453,
        labelText: 'Static',
    },
    {
        startTime: 12.453,
        endTime: 26.0,
        labelText: 'Active'
    },
    {
        startTime: 26.0,
        endTime: 31.0,
        labelText: 'Static'
    }
]

export const interAlbum = {
    prefix : '/pieces/inter/',
    trackData : [
        { name: 'eee', audio: 'eee.mp3', peaks: 'eee.dat' },
        { name: 'anchors', audio: 'anchors.mp3', peaks: 'anchors.dat' },
    ]
}

export const kindleModes = [
    { startTime : 0.0, endTime: 1.83, labelText: 'Initial static state.' },
    { startTime: 1.83, endTime: 119.0, labelText: 'Activity induced through user interaction.' },
    { startTime: 119.0, endTime: 127.0, labelText: 'Static state returns after activity ends.'}
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