const fs = require('fs');
const path = require('path');

// 1. FACTIONS MAP (IDs from Lexicon type 'faction')
const FACTIONS = {
  ASTRA: '_21gByQrKjPmWCd2jh3y83',
  ACES: '_GaQ8B1wLA7NCM1zP8JW6q',
  OTHER_CONTRACTORS: '_7H2Ve9Y7f33rTxNN9Ep91',
  KELPIES: '_xB6wzXC39XpCgVmD89Y2h',
  THOMPSON: '_J6c9agBEXD2Pg4YHU6Gy3',
  DMHA: '_P1emQkeq2yE3DPpHyajKp',
  HORNED_SKULL: '_khhNdHFj4KnzEdwHYrTja',
  IRONHORN: '_eVzj3Ve4fxDCXyAmc9qXD',
  MF_INC: '_6RWCeX3jQPxpn8yAVWTB9',
  COCKETEERS: '_3t3WYTw2e4bPEtLtKe74G',
  SRF: '_C6JqdNxNgtqeneW1DxbrK',
  COUNCIL_CAUSE: '_bnxdrfAqyM3QwqMpwDjCj',
  SERAPHIM: '_ddw3Et6V743dYqh7H6nNy',
  DCC: '_K4bmN3tGC8ExmTgLYRD4z',
  DDM_INC: '_QNJdCq9fYQ46mRPdNhcVq',
  DDM_DEPTS: '_wM3nMKMeHAb2Fd46KyP72',
  BLOODHOUND: '_rfj12HwP3pMq2NTkJdVPw',
  BALLANTINE: '_X2qqf3HhhdMahnhFUW3j7',
  SINNERS: '_4AWPQQahw4hQVrkPVAJwY',
  BULLS: '_HPQnf2PEMBKYVdYDBLejW',
  BEARS: '_4QX9aHTxU71gaHHWk7M4W',
  HUMANS_FIRST: '_GjTyz8HeLXxhmNzaqqE48',
  GRAVE_MISTAKE: '_9c77BBEh4e8wCrMtUwpXt'
};

function resolveFaction(c) {
  const name = c.display_name.toLowerCase();
  const text = ((c.long_summary || '') + ' ' + (c.summary || '')).toLowerCase();
  
  if (name.includes('douglas') || name.includes('bloodmoon') || text.includes('house douglas') || text.includes('branco douglas')) return FACTIONS.DCC;
  if (name.includes('darkfire') || text.includes('horned skull') || text.includes('hsk')) return FACTIONS.HORNED_SKULL;
  if (name.includes('thompson')) return FACTIONS.THOMPSON;
  if (name.includes('ballantine') || text.includes('ballantine')) return FACTIONS.BALLANTINE;
  if (name.includes('danny boone') || name.includes('sully')) return FACTIONS.BALLANTINE;
  if (name.includes('sanchez-rogers') || name.includes('viola carter') || name.includes('roland vickers') || text.includes('grave mistake')) return FACTIONS.GRAVE_MISTAKE;
  if (name.includes('virtuoso') || name.includes('zero') || text.includes('the sinners') || text.includes('sinners')) return FACTIONS.SINNERS;
  if (name.includes('dullahan') || text.includes('ddm inc') || text.includes('contractor')) return FACTIONS.DDM_INC;
  if (name.includes('kaladin') || text.includes('bloodhound') || text.includes('dcc security')) return FACTIONS.DCC;
  if (name.includes('bryson') || text.includes('mf inc')) return FACTIONS.MF_INC;
  if (name.includes('vincent campbell') || text.includes('succ bears') || text.includes('bears')) return FACTIONS.BEARS;
  if (name.includes('tomas matthews') || text.includes('humans first')) return FACTIONS.HUMANS_FIRST;
  if (name.includes('marek') || text.includes('ironhorn nomads')) return FACTIONS.IRONHORN;
  if (name.includes('eithne') || text.includes('obsidian blades')) return FACTIONS.SINNERS;
  if (name.includes('santiago herrera') || text.includes('succ bulls') || text.includes('bulls')) return FACTIONS.BULLS;
  if (text.includes('dmha') || text.includes('guild vanguard') || text.includes('guild tank') || text.includes('guild support')) return FACTIONS.DMHA;
  if (text.includes('srf') || text.includes('supernatural reserve')) return FACTIONS.SRF;
  if (text.includes('council')) return FACTIONS.COUNCIL_CAUSE;
  if (text.includes('succ')) return FACTIONS.BULLS;
  return FACTIONS.DCC;
}

// 2. LEVEL CALCULATION FORMULA (13: Lv1, 14-18: Lv2, 19: Lv3, +1 every 5 yrs)
const fallbackAges = {
  'Jet Thompson': 14,
  'Dominic Rogers': 48,
  'Roman Blackwood': 23,
  'Eric': 21,
  'Javier Reyes': 22,
  'Raymond': 22,
  'Dean': 22,
  'Bryson': 28,
  'Scarlett Rose': 21,
  'Sierra': 21,
  'Varg Darkfire': 58,
  'Karshin Darkfire': 45,
  'Boros Darkfire': 42,
  'Aras Darkfire': 39,
  'Kolya Varenkov': 26,
  'Russ Sinclair': 19,
  'Abel Vilas': 30
};

function getAge(c) {
  const cleanName = c.display_name.trim();
  if (fallbackAges[cleanName]) return fallbackAges[cleanName];
  let bd = c.birthdate;
  if (bd !== undefined && bd !== null) {
    let age = Math.floor((10486470 - bd) / (24 * 365.25));
    return Math.max(1, age);
  }
  const text = (c.long_summary || '') + ' ' + (c.summary || '');
  const m = text.match(/AGE:\s*([0-9]{1,4})/i);
  if (m) return parseInt(m[1]);
  return 25;
}

function calculateNewLevel(age) {
  if (age <= 13) return 1;
  const lvl = 2 + Math.floor((age - 14) / 5);
  return Math.max(1, Math.min(99, lvl));
}

// 3. HOME LOCATIONS FOR THE 20 UNASSIGNED
const missingHomeAssignments = {
  '_eVGFKNJmJX8Cw7rc2D81A': '_UeKEhHTnCP6yQk7mhMVU1', // Jet Thompson -> Coastal Residential
  '_cUjgkJRebCRGKjTj23aNR': '_CAhgArEXA2eBDQPpPe1gE', // Dominic Rogers -> Rogers' Bargain Motors
  '_DknhDnJqKdaTGUkf8ANHz': '_gpBY7HGddd4KHfqaDyy3c', // Roman Blackwood -> The Underground Fighting Ring
  '_a3hxDtxP7XHDy78FGAnej': '_wEkzHgpxfetQr16bTWNUP', // Eric -> Apollo Dorms
  '_tCT6W9WtrWGfycdUKYt4C': '_wEkzHgpxfetQr16bTWNUP', // Javier Reyes -> Apollo Dorms
  '_9Upm7RQLy1TtqrtENTEYn': '_p1JatqFwBPeKPQrh6CmGe', // Raymond -> Beta Rho Omega
  '_9nK87nkhNKmJbmD972D9X': '_wEkzHgpxfetQr16bTWNUP', // Dean -> Apollo Dorms
  '_K19J76QhMPMQAKXtk4pUm': '_VzByV4y4PKCw7N7hJyDkV', // Bryson -> Bulls Football Field
  '_GFmTXgcz2X12wGByRrNqY': '_Ep6xM191zpn6jpUygJakP', // Scarlett Rose -> Theta Iota Theta
  '_mCw4f7E4Q3NCFPG2gNBhB': '_Ep6xM191zpn6jpUygJakP', // Sierra -> Theta Iota Theta
  '_7EEzdyFQ7LFYUaV7DwVW1': '_RVRf9PtEdwhGt3rGGFjMC', // Varg Darkfire -> The Cable District
  '_zW44m7rAwPfRGEEFHm161': '_RVRf9PtEdwhGt3rGGFjMC', // Karshin Darkfire -> The Cable District
  '_N9mRBWXGfaz8Ldw6GaRPq': '_RVRf9PtEdwhGt3rGGFjMC', // Boros Darkfire -> The Cable District
  '_w7m1edfM4zyTALpxnXL41': '_RVRf9PtEdwhGt3rGGFjMC', // Aras Darkfire -> The Cable District
  '_Y4LfnqyPLmfYxmyC4e8Vh': '_6KT7hL8LMFzU3dK6h1wax', // Kolya Varenkov -> Wyrm Dormitories
  '_crx1UKHULm7WNwtDrnBCQ': '_3tNeXcGBfcUX6J1mtjqAw', // Russ Sinclair -> Claws Steel & Ink
  '_FDmwhyCQBcgzWqWjADD3g': '_TLEaxwQCB24kQYfYHy8pq', // Danny Boone -> Rory's Estate
  '_hkbBHVM27mhpXEbMGNM8J': '_Gnm9WMQNjhUWJLhrkpqQk', // Marlowe Voss -> Oldtown
  '_xb7wEMFXBKrWQwCkpkkKK': '_k118p3PTLgG88pkXn48BQ', // Cassian Aralas -> Hex Valley
  '_Tjyn1rghFtf9F9Y91CMx6': '_MkkwDR7AHq4tYLmnk134f'  // Harrison Black -> Bluemoon
};

// 4. JARED & MAC OUTFITS RAW DUMP DATA
const rawCharacters = JSON.parse(fs.readFileSync('ARCHIVIO/05_Snapshots_and_Extractions/raw_db_dumps/raw_characters.json', 'utf8'));
const rawMac = rawCharacters.find(c => (c.display_name || c.name || '').includes('Mackenzie'));
const rawJared = rawCharacters.find(c => (c.display_name || c.name || '').includes('Jared'));

async function applyAllUpdates() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0' };
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  // Fetch all characters
  const res = await fetch(`https://app.wyvern.chat/api/worlds/characters/world/${worldId}`, { headers });
  const chars = await res.json();
  console.log(`Starting global update on ${chars.length} characters in batches of 20...`);

  const batchSize = 20;
  let successCount = 0;

  for (let i = 0; i < chars.length; i += batchSize) {
    const batch = chars.slice(i, i + batchSize);
    const batchNum = Math.floor(i / batchSize) + 1;
    const totalBatches = Math.ceil(chars.length / batchSize);
    console.log(`\n=== BATCH ${batchNum}/${totalBatches} (${batch.length} characters) ===`);

    for (const c of batch) {
      const cid = c.id;
      const name = c.display_name;
      const cUrl = `https://app.wyvern.chat/api/worlds/characters/${cid}`;

      // 1. Fetch detailed character to inspect outfits and existing fields
      const detailRes = await fetch(cUrl, { headers });
      const detail = await detailRes.json();

      const patch = {};

      // A. FACTION
      const targetFaction = resolveFaction(c);
      patch.faction_id = targetFaction;

      // B. LEVEL
      const age = getAge(c);
      const newLvl = calculateNewLevel(age);
      patch.level = newLvl;
      if (detail.rpg_stats) {
        patch.rpg_stats = {
          ...detail.rpg_stats,
          level: newLvl
        };
      }

      // C. HOME LOCATION (if missing)
      if (!detail.home_location_id) {
        if (missingHomeAssignments[cid]) {
          patch.home_location_id = missingHomeAssignments[cid];
        }
      }

      // D. APPEARANCES & OUTFITS REFACTOR
      const currentOutfits = detail.outfits || [];
      const isWerewolf = ((c.long_summary || '') + ' ' + (c.summary || '')).toLowerCase().includes('werewolf');
      
      let shiftFull = currentOutfits.find(o => o.name.toLowerCase().includes('full shift') || o.name.toLowerCase().includes('fullshift'));
      let shiftHybrid = currentOutfits.find(o => o.name.toLowerCase().includes('hybrid shift') || o.name.toLowerCase().includes('hybrid'));

      if (isWerewolf || shiftFull || shiftHybrid) {
        // Create / populate appearances
        const appearancesList = [];

        // Base
        appearancesList.push({
          id: 'app-base',
          name: 'Base',
          description: `Forma umanoide base di ${name}. Bipede, fisionomia naturale con singoli tratti lupini parziali (orecchie lupine singole e coda) secondo la genetica Douglas/Svartulfr.`
        });

        // Hybrid Shift
        const hybridDesc = (shiftHybrid && shiftHybrid.description && shiftHybrid.description.trim())
          ? shiftHybrid.description
          : `Forma ibrida bipede colossale da combattimento di ${name}. Muscolatura ipertrofica, pelliccia densa, artigli ricurvi affilati da lacerazione, fauci allungate e orecchie lupine singole erette ed attente.`;
        appearancesList.push({
          id: 'app-hybrid-shift',
          name: 'Hybrid Shift',
          description: hybridDesc
        });

        // Full Shift
        const fullDesc = (shiftFull && shiftFull.description && shiftFull.description.trim())
          ? shiftFull.description
          : `Forma quadrupede completa da lupo gigante da caccia/assalto di ${name}. Mantello folto e compatto, torace possente da predatore d'apice, zampe poderose con cuscinetti plantari callosi e mandibole micidiali.`;
        appearancesList.push({
          id: 'app-full-shift',
          name: 'Full Shift',
          description: fullDesc
        });

        patch.appearances = appearancesList;

        // Clean outfits (remove Full Shift and Hybrid Shift)
        let cleanedOutfits = currentOutfits.filter(o => 
          !o.name.toLowerCase().includes('full shift') && 
          !o.name.toLowerCase().includes('fullshift') && 
          !o.name.toLowerCase().includes('hybrid')
        );

        // Special fix for Mac: restore descriptions from raw dump if empty
        if (cid === '_YY8VbpgzYk4dfFAL78rM3' && rawMac && rawMac.outfits) {
          cleanedOutfits = rawMac.outfits
            .filter(o => !o.name.toLowerCase().includes('shift'))
            .map(o => ({ id: o.id, name: o.name, description: o.description, avatar: o.avatar || '' }));
        }

        // Special fix for Jared: restore descriptions from raw dump if empty
        if (cid === '_BzKwAkgpPfbVkBzbDaEth' && rawJared && rawJared.outfits) {
          cleanedOutfits = rawJared.outfits
            .map(o => ({ id: o.id, name: o.name, description: o.description, avatar: o.avatar || '' }));
        }

        patch.outfits = cleanedOutfits;
      } else {
        // Not a werewolf: still fix Jared if needed
        if (cid === '_BzKwAkgpPfbVkBzbDaEth' && rawJared && rawJared.outfits) {
          patch.outfits = rawJared.outfits.map(o => ({ id: o.id, name: o.name, description: o.description, avatar: o.avatar || '' }));
        }
      }

      // SEND PUT
      try {
        const putRes = await fetch(cUrl, {
          method: 'PUT',
          headers: { ...headers, 'Content-Type': 'application/json' },
          body: JSON.stringify(patch)
        });

        if (putRes.ok) {
          successCount++;
          console.log(`  [OK] ${name.padEnd(28)} | Lv ${String(newLvl).padStart(2)} (Age ${age}) | Faction: OK | Home: ${patch.home_location_id ? 'SET' : 'EXISTING'} | App: ${patch.appearances ? patch.appearances.length : 0}`);
        } else {
          console.error(`  [FAIL ${putRes.status}] ${name}: ${await putRes.text()}`);
        }
      } catch (err) {
        console.error(`  [ERR] ${name}: ${err.message}`);
      }

      await new Promise(r => setTimeout(r, 150));
    }
  }

  console.log(`\n=== COMPLETED! Successfully updated ${successCount} / ${chars.length} characters ===`);
}

applyAllUpdates().catch(console.error);
