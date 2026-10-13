const fs = require('fs');

async function main() {
  const t = await (await fetch('https://app.wyvern.chat/_next/static/chunks/webpack-f2b63dafb1282dca.js')).text();
  
  const matches = [...t.matchAll(/"static\/chunks\/[^"]+\.js"/g)].map(m => m[0].replace(/"/g, ''));
  const cMatches = [...t.matchAll(/([0-9]+)===[a-z]\?"static\/chunks\/"\+[a-z]\+"\.(.+?)\.js"/g)].map(m => `static/chunks/${m[1]}.${m[2]}.js`);
  
  const allChunkPaths = [...new Set([...matches, ...cMatches])];
  console.log(`Found ${allChunkPaths.length} chunks mapped!`);

  for (const cp of allChunkPaths) {
    try {
      const chunkText = await (await fetch('https://app.wyvern.chat/_next/' + cp)).text();
      if (chunkText.includes('86411:function(')) {
        console.log('FOUND 86411 in:', cp);
        let idx = chunkText.indexOf('86411:function(');
        console.log(chunkText.slice(idx, idx + 1000));
        return;
      }
    } catch(e) {}
  }
  console.log('Search finished.');
}

main().catch(console.error);
