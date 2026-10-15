const fs = require('fs');
const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();

const mapping = [
  { mineId: '_t4J9aQNJM36cUKAP4wB4U', worldId: '_x3VY2kcbaDbKyCqywGeET', name: 'Jasper Douglas Bloodmoon' },
  { mineId: '_EWqmxx3Q1fdK97AVBRqEW', worldId: '_d44gDc8N18kkbEhAcfUCG', name: 'Erik Douglas' },
  { mineId: '_AjphrWj2BMT9KJTx4KETE', worldId: '_r42cVzMjcGTAx7bR1DQVt', name: 'Noah Douglas Bloodmoon' },
  { mineId: '_yQeae3DnARft2RH4gaFNx', worldId: '_rAcN9GXD1Le4WxY28e49W', name: 'Malachia Douglas Bloodmoon' },
  { mineId: '_BQ4THBW3BKL2RN9Xy4YHb', worldId: '_JL37wK9PQMNDChULCDrWj', name: 'Logan Douglas' },
  { mineId: '_tJ8zaBLAb6n7XAyd8qhHQ', worldId: '_a6KYGdN3BWTgbYEbT4mx8', name: 'Zeera Darkfire' },
  { mineId: '_G4126zBQhWEtFkKCG3Dw3', worldId: '_BzKwAkgpPfbVkBzbDaEth', name: 'Jared Thompson' },
  { mineId: '_HqzMU3zVrgHaHBFKw4nQA', worldId: '_YY8VbpgzYk4dfFAL78rM3', name: 'Mackenzie Sanchez-Rogers' }
];

async function inspectMineCards() {
  for (const m of mapping) {
    const res = await fetch(`https://app.wyvern.chat/api/characters/${m.mineId}`, {
      headers: { 'Authorization': `Bearer ${token}` }
    });
    if (res.ok) {
      const d = await res.json();
      console.log(`Mine card: ${m.name} (ID: ${m.mineId})`);
      console.log(`  description len: ${(d.description||'').length} | personality len: ${(d.personality||'').length}`);
      console.log(`  lorebooks attached: ${JSON.stringify(d.lorebooks || [])}`);
    } else {
      console.log(`Error GET ${m.mineId}: ${res.status}`);
    }
  }
}
inspectMineCards().catch(console.error);
