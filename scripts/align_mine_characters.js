const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const updates = [
    {
      id: '_t4J9aQNJM36cUKAP4wB4U',
      newName: 'Jasper Svartr Douglas Bloodmoon',
      updateHeader: (oldLine) => {
        return '[NAME: Jasper Svartr Douglas Bloodmoon; FIRST_NAME: Jasper; MIDDLE_NAME: Svartr (Wolf Name, Presentation at 13); LAST_NAME: Douglas Bloodmoon; ALIASES: DJ Frequency, Jas, Twin, Bro, DJ F, "The Ghost"; AGE: 19 (Born April 22, 2005); GENDER: Male (He/Him); BIRTHDAY: April 22; ZODIAC: Taurus Sun, Gemini Ascendant, Libra Moon; SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Beta; HOUSE: Douglas and Bloodmoon; PACK: Seven Hills; BIRTH_RUNE: Gebo (5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink, Twin Bond); SOCIAL_STATUS: Citizen, Black-Market Info-Broker, Guild Infiltrator, Outlaw; OCCUPATION: 1st-year undergrad (SUCC) Acoustic and Sound Engineering, Underground DJ, Arcane-Rogue and Spell-Hacker in the Guild, Caretaker and Left Hand designate to Malachia; HEIGHT: 193cm (6\'4"); BUILD: Lean, acrobatic, slouched gamer build; HAIR: Messy caramel-chestnut hair falling into eyes; EYES: Mint-green illuminated by screen glare; FEATURES: Perpetual knowing ironic smirk, lazy caramel wolf ears that flick when amused, Gebo birth-rune protection tattoo on left wrist, Moon Aegis blessing in white ink on collarbone, arcane neural plug at base of neck, silver ring piercings on both nipples; HYBRID_FORM: 223cm (7\'4") agile speed hybrid; FULL_SHIFT: Svartr, agile caramel-and-shadow wolf; SCENT: Fresh rain, ice, silver, artificial energy drinks, ozone, worn leather, spiced rum]';
      }
    },
    {
      id: '_yQeae3DnARft2RH4gaFNx',
      newName: 'Malachia Björn Douglas Bloodmoon',
      updateHeader: (oldLine) => {
        if (oldLine.includes('FIRST_NAME: Malachia')) return oldLine;
        return oldLine.replace('[NAME: Malachia Douglas-Bloodmoon;', '[NAME: Malachia Björn Douglas Bloodmoon; FIRST_NAME: Malachia; MIDDLE_NAME: Björn (Wolf Name, Presentation at 12); LAST_NAME: Douglas Bloodmoon; BIRTH_RUNE: Thurisaz (Brute Force & Defense, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
    },
    {
      id: '_AjphrWj2BMT9KJTx4KETE',
      newName: 'Noah Loki Douglas Bloodmoon',
      updateHeader: (oldLine) => {
        if (oldLine.includes('FIRST_NAME: Noah')) return oldLine;
        return oldLine.replace('[NAME: Noah Douglas-Bloodmoon;', '[NAME: Noah Loki Douglas Bloodmoon; FIRST_NAME: Noah; MIDDLE_NAME: Loki (Wolf Name, Presentation at 13); LAST_NAME: Douglas Bloodmoon; BIRTH_RUNE: Kenaz (Torch of Strategic Intellect & Diplomacy, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
    },
    {
      id: '_EWqmxx3Q1fdK97AVBRqEW',
      newName: 'Erik Ulfr Douglas',
      updateHeader: (oldLine) => {
        if (oldLine.includes('FIRST_NAME: Erik')) return oldLine;
        return oldLine.replace('[NAME: Erik Douglas;', '[NAME: Erik Ulfr Douglas; FIRST_NAME: Erik; MIDDLE_NAME: Cornelius (Civil), Ulfr (Wolf Name, Presentation at 13); LAST_NAME: Douglas; BIRTH_RUNE: Tiwaz (Rightful Military Command & Alpha Authority, 5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink);');
      }
    }
  ];

  console.log('=== UPDATING STANDALONE CARDS IN /mine ===');
  for (const item of updates) {
    const resGet = await fetch(`https://app.wyvern.chat/api/characters/${item.id}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (!resGet.ok) {
      console.error(`Failed to GET ${item.id}:`, resGet.status);
      continue;
    }
    const card = await resGet.json();
    const lines = (card.description || '').split('\n');
    lines[0] = item.updateHeader(lines[0]);
    const updatedDesc = lines.join('\n');

    const payload = {
      name: item.newName,
      description: updatedDesc
    };

    const resPut = await fetch(`https://app.wyvern.chat/api/characters/${item.id}`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify(payload)
    });
    console.log(`Card [${item.newName}] (${item.id}) PUT status:`, resPut.status);
  }

  console.log('\n=== VERIFICATION GET ===');
  for (const item of updates) {
    const v = await (await fetch(`https://app.wyvern.chat/api/characters/${item.id}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
    console.log(`Verified /mine Card: ${v.name}`);
    console.log(` -> Header: ${v.description.split('\n')[0].slice(0, 100)}...`);
  }
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
