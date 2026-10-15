const fs = require('fs');

const original = JSON.parse(fs.readFileSync('scratch/alyssa_persona_live.json', 'utf8'));

// 1. Prepare updated appearances
const updatedAppearances = original.appearances.map(a => {
  if (a.id === 'appearance_6_pa6kZ9BzwLC05qO5Fuk' || a.name.toLowerCase() === 'base') {
    return {
      ...a,
      name: 'Base',
      description: `Fisionomia naturale di Alyssa Douglas Bloodmoon in forma bipede parziale (Founding Bloodline Douglas-Bloodmoon).
Statura e corporatura: Altezza minuta di 155 cm con silhouette sinuosa e femminile a clessidra accentuata (misure 95-55-95 cm), torace minuto con seno abbondante e pesante DD-cup, vita stretta e fianchi dolcemente arrotondati.
Pelle e tratti biologici: Pelle chiara, liscia, immacolata e iper-sensibile al tatto e alle variazioni termiche; caratteristica marcatura lunare a mezzaluna color madreperla sul fianco sinistro (Segno di Mani). Tatuaggio runico Gebo impresso all'interno del polso sinistro (legame gemellare con Jasper). Anello con sigillo d'argento della casata Douglas portato all'anulare sinistro.
Tratti lupini e appendici: Singolo paio di orecchie da lupo mobili, grandi e soffici situate sulla sommità del capo, rivestite di morbida pelliccia color castano-caramello all'esterno e piumaggio chiaro all'interno (nessun orecchio umano laterale). Coda da lupo folta, maestosa e vaporosa color caramello con punta nero netto, altamente espressiva e reattiva agli stati emotivi.
Volto e chioma: Viso dolce a cuore con lineamenti gentili, grandi occhi a mandorla color verde menta limpido e luminoso, ciglia lunghe e labbra naturalmente piene e rosee. Lunghi e setosi capelli color castano-caramello caldo che scendono in morbide onde fino all'osso sacro e al coccige.
Firma aromatica: Scent naturale e avvolgente di miele millefiori selvatico, petali di moonflower e note fresche di erbe officinali.`
    };
  }
  if (a.id === 'appearance_gLMMhcPOERIB-Ybzqjywa' || a.name.toLowerCase() === 'hybrid') {
    return {
      ...a,
      name: 'Hybrid',
      description: `Forma licantropica ibrida bipede di Alyssa Douglas Bloodmoon (White Moon Hybrid Shift).
Statura e corporatura: Statura imponente di 185 cm con postura eretta da lupo mannaro bipede, corporatura atletica, muscolosa ma snella e slanciata.
Mantello e pelliccia: Folto mantello serico color castano-caramello che copre interamente il corpo, sfumando sul petto e sul ventre in un luminoso bianco lunare a forma di cuore perfetto. Gorgiera di pelliccia più lunga e vaporosa che avvolge collo e spalle, sfumando nella chioma di pelo castano-caramello lungo la nuca. Grande e maestosa coda castano-caramello con punta nera pronunciata.
Anatomia degli arti e zampe: Struttura a potente conformazione digitigrade con polpastrelli plantari scuri ammortizzanti e artigli ricurvi retrattili in ebano venato d'oro alle zampe inferiori. Zampe anteriori prensili dotate di artigli ricurvi neri venati d'oro; pesante anello con sigillo d'argento della casata Douglas incastonato all'anulare sinistro della zampa e marcatura runica Gebo impressa misticamente tra i fasci di pelo del polso sinistro.
Testa e fisionomia lupina: Cranio da lupo con muso corto armonioso, tartufo nero lucido, labbra scure serrate su dentatura affilata da predatore e folte vibrisse chiare. Singolo paio di orecchie lupine grandi, mobili ed erette sulla cima della testa. Grandi occhi a mandorla color verde menta che conservano espressività e dolcezza umana.
Stato: Priva di indumenti in shift completo; l'anatomia biologica è interamente protetta dalla folta pelliccia.`
    };
  }
  if (a.id === 'appearance_9ea9ur0IXwhQPcO_yb9CB' || a.name.toLowerCase().includes('shift')) {
    return {
      ...a,
      name: 'full-shift',
      description: `Forma lupina ancestrale quadrupede completa (Hvit, la Luna Bianca dei Douglas).
Statura e proporzioni: Enorme lupo dire wolf quadrupede di proporzioni superiori alla norma, maestoso, agile e imponente, con garrese alto e portamento fiero.
Mantello e colorazione: Doppio mantello fitto, soffice e lucido di colore castano-caramello caldo lungo il dorso, il collo e la parte superiore dei fianchi, che degrada gradualmente in bianco lunare immacolato e luminescente sul muso, sul petto (distinta marcatura a cuore) e sul ventre. Sulla groppa posteriore sinistra spicca una nitida marcatura di pelo bianco a forma di luna crescente (Segno di Mani). Coda lupina foltissima, lunga e vaporosa con punta d'ebano nero netto.
Anatomia e zampe: Quattro zampe robuste da lupo con cuscinetti plantari soffici e resistenti, unghie nere affilate. Passo potente e felpato. Pesante anello con sigillo d'argento della casata Douglas assicurato a un sottile cordino di cuoio scuro intrecciato, annodato alla base del collo e parzialmente sepolto nella foltissima gorgiera di pelo bianco del petto.
Testa e sensi: Fisionomia interamente lupina. Muso allungato con tartufo umido nero carbone, dentatura affilata con canini pronunciati ma priva di ferinità minacciosa. Orecchie lupine grandi, spesse e foderate di morbido pelo bianco all'interno, sempre all'erta e mobili in cima al cranio. Grandi occhi a mandorla color verde menta limpido, intelligenti ed empatici.
Stato: Forma lupina naturale protetta dal fitto doppio mantello serico.`
    };
  }
  return a;
});

// 2. Prepare updated outfits (only hybrid and fullshift streamlined; all other 16 outfits untouched)
const updatedOutfits = original.outfits.map(o => {
  if (o.id === 'outfit_nPERIvpkjbT9anBosZYMJ' || o.name.toLowerCase() === 'hybrid') {
    return {
      ...o,
      description: `Assetto visivo: Avatar e portamento visivo di Alyssa nella sua forma ibrida bipede da lupo mannaro (Hvit).
Abbigliamento: Nessun capo di vestiario né indumento indosso; vesti civili rimosse o lacerate durante la trasformazione licantropica.
Accessori e dettagli visivi: Portamento eretto vigile ed empatico; sigillo d'argento Douglas incastonato all'anulare della zampa sinistra e marcatura runica Gebo visibile tra il pelo del polso. Sguardo verde menta caldo ed espressivo.`
    };
  }
  if (o.id === 'outfit_s0b5DFsbIKbNQibgsOV8v' || o.name.toLowerCase() === 'fullshift') {
    return {
      ...o,
      description: `Assetto visivo: Avatar e portamento visivo del maestoso lupo bianco e caramello Hvit a quattro zampe.
Abbigliamento: Nessun vestito; forma lupina quadrupede naturale protetta dal doppio mantello.
Accessori e dettagli visivi: Cordino di cuoio scuro con l'anello con sigillo d'argento Douglas annodato al collo tra il pelo bianco della gorgiera del petto; portamento calmo, fiero e vigile.`
    };
  }
  return o;
});

// 3. Prepare harmonized description header
const lines = original.description.split('\n');
const newHeader = `[NAME: Alyssa Douglas Bloodmoon; ALIASES: Lys, Little Moon, Sunflower, The White Moon, The Anchor; AGE: 19 (Born April 22, 2005); GENDER: Female (She/Her); SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Dominant Omega (White Moon); HOUSE: Bloodmoon and Douglas; PACK: Seven Hills; SOCIAL_STATUS: Citizen, Core of Villa Douglas compound, Guild Member; OCCUPATION: 1st-year undergrad (SUCC) Pre-Med, Novice Healing Mage, Botanist, Field Medic in the Guild, Pack Mom designate (inheriting office from Elizabeth Duskwood at 21); HEIGHT: 155cm (5'1"); BUILD: Petite hourglass frame (Bust: 95cm, Waist: 55cm, Hips: 95cm); HAIR: Caramel-chestnut waves to the tailbone; EYES: Mint-green doe eyes; FEATURES: Luminous skin, crescent moon birthmark on left hip (Mark of Mani), shared Gebo tattoo on left wrist with Jasper, pierced belly button and ears; SHIFTS: Active physical form defined by Appearance (Base, Hybrid, full-shift); SCENT: Wild honey, moonflower, and medicinal herbs]`;
lines[0] = newHeader;
const updatedDescription = lines.join('\n');

const payload = {
  appearances: updatedAppearances,
  outfits: updatedOutfits,
  description: updatedDescription,
  default_appearance: original.default_appearance || 'appearance_6_pa6kZ9BzwLC05qO5Fuk',
  default_outfit: original.default_outfit || 'outfit_UT8FhemAi1PDZeh0Q11wC'
};

fs.writeFileSync('scratch/alyssa_persona_payload.json', JSON.stringify(payload, null, 2));
console.log('Payload generated successfully:');
console.log('Appearances count:', payload.appearances.length);
payload.appearances.forEach(a => console.log(' - ' + a.name + ': ' + a.description.length + ' chars'));
console.log('Outfits count:', payload.outfits.length);
console.log('Hybrid outfit desc len:', payload.outfits.find(o => o.name === 'hybrid').description.length);
console.log('Fullshift outfit desc len:', payload.outfits.find(o => o.name === 'fullshift').description.length);
console.log('Description total len:', payload.description.length);
