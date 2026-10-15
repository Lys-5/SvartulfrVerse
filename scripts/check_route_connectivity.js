const fs = require('fs');

const routes = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/current_travel_routes.json', 'utf8'));
const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));

const locById = new Map();
locs.forEach(l => locById.set(l.id || l._id, l));

// Check connectivity: a location is connected if it has a parent or children, OR is in a route
const routeNodes = new Set();
routes.forEach(r => {
  routeNodes.add(r.from_location_id);
  routeNodes.add(r.to_location_id);
});

console.log('Total locations:', locs.length);
console.log('Locations directly in travel_routes:', routeNodes.size);

// Print root locations and major destinations not in travel_routes
const roots = locs.filter(l => !l.parent_location);
console.log('\n=== ROOT LOCATIONS ===');
roots.forEach(r => {
  console.log(`[${r.id}] "${r.name}" | In route: ${routeNodes.has(r.id)}`);
});

const majorMissing = locs.filter(l => {
  // If location has no route directly and is a key destination
  return !routeNodes.has(l.id) && (!l.parent_location || roots.some(r => r.id === l.parent_location.id || r.id === l.parent_location._id));
});

console.log(`\nMajor level-1 locations missing from routes: ${majorMissing.length}`);
majorMissing.forEach(m => {
  const pName = m.parent_location ? locById.get(m.parent_location.id || m.parent_location._id)?.name : 'ROOT';
  console.log(`- [${m.id}] "${m.name}" (Parent: ${pName})`);
});
