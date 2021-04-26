const node = require('@sveltejs/adapter-static');
const pkg = require('./package.json');
const { mdsvex } = require('mdsvex');
const slug = require('remark-slug');
const externalLinks = require('remark-external-links');

/** @type {import('@sveltejs/kit').Config} */
module.exports = {
	extensions: [ '.svelte', '.svx' ],
	preprocess: [ mdsvex({
		remarkPlugins: [
			slug,
			[externalLinks, {target: "_blank"}]
		]
	})
	],
	kit: {
		// By default, `npm run build` will create a standard Node app.
		// You can create optimized builds for different platforms by
		// specifying a different adapter
		adapter: node(),

		// hydrate the <div id="svelte"> element in src/app.html
		target: '#svelte',

		vite: {}
	}
};
