export const eReaderPoints = [ { time: 18.3, editable: false, labelText: 'Interjection'} ]

export const eReaderSegs = [
    { startTime: 0.0, endTime: 18.3, labelText: 'Static' },
    { startTime: 18.3, endTime: 136.0, labelText: 'Active' },
]

export const anchors = {
    prefix: '/inter/anchors/',
    trackData: [
        { name: 'Anchor 1', audio: 'anchor1.mp3', peaks: 'anchor1.dat' },
        { name: 'Anchor 2', audio: 'anchor2.mp3', peaks: 'anchor2.dat' },
        { name: 'Anchor 3', audio: 'anchor3.mp3', peaks: 'anchor3.dat' },
    ]
}

export const eeeSegments = [
    { startTime: 0.0, endTime: 221.0, labelText: 'Extension of antiphony between active and static states' },
    { startTime: 221.0, endTime: 408.0, labelText: 'Development of static musical behaviour' },
    { startTime: 408.0 , endTime: 712, labelText: 'Rhythmicised static and active behaviours' },
]

export const anchorsSegments = [
    {}
]

export const rhythmicConstructs = {
    prefix: '/inter/rhythmic-constructs/',
    trackData : [
        { name: 'Rhythmic Construct 1', audio: '1.mp3', peaks: '1.dat' },
        { name: 'Rhythmic Construct 2', audio: '2.mp3', peaks: '2.dat' },
        { name: 'Rhythmic Construct 3', audio: '3.mp3', peaks: '3.dat' }
    ]
}

export const foundations = {
    prefix : '/inter/',
    trackData : [
      { name: "Foundational Layer 1", audio: "foundation-1.mp3", peaks: "foundation-1.dat" },
      { name: "Foundational Layer 2", audio: "foundation-2.mp3", peaks: "foundation-2.dat" }
    ]
}

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
    prefix : '/pieces/Interferences/',
    trackData : [
        { name: 'G090G10564620B7Q', audio: 'G090G10564620B7Q.mp3', peaks: 'G090G10564620B7Q.dat' },
        { name: 'P 08_19', audio: 'P 08_19.mp3', peaks: 'P 08_19.dat' },
    ]
}

export const kindleModes = [
    { startTime : 0.0, endTime: 1.83, labelText: 'Initial static state' },
    { startTime: 1.83, endTime: 119.0, labelText: 'Activity induced through user interaction' },
    { startTime: 119.0, endTime: 127.0, labelText: 'Static state returns after activity ends'}
]

export const xiaomiModes = [
    {
        startTime : 0.0,
        endTime: 40.0,
        labelText: 'Static state'
    },
    {
        startTime: 40.0,
        endTime: 102.0,
        labelText: 'Active state'
    }
]

export const loopExperiments = {
    prefix: '/inter/loop-experiments/',
    trackData : [
        { name: 'Loop Experiment 1', audio: '1.mp3', peaks: '1.dat' },
        { name: 'Loop Experiment 2', audio: '2.mp3', peaks: '2.dat' },
        { name: 'Loop Experiment 3', audio: '3.mp3', peaks: '3.dat' },
        { name: 'Loop Experiment 4', audio: '4.mp3', peaks: '4.dat' },
        { name: 'Loop Experiment 5', audio: '5.mp3', peaks: '5.dat' }
    ]
}

export const baseSketchSegs = [
    { startTime: 33.0 , endTime: 67.0, labelText: 'Machine-like "error" tones (1)' },
    { startTime: 100.0, endTime: 135.0, labelText: 'Machine-like "error" tones (2)' },
    { startTime: 284.0, endTime: 372.0, labelText: 'High frequency content panned centre between conflicting tones' },
    { startTime: 402.0, endTime: 438.0, labelText: 'Mid to low frequency "rhythmic static"' },
    { startTime: 468.0, endTime: 516.0, labelText: 'Detailed, chaotic and rapidly morphing sounds'}
]