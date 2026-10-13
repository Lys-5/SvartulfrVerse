const fs = require('fs');

const routes = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/current_travel_routes.json', 'utf8'));
const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));

const locIds = new Set(locs.map(l => l.id || l._id));

routes.forEach((r, idx) => {
  const fromOk = locIds.has(r.from_location_id);
  const toOk = locIds.has(r.to_location_id);
  if (!fromOk || !toOk) {
    console.log(`Route [${idx + 1}] (${r.id}) has invalid loc: from (${r.from_location_id} ${fromOk}) -> to (${r.to_location_id} ${toOk}) | desc: ${r.description}`);
  }
});
