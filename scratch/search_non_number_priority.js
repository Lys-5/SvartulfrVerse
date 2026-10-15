const fs = require('fs');
const path = require('path');

function checkFile(f) {
  try {
    const raw = fs.readFileSync(f, 'utf8');
    if (!raw.includes('"priority"')) return;
    const json = JSON.parse(raw);
    function scan(obj, cur = '') {
      if (!obj || typeof obj !== 'object') return;
      for (const [k, v] of Object.entries(obj)) {
        const p = cur ? cur + '.' + k : k;
        if (k === 'priority') {
          if (typeof v !== 'number') {
            console.log(`MATCH IN FILE ${f} at ${p} -> typeof: ${typeof v}, val: ${JSON.stringify(v)}`);
          }
        }
        scan(v, p);
      }
    }
    scan(json);
  } catch (e) {}
}

const dir = 'scratch';
for (const file of fs.readdirSync(dir)) {
  if (file.endsWith('.json')) {
    checkFile(path.join(dir, file));
  }
}
console.log('Search in scratch finished.');
