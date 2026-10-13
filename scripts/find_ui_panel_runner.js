const fs = require('fs');

async function run() {
  const t = await (await fetch('https://app.wyvern.chat/_next/static/chunks/webpack-f2b63dafb1282dca.js')).text();
  const matches = [...t.matchAll(/"static\/chunks\/[^"]+\.js"/g)].map(m => m[0].replace(/"/g, ''));
  const cMatches = [...t.matchAll(/([0-9]+)===[a-z]\?"static\/chunks\/"\+[a-z]\+"\.(.+?)\.js"/g)].map(m => `static/chunks/${m[1]}.${m[2]}.js`);
  const allChunkPaths = [...new Set([...matches, ...cMatches])];

  for (let cp of allChunkPaths) {
    try {
      let code = await (await fetch('https://app.wyvern.chat/_next/' + cp)).text();
      if (code.includes('ui_panels') && (code.includes('createContext') || code.includes('compile') || code.includes('component_code') || code.includes('values'))) {
        console.log('Found in:', cp);
        let idx = code.indexOf('ui_panels');
        console.log(code.slice(Math.max(0, idx - 200), Math.min(code.length, idx + 400)));
        return;
      }
    } catch(e) {}
  }
  console.log('Finished search.');
}

run().catch(console.error);
