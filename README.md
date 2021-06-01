This is the code which generates my thesis: *Harnessing Content-Aware Programs For Computer-Aided Composition In A Studio-Based Workflow*. It is created with [Svelte Kit](https://kit.svelte.dev/) and uses a node runtime.

### How do I host this thesis locally?
1. `pnpm i`
2. `pnpm run dev`
3. Open browser to localhost:3001

### How can I build it as a static site?
Currently the website is built using the svelte kit static adapter, so the output is a statically rendered site which can be hosted anywhere.

1. `pnpm run build`
2. Output is in the `build` folder

### How can I produce plain text from the written work?
1. `pnpm run convert` or `sh convert.sh`

### How can I get a word count?
1. `pnpm run count` (requires `nltk` python package)

