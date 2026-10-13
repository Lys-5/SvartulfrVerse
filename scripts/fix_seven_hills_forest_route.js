const fs = require('fs');

const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
const worldId = '_CgYT8fHXpDC4crjmegQF7';

const LOC = {
  SevenHills: "_EwMMJ7KEg9ATJ3mTXBaha",
  Oldtown: "_Gnm9WMQNjhUWJLhrkpqQk",
  Arcadia: "_X6R6dKTzkjdFk6cqdt2we",
  BlackwoodForest: "_HN1tmm3Ex4LBh2HtWGUbq",
  BloodmoonPack: "_xEB9X8wUGwQrELYzKX7gt",
  VillaDouglas: "_9H2EmzRm92QxBpkmJUR1z"
};

async function main() {
  console.log('Fetching world data...');
  const res = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  if (!res.ok) throw new Error('Fetch failed: ' + res.status);
  const world = await res.json();

  let routes = world.travel_routes || [];
  console.log(`Current routes: ${routes.length}`);

  let modifiedCount = 0;

  routes = routes.map(r => {
    // 1. If route connects Oldtown to Blackwood Forest, re-route from Seven Hills
    if ((r.from_location_id === LOC.Oldtown && r.to_location_id === LOC.BlackwoodForest) ||
        (r.from_location_id === LOC.BlackwoodForest && r.to_location_id === LOC.Oldtown)) {
      console.log(`Re-routing [${r.id}] from Oldtown <-> Blackwood Forest to Seven Hills <-> Blackwood Forest`);
      modifiedCount++;
      return {
        ...r,
        from_location_id: LOC.SevenHills,
        to_location_id: LOC.BlackwoodForest,
        travel_time: 1,
        distance: 6,
        description: "Mountain ridge road climbing from Seven Hills directly into the dense pines of Blackwood Forest."
      };
    }

    // 2. If route connects Oldtown to Bloodmoon Pack, re-route from Seven Hills
    if ((r.from_location_id === LOC.Oldtown && r.to_location_id === LOC.BloodmoonPack) ||
        (r.from_location_id === LOC.BloodmoonPack && r.to_location_id === LOC.Oldtown)) {
      console.log(`Re-routing [${r.id}] from Oldtown <-> Bloodmoon Pack to Seven Hills <-> Bloodmoon Pack`);
      modifiedCount++;
      return {
        ...r,
        from_location_id: LOC.SevenHills,
        to_location_id: LOC.BloodmoonPack,
        travel_time: 1,
        distance: 8,
        description: "Northern ridge crossing leading from Seven Hills into the wild, unlit woods of Bloodmoon Pack Territory."
      };
    }

    return r;
  });

  // 3. Ensure Seven Hills <-> Arcadia exists (directly bordering as shown in map)
  const hasSevenHillsArcadia = routes.some(r =>
    (r.from_location_id === LOC.SevenHills && r.to_location_id === LOC.Arcadia) ||
    (r.from_location_id === LOC.Arcadia && r.to_location_id === LOC.SevenHills)
  );

  if (!hasSevenHillsArcadia) {
    console.log('Adding missing direct route: Seven Hills <-> Arcadia');
    routes.push({
      id: "seven-hills-to-arcadia-direct",
      from_location_id: LOC.SevenHills,
      to_location_id: LOC.Arcadia,
      bidirectional: true,
      travel_time: 0,
      distance: 3,
      required_mediums: ["land"],
      description: "Scenic foothill road connecting Seven Hills estates down into the quiet suburban streets of Arcadia.",
      hidden: false
    });
    modifiedCount++;
  }

  console.log(`Modifications prepared: ${modifiedCount}. Total routes: ${routes.length}`);

  // Send PUT update
  const putRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      free_travel: false,
      travel_routes: routes
    })
  });

  if (!putRes.ok) throw new Error('PUT failed: ' + putRes.status);
  console.log('PUT succeeded (200).');

  // Verify fresh GET
  const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const verified = await verifyRes.json();
  console.log('Verified travel_routes count:', verified.travel_routes?.length);

  // Check specific Seven Hills routes
  const shRoutes = verified.travel_routes.filter(r =>
    r.from_location_id === LOC.SevenHills || r.to_location_id === LOC.SevenHills
  );
  console.log('\nVerified Seven Hills connections:');
  const locs = JSON.parse(fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/all_locations_dump.json', 'utf8'));
  const map = new Map(locs.map(l => [l.id || l._id, l.name]));

  shRoutes.forEach(r => {
    console.log(`- "${map.get(r.from_location_id)}" <-> "${map.get(r.to_location_id)}" | time: ${r.travel_time}h | dist: ${r.distance} | desc: ${r.description}`);
  });

  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/updated_travel_routes.json', JSON.stringify(verified.travel_routes, null, 2));
}

main().catch(console.error);
