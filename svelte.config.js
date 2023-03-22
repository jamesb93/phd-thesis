import adapter from '@sveltejs/adapter-static';
import { mdsvex } from 'mdsvex';
import slug from 'rehype-slug';
import externalLinks from 'remark-external-links';

/** @type {import('@sveltejs/kit').Config} */
const config = {
	extensions: [ '.svelte', '.svx' ],
	preprocess: [ mdsvex({
		remarkPlugins: [
			[externalLinks, {target: "_blank"}]
		],
		rehypePlugins : [
			slug
		]
	})
	],
	kit: {
		adapter: adapter(),
	}
};

export default config;