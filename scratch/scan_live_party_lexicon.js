const fs = require('fs');
const bad = JSON.parse(fs.readFileSync('scratch/live_bad_party.json', 'utf8'));
const entries = bad.world_lexicon_entries || [];
console.log('Total entries:', entries.length);

let alertCount = 0;
for (let i = 0; i < entries.length; i++) {
  const e = entries[i];
  // Check every key in e
  for (const [k, v] of Object.entries(e)) {
    if (k.toLowerCase().includes('priority')) {
      if (typeof v !== 'number') {
        console.log(`[ALERT] Entry ${i} (${e.name || e.id}) has non-number priority property '${k}': type=${typeof v}, val=${JSON.stringify(v)}`);
        alertCount++;
      }
    }
    // Also check sub-objects
    if (v && typeof v === 'object') {
      for (const [subK, subV] of Object.entries(v)) {
        if (subK.toLowerCase().includes('priority')) {
          if (typeof subV !== 'number') {
            console.log(`[ALERT] Entry ${i} (${e.name || e.id}) has nested non-number priority '${k}.${subK}': type=${typeof subV}, val=${JSON.stringify(subV)}`);
            alertCount++;
          }
        }
      }
    }
  }
}
console.log(`Done scanning. Total alerts: ${alertCount}`);
