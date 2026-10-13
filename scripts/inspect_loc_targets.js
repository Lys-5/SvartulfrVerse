const fs = require('fs');
const path = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json';
const locs = JSON.parse(fs.readFileSync(path, 'utf8'));

const targets = ['Refuge', 'Rifugio', 'Cable', 'Marek', 'Rhodes', 'Farm', 'Dairy', 'Dead Dog', 'Ukiyo', 'Apartment C', 'Flat above', 'Dorm', 'Suites', 'Estates', 'Roulotte', 'Villa Douglas', 'Coastal Residential', 'Greek Row', 'Housing', 'Diner', 'Bakery', 'Bean', 'Pharmacy', 'Butcher', 'Sidewinder', 'Verve', 'Claws', 'Tidewrack', 'Camp Mystic', 'Market'];

locs.forEach(l => {
  for (const t of targets) {
    if (l.name.toLowerCase().includes(t.toLowerCase())) {
      console.log(`[${l.id}] "${l.name}" | Prop: ${l.property_config?.enabled || false} | Market: ${l.marketplace_config?.enabled || false} | Jobs: ${l.jobs?.length || 0}`);
      break;
    }
  }
});
