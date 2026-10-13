const fs = require('fs');

async function searchChunksForTypes() {
  const webpackManifest = await (await fetch('https://app.wyvern.chat/_next/static/chunks/webpack-f2b63dafb1282dca.js')).text();
  const matches = [...webpackManifest.matchAll(/"static\/chunks\/[^"]+\.js"/g)].map(m => m[0].replace(/"/g, ''));
  const cMatches = [...webpackManifest.matchAll(/([0-9]+)===[a-z]\?"static\/chunks\/"\+[a-z]\+"\.(.+?)\.js"/g)].map(m => `static/chunks/${m[1]}.${m[2]}.js`);
  const allChunkPaths = [...new Set([...matches, ...cMatches])];

  console.log(`Searching ${allChunkPaths.length} chunk paths concurrently...`);

  await Promise.all(allChunkPaths.map(async (cp) => {
    try {
      const res = await fetch('https://app.wyvern.chat/_next/' + cp);
      if (!res.ok) return;
      const text = await res.text();
      
      const keywords = ['introduction_pages', 'intro_fields', 'p_species_select'];
      const found = keywords.filter(k => text.includes(k));
      if (found.length > 0) {
        console.log(`\n=== MATCH in ${cp} (found: ${found.join(', ')}) ===`);
        for (const kw of found) {
          let idx = text.indexOf(kw);
          while (idx !== -1) {
            console.log(`[KW: ${kw}] ` + text.slice(Math.max(0, idx - 150), Math.min(text.length, idx + 250)));
            idx = text.indexOf(kw, idx + kw.length + 50);
          }
        }
      }
    } catch(e) {}
  }));
  console.log('Search completed.');
}

searchChunksForTypes().catch(console.error);
