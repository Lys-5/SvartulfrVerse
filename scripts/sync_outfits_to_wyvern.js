const fs = require('fs');
const path = require('path');
const crypto = require('crypto');

function generateNanoid() {
  const chars = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_-';
  const bytes = crypto.randomBytes(21);
  let res = '';
  for (let i = 0; i < 21; i++) {
    res += chars[bytes[i] % chars.length];
  }
  return res;
}

const charMap = [
  { id: '_QPea6g4Q1QfeYCVHCLMPR', file: 'FINAL/Erik_Douglas_card.json', name: 'Erik Ulfr Douglas' },
  { id: '_RDfz7XzTpM23LpPALVXHM', file: 'FINAL/Malachia_Douglas_Bloodmoon_card.json', name: 'Malachia Björn Douglas Bloodmoon' },
  { id: '_zFLUjV8aVxQRAfQxGcAcY', file: 'FINAL/Noah_Douglas_Bloodmoon_card.json', name: 'Noah Loki Douglas Bloodmoon' },
  { id: '_T8Ywcr9FEqNf9JxbK6eHP', file: 'FINAL/Logan_Douglas_card.json', name: 'Logan Járn Douglas' },
  { id: '_TbRM3EdxDjHFgqztTbCpL', file: 'FINAL/Edric_Douglas_card.json', name: 'Edric Douglas' },
  { id: '_zBD6rWUkJBAjLfXnja4xh', file: 'FINAL/Elizabeth_Duskwood_card.json', name: 'Elizabeth Duskwood' },
  { id: '_xJVPtBLL3dxy69RLKL9X9', file: 'FINAL/Jared_Thompson_card.json', name: 'Jared Thompson' },
  { id: '_EnRGd1jfbjTTGmz4EFJdd', file: 'FINAL/Kaladin_Nargathon_card.json', name: 'Major Kaladin Blackwolf Nargathon' },
  { id: '_zn24784jfcchQ7EwCyAnm', file: 'FINAL/Mackenzie_Sanchez_Rogers_card.json', name: 'Mackenzie Sanchez-Rogers' },
  { id: '_dJ7nRMQEbcUgdWG96MqLz', file: 'FINAL/Magnus_Douglas_III_card.json', name: 'Magnus Douglas III' },
  { id: '_HEQQbbRFwKdG8QE2Fh1z1', file: 'FINAL/Wulfnic_Bloodmoon_card.json', name: 'Wulfnic Báleygr Bloodmoon' },
  { id: '_3tMk6cRAFewRnKMkdJ4XU', file: 'FINAL/Zeera_Darkfire_card.json', name: 'Zeera Darkfire' }
];

async function syncOutfits() {
  const token = fs.readFileSync('scratch/wyvern_token.txt', 'utf8').trim();
  console.log('=== ASSIGNING OUTFIT IDS & SYNCING TO WYVERN ===\n');

  for (const item of charMap) {
    const data = JSON.parse(fs.readFileSync(item.file, 'utf8'));
    const outfits = data.outfits || [];
    
    // Ensure every outfit has an id
    let idsAssigned = 0;
    outfits.forEach(o => {
      if (!o.id) {
        o.id = generateNanoid();
        idsAssigned++;
      }
    });

    data.outfits = outfits;
    data.visibility = 'private';
    data.rating = 'explicit';
    fs.writeFileSync(item.file, JSON.stringify(data, null, 2), 'utf8');

    console.log(`Syncing ${item.name} (${item.id}): ${outfits.length} outfits (${idsAssigned} new IDs assigned)...`);

    const putRes = await fetch(`https://app.wyvern.chat/api/characters/${item.id}`, {
      method: 'PUT',
      headers: {
        'Authorization': `Bearer ${token}`,
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
      },
      body: JSON.stringify({
        outfits: outfits,
        visibility: 'private',
        rating: 'explicit'
      })
    });

    console.log(`  PUT Status: HTTP ${putRes.status}`);
    if (!putRes.ok) {
      console.error('  Error:', (await putRes.text()).slice(0, 200));
    }
  }

  console.log('\n=== VERIFYING LIVE OUTFIT COUNTS ON WYVERN ===');
  for (const item of charMap) {
    const res = await fetch(`https://app.wyvern.chat/api/characters/${item.id}`, {
      headers: { 'Authorization': `Bearer ${token}`, 'User-Agent': 'Mozilla/5.0' }
    });
    const c = await res.json();
    const liveOutfits = c.outfits || [];
    console.log(`Verified ${c.name}: ${liveOutfits.length} outfits, visibility=${c.visibility}, rating=${c.rating}`);
  }
}

syncOutfits().catch(console.error);
