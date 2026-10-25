const fs = require('fs');

async function run() {
  const chunkUrl = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/assistants/%5Bid%5D/page-cbe4530944bdffb9.js';
  const res = await fetch(chunkUrl);
  const code = await res.text();
  console.log('Fetched assistant page chunk. Size:', code.length);
  fs.writeFileSync('scratch/assistant_chunk.js', code);

  // Also let's inspect the HTML of assistant_page.html to see if initial data or hydration state is embedded!
  const html = fs.readFileSync('scratch/assistant_page.html', 'utf8');
  const selfDataMatches = [...html.matchAll(/self\.__next_f\.push\(\[1,"(.*?)"\]\)/g)].map(m => m[1]);
  console.log('Next.js hydration chunks:', selfDataMatches.length);
  fs.writeFileSync('scratch/hydration_data.txt', selfDataMatches.join('\n\n---CHUNK---\n\n'));
}

run().catch(console.error);
