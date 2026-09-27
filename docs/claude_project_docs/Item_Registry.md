# Registro Item, Inventari e Marketplace

**Documento vivo.** Si riempie man mano che si lavorano i personaggi. **L'esecuzione su Wyvern è rimandata a fine lavori sui PNG**, perché è flavor e non blocca niente.

Ogni nuovo personaggio lavorato aggiunge una riga alla tabella inventari e, se serve, righe alle tabelle degli oggetti da creare.

---

## Legenda stato

| Simbolo | Significato |
|---|---|
| ✅ | Esiste già su Wyvern |
| ⬜ | Da creare |

---

## Meccanica verificata

| Dove | Cosa |
|---|---|
| **Character → Default Inventory → Add Item** | Il picker pesca dal Lexicon **solo i tipi `Item` e `Vehicle`**. Creature e Furniture non compaiono qui. |
| **Lexicon → Entry Type** | No specific type, NPC/Generic Character, Mob, **Creature**, Move, **Item**, **Furniture**, Job, **Vehicle**, Location, Event, Concept, Memory, Other. |
| **Lexicon → ITEM PROPERTIES** | Sale price + valuta, buy-back rate, Stackable, Consumable, Tradeable, Max Stack, Weight, Equip Slot, Rarity, Key Item, Teaches Move, Flags, Effects. |
| **Location → Simulation Overrides** | Enable Marketplace, sell rate multiplier, **Shop Inventory → Add Item**, Purchasable Property, Jobs Offered Here. |

**Non esiste un tipo "Property".** Una proprietà acquistabile è una **Location** con `Purchasable Property` attivo, non una entry Lexicon.

### ⚠️ I combobox richiedono click REALI del mouse

I `[role="combobox"]` non rispondono agli eventi sintetici, nemmeno alla sequenza PointerEvent completa che funziona su bottoni e switch. Il valore sembra impostarsi e poi torna indietro.

**Metodo che funziona:** `find` per ottenere il `ref_N`, poi `computer` con `left_click` su quel ref. Il dropdown non filtra digitando, quindi per le liste lunghe serve `scroll` dentro il dropdown e poi `find` sull'opzione.

**Il `Parent Location` di una Location nuova offre zero opzioni finché la Location non viene salvata almeno una volta.** Prima Save, poi il parent.

### Bug Species/Occupation: confermato, non è colpa dell'automazione

Ri-testato con il metodo del click reale su Finnegan Novak: Species impostata a `Demi-humans`, valore visibile, Save, reload → torna a `None`. È un difetto di piattaforma vero, verificato su quattro personaggi e con entrambi i metodi di click. Da segnalare a Wyvern con l'errore 500 su `linked-characters` e il pulsante Save che si blocca su "Saving...".

---

## ✅ Già fatto — la Location Medusa

Creata come **Location**, non come entry Lexicon. Parent `Bricklane Mall`, Environment `Solarton`, `Enable Marketplace` ON, descrizione 1.738 caratteri.

Negozio di abbigliamento per soprannaturali: vende **il taglio giusto**, non i vestiti. Jeans con la porta per la coda rifinita e rinforzata invece che tagliata con le forbici a casa, giacche con i pannelli posteriori divisi per l'apertura alare, cappelli con i fori per le corna, scarpe per piedi digitigradi e zoccoli, compression wear che non sfrega sulle squame. Il formale è la fascia cara ed è il motivo per cui il negozio sta in piedi. Sul banco delle modifiche c'è un cartello scritto a mano: WE HAVE SEEN WORSE.

Spiega retroattivamente i jeans di Finn, la maglia di Bailey con la fessura, e il problema di Casey con tre metri di apertura alare.

---

## Oggetti base: a tutti

| Item | Stato |
|---|---|
| Smartphone | ✅ |
| Wallet | ✅ |
| Keys | ✅ |

## Veicoli

Tutti già esistenti, vanno solo agganciati: **Erik's SUV** ✅, **Alyssa's Yellow Beetle** ✅, **Jasper's Porsche** ✅, **Noah's Sedan** ✅, **Malachia's Motorcycle** ✅, **Logan's Harley** ✅, **Wulfnic's Rolls-Royce** ✅.

⬜ Da creare quando serviranno: veicolo di Nikolaj (se ne ha uno), auto di Loewe.

---

## Item firma — senza prezzo, `Key Item` ON

Non vendibili, non perdibili.

| Item | Di chi | Stato |
|---|---|---|
| Douglas Clan Signet Ring | Erik, e Alyssa lo porta al collo | ⬜ |
| Erik's Gold Chain | Erik | ⬜ |
| Erik's Patek Philippe | Erik, lo tamburella quando è teso | ⬜ |
| Magnus's Pocket Watch | Magnus III | ⬜ |
| Magnus's Walking Stick | Magnus III, nessun uso medico | ⬜ |
| Cornelius's Cane | Cornelius | ⬜ |
| Nixara's Knife | Nixara, non se lo toglieva mai | ⬜ |
| Wulfnic's Rune-Carved Axe | Wulfnic | ⬜ |
| Firstborn Tooth Cord | Wulfnic | ⬜ |
| Logan's Coin Pendant | Logan | ⬜ |
| Logan's Leather Cuff | Logan | ⬜ |
| KSA Signet Ring | Noah | ⬜ |
| Noah's Watch | Noah, ci gioca quando mente | ⬜ |
| Jasper's Slicing Smartwatch | Jasper | ⬜ |
| Alyssa's Crescent Belly Ring | Alyssa | ⬜ |
| Malachia's Hand Wraps | Malachia | ⬜ |
| Kaladin's Sidearm | Kaladin | ⬜ |
| Kaladin's Earpiece | Kaladin | ⬜ |
| Ut's Warhammer | Ut | ✅ |
| Ut's Forge Hammer | Ut, distinto dal precedente | ⬜ |
| Ut's Heavy Gloves | Ut, li ignora quasi sempre | ⬜ |
| Zefir's Blade | Zefir | ✅ |
| Loewe's Antique Wristwatch | Loewe, caricato a mano ogni mattina | ⬜ |
| Nikolaj's Competition Rifle | Nikolaj | ⬜ |
| Nikolaj's Surgical Mask | Nikolaj, non se la toglie mai | ⬜ |
| Nikolaj's Notebook | Nikolaj, calligrafia illeggibile | ⬜ |
| Casey's Camera | Casey, gli pende sempre al collo | ⬜ |
| Casey's Long Lens | Casey | ⬜ |
| Casey's Polaroid | Casey | ⬜ |
| Stan's Dog Collar | Stanley Jr. | ⬜ |
| Stan's Father's Dogtags | Stanley Jr. | ⬜ |
| Hank's Whistle | Hank | ⬜ |

## Item comprabili — con prezzo e negozio

| Item | Prezzo | Dove | Stato |
|---|---|---|---|
| Designer Sunglasses | $320 | Medusa, Paradise | ⬜ |
| Straw Tote Bag | $45 | Medusa | ⬜ |
| Nesting Blanket | $60 | Medusa, Bricklane Mall | ⬜ |
| SUCC Letterman Jacket | $180 | Medusa, Lunar Quad | ⬜ |
| Noise-Cancelling Headphones | $350 | Bricklane Mall, Lunar Quad | ⬜ |
| Wireless Earbuds | $150 | Bricklane Mall | ✅ |
| Laptop | $1.400 | Bricklane Mall, Lunar Quad | ⬜ |
| Laptop Bag | $90 | Bricklane Mall, Lunar Quad | ⬜ |
| USB Drive | $25 | Lunar Quad | ⬜ |
| Drawing Tablet | $700 | Bricklane Mall | ⬜ |
| Game Controller | $70 | Bricklane Mall | ⬜ |
| Camera Bag | $120 | Bricklane Mall | ⬜ |
| Reading Glasses | $180 | Bricklane Mall | ⬜ |
| Ice Skates | $280 | Bricklane Mall, Lunar Quad | ⬜ |
| Hockey Stick | $250 | Lunar Quad | ⬜ |
| Gym Bag | $60 | Lunar Quad, Bricklane Mall | ⬜ |
| Mouthguard | $12 | Lunar Quad | ⬜ |
| Scrubs | $55 | Lunar Quad | ⬜ |
| Whistle | $15 | Lunar Quad | ⬜ |
| Body Spray | $9 | Bricklane Mall | ⬜ |
| Lighter | — | Bricklane Mall, Sidewinders | ✅ |
| Cigarettes | $12 | Bricklane Mall, Sidewinders | ⬜ |
| Energy Drink | $4 | Lunar Quad, The Verve | ⬜ |
| Diet Coke | $3 | Lunar Quad, The Verve, Bricklane Mall | ⬜ |
| Coffee | $5 | Lunar Quad, The Verve | ⬜ |
| Tea | $4 | Lunar Quad | ⬜ |
| Beer | $8 | The Verve, Sidewinders | ⬜ |
| Cigar | $28 | Paradise | ⬜ |

Consumabili con `Consumable` + `Stackable` ON: Energy Drink, Diet Coke, Coffee, Tea, Beer, Cigarettes, Cigar, Mouthguard.

## Creature — tipo `Creature`

| Nome | Di chi | Stato |
|---|---|---|
| Diana | Gatta di Richard Loewe. Governa lei la casa sulle colline. | ⬜ |

## Furniture — tipo `Furniture`

Nessuna ancora identificata. Candidate future: l'attrezzatura DJ di Jasper, le rastrelliere server, la poltrona di Loewe.

---

## Mappatura inventari

### FAMILY

| Personaggio | Inventario |
|---|---|
| Erik Douglas | Smartphone, Wallet, Keys, Erik's SUV, Douglas Clan Signet Ring, Erik's Gold Chain, Erik's Patek Philippe, Designer Sunglasses |
| Alyssa | Smartphone, Wallet, Keys, Alyssa's Yellow Beetle, Douglas Clan Signet Ring, Crescent Belly Ring, Nesting Blanket, Straw Tote Bag |
| Jasper | Smartphone, Wallet, Keys, Jasper's Porsche, Laptop, Laptop Bag, Noise-Cancelling Headphones, Wireless Earbuds, Slicing Smartwatch, USB Drive, Energy Drink |
| Noah | Smartphone, Wallet, Keys, Noah's Sedan, KSA Signet Ring, Noah's Watch, Designer Sunglasses, Ice Skates |
| Malachia | Smartphone, Wallet, Keys, Malachia's Motorcycle, Hand Wraps |
| Logan | Smartphone, Wallet, Keys, Logan's Harley, Lighter, Cigarettes, Coin Pendant, Leather Cuff |
| Edric | Smartphone, Wallet, Keys, Designer Sunglasses |
| Magnus III | Pocket Watch, Walking Stick, Douglas Clan Signet Ring, Reading Glasses, Wallet |
| Elizabeth Duskwood | Smartphone, Wallet, Keys — **la sua scheda non cita un solo oggetto, servono indicazioni** |
| Cornelius | Cornelius's Cane, Pocket Watch |
| Nixara | Nixara's Knife |
| Wulfnic | Wulfnic's Rolls-Royce, Rune-Carved Axe, Firstborn Tooth Cord |

### PACK

| Personaggio | Inventario |
|---|---|
| Ut Berg | Ut's Warhammer, Ut's Forge Hammer, Heavy Gloves |
| Zefir Hvitskog | Zefir's Blade, Smartphone |
| Kaladin Nargathon | Smartphone, Wallet, Keys, Sidearm, Earpiece |
| Marcus Thornfield | Smartphone, Wallet, Keys, Designer Sunglasses |

### NPC lavorati

| Personaggio | Inventario |
|---|---|
| Finnegan Novak | Smartphone, Wallet, Keys, Hockey Stick, Ice Skates, Gym Bag, Mouthguard, SUCC Letterman Jacket |
| Bailey Rogers | Smartphone, Wallet, Keys, Gym Bag, Game Controller, Body Spray |
| Richard Loewe | Smartphone, Wallet, Keys, Antique Wristwatch, Reading Glasses, Cigar, Tea, **Diana** (creature) |
| Iordan R. Vess | Smartphone, Keys, Laptop, Noise-Cancelling Headphones, Diet Coke, Game Controller |
| Casey Williams | Smartphone, Wallet, Keys, Casey's Camera, Long Lens, Polaroid, Camera Bag |
| Nikolaj Jökull | Smartphone, Keys, Competition Rifle, Surgical Mask, Notebook |
| Jared Thompson | Smartphone, Wallet, Keys, Gym Bag, SUCC Letterman Jacket |
| Janice Thompson | Smartphone, Wallet, Keys, Laptop, Laptop Bag |
| Stanley Davies Jr. | Smartphone, Wallet, Keys, Drawing Tablet, Dog Collar, Father's Dogtags, Lighter, Game Controller |
| Hank Thompson | Smartphone, Wallet, Keys, Whistle, Gym Bag |
| Jasmin Thompson | Smartphone, Wallet, Keys |
| Stanley Davies Sr. | Smartphone, Wallet, Keys, Reading Glasses |
| Eris Davies | Smartphone, Wallet, Keys |

---

## Da fare quando si esegue

1. Creare le entry Lexicon mancanti, con il protocollo anti-overwrite: reload completo prima di ognuna, verifica del contatore N+1 **e** del nome nella lista enumerata. Il tipo va scelto con un **click reale**.
2. Popolare i Default Inventory dei personaggi.
3. Attivare `Enable Marketplace` e riempire lo `Shop Inventory` di: **Medusa** (già attivo), Bricklane Mall, Lunar Quad, The Verve, Paradise, Sidewinders.

**Costo misurato:** circa 8 chiamate per entry Lexicon. Con 50+ entry, 29 inventari e 6 marketplace è un lavoro da spalmare su più sessioni o da spartire.
