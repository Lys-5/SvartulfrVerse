const fs = require('fs');

const routes = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/updated_travel_routes.json', 'utf8'));
const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));
const map = new Map(locs.map(l => [l.id || l._id, l.name]));

console.log('Total verified routes:', routes.length);
console.log('\nTop 5 initial routes:');
routes.slice(0, 5).forEach((r, i) => {
  console.log(`[${i+1}] "${map.get(r.from_location_id)}" <-> "${map.get(r.to_location_id)}" | time: ${r.travel_time}h | dist: ${r.distance} | med: ${r.required_mediums?.join(',')}`);
});

console.log('\nSample newly added routes:');
routes.slice(63, 78).forEach((r, i) => {
  console.log(`[${i+64}] "${map.get(r.from_location_id)}" <-> "${map.get(r.to_location_id)}" | time: ${r.travel_time}h | dist: ${r.distance} | med: ${r.required_mediums?.join(',')}`);
});
