const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const npcLbId = '_LBkRWNpPxpdn6dxYaDU2b';

  console.log('=== STEP 4: DEPLOY DOUGLAS/BLOODMOON FAMILY WOLF NAMES & BIRTH-RUNES ===');

  const familyUpdates = [
    {
      id: '_x3VY2kcbaDbKyCqywGeET', // Jasper
      lbMatchName: 'Jasper Douglas Bloodmoon',
      newDisplayName: 'Jasper Svartr Douglas Bloodmoon',
      first_name: 'Jasper',
      middle_names: ['Svartr'],
      last_name: 'Douglas Bloodmoon',
      newLbKeys: ['Jasper', 'Svartr', 'Jasper Svartr', 'twin', 'brother', 'DJ Frequency'],
      updateHeader: (oldLine) => {
        return '[NAME: Jasper Svartr Douglas Bloodmoon; FIRST_NAME: Jasper; MIDDLE_NAME: Svartr (Wolf Name, Presentation at 13); LAST_NAME: Douglas Bloodmoon; ALIASES: DJ Frequency, Jas, Twin, Bro, DJ F, "The Ghost"; AGE: 19 (Born April 22, 2005); GENDER: Male (He/Him); BIRTHDAY: April 22; ZODIAC: Taurus Sun, Gemini Ascendant, Libra Moon; SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Beta; HOUSE: Douglas and Bloodmoon; PACK: Seven Hills; BIRTH_RUNE: Gebo (5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink, Twin Bond); SOCIAL_STATUS: Citizen, Black-Market Info-Broker, Guild Infiltrator, Outlaw; OCCUPATION: 1st-year undergrad (SUCC) Acoustic and Sound Engineering, Underground DJ, Arcane-Rogue and Spell-Hacker in the Guild, Caretaker and Left Hand designate to Malachia; HEIGHT: 193cm (6\'4"); BUILD: Lean, acrobatic, slouched gamer build; HAIR: Messy caramel-chestnut hair falling into eyes; EYES: Mint-green illuminated by screen glare; FEATURES: Perpetual knowing ironic smirk, lazy caramel wolf ears that flick when amused, Gebo birth-rune protection tattoo on left wrist, Moon Aegis blessing in white ink on collarbone, arcane neural plug at base of neck, silver ring piercings on both nipples; HYBRID_FORM: 223cm (7\'4") agile speed hybrid; FULL_SHIFT: Svartr, agile caramel-and-shadow wolf; SCENT: Fresh rain, ice, silver, artificial energy drinks, ozone, worn leather, spiced rum]';
      }
    },
    {
      id: '_rAcN9GXD1Le4WxY28e49W', // Malachia
      lbMatchName: 'Malachia Douglas Bloodmoon',
      newDisplayName: 'Malachia Björn Douglas Bloodmoon',
      first_name: 'Malachia',
      middle_names: ['Björn'],
      last_name: 'Douglas Bloodmoon',
      newLbKeys: ['Malachia', 'Björn', 'Malachia Björn', 'Mal', 'The King'],
      updateHeader: (oldLine) => {
        if (oldLine.includes('FIRST_NAME: Malachia')) return oldLine;
        return oldLine.replace('[NAME: Malachia Douglas-Bloodmoon;', '[NAME: Malachia Björn Douglas Bloodmoon; FIRST_NAME: Malachia; MIDDLE_NAME: Björn (Wolf Name, Presentation at 12); LAST_NAME: Douglas Bloodmoon; BIRTH_RUNE: Thurisaz (Brute Force & Defense, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
    },
    {
      id: '_r42cVzMjcGTAx7bR1DQVt', // Noah
      lbMatchName: 'Noah Douglas Bloodmoon',
      newDisplayName: 'Noah Loki Douglas Bloodmoon',
      first_name: 'Noah',
      middle_names: ['Loki'],
      last_name: 'Douglas Bloodmoon',
      newLbKeys: ['Noah', 'Loki', 'Noah Loki', 'Blondie', 'brother'],
      updateHeader: (oldLine) => {
        if (oldLine.includes('FIRST_NAME: Noah')) return oldLine;
        return oldLine.replace('[NAME: Noah Douglas-Bloodmoon;', '[NAME: Noah Loki Douglas Bloodmoon; FIRST_NAME: Noah; MIDDLE_NAME: Loki (Wolf Name, Presentation at 13); LAST_NAME: Douglas Bloodmoon; BIRTH_RUNE: Kenaz (Torch of Strategic Intellect & Diplomacy, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
    },
    {
      id: '_d44gDc8N18kkbEhAcfUCG', // Erik
      lbMatchName: 'Erik Douglas',
      newDisplayName: 'Erik Ulfr Douglas',
      first_name: 'Erik',
      middle_names: ['Cornelius', 'Ulfr'],
      last_name: 'Douglas',
      newLbKeys: ['Erik', 'Ulfr', 'Erik Ulfr', 'Erik Douglas', 'Prime Alpha'],
      updateHeader: (oldLine) => {
        if (oldLine.includes('FIRST_NAME: Erik')) return oldLine;
        return oldLine.replace('[NAME: Erik Douglas;', '[NAME: Erik Ulfr Douglas; FIRST_NAME: Erik; MIDDLE_NAME: Cornelius (Civil), Ulfr (Wolf Name, Presentation at 13); LAST_NAME: Douglas; BIRTH_RUNE: Tiwaz (Rightful Military Command & Alpha Authority, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
    },
    {
      id: '_fmzBDjDn3Gnq2hXKy7tY6', // Nixara
      lbMatchName: 'Nixara Bloodmoon',
      newDisplayName: 'Nixara Hvit Bloodmoon',
      first_name: 'Nixara',
      middle_names: ['Hvit'],
      last_name: 'Bloodmoon',
      newLbKeys: ['Nixara', 'Hvit', 'Nixara Hvit', 'Wife', 'Mate', 'Whitemoon', 'White Moon'],
      updateHeader: (oldLine) => {
        if (oldLine.includes('FIRST_NAME: Nixara')) return oldLine;
        return oldLine.replace('[NAME: Nixara Bloodmoon;', '[NAME: Nixara Hvit Bloodmoon; FIRST_NAME: Nixara; MIDDLE_NAME: Hvit (Wolf Name, White Moon Sacred Tradition); LAST_NAME: Bloodmoon; BIRTH_RUNE: Perthro (Lunar Fate & Primordial Secret, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
    },
    {
      id: '_W9PLYt9ERTBJBXqKQL2en', // Wulfnic
      lbMatchName: 'Wulfnic Bloodmoon',
      newDisplayName: 'Wulfnic Báleygr Bloodmoon',
      first_name: 'Wulfnic',
      middle_names: [],
      last_name: 'Bloodmoon',
      newLbKeys: ['Wulfnic', 'Báleygr', 'grandfather', 'Firstborn', 'Alpha of Alphas'],
      updateHeader: (oldLine) => {
        if (oldLine.includes('FIRST_NAME: Wulfnic')) return oldLine;
        return oldLine.replace('[NAME: Wulfnic Bloodmoon (Báleygr);', '[NAME: Wulfnic Báleygr Bloodmoon; FIRST_NAME: Wulfnic; WOLF_NAME: Unified Firstblood Entity (Original Viking Name, Fenris-consecrated); LAST_NAME: Bloodmoon; BIRTH_RUNE: Othala (Ancestral Sovereign Lineage & Root Heritage, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
    }
  ];

  // 1. UPDATE WORLD CHARACTERS
  console.log('\n--- 1. UPDATING WORLD CHARACTERS ---');
  for (const item of familyUpdates) {
    const resGet = await fetch(`https://app.wyvern.chat/api/worlds/characters/${item.id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!resGet.ok) {
      console.error(`Failed to fetch World Character ${item.id}:`, resGet.status);
      continue;
    }
    const charData = await resGet.json();
    const lines = (charData.long_summary || '').split('\n');
    lines[0] = item.updateHeader(lines[0]);
    const updatedSummary = lines.join('\n');

    const payload = {
      display_name: item.newDisplayName,
      first_name: item.first_name,
      middle_names: item.middle_names,
      last_name: item.last_name,
      long_summary: updatedSummary
    };

    const resPut = await fetch(`https://app.wyvern.chat/api/worlds/characters/${item.id}`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    console.log(`World Char [${item.newDisplayName}] (${item.id}) PUT status:`, resPut.status);
  }

  // 2. UPDATE NPC PRIMARY LOREBOOK
  console.log('\n--- 2. UPDATING NPC PRIMARY LOREBOOK ---');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lbData = await resLb.json();
  fs.writeFileSync('scratch/pre_step4_npc_primary_backup.json', JSON.stringify(lbData, null, 2));

  const updatedLexicon = lbData.lexicon.map(entry => {
    const match = familyUpdates.find(u => u.lbMatchName === entry.name || (entry.name && entry.name.includes(u.first_name)));
    if (match) {
      console.log(`Updating NPC Primary entry for: ${entry.name} -> ${match.newDisplayName}`);
      const lines = (entry.content || '').split('\n');
      lines[0] = match.updateHeader(lines[0]);
      return {
        ...entry,
        name: match.newDisplayName,
        keys: match.newLbKeys,
        content: lines.join('\n')
      };
    }
    return entry;
  });

  const resPutLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify({ lexicon: updatedLexicon })
  });
  console.log('NPC Primary Lorebook PUT status:', resPutLb.status);

  // 3. VERIFICATION
  console.log('\n=== VERIFICATION GET ===');
  for (const item of familyUpdates) {
    const vC = await (await fetch(`https://app.wyvern.chat/api/worlds/characters/${item.id}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
    console.log(`Verified World Char: ${vC.display_name} | first: ${vC.first_name} | middle: ${JSON.stringify(vC.middle_names)} | last: ${vC.last_name}`);
    console.log(` -> Header: ${vC.long_summary.split('\n')[0].slice(0, 100)}...`);
  }

  const vLb = await (await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  console.log(`\nVerified NPC Primary entries count: ${vLb.lexicon?.length}`);
  familyUpdates.forEach(u => {
    const e = vLb.lexicon?.find(entry => entry.name === u.newDisplayName);
    console.log(` - NPC Primary: ${e?.name} (Found: ${!!e}) | Keys: ${JSON.stringify(e?.keys)}`);
  });
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
