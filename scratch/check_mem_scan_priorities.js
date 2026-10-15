const fs = require('fs');

const entries = JSON.parse(fs.readFileSync('scratch/party_c8_lexicon_endpoint.json', 'utf8'));
console.log('Total entries:', entries.length);

const memoryScanEntries = entries.filter(e => e.labels && e.labels.includes('memory-scan'));
console.log('Memory scan entries count:', memoryScanEntries.length);

for (let i = 0; i < memoryScanEntries.length; i++) {
  const e = memoryScanEntries[i];
  for (const [k, v] of Object.entries(e)) {
    if (k.toLowerCase().includes('priority') && typeof v !== 'number') {
      console.log(`[ALERT] Entry ${i} (${e.name}) has non-number priority: ${k}=${JSON.stringify(v)}`);
    }
  }
}
console.log('Checked priority on all memory scan entries.');
