const fs = require('fs');
const entries = JSON.parse(fs.readFileSync('scratch/party_c8_lexicon_endpoint.json', 'utf8'));

const memScan = entries.filter(e => e.labels && e.labels.includes('memory-scan'));
const nonMemScan = entries.filter(e => !e.labels || !e.labels.includes('memory-scan'));

console.log('Total entries:', entries.length);
console.log('Memory scan entries:', memScan.length);
console.log('Non-memory-scan entries:', nonMemScan.length);

if (nonMemScan.length > 0) {
  console.log('Sample non-memory-scan entries:');
  for (const e of nonMemScan.slice(0, 10)) {
    console.log(`- ${e.id} | ${e.name} | type=${e.type} | is_global=${e.is_global}`);
  }
}
