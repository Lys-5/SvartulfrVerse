const fs = require('fs');

const routes = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/updated_travel_routes.json', 'utf8'));
const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));
const map = new Map(locs.map(l => [l.id || l._id, l.name]));

routes.filter(r => {
  const f = map.get(r.from_location_id) || '';
  const t = map.get(r.to_location_id) || '';
  return f === 'Solarton' || t === 'Solarton' || f.includes('Solarton Ferry') || t.includes('Solarton Ferry');
}).forEach(r => {
  console.log(`["${map.get(r.from_location_id)}" <-> "${map.get(r.to_location_id)}"] time: ${r.travel_time}h | dist: ${r.distance} mi | desc: ${r.description}`);
});
