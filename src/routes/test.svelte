<script>
    import Album from '$lib/components/Album.svelte';

    const trackData = [
        { name: '--isn', audio: '/pieces/re/--isn.mp3', peaks: '/pieces/re/--isn.dat' },
        { name: 'dotmaxwave', audio: '/pieces/re/dotmaxwave.mp3', peaks: '/pieces/re/dotmaxwave.dat' },
        { name: 'segmnoittet', audio: '/pieces/re/segmnoittet.mp3', peaks: '/pieces/re/segmnoittet.dat' },
        { name: 'sys.ji_', audio: '/pieces/re/sys.ji_.mp3', peaks: '/pieces/re/sys.ji_.dat' },
        { name: 'X86Desc.a', audio: '/pieces/re/X86Desc.a.mp3', peaks: '/pieces/re/X86Desc.a.dat' },
    ]
</script>
<Album
id={'audio1'}
tracks={trackData}
title={'Reconstruction Error'}
/>