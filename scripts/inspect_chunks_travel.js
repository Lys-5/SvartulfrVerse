const fs = require('fs');
const urls = [
  '72004-17555a95f9a477eb.js',
  '82025-d45851e01a02ef68.js',
  '60419-be51aadadc86068b.js',
  '55846-670497f4a71bfe73.js',
  '49610-1c1b0eb57527b2e1.js',
  '58501-ff183c34fe29d7b3.js',
  '59364-07b37c24b9a03959.js'
];

async function inspect() {
  for (const f of urls) {
    const res = await fetch('https://app.wyvern.chat/_next/static/chunks/' + f);
    const text = await res.text();
    for (const kw of ['Distance (flavor)', 'Distance', 'flavor', 'hidden']) {
      let pos = 0;
      while ((pos = text.toLowerCase().indexOf(kw.toLowerCase(), pos)) !== -1) {
        const snippet = text.slice(Math.max(0, pos - 100), pos + 100);
        if (snippet.includes('travel') || snippet.includes('route')) {
          console.log(`=== Match '${kw}' in ${f} at ${pos} ===`);
          console.log(text.slice(Math.max(0, pos - 120), pos + 150));
        }
        pos += kw.length;
      }
    }
  }
}

inspect().catch(console.error);
