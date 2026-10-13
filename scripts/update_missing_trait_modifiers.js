const fs = require('fs');

async function updateMissingTraits() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';

  // I 5 tratti identificati senza modificatori
  const traitUpdates = [
    {
      id: '_NL4ANGp2gjKtbAgRTFxbD',
      name: 'Apex Predator Divine Core',
      description: 'Consacrato dal Dio Lupo Fenris. Immunità biologica totale, sensi onnidirezionali e aura che proietta la supremazia fisica e carismatica dei Firstborn.',
      stat_modifiers: {
        strength: 3,
        endurance: 3,
        perception: 2,
        charisma: 2
      },
      player_selectable: true
    },
    {
      id: '_L2xQk9j8RnMKUgGnCVWRR',
      name: 'Berserker Internal Furnace',
      description: 'Metabolismo ipertermico a consumo di ferro. La forza e la rigenerazione scalano in modo colossale in battaglia a scapito di un consumo metabolico e di ferro accelerato.',
      stat_modifiers: {
        strength: 3,
        endurance: 3,
        agility: 1,
        intelligence: -1
      },
      player_selectable: true
    },
    {
      id: '_kUV13hFp2R2a4aYEXq3c4',
      name: 'Familiar Soulbound Synergy',
      description: 'Legame simbiotico profondo con un compagno animale sovrannaturale, con condivisione di percezione sensoriale e risonanza aurica.',
      stat_modifiers: {
        perception: 2,
        intelligence: 2,
        charisma: 1
      },
      player_selectable: true
    },
    {
      id: '_C8XXTwLd1mmF33EkQMUyD',
      name: 'Puppeteer Mana Strings',
      description: 'Capacita di tessere fili di mana invisibili per controllare burattini, simulacri o guidare traiettorie con precisione millimetrica.',
      stat_modifiers: {
        agility: 2,
        intelligence: 2,
        perception: 1,
        strength: -1
      },
      player_selectable: true
    },
    {
      id: '_AQ6Qy4KHMDgFWKPHDJeqb',
      name: 'Technomantic Data Resonance',
      description: 'Capacita di percepire il flusso di bit e la fibra ottica come tessuto eterico vivo, canalizzando incantesimi attraverso circuiti elettronici e reti digitali.',
      stat_modifiers: {
        intelligence: 3,
        perception: 2,
        strength: -1
      },
      player_selectable: true
    }
  ];

  console.log(`Aggiornamento modificatori per i 5 tratti RPG nel World ${worldId}...`);
  for (const t of traitUpdates) {
    const url = `https://app.wyvern.chat/api/worlds/rpg/traits/${t.id}`;
    const payload = {
      name: t.name,
      description: t.description,
      stat_modifiers: t.stat_modifiers,
      player_selectable: t.player_selectable
    };

    const res = await fetch(url, {
      method: 'PUT',
      headers: {
        'Authorization': 'Bearer ' + token,
        'Content-Type': 'application/json'
      },
      body: JSON.stringify(payload)
    });

    if (res.ok) {
      console.log(`[OK] Tratto aggiornato: "${t.name}" (${t.id}) -> Modifiers:`, JSON.stringify(t.stat_modifiers));
    } else {
      console.error(`[ERRORE ${res.status}] ${t.name}:`, await res.text());
    }
    await new Promise(r => setTimeout(r, 80));
  }

  // Verifica
  console.log('\nVerifica post-aggiornamento da API...');
  const checkRes = await fetch(`https://app.wyvern.chat/api/worlds/rpg/traits/${worldId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const allTraits = await checkRes.json();
  const stillWithout = allTraits.filter(t => !t.stat_modifiers || Object.keys(t.stat_modifiers).length === 0);
  console.log(`Tratti senza modificatori rimasti: ${stillWithout.length} (su ${allTraits.length} totali)`);
}

updateMissingTraits().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});
