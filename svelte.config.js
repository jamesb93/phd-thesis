import adapter from '@sveltejs/adapter-static';
import { mdsvex } from 'mdsvex';
import slug from 'remark-slug';
import externalLinks from 'remark-external-links';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: [ '.svelte', '.svx' ],
	preprocess: [ mdsvex({
		remarkPlugins: [
			slug,
			[externalLinks, {target: "_blank"}]
		]
	})
	],
	kit: {
		adapter: adapter(),
		target: '#svelte',
	}
};

export default config;