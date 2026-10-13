const fs = require('fs');

async function inspectRemainingLorebooks() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  // Mapping dei lorebook identificati
  const lorebooks = [
    { key: 'apex_predator', id: '_pEDXhabGEAnJQAmFcLqz3', name: 'Apex Predator' },
    { key: 'familiars', id: '_HUPcrweNDmaMH4pJQX7WP', name: 'The Familiar Species (OC)' },
    { key: 'cybers', id: '_THLNxM9bngdhH91dHMPf7', name: 'Cybers And Cyberspace' },
    { key: 'technomancer', id: '_P2BkDKXn7mqmnma8Qatrk', name: 'Technomancer' },
    { key: 'berserker', id: '_rHVJVjyqb3pTdrmf3tMY4', name: 'Berserker Bloodline Codex' },
    { key: 'puppet_master', id: '_BJTdnhRUHtHtqay4CPr7z', name: 'Puppet Master' },
    { key: 'graviton', id: '_eCThV9RTzGGEpkTr2zpn3', name: 'Graviton' },
    { key: 'shapeshifter', id: '_9K9xwzxPkPNTCYTNmTTDA', name: 'Shapeshifter' },
    { key: 'dreamwalker', id: '_RKQMRm1yUFPK3jz6reNzL', name: 'Dreamwalker' },
    { key: 'warper', id: '_BEEJhmr7CFWNCgAHxg37m', name: 'The Warper' },
    { key: 'shadow_lord', id: '_8KbBWGpqFt14m91C76H1n', name: 'Shaow Lord' },
    { key: 'druid', id: '_afbdPa9XrrGXx1JmeMfTE', name: 'Druid' },
    { key: 'sculpter', id: '_EMLg2NLrJXHNK6HbDNCJV', name: 'Sculpter' },
    { key: 'mystics', id: '_GypjWdEHxNaJJ3bA8d8p6', name: '✨️Mystics' },
    { key: 'mystics_extras', id: '_RdmpwA7cYM7FqrYhBV2UC', name: '⭐️Mystics Extras' },
    { key: 'spell_compendium', id: '_JqtjUra49EXrPBDgpKLWy', name: '✨ Spell Compendium (120 Spells)' },
    { key: 'camp_mystic', id: '_tYwzE6zhLYFAmKV6mm6Tq', name: 'Camp Mystic' }
  ];

  console.log(`Inizio scansione e salvataggio di ${lorebooks.length} lorebook...`);
  const summary = {};

  for (const lb of lorebooks) {
    try {
      const res = await fetch(`https://app.wyvern.chat/api/lorebooks/${lb.id}`, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (res.ok) {
        const data = await res.json();
        const entries = Array.isArray(data.entries) ? data.entries : Object.values(data.entries || {});
        summary[lb.key] = {
          id: lb.id,
          name: data.name,
          entriesCount: entries.length,
          sampleEntries: entries.slice(0, 5).map(e => ({
            keys: e.keys,
            firstLine: (e.content || '').split('\n')[0].slice(0, 80)
          }))
        };
        fs.writeFileSync(
          `C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/lb_${lb.key}.json`,
          JSON.stringify(entries, null, 2),
          'utf8'
        );
        console.log(`[OK] ${lb.name} (${lb.id}): ${entries.length} entries`);
      } else {
        console.error(`[ERRORE ${res.status}] ${lb.name} (${lb.id})`);
      }
    } catch (e) {
      console.error(`[ECCEZIONE] ${lb.name}: ${e.message}`);
    }
  }

  fs.writeFileSync(
    'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/lorebooks_inspection_summary.json',
    JSON.stringify(summary, null, 2),
    'utf8'
  );
  console.log('Riepilogo salvato!');
}

inspectRemainingLorebooks();
