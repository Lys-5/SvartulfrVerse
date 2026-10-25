const fs = require('fs');

async function run() {
  const scripts = JSON.parse(fs.readFileSync('scratch/wyvern_scripts.json', 'utf8'));
  console.log(`Searching across ${scripts.length} script chunks...`);

  const results = [];
  for (let i = 0; i < scripts.length; i++) {
    const s = scripts[i];
    const url = 'https://app.wyvern.chat' + s;
    try {
      const res = await fetch(url);
      const code = await res.text();
      if (code.includes('simple-assistant-config') || code.includes('prompt-assembly') || code.includes('prompt_assembly') || code.includes('simple_assistant') || code.includes('narrator-presets')) {
        console.log(`Match found in chunk ${i}: ${s} (size: ${code.length})`);
        results.push({ script: s, size: code.length });
        fs.writeFileSync(`scratch/match_chunk_${i}.js`, code);
      }
    } catch (e) {
      // ignore
    }
  }

  console.log('Total matches found:', results.length);
  fs.writeFileSync('scratch/matched_chunks.json', JSON.stringify(results, null, 2));
}

run().catch(console.error);
