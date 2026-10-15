const fs = require('fs');
const entries = JSON.parse(fs.readFileSync('scratch/party_c8_lexicon_endpoint.json', 'utf8'));

const oct14 = entries.filter(e => e.created_at && e.created_at.startsWith('2026-10-14'));
console.log('Entries created on 2026-10-14:', oct14.length);

for (const e of oct14) {
  console.log(`- ${e.id} | "${e.name}" | type=${e.type} | labels=${JSON.stringify(e.labels)} | priority: typeof=${typeof e.priority}, val=${JSON.stringify(e.priority)}`);
}
