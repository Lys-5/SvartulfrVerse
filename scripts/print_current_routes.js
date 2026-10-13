const fs = require('fs');
const routes = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/current_travel_routes.json', 'utf8'));
const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));
const map = new Map(locs.map(l => [l.id || l._id, l.name]));

console.log('Total routes:', routes.length);
console.log('Routes with no distance:', routes.filter(r => r.distance == null).length);

routes.forEach((r, i) => {
  const from = map.get(r.from_location_id) || r.from_location_id;
  const to = map.get(r.to_location_id) || r.to_location_id;
  console.log(`[${i+1}] "${from}" <-> "${to}" | time: ${r.travel_time}h | dist: ${r.distance ?? 'NONE'} | med: ${r.required_mediums?.join(',')}`);
});
