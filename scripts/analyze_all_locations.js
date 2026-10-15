const fs = require('fs');
const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));

const lines = locs.map((l, i) => {
  const p = l.parent_location ? l.parent_location.name : 'ROOT';
  const hasProp = l.property_config && Object.keys(l.property_config).length > 0;
  const hasMarket = l.marketplace_config && l.marketplace_config.enabled;
  const hasJobs = l.jobs && l.jobs.length > 0;
  return `${i + 1}. [${l.id}] "${l.name}" (Parent: ${p}) | Prop: ${hasProp ? 'YES' : 'NO'} | Market: ${hasMarket ? 'YES' : 'NO'} | Jobs: ${hasJobs ? 'YES' : 'NO'}`;
});

fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/locations_summary.txt', lines.join('\n'), 'utf8');
console.log('Summary saved! Total:', lines.length);
