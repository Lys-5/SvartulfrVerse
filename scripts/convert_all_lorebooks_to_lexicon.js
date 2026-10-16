const fs = require('fs');
const path = require('path');

function determineLexiconType(entry, lbKey) {
  if (lbKey === 'location') return 'location';
  if (lbKey === 'npc_primary' || lbKey === 'npc_secondary') return 'npc';

  const current = (entry.type || '').trim();
  if (['location', 'npc', 'item', 'creature', 'ability', 'job'].includes(current)) {
    return current;
  }
  
  const name = (entry.name || '').trim();
  const nLow = name.toLowerCase();

  // Explicit Location overrides
  if (nLow.includes('cavern') || (nLow.includes('dungeon') && !nLow.includes('mode') && !nLow.includes('cycle') && !nLow.includes('core') && !nLow.includes('hazard')) || nLow.includes('earth-121789') || nLow.includes('the tear beneath the yew') || nLow.includes('dressing suites') || nLow.includes('vip zone') || nLow.includes('reality tear') || nLow.includes('dungeon gates')) {
    return 'location';
  }
  // Explicit Item overrides
  if (nLow.includes('cock almanac') || nLow.includes('golden cock') || nLow.includes('concierge (app)') || nLow.includes('ceremonial attire') || nLow.includes('potions and alchemical') || nLow.includes('dungeon core') || nLow.includes('abyssal dawn collection') || nLow.includes('ambrosia')) {
    return 'item';
  }
  // Explicit NPC overrides
  if (nLow.includes('nurse ariadne')) {
    return 'npc';
  }
  // Explicit Ability overrides
  if (nLow.includes('absolute pacifist vow') || nLow.includes('shielding maneuver')) {
    return 'ability';
  }
  // Explicit Memory / Intimate Profile / Chat Log overrides
  if (nLow.includes('coping mechanism') || nLow.includes('group chat') || nLow.includes('digital interaction') || nLow.includes('viaggio di wulfnic') || nLow.includes('luisa sanchez-rogers') || nLow.includes('twin bond') || (nLow.includes('pheromones') && (nLow.includes('satyr') || nLow.includes('orc'))) || nLow.includes('reproduction and') || nLow.includes('longhouse: doni') || nLow.includes('origine vera dei nove') || current === 'memory') {
    return 'memory';
  }
  // Explicit Event overrides
  if (nLow.includes('guerra di fenris') || nLow.includes('sacred calendar') || nLow.includes('history:') || nLow.includes('history timeline') || nLow.includes('master calendar') || nLow.includes('night mode') || nLow.includes('ciclo notturno') || nLow.includes('compie 21 anni') || nLow.includes('fondazione della succ') || nLow.includes('manifestation') || nLow.includes('celebration') || (nLow.includes('grande caccia') && !nLow.includes('rules')) || nLow.includes('future era') || nLow.includes('the broken altar') || nLow.includes('dormancy') || current === 'event') {
    return 'event';
  }
  // Explicit Faction overrides
  if (nLow.includes('genealogies summary') || (nLow.includes('family') && !nLow.includes('lse')) || nLow.includes('astra industries') || nLow.includes('the aces') || nLow.includes('other contractors') || nLow.includes('kelpies') || nLow.includes('clan') || nLow.includes('nomads mc') || nLow.includes('mf inc') || nLow.includes('cocketeers') || nLow.includes('reserve forces') || nLow.includes('the cause') || nLow.includes('the council') || nLow.includes('seraphim') || nLow.includes('coalition') || nLow.includes('ddm inc') || nLow.includes('pmc') || nLow.includes('council & treaties') || nLow.includes('religious institutions') || nLow.includes('frats & sororities') || nLow.includes('campus & teams') || nLow.includes('rivalry with cums') || nLow.includes('sports @ succ') || nLow.includes('contatti esterni') || nLow.includes('underworld') || current === 'faction') {
    return 'faction';
  }

  return 'concept';
}

async function convertAndDeployLorebooks() {
  const token = fs.readFileSync('scratch/wyvern_token.txt', 'utf8').trim();

  const lorebooks = [
    { key: 'lb1', file: 'FINAL/Svartulfr_Lorebook_I.json', id: '_gwwCxCfQ6PQaLEjAQVpJL', name: 'Svartúlfr - Lorebook I' },
    { key: 'lb2', file: 'FINAL/Svartulfr_Lorebook_II.json', id: '_HfG7TeV6MJyj6bxMwxkpt', name: 'Svartúlfr - Lorebook II' },
    { key: 'lb3', file: 'FINAL/Svartulfr_Lorebook_III.json', id: '_9zWTGqYJNJ4BCDMj8gfcD', name: 'Svartúlfr - Lorebook III' },
    { key: 'location', file: 'FINAL/Svartulfr_Location.json', id: '_EjXxkmPVhpCXg8xABpFkK', name: 'Svartúlfr - Location' },
    { key: 'npc_primary', file: 'FINAL/Svartulfr_NPC_Primary.json', id: '_zwEqgEEzh12X6gHVmMKKC', name: 'Svartúlfr - NPC Primary' },
    { key: 'npc_secondary', file: 'FINAL/Svartulfr_NPC_Secondary.json', id: '_Uht3Ckz44JBDrPnUHq7LV', name: 'Svartúlfr - NPC Secondary' }
  ];

  console.log('=== CONVERTING ALL 6 LOREBOOKS TO WYVERN ADVANCED LEXICON ===\n');

  for (const lb of lorebooks) {
    console.log(`Processing ${lb.name} (${lb.file})...`);
    const rawData = JSON.parse(fs.readFileSync(lb.file, 'utf8'));
    const sourceEntries = rawData.entries || rawData.lexicon || [];

    const typeCounts = {};
    const converted = sourceEntries.map((e, idx) => {
      const standardType = determineLexiconType(e, lb.key);
      typeCounts[standardType] = (typeCounts[standardType] || 0) + 1;

      return {
        entry_id: e.entry_id || `${lb.key}_${idx}`,
        keys: e.keys || [],
        secondary_keys: e.secondary_keys || [],
        regex_patterns: e.regex_patterns || [],
        content: e.content || '',
        extensions: e.extensions || {},
        enabled: e.enabled !== false,
        case_sensitive: e.case_sensitive || false,
        insertion_order: e.insertion_order || 10,
        name: e.name || (e.keys && e.keys[0]) || `Entry ${idx}`,
        priority: typeof e.priority === 'number' ? e.priority : 10,
        comment: e.comment || '',
        constant: e.constant || false,
        position: e.position || 'before_char',
        scan_persona: e.scan_persona || false,
        whole_words_only: e.whole_words_only !== false,
        key_logic: e.key_logic || 'AND_ANY',
        delay: e.delay || 0,
        sticky: e.sticky || 0,
        cooldown: e.cooldown || 0,
        activation_chance: typeof e.activation_chance === 'number' ? e.activation_chance : 100,
        labels: e.labels || [],
        custom_fields: e.custom_fields || {},
        related_entries: e.related_entries || [],
        avatar: e.avatar || '',
        avatar_activation_regex: e.avatar_activation_regex || '',
        type: standardType,
        callback: e.callback || '',
        provenance: e.provenance || {
          source: { kind: 'lorebook', container_id: lb.id, entry_id: e.entry_id || `${lb.key}_${idx}` },
          captured_at: new Date().toISOString()
        }
      };
    });

    // Update local JSON file
    rawData.entries = converted;
    rawData.lexicon = converted;
    fs.writeFileSync(lb.file, JSON.stringify(rawData, null, 2), 'utf8');
    console.log(`  Local file updated: ${converted.length} entries & ${converted.length} lexicon.`);
    console.log(`  Typology Breakdown:`, JSON.stringify(typeCounts));

    // Deploy to Wyvern via PUT
    console.log(`  Deploying to Wyvern API (${lb.id})...`);
    const putRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
      },
      body: JSON.stringify({
        entries: converted,
        lexicon: converted
      })
    });

    console.log(`  PUT Status: HTTP ${putRes.status}`);
    if (!putRes.ok) {
      const errText = await putRes.text();
      console.error(`  [ERROR]:`, errText.slice(0, 300));
    } else {
      // Verification GET
      const verifyRes = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
        headers: { 'Authorization': `Bearer ${token}`, 'User-Agent': 'Mozilla/5.0' }
      });
      const v = await verifyRes.json();
      console.log(`  Verified on Wyvern: entries=${v.entries ? v.entries.length : 0}, lexicon=${v.lexicon ? v.lexicon.length : 0}`);
    }
    console.log('------------------------------------------------------------\n');
  }

  console.log('=== ALL 6 LOREBOOKS SUCCESSFULLY CONVERTED & SYNCED ===');
}

convertAndDeployLorebooks().catch(console.error);
