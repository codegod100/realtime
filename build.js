const esbuild = require('esbuild');
const sveltePlugin = require('esbuild-svelte');

async function watch() {
    let ctx = await esbuild.context({
        entryPoints: ['components/index.js'], // replace with your entry file
        mainFields: ["svelte", "browser", "module", "main"],
        conditions: ["svelte", "browser"],
        bundle: true,
        outfile: 'static/bundle.js', // replace with your output file
        plugins: [sveltePlugin()],
        logLevel: 'info',
    })
    await ctx.watch();
    console.log("watching")
}


function build() {
    esbuild
        .build({
            entryPoints: ['components/index.js'], // replace with your entry file
            mainFields: ["svelte", "browser", "module", "main"],
            conditions: ["svelte", "browser"],
            bundle: true,
            outfile: 'static/bundle.js', // replace with your output file
            plugins: [sveltePlugin()],
            logLevel: 'info',
        })
        .catch(() => process.exit(1));
}

build()