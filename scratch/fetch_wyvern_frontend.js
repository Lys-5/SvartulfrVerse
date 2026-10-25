const fs = require('fs');

async function run() {
  const res = await fetch('https://app.wyvern.chat/');
  const html = await res.text();
  console.log('Fetched index HTML. Size:', html.length);
  fs.writeFileSync('scratch/wyvern_index.html', html);

  const scriptMatches = [...html.matchAll(/src=["']([^"']+\.js[^"']*)["']/g)].map(m => m[1]);
  console.log('Scripts found:', scriptMatches);
  fs.writeFileSync('scratch/wyvern_scripts.json', JSON.stringify(scriptMatches, null, 2));
}

run().catch(console.error);
