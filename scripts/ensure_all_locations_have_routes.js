const fs = require('fs');
const crypto = require('crypto');

const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
const worldId = '_CgYT8fHXpDC4crjmegQF7';

function genUuid() {
  return crypto.randomUUID();
}

async function main() {
  console.log('Fetching world data...');
  const res = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (!res.ok) throw new Error('Fetch failed: ' + res.status);
  const world = await res.json();

  let routes = world.travel_routes || [];
  const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));

  const locById = new Map();
  locs.forEach(l => locById.set(l.id || l._id, l));

  // Determine which locations currently have routes
  const connectedLocs = new Set();
  routes.forEach(r => {
    connectedLocs.add(r.from_location_id);
    connectedLocs.add(r.to_location_id);
  });

  const missingLocs = locs.filter(l => !connectedLocs.has(l.id || l._id));
  console.log(`Current routes: ${routes.length}`);
  console.log(`Connected locations: ${connectedLocs.size} / ${locs.length}`);
  console.log(`Missing locations: ${missingLocs.length}`);

  const addedRoutes = [];

  missingLocs.forEach(loc => {
    const locId = loc.id || loc._id;
    let targetParentId = loc.parent_location ? (loc.parent_location.id || loc.parent_location._id) : null;
    let medium = ["land"];
    let dist = 1;
    let time = 0;
    let desc = `Walkway connecting ${loc.name} with its local district.`;

    // Specific routing logic depending on the location
    if (!targetParentId) {
      // It's a root location like "Zone di Transito e Confine"
      if (locId === "_zjA9MJEAVjjFn64jjtcb6") {
        targetParentId = "_FrXnp2CALTP44CP3KVAhb"; // Ventura / Route 101
        desc = "Highway interchange connecting Zone di Transito to Route 101 corridor.";
        dist = 2;
      }
    } else {
      const parent = locById.get(targetParentId);
      const parentName = parent ? parent.name : "local area";

      if (parentName.includes("DDM") || loc.name.includes("DDM") || loc.name.includes("Euclidean") || loc.name.includes("Lower Levels")) {
        medium = ["omniversal"];
        desc = `Non-euclidean corridor connecting ${loc.name} within DDM Headquarters.`;
      } else if (parentName.includes("Otherworld") || loc.name.includes("Otherworld")) {
        desc = `Glimmering fae pathway leading to ${loc.name} across The Otherworld.`;
        dist = 2;
      } else if (parentName.includes("Greek Row")) {
        desc = `Greek Row residential walkway leading into the chapter house of ${loc.name}.`;
        dist = 1;
      } else if (parentName.includes("Wyrm Dormitories")) {
        desc = `Interior dormitory corridor leading into ${loc.name}.`;
        dist = 1;
      } else if (parentName.includes("Bricklane Mall")) {
        desc = `Covered shopping promenade leading directly into ${loc.name}.`;
        dist = 1;
      } else if (parentName.includes("Science Quarter")) {
        desc = `Laboratory concourse and containment corridor leading to ${loc.name}.`;
        dist = 1;
      } else if (parentName.includes("Basilica Library")) {
        desc = `Quiet gothic library wing opening into ${loc.name}.`;
        dist = 1;
      } else if (parentName.includes("Archer Wolfwood Hall")) {
        desc = `Academic lecture hallway leading into ${loc.name}.`;
        dist = 1;
      } else if (parentName.includes("CUMS") || parentName.includes("Magical Sciences")) {
        desc = `Enchanted stone avenue leading into ${loc.name} on the CUMS campus.`;
        dist = 2;
      } else if (parentName.includes("Villa Douglas")) {
        desc = `Private family wing passage leading into ${loc.name}.`;
        dist = 1;
      } else if (parentName.includes("Bulls Stadium")) {
        desc = `Athletic breezeway leading into ${loc.name}.`;
        dist = 1;
      } else {
        desc = `Local street connecting ${loc.name} to ${parentName}.`;
        dist = 1;
      }
    }

    if (targetParentId) {
      addedRoutes.push({
        id: genUuid(),
        from_location_id: targetParentId,
        to_location_id: locId,
        bidirectional: true,
        travel_time: time,
        distance: dist,
        required_mediums: medium,
        description: desc,
        hidden: false
      });
      connectedLocs.add(locId);
    }
  });

  console.log(`Generated ${addedRoutes.length} new routes to connect all locations.`);
  const finalRoutes = [...routes, ...addedRoutes];

  // Send PUT update
  console.log('Sending PUT update to World API...');
  const putRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      free_travel: false,
      travel_routes: finalRoutes
    })
  });

  if (!putRes.ok) throw new Error('PUT failed: ' + putRes.status);
  console.log('PUT succeeded (200).');

  // Verify fresh GET
  console.log('Verifying with fresh GET...');
  const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const verified = await verifyRes.json();
  const vRoutes = verified.travel_routes || [];
  console.log(`Verified travel_routes count: ${vRoutes.length}`);

  const finalConnected = new Set();
  vRoutes.forEach(r => {
    finalConnected.add(r.from_location_id);
    finalConnected.add(r.to_location_id);
  });

  const finalMissing = locs.filter(l => !finalConnected.has(l.id || l._id));
  console.log(`\nFinal check: ${finalConnected.size} / ${locs.length} locations connected.`);
  console.log(`Locations still missing routes: ${finalMissing.length}`);
  if (finalMissing.length > 0) {
    console.log('Missing:', finalMissing.map(m => m.name));
  } else {
    console.log('SUCCESS! ALL 188 LOCATIONS HAVE AT LEAST 1 TRAVEL ROUTE!');
  }

  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/updated_travel_routes.json', JSON.stringify(vRoutes, null, 2));
}

main().catch(console.error);
