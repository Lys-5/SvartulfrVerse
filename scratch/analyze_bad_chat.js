const fs = require('fs');

const log = JSON.parse(fs.readFileSync('scratch/bad_chat_log.json', 'utf8'));

console.log('Top level keys:');
for (const [k, v] of Object.entries(log)) {
  const t = Array.isArray(v) ? `Array(${v.length})` : typeof v;
  console.log(` - ${k}: ${t}`);
}

function findPriority(obj, path = '') {
  if (!obj || typeof obj !== 'object') return;
  for (const [k, v] of Object.entries(obj)) {
    const cur = path ? path + '.' + k : k;
    if (k.toLowerCase().includes('priority')) {
      console.log(`MATCH at ${cur}: typeof=${typeof v}, val=${JSON.stringify(v)}`);
    }
    if (typeof v === 'object') {
      findPriority(v, cur);
    }
  }
}

console.log('\nSearching priority:');
findPriority(log);
