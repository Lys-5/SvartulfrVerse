const fs = require('fs');

const routes = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/current_travel_routes.json', 'utf8'));
const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));

const locMap = new Map();
locs.forEach(l => locMap.set(l.id || l._id, l.name));

console.log('Total routes:', routes.length);
console.log('Route fields sample:', Object.keys(routes[0]));

routes.slice(0, 15).forEach((r, idx) => {
  const fromName = locMap.get(r.from_location_id) || r.from_location_id;
  const toName = locMap.get(r.to_location_id) || r.to_location_id;
  console.log(`[${idx + 1}] "${fromName}" <-> "${toName}" | time: ${r.travel_time}h | distance: ${r.distance || '(empty)'} | mediums: ${r.required_mediums?.join(',')} | desc: ${r.description?.slice(0, 50)}...`);
});
