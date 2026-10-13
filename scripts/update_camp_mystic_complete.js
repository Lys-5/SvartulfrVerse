const fs = require('fs');

async function updateCampMysticComplete() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const scenarioId = '_a9yMR9Q3NJzLeXLGnQpbX';

  const introText = `=>Narrator:
Domenica 7 luglio 2024, ore 14:30 - Ingresso di Camp Mystic, Riserva Boschiva sul Lago

La sessione estiva della Solarton University si e' appena conclusa e l'aria della California lascia spazio alla brezza fresca del lago e al profumo intenso di aghi di pino e legna arsa. Oltre il monumentale cancello in travi di quercia e ferro runico si apre Camp Mystic: migliaia di acri di foresta protetta, chalet in legno massiccio affacciati sui moli d'attracco e quattro distretti residenziali dedicati alle vacanze estive e all'addestramento all'aperto degli studenti.

Il furgone della Douglas Commercial Coalition e' parcheggiato vicino alla Lodge principale con il portellone aperto, mentre l'aria risuona del frinire delle cicale e del rumore dell'acqua limpida che si infrange sui pontili.

=>Alyssa:
Alyssa scende dal gradino del veicolo, stringendo a se' una borsa di tela con i costumi e il blocco note di botanica. Indossa un top leggero azzurro, shorts estivi e sandali comodi, le orecchie lupine che si orientano curiose verso il fruscio del bosco.

"L'aria e' incredibile qui," mormora, girandosi verso i suoi fratelli con un sorriso radioso che scioglie settimane di tensione accumulate sugli esami del SUCC. "Niente clacson di Solarton, niente odore di asfalto rovente. Solo alberi e acqua."

=>Jasper:
Jasper scende con il suo zaino tecnico e un paio di occhiali da sole da cui pendono cuffie wireless impermeabili. Osserva la vegetazione e annuisce con calma.

"I ripetitori del campo sono schermati a frequenza runica," dice, controllando il segnale sullo smartphone prima di infilarlo nella tasca posteriore. "Vuol dire niente chiamate di lavoro della DCC per tre settimane intere. Papa' ha dovuto accettarlo per iscritto."

=>Malachia:
Malachia scende per ultimo, scaricando a terra con una mano sola un baule di attrezzatura pesante da trekking e canottaggio. I suoi occhi ambra esaminano il limitare degli alberi, fiutando il vento. La sua postura, pur rilassata per gli standard di un cacciatore Apex, trasmette la consueta presenza solida e rassicurante.

"La riserva e' pulita," dice Malachia a bassa voce, incrociando lo sguardo di Alyssa. "Le barriere tengono fuori qualsiasi squarcio selvaggio. Si puo' nuotare fino alla boa centrale senza pensieri."

=>Noah:
Noah chiude il portellone con un tonfo teatrale, stendendo le braccia verso il cielo azzurro e respirando a pieni polmoni.

"Benvenuti alle vacanze estive, famiglia. Le canoe ci aspettano, il falo' di stasera e' gia' prenotato, e per le prossime tre settimane l'unico nostro dovere e' rilassarci e goderci il lago."`;

  const pool = [
    { character_id: '_x3VY2kcbaDbKyCqywGeET', participation_weight: 50 }, // Jasper
    { character_id: '_dZzV6Hw8e3Qe67mEa6Tq3', participation_weight: 50 }, // Noah
    { character_id: '_rAcN9GXD1Le4WxY28e49W', participation_weight: 50 }, // Malachia
    { character_id: '_t3YfA6eWqQp4B9WjX2L7b', participation_weight: 40 }, // Jared
    { character_id: '_E3XgK9eM8wb4J6QpY1Lm7', participation_weight: 40 }  // Mac
  ];

  const premadeScenes = [
    {
      id: 'scene-camp-mystic-arrival',
      description: 'Arrivo a Camp Mystic: Benvenuti al Lago (Apertura Vacanze Estive)',
      scene_text: introText
    }
  ];

  const payload = {
    name: 'Camp Mystic: Vacanze Estive & Addestramento sul Lago',
    scenario_premise: 'La sessione estiva della Solarton University e giunta al termine. Alyssa, Jasper, Noah, Malachia e gli studenti del SUCC si trasferiscono per tre settimane a Camp Mystic, una vasta riserva residenziale lacustre immersa nei boschi. Tra gite in canoa, addestramento outdoor, falo serali e distensione dopo gli esami, la famiglia e il party vivono le vacanze estive lontani dallo stress metropolitano.',
    description: 'Scenario estivo ufficiale ambientato a Camp Mystic sul Lago Erie durante la pausa universitaria del SUCC. Include chalet residenziali, attivita outdoor, balneazione e dinamiche di branco rilassate.',
    included_character_pool: pool,
    premade_scenes: premadeScenes,
    playable_character_ids: ['_MXcEC8Y6B3BNm3b1ttHj6'],
    include_character_select: true,
    include_rpg_build: true
  };

  const res = await fetch(`https://app.wyvern.chat/api/worlds/scenarios/${scenarioId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });

  console.log('Update scenario status:', res.status);
  if (res.ok) {
    const d = await res.json();
    console.log('Aggiornato scenario con successo:', d.id, d.name);
  } else {
    const err = await res.text();
    console.log('Errore update:', err);
  }
}

updateCampMysticComplete();
