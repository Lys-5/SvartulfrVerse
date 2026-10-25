const fs = require('fs');

async function run() {
  const url = 'https://app.wyvern.chat/assistants/simple_assistant_6FXbE28w7n8ETrU41ph7V';
  const res = await fetch(url);
  const html = await res.text();
  console.log('Fetched assistant page HTML. Status:', res.status, 'Size:', html.length);
  fs.writeFileSync('scratch/assistant_page.html', html);

  const scripts = [...html.matchAll(/src=["']([^"']+\.js[^"']*)["']/g)].map(m => m[1]);
  console.log('Total scripts on assistant page:', scripts.length);
  const relevant = scripts.filter(s => s.includes('assistant') || s.includes('mine') || s.includes('edit'));
  console.log('Relevant scripts:', relevant);
  fs.writeFileSync('scratch/assistant_scripts.json', JSON.stringify(scripts, null, 2));
}

run().catch(console.error);
