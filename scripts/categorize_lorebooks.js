const fs = require('fs');

async function analyzeLorebooks() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  // 1. Fetch LA: New Moon Compendium
  const resL = await fetch('https://app.wyvern.chat/api/lorebooks/_U9TVTNMFk3R1VdAUV9yhP', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const dL = await resL.json();
  const entriesL = Array.isArray(dL.entries) ? dL.entries : Object.values(dL.entries || {});

  // 2. Fetch Aegis City Hunters
  const resA = await fetch('https://app.wyvern.chat/api/lorebooks/_1fPzRX9nz4LgtkcQWVha8', {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const dA = await resA.json();
  const entriesA = Array.isArray(dA.entries) ? dA.entries : Object.values(dA.entries || {});

  console.log('=== ANALISI LA: NEW MOON (' + entriesL.length + ' voci) ===');
  // Group entries by topic
  const laCategories = {
    campus_life_and_academics: [],
    werebeast_and_shifter_biology: [],
    beastweres_and_reverse_shifters: [],
    powered_humans_and_magic: [],
    students_and_faculty_chars: [],
    forest_and_locations: [],
    other: []
  };

  entriesL.forEach((e, i) => {
    const text = (e.content || '') + ' ' + (Array.isArray(e.keys) ? e.keys.join(' ') : '');
    const firstLine = (e.content || '').split('\n')[0];
    if (firstLine.startsWith('Name: ') || text.includes('Student Profile') || text.includes('Faculty Profile')) {
      laCategories.students_and_faculty_chars.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('Beastwere') || text.includes('reverse shifter') || text.includes('Right of True Form')) {
      laCategories.beastweres_and_reverse_shifters.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('Werebeast') || text.includes('werewolf') || text.includes('pack resonance') || text.includes('lunar cycle')) {
      laCategories.werebeast_and_shifter_biology.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('Powered human') || text.includes('magic') || text.includes('ward') || text.includes('enchant')) {
      laCategories.powered_humans_and_magic.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('campus') || text.includes('curriculum') || text.includes('calendar') || text.includes('sanctuary') || text.includes('club') || text.includes('tradition')) {
      laCategories.campus_life_and_academics.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('Forest') || text.includes('Basin') || text.includes('Pineharbor') || text.includes('location')) {
      laCategories.forest_and_locations.push({ idx: i, keys: e.keys, title: firstLine });
    } else {
      laCategories.other.push({ idx: i, keys: e.keys, title: firstLine });
    }
  });

  for (const [k, v] of Object.entries(laCategories)) {
    console.log(`- ${k}: ${v.length} voci`);
  }

  console.log('\n=== ANALISI AEGIS CITY HUNTERS (' + entriesA.length + ' voci) ===');
  const aegisCategories = {
    hunter_ranks_and_gear: [],
    monsters_and_threats: [],
    organizations_and_factions: [],
    individual_hunters_and_npcs: [],
    city_and_locations: [],
    other: []
  };

  entriesA.forEach((e, i) => {
    const text = (e.content || '') + ' ' + (Array.isArray(e.keys) ? e.keys.join(' ') : '');
    const firstLine = (e.content || '').split('\n')[0];
    if (firstLine.includes('is a ') && (firstLine.includes('woman') || firstLine.includes('man') || firstLine.includes('Hunter') || firstLine.includes('detective') || firstLine.includes('leader'))) {
      aegisCategories.individual_hunters_and_npcs.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('Messor') || text.includes('monster') || text.includes('Book of Monsters') || text.includes('threat')) {
      aegisCategories.monsters_and_threats.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('Hunter') || text.includes('weapon') || text.includes('Mana Field') || text.includes('gear') || text.includes('ballistics')) {
      aegisCategories.hunter_ranks_and_gear.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('Society') || text.includes('Division') || text.includes('Agency') || text.includes('Cult')) {
      aegisCategories.organizations_and_factions.push({ idx: i, keys: e.keys, title: firstLine });
    } else if (text.includes('City') || text.includes('Forest') || text.includes('Shrine') || text.includes('Mansion') || text.includes('District')) {
      aegisCategories.city_and_locations.push({ idx: i, keys: e.keys, title: firstLine });
    } else {
      aegisCategories.other.push({ idx: i, keys: e.keys, title: firstLine });
    }
  });

  for (const [k, v] of Object.entries(aegisCategories)) {
    console.log(`- ${k}: ${v.length} voci`);
  }
}

analyzeLorebooks();
