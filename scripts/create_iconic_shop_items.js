const fs = require('fs');

const CURRENCY_USD = 'fbecc738-f9f7-4426-b8a1-a237b8ad922c';
const CURRENCY_CR = '8c7bca5a-5d3f-4780-93cb-5cb63dc2cf0a';

function sanitize(str) {
  return str.replace(/—/g, ', ').replace(/–/g, '-').replace(/\*\*/g, '').trim();
}

// Catalogo item iconici per gli shop del World
const itemsData = [
  // 1. Sugar Moon Bakery & Cafe (Neve & Jaelyn)
  {
    shop: 'sugar_moon',
    name: 'Moonflower Honey Pastry',
    keys: ['Moonflower Honey Pastry', 'pasticcino miele lunare', 'dolce fiore di luna'],
    content: sanitize('Soffice sfoglia dorata ripiena di crema pasticcera al miele di moonflower selvatico. Emana un delicato profumo zuccherino che distende i sensi e riduce lo stress somatico nei mutaforma.'),
    price: 8,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'sugar_moon',
    name: 'Artisanal Silver-Crust Loaf',
    keys: ['Silver-Crust Loaf', 'pane crosta argento', 'filone artigianale'],
    content: sanitize('Pane rustico a lievitazione naturale cotto su pietra refrattaria, arricchito con semi tostati di girasole ed erbe purificanti. Base alimentare perfetta per ricaricare le energie metabolico-lupine.'),
    price: 6,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'sugar_moon',
    name: 'Chamomile & Moon-Herb Infusion',
    keys: ['Chamomile Moon-Herb Infusion', 'tisana camomilla lunare', 'infuso rilassante'],
    content: sanitize('Tisana calda alle erbe biologiche di Hex Valley con fiori di camomilla e melissa. Ideale prima del riposo notturno o per placare l irrequietezza olfattiva durante il pre-rut.'),
    price: 5,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'sugar_moon',
    name: 'Full Moon Glazed Doughnut',
    keys: ['Full Moon Glazed Doughnut', 'ciambella plenilunio', 'doughnut zucchero velo'],
    content: sanitize('Ciambella soffice con glassa vanigliata brillante che ricorda il disco del plenilunio. La combinazione di glucosio rapido rinvigorisce all istante l umore dello studente o del cliente stanco.'),
    price: 4,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 2. The Roasted Bean (Basilica Library SUCC)
  {
    shop: 'roasted_bean',
    name: 'Double-Shot Mana Espresso',
    keys: ['Double-Shot Mana Espresso', 'espresso mana SUCC', 'caffe risonante'],
    content: sanitize('Caffe espresso ad alta concentrazione preparato con chicchi torrefatti in camera eterica. Risveglia la concentrazione e allontana il sonno per quattro ore piene di studio o guardia.'),
    price: 6,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'roasted_bean',
    name: 'Therianthrope Protein Shake',
    keys: ['Therianthrope Protein Shake', 'frullato proteico shifters', 'protein shake lupine'],
    content: sanitize('Frullato iperproteico da 750ml formulato con siero di latte arricchito di ferro e aminoacidi ramificati. Soddisfa il fabbisogno muscolare degli atleti Bulls e degli shifters in allenamento.'),
    price: 9,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'roasted_bean',
    name: 'Cold Brew Nitro Focus',
    keys: ['Cold Brew Nitro Focus', 'nitro cold brew SUCC', 'caffe estratto a freddo'],
    content: sanitize('Caffe estratto a freddo con azoto arricchito da micro-cristalli di quarzo risonante. Fornisce energia prolungata e costante senza picchi di tachicardia o tremori sensoriali.'),
    price: 7,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 3. Le Refuge des Chats (Arcadia)
  {
    shop: 'refuge_chats',
    name: 'Spiced Catnip Steamer Latte',
    keys: ['Spiced Catnip Steamer Latte', 'latte erba gatta', 'bevanda famigli felini'],
    content: sanitize('Latte tiepido montato con gocce distillate di nepeta cataria purificata e cannella. Una coccola irrinunciabile per demi-umani felini, famigli e spiriti guardiani del quartiere.'),
    price: 7,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'refuge_chats',
    name: 'Familiar Empathetic Treat Biscuit',
    keys: ['Familiar Empathetic Treat Biscuit', 'biscotto famigli', 'snack empatico animale'],
    content: sanitize('Biscotto croccante ad alto valore empatico. Quando offerto a un famiglio o animale da compagnia sovrannaturale, rafforza momentaneamente la sincronia telepatica e l affetto reciproco.'),
    price: 5,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 4. The Lunar Pharmacy / Clinica Ortus / SUCC Dispensary
  {
    shop: 'lunar_pharmacy',
    name: 'LSE Scent Suppressor Spray Bottle',
    keys: ['LSE Scent Suppressor Spray Bottle', 'spray soppressore feromoni', 'flacone soppressore LSE'],
    content: sanitize('Flacone nebulizzatore da 100ml contenente formula inibitrice dei feromoni biologici. Maschera per otto ore odori territoriali, sentori di rut e ormoni di stress, evitando attenzioni indesiderate.'),
    price: 45,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'lunar_pharmacy',
    name: 'Anti-Silver Burn Healing Salve',
    keys: ['Anti-Silver Burn Healing Salve', 'pomata anti-argento', 'salve ustioni argento'],
    content: sanitize('Pomata medicale formulata con estratti di corteccia d ontano e polvere di quarzo calmante. Neutralizza l intossicazione da argento cutaneo e accelera la riparazione dell epidermide mutaforma.'),
    price: 35,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'lunar_pharmacy',
    name: 'Wolfsbane Toxin Neutralizer',
    keys: ['Wolfsbane Toxin Neutralizer', 'antidoto aconito', 'neutralizzante wolfsbane'],
    content: sanitize('Fiala iniettabile o bevibile di alcaloidi sintetici DCC. Lega e disattiva le molecole di aconito nel circolo sanguigno, bloccando convulsioni e paralisi morfologica.'),
    price: 60,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'lunar_pharmacy',
    name: 'Cellular Regeneration Ampoule',
    keys: ['Cellular Regeneration Ampoule', 'fiala rigenerazione', 'tonico cellulare'],
    content: sanitize('Fiala concentrata di nutrienti cellulari arricchita da ferro ionico. Stimola il fattore rigenerativo endogeno rimarginando lacerazioni e traumi muscolari in pochi minuti.'),
    price: 50,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 5. Cable District Garages / Marek's Workshop (Ironhorn Nomads)
  {
    shop: 'marek_workshop',
    name: 'High-Performance Graphene Chain Lubricant',
    keys: ['Graphene Chain Lubricant', 'grasso catena grafene', 'lubrificante moto marek'],
    content: sanitize('Flacone di grasso sintetico al grafene e micro-particelle alchemiche per catene e trasmissioni primarie di moto pesanti. Resiste a temperature e torsioni estreme.'),
    price: 25,
    currency: CURRENCY_USD,
    category: 'Material'
  },
  {
    shop: 'marek_workshop',
    name: 'Reinforced Runic Mechanic Wrench',
    keys: ['Reinforced Runic Mechanic Wrench', 'chiave inglese runica', 'attrezzo officina marek'],
    content: sanitize('Chiave da officina in cromo-vanadio temperata con leghe d acciaio antimagico. Non si deforma nemmeno se utilizzata con la forza sovrumana di un minotauro o di un enforcer.'),
    price: 45,
    currency: CURRENCY_USD,
    category: 'Equipment'
  },
  {
    shop: 'marek_workshop',
    name: 'Ironhorn Nomads Leather Vest Patch',
    keys: ['Ironhorn Nomads Leather Vest Patch', 'toppa cuoio ironhorn', 'patch club marek'],
    content: sanitize('Toppa ufficiale in cuoio pesante marchiata a fuoco con il teschio taurino degli Ironhorn Nomads. Segno di rispetto e libera circolazione nei garage del Cable District.'),
    price: 20,
    currency: CURRENCY_USD,
    category: 'Key Item'
  },

  // 6. Directions & Dragons (Solarton Square)
  {
    shop: 'directions_dragons',
    name: 'Obsidian Balanced Polyhedral Dice Set',
    keys: ['Obsidian Balanced Polyhedral Dice Set', 'set dadi ossidiana', 'dadi dnd solarton'],
    content: sanitize('Elegante set completo da sette dadi per gioco di ruolo intagliati in autentica ossidiana vulcanica. I baricentri sono calibrati con precisione millimetrica per tiri impeccabili.'),
    price: 35,
    currency: CURRENCY_USD,
    category: 'Trade Good'
  },
  {
    shop: 'directions_dragons',
    name: 'Acoustic-Dampening Game Master Screen',
    keys: ['Game Master Screen', 'schermo del master fonoassorbente', 'manuali dnd'],
    content: sanitize('Schermo del master a quattro ante rivestito in feltro runico fonoassorbente: impedisce a compagni demi-umani dall udito ipersviluppato di origliare i piani della campagna.'),
    price: 40,
    currency: CURRENCY_USD,
    category: 'Trade Good'
  },
  {
    shop: 'directions_dragons',
    name: 'Miniature Pewter Werewolf Warlord',
    keys: ['Pewter Werewolf Warlord Miniature', 'miniatura lupo mannaro', 'figurina peltro'],
    content: sanitize('Miniatura da collezione in peltro massiccio finemente scolpita e dipinta a mano raffigurante un colossale capo branco licantropo armato di ascia bipenne.'),
    price: 18,
    currency: CURRENCY_USD,
    category: 'Trade Good'
  },

  // 7. Solarton Valley Dairy Farm (Bessie May)
  {
    shop: 'dairy_farm',
    name: 'Raw Clover Valley Whole Milk (Gallon)',
    keys: ['Raw Clover Whole Milk', 'latte intero trifoglio', 'latte bio solarton farm'],
    content: sanitize('Gallone di latte vaccino intero biologico non pastorizzato munto a mano presso i pascoli fatati della Solarton Valley. Ricco di grassi nobili, calcio e vitalita pastorale.'),
    price: 7,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'dairy_farm',
    name: 'Oak-Aged Smoked Farmhouse Cheese Wheel',
    keys: ['Oak-Aged Farmhouse Cheese', 'forma formaggio affumicato', 'formaggio bessie may'],
    content: sanitize('Piccola forma di formaggio a pasta dura affumicata lentamente con legno di quercia. Sapore intenso, sapido e corposo perfetto per saziare appetiti vigorosi.'),
    price: 16,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'dairy_farm',
    name: 'Hand-Churned Sweet Cream Butter',
    keys: ['Hand-Churned Sweet Cream Butter', 'burro mantecato', 'panetto burro farm'],
    content: sanitize('Panetto di burro artigianale ottenuto da panna dolce affiorata naturalmente. Consistenza vellutata e sapore puro di pascolo incontaminato.'),
    price: 6,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 8. Kerrigan & Sons Butchers (Bricklane Mall)
  {
    shop: 'kerrigan_butchers',
    name: 'Prime Bone-In Ribeye Steak (2 lbs)',
    keys: ['Prime Bone-In Ribeye Steak', 'costata manzo kerrigan', 'bistecca predatore'],
    content: sanitize('Colossale costata di manzo Angus con osso, frollata a secco per trenta giorni. Taglio marmorizzato e ricchissimo di mioglobina, ideale sia cruda per licantropi che scottata alla brace.'),
    price: 32,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'kerrigan_butchers',
    name: 'Smoked Wild Boar Hunter Sausages',
    keys: ['Smoked Wild Boar Sausages', 'salsicce cinghiale', 'salumi caccia kerrigan'],
    content: sanitize('Filza di salsicce di cinghiale selvatico affumicate con legno di ginepro e pepe nero spezzato. Pratiche da portare in tasca durante pattugliamenti o lunghe camminate nei boschi.'),
    price: 14,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'kerrigan_butchers',
    name: 'Raw Beef Marrow Bones Pack',
    keys: ['Raw Beef Marrow Bones Pack', 'ossa midollo manzo', 'pre-shift marrow bones'],
    content: sanitize('Confezione di tre grandi ossa di manzo tagliate longitudinalmente con midollo fresco intatto. Essenziali prima del plenilunio per consolidare la densita ossea nel Partial Shift.'),
    price: 12,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 9. The Dusty Coyote Diner (Bakersfield)
  {
    shop: 'dusty_coyote',
    name: 'Coyote Deluxe Monster Burger',
    keys: ['Coyote Deluxe Monster Burger', 'hamburger dusty coyote', 'burger bakersfield'],
    content: sanitize('Doppio hamburger di manzo da mezza libbra con formaggio fuso, bacon croccante, anelli di cipolla e salsa piccante della casa, servito con abbondanti patatine fritte.'),
    price: 15,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'dusty_coyote',
    name: 'Bottomless Black Roadhouse Drip Coffee',
    keys: ['Bottomless Black Drip Coffee', 'caffe americano coyote', 'coffee refill diner'],
    content: sanitize('Tazza mug di caffe americano nero bollente con refill continuo dal boccale della cameriera. Aroma tostato e amaro come l asfalto caldo della Route 99.'),
    price: 4,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'dusty_coyote',
    name: 'Warm Homemade Pecan Pie Slice',
    keys: ['Warm Homemade Pecan Pie', 'torta noci pecan', 'pecan pie diner'],
    content: sanitize('Generosa fetta di crostata tradizionale alle noci pecan della valle, servita tiepida con una pallina di gelato alla vaniglia fusa a lato.'),
    price: 7,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 10. Sidewinders Bar & Nightclub (Solarton)
  {
    shop: 'sidewinders',
    name: 'Venom-Gold Agave Tequila Shot',
    keys: ['Venom-Gold Agave Tequila Shot', 'tequila shot sidewinders', 'shot bar solarton'],
    content: sanitize('Bicchiere da shot di tequila d agave invecchiata con scaglie di sale purificato e una goccia di aroma al lime. Brucia la gola con energia alcolica decisa.'),
    price: 8,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'sidewinders',
    name: 'Neon Blue Highball Cocktail',
    keys: ['Neon Blue Highball Cocktail', 'cocktail neon sidewinders', 'drink discoteca'],
    content: sanitize('Long drink luminescente che brilla sotto le luci UV del club, a base di gin, tonica amara e liquore di curaçao alchemico. Rinfrescante e festoso.'),
    price: 12,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 11. The Verve (Bluemoon Lounge Blackwood)
  {
    shop: 'the_verve',
    name: 'Douglas Reserve 18-Year Bourbon',
    keys: ['Douglas Reserve 18-Year Bourbon', 'bourbon riserva douglas', 'whisky verve'],
    content: sanitize('Bicchiere tumbler con ghiaccio sferico di bourbon invecchiato diciotto anni in botti di rovere tostato della riserva Douglas. Note di vaniglia, cuoio nobile e fumo di cedro.'),
    price: 28,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'the_verve',
    name: 'Vintage Noir Crystal Champagne',
    keys: ['Vintage Noir Crystal Champagne', 'champagne noir verve', 'flute champagne lusso'],
    content: sanitize('Flute di cristallo soffiato contenente champagne millesimato d alta quota con perlage finissimo e sentori di frutti di bosco scuri. L apice dell eleganza notturna di Blackwood.'),
    price: 35,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 12. Claws Steel & Ink (Bricklane Mall)
  {
    shop: 'claws_ink',
    name: 'Aloe & Vitamin E Tattoo Aftercare Butter',
    keys: ['Aloe Vitamin E Tattoo Butter', 'balsamo tatuaggi claws', 'crema cura tattoo'],
    content: sanitize('Vasetto di burro biologico lenitivo per la cura e la cicatrizzazione rapida dei tatuaggi. Formula ipoallergenica all aloe arborescens adatta alla pelle dei mutaforma.'),
    price: 18,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },
  {
    shop: 'claws_ink',
    name: 'Surgical Black Titanium Industrial Piercing',
    keys: ['Black Titanium Industrial Piercing', 'piercing titanio nero', 'gioiello orecchio claws'],
    content: sanitize('Barretta da piercing industriale in titanio grado ASTM-F136 anodizzato nero lucido. Sterile, anallergica e sagomata per accomodare la cartilagine d orecchie animali e umane.'),
    price: 25,
    currency: CURRENCY_USD,
    category: 'Equipment'
  },

  // 13. Tidewrack Surf & Rental (Bricklane Mall)
  {
    shop: 'tidewrack_surf',
    name: 'Reinforced Carbon-Fiber Shortboard',
    keys: ['Carbon-Fiber Shortboard', 'tavola surf carbonio', 'surfboard tidewrack'],
    content: sanitize('Tavola da surf da sei piedi con anima rinforzata in fibra di carbonio. Leggera sull onda ma abbastanza robusta da non spezzarsi sotto la forza fisica di uno shifter.'),
    price: 380,
    currency: CURRENCY_USD,
    category: 'Equipment'
  },
  {
    shop: 'tidewrack_surf',
    name: 'Thermal Neoprene Pacific Wetsuit (4/3mm)',
    keys: ['Thermal Neoprene Wetsuit', 'muta termica neoprene', 'wetsuit surf pacific'],
    content: sanitize('Muta integrale termica spessore 4/3mm con cuciture nastrate a tenuta stagna. Protegge dal freddo delle correnti oceaniche della California settentrionale.'),
    price: 160,
    currency: CURRENCY_USD,
    category: 'Equipment'
  },
  {
    shop: 'tidewrack_surf',
    name: 'Organic Coconut Cold-Water Surf Wax',
    keys: ['Organic Coconut Surf Wax', 'cera surf cocco', 'surf wax tidewrack'],
    content: sanitize('Panetto di cera antiscivolo naturale al profumo intenso di cocco per deck di tavole da surf. Garantisce un grip eccellente anche in acque fredde.'),
    price: 8,
    currency: CURRENCY_USD,
    category: 'Consumable'
  },

  // 14. Full Moon Market & Bricklane Night Stalls (Solarton Square)
  {
    shop: 'full_moon_market',
    name: 'Braided Silver Thread Talisman Bracelet',
    keys: ['Braided Silver Thread Bracelet', 'bracciale filo argento', 'talismano protettivo'],
    content: sanitize('Bracciale artigianale intrecciato con filo di seta nera e sottilissima lamina d argento schermato, con un ciondolo apotropaico che vibra in presenza di veleni o miasmi eterici.'),
    price: 30,
    currency: CURRENCY_USD,
    category: 'Equipment'
  },
  {
    shop: 'full_moon_market',
    name: 'Jar of Luminescent Hex Valley Moon Moss',
    keys: ['Luminescent Moon Moss', 'muschio luminescente', 'barattolo moon moss'],
    content: sanitize('Barattolo in vetro trasparente contenente muschio vivo bioluminescente raccolto nelle caverne di Hex Valley. Emana una morbida luce verde-azzurra permanente per camere e tende.'),
    price: 22,
    currency: CURRENCY_USD,
    category: 'Trade Good'
  },
  {
    shop: 'full_moon_market',
    name: 'Handcrafted Distressed Leather Belt Pouch',
    keys: ['Handcrafted Leather Belt Pouch', 'borsello cuoio cintura', 'pouch pelle mercato'],
    content: sanitize('Borsello compatto da cintura in cuoio conciato al vegetale con bottone in corno e cuciture cerate rinforzate. Contiene comodamente chiavi, monete, pozioni o fiale medicinali.'),
    price: 25,
    currency: CURRENCY_USD,
    category: 'Equipment'
  }
];

async function createAllIconicItems() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const url = 'https://app.wyvern.chat/api/worlds/lexicon';

  console.log(`Creazione di ${itemsData.length} item iconici per gli shop del World...`);
  const createdItems = [];

  for (let i = 0; i < itemsData.length; i++) {
    const it = itemsData[i];
    const payload = {
      world_id: worldId,
      name: it.name,
      type: 'item',
      keys: it.keys,
      key_logic: 'AND_ANY',
      content: it.content,
      is_global: true,
      enabled: true,
      position: 'before_char',
      priority: 0
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
        createdItems.push({
          id: d.id,
          name: it.name,
          shop: it.shop,
          price: it.price,
          currency: it.currency,
          category: it.category
        });
        process.stdout.write(`\r[${i + 1}/${itemsData.length}] Creato: "${it.name.slice(0, 35)}" -> ${d.id}`);
      } else {
        console.error(`\n[ERRORE ${res.status}] ${it.name}:`, await res.text());
      }
    } catch (e) {
      console.error(`\n[ECCEZIONE] ${it.name}:`, e.message);
    }

    await new Promise(r => setTimeout(r, 70));
  }

  console.log(`\n\nCreazione completata! ${createdItems.length} item creati.`);
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/created_iconic_shop_items.json', JSON.stringify(createdItems, null, 2), 'utf8');
}

createAllIconicItems().catch(err => {
  console.error('Fatal:', err);
  process.exit(1);
});
