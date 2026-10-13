const fs = require('fs');

async function saveAllProperly() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const lorebooks = [
    { key: 'apex_predator', id: '_pEDXhabGEAnJQAmFcLqz3' },
    { key: 'familiars', id: '_HUPcrweNDmaMH4pJQX7WP' },
    { key: 'cybers', id: '_THLNxM9bngdhH91dHMPf7' },
    { key: 'technomancer', id: '_P2BkDKXn7mqmnma8Qatrk' },
    { key: 'berserker', id: '_rHVJVjyqb3pTdrmf3tMY4' },
    { key: 'puppet_master', id: '_BJTdnhRUHtHtqay4CPr7z' },
    { key: 'graviton', id: '_eCThV9RTzGGEpkTr2zpn3' },
    { key: 'shapeshifter', id: '_9K9xwzxPkPNTCYTNmTTDA' },
    { key: 'dreamwalker', id: '_RKQMRm1yUFPK3jz6reNzL' },
    { key: 'warper', id: '_BEEJhmr7CFWNCgAHxg37m' },
    { key: 'shadow_lord', id: '_8KbBWGpqFt14m91C76H1n' },
    { key: 'druid', id: '_afbdPa9XrrGXx1JmeMfTE' },
    { key: 'sculpter', id: '_EMLg2NLrJXHNK6HbDNCJV' },
    { key: 'mystics', id: '_GypjWdEHxNaJJ3bA8d8p6' },
    { key: 'mystics_extras', id: '_RdmpwA7cYM7FqrYhBV2UC' },
    { key: 'spell_compendium', id: '_JqtjUra49EXrPBDgpKLWy' },
    { key: 'camp_mystic', id: '_tYwzE6zhLYFAmKV6mm6Tq' }
  ];

  for (const lb of lorebooks) {
    const res = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
      headers: { 'Authorization': 'Bearer ' + token }
    });
    const d = await res.json();
    let entries = [];
    if (d.lexicon && Array.isArray(d.lexicon.entries) && d.lexicon.entries.length > 0) {
      entries = d.lexicon.entries;
    } else if (Array.isArray(d.entries) && d.entries.length > 0) {
      entries = d.entries;
    } else if (d.entries && typeof d.entries === 'object') {
      entries = Object.values(d.entries);
    }
    fs.writeFileSync(
      `C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/lb_${lb.key}.json`,
      JSON.stringify(entries, null, 2),
      'utf8'
    );
    console.log(`${lb.key}: ${entries.length} voci salvate.`);
  }
}

saveAllProperly();
