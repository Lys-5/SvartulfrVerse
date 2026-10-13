const fs = require('fs');

const CURRENCY_USD = 'fbecc738-f9f7-4426-b8a1-a237b8ad922c';
const CURRENCY_CR = '8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a';

function sanitize(str) {
  return str.replace(/—/g, ', ').replace(/–/g, '-').replace(/\*\*/g, '').trim();
}

const jobsData = [
  {
    targetLoc: 'sugar_moon',
    name: 'Sugar Moon: Baker Apprentice & Counter Attendant',
    keys: ['lavoro panetteria', 'baker assistant', 'sugar moon job'],
    content: sanitize('Mansioni di impasto mattutino, sfornata dolci lunari e servizio al banco clienti presso Sugar Moon Bakery in Arcadia.'),
    wage: 350,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'roasted_bean',
    name: 'The Roasted Bean: Campus Barista & Study Monitor',
    keys: ['lavoro barista SUCC', 'roasted bean job', 'barista biblioteca'],
    content: sanitize('Preparazione di caffe espresso e bibite energizzanti per studenti e docenti presso The Roasted Bean nella Basilica Library.'),
    wage: 320,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'refuge_chats',
    name: 'Le Refuge des Chats: Familiar Care Assistant',
    keys: ['lavoro rifugio gatti', 'familiar care job', 'assistente famigli'],
    content: sanitize('Cura, spazzolatura, somministrazione snack e monitoraggio comportamentale dei famigli felini e compagni sovrannaturali ospitati.'),
    wage: 380,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'lunar_pharmacy',
    name: 'The Lunar Pharmacy: Dispensary Tech & Salve Mixer',
    keys: ['lavoro farmacia', 'lunar pharmacy job', 'tecnico dispensario'],
    content: sanitize('Miscelazione di pomate lenitive anti-argento, confezionamento di soppressori olfattivi LSE e gestione ricette mediche.'),
    wage: 450,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'marek_workshop',
    name: 'Cable District Garages: Heavy Bike Mechanic Apprentice',
    keys: ['lavoro officina marek', 'meccanico moto nomadi', 'mechanic apprentice'],
    content: sanitize('Apprendistato d officina con Marek: manutenzione telai pesanti, cambio oli alchemici, saldatura cromo-vanadio e supporto moto Ironhorn.'),
    wage: 520,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'directions_dragons',
    name: 'Directions & Dragons: Tabletop Clerk & Event Host',
    keys: ['lavoro negozio dnd', 'commesso giochi ruolo', 'directions dragons job'],
    content: sanitize('Vendita manuali, gestione tornei serali di miniature e supporto ai gruppi di gioco di ruolo sovrannaturali di Solarton.'),
    wage: 300,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'dairy_farm',
    name: 'Solarton Valley Dairy: Pasture Hand & Milker',
    keys: ['lavoro fattoria', 'mungitore dairy farm', 'bessie may job'],
    content: sanitize('Mungitura mattutina, cura del bestiame nei pascoli fatati e confezionamento latte bio e forme di formaggio con Bessie May.'),
    wage: 360,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'kerrigan_butchers',
    name: 'Kerrigan Butchers: Assistant Meat Cutter & Smoker',
    keys: ['lavoro macelleria', 'butcher apprentice', 'kerrigan sons job'],
    content: sanitize('Sezionamento carni bovine e suine per appetiti mannari, marinature spezzate e controllo dei forni di affumicatura a legno nobile.'),
    wage: 400,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'dusty_coyote',
    name: 'Dusty Coyote: Short-Order Line Cook',
    keys: ['lavoro cuoco diner', 'line cook dusty coyote', 'cameriere bakersfield'],
    content: sanitize('Cottura alla piastra di hamburger monumentali, preparazione patatine speziate e rifornimento continuo caraffe di caffe nero.'),
    wage: 340,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'sidewinders',
    name: 'Sidewinders Bar: Night Bartender & Floor Attendant',
    keys: ['lavoro bar solarton', 'bartender sidewinders', 'barback nightclub'],
    content: sanitize('Servizio cocktail sotto luci neon, gestione approvvigionamento fusti e controllo ordine durante serate musicali studentesche.'),
    wage: 420,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'the_verve',
    name: 'The Verve: VIP Lounge Server & Wine Steward',
    keys: ['lavoro lounge verve', 'server lusso bluemoon', 'sommelier blackwood'],
    content: sanitize('Servizio di alta classe ai tavoli VIP, decantazione bourbon e champagne d annata per esponenti delle casate di Blackwood City.'),
    wage: 550,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'claws_ink',
    name: 'Claws Steel & Ink: Studio Apprentice & Sanitizer',
    keys: ['lavoro studio tattoo', 'tattoo apprentice claws', 'assistente piercing'],
    content: sanitize('Sterilizzazione aghi e gioielli in titanio, accoglienza clienti, disegno stencil e cura igienica delle postazioni di tatuaggio.'),
    wage: 350,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'tidewrack_surf',
    name: 'Tidewrack Surf: Rental Clerk & Beach Safety Aide',
    keys: ['lavoro noleggio surf', 'surf rental clerk', 'bagnino solarton beach'],
    content: sanitize('Assegnazione mute e tavole da surf in fibra, stesura cere protettive e vigilanza sulla linea di costa durante l alta marea.'),
    wage: 320,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'basilica_library',
    name: 'Basilica Library: Grimoire Cataloger & Page',
    keys: ['lavoro archivio biblioteca', 'catalogatore grimoire', 'library page SUCC'],
    content: sanitize('Catalogazione tomi antichi, risistemazione scaffali nelle sezioni di magia protetta e assistenza agli studenti nella ricerca accademica.'),
    wage: 340,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'team_ukiyo',
    name: 'Team Ukiyo: Vault Porter & Tactical Supply Aide',
    keys: ['lavoro team ukiyo', 'porter vault caccia', 'supply aide radek'],
    content: sanitize('Gestione magazzino lame d argento, stoccaggio nuclei di mostro recuperati dai dungeon e conteggio munizioni per la squadra di Radek.'),
    wage: 650,
    currency: CURRENCY_CR,
    pay_period: 'weekly'
  },
  {
    targetLoc: 'camp_mystic',
    name: 'Camp Mystic: Outdoor Counselor & Trail Patrol',
    keys: ['lavoro camp mystic', 'istruttore outdoor lago erie', 'counselor campo estivo'],
    content: sanitize('Guida sentieri nei boschi della riserva, manutenzione canoe e canoe dock, e sorveglianza perimetrale barriere antimostro serali.'),
    wage: 380,
    currency: CURRENCY_USD,
    pay_period: 'weekly'
  }
];

async function createAllJobs() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const url = 'https://app.wyvern.chat/api/worlds/lexicon';

  console.log(`Creazione di ${jobsData.length} Job nel Lexicon del World...`);
  const createdJobs = [];

  for (let i = 0; i < jobsData.length; i++) {
    const j = jobsData[i];
    const payload = {
      world_id: worldId,
      name: j.name,
      type: 'job',
      keys: j.keys,
      key_logic: 'AND_ANY',
      content: j.content,
      is_global: false,
      enabled: true,
      position: 'before_char',
      priority: 0,
      job_config: {
        wage: j.wage,
        currency_id: j.currency,
        pay_period: j.pay_period,
        scope: 'local',
        only_paid_at_workplace: true
      }
    };

    try {
      const res = await fetch(url, {
        method: 'POST',
        headers: {
          'Authorization': 'Bearer ' + token,
          'Content-Type': 'application/json'
        },
        body: JSON.stringify(payload)
      });

      if (res.ok) {
        const d = await res.json();
        createdJobs.push({
          id: d.id,
          name: j.name,
          targetLoc: j.targetLoc,
          wage: j.wage,
          currency: j.currency
        });
        process.stdout.write(`\r[${i + 1}/${jobsData.length}] Creato: "${j.name.slice(0, 35)}" -> ${d.id}`);
      } else {
        console.error(`\n[ERRORE ${res.status}] ${j.name}:`, await res.text());
      }
    } catch (e) {
      console.error(`\n[ECCEZIONE] ${j.name}:`, e.message);
    }

    await new Promise(r => setTimeout(r, 70));
  }

  console.log(`\n\nCreazione completata! ${createdJobs.length} Job creati.`);
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/created_iconic_jobs.json', JSON.stringify(createdJobs, null, 2), 'utf8');
}

createAllJobs().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});
