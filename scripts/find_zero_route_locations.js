const fs = require('fs');

const routes = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/updated_travel_routes.json', 'utf8'));
const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));

const routeLocIds = new Set();
routes.forEach(r => {
  routeLocIds.add(r.from_location_id);
  routeLocIds.add(r.to_location_id);
});

const missing = locs.filter(l => !routeLocIds.has(l.id || l._id));
console.log('Total locations:', locs.length);
console.log('Locations in at least 1 route:', routeLocIds.size);
console.log('Locations with ZERO routes:', missing.length);

missing.forEach(m => {
  const parentName = m.parent_location?.name || 'ROOT';
  console.log(`- [${m.id}] "${m.name}" (Parent: ${parentName})`);
});
