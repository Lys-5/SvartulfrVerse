const fs = require('fs');

function deepCheck(obj, path, file) {
  if (!obj || typeof obj !== 'object') return;
  for (const [k, v] of Object.entries(obj)) {
    const curPath = path ? `${path}.${k}` : k;
    if (k.toLowerCase().includes('priority')) {
      if (typeof v !== 'number') {
        console.log(`[ALERT in ${file}] at ${curPath}: type=${typeof v}, val=${JSON.stringify(v)}`);
      }
    }
    if (v && typeof v === 'object') {
      deepCheck(v, curPath, file);
    }
  }
}

const files = [
  'scratch/live_bad_party.json',
  'scratch/bad_chat_log.json',
  'scratch/world_characters.json',
  'scratch/world_locations.json',
  'scratch/world_lexicon.json'
];

for (const f of files) {
  if (fs.existsSync(f)) {
    console.log(`Scanning ${f}...`);
    try {
      const data = JSON.parse(fs.readFileSync(f, 'utf8'));
      deepCheck(data, '', f);
    } catch(e) {
      console.log(`Error parsing ${f}: ${e.message}`);
    }
  }
}
console.log('Finished deep check across all files.');
