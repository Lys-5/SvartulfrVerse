# Regola 03 — Outfits, Accessori, Coerenza Visiva & Stile Definitivo Argon / Gemini

## 1. Evitare Oggetti e Tratti "Sempre Visibili"

*Lezione empirica:* Qualunque accessorio o tratto scritto come "always on" o "never removed" nella description (es. le bende di Malachia, i tatuaggi di Logan, catena/anello/occhiali di Erik) induce l'LLM in loop rigidi, costringendolo a inserire l'elemento anche in scene prive di senso (piscina, doccia, cene formali, situazioni intime).

**Regola operativa:** Se un elemento visivo o un accessorio non è strutturalmente fuso con il corpo del personaggio, non deve essere descritto come costante. Adottare una delle due opzioni (in ordine di priorità):

1. **Sistema Outfit Nativo di Wyvern (Soluzione preferita):** Utilizzare la sezione *Appearance & Outfits* configurando outfit distinti e contestuali (es. Allenamento, Casa/Casual, Formale, Tattico, Notturno, Hybrid Shift, Full Shift, Nude).
2. **Descrizione Contestuale:** Se il sistema Outfit non è ancora popolato per quella card, specificare il tratto come strettamente contestuale nella prosa della description:
   > *"X indossa Y solo quando si trova in Z; in altri contesti non è presente."*

**Eccezione Ammessa:** Un tratto può restare costante se e solo se la sua costanza è l'essenza stessa dell'identità del personaggio e la scheda lo dichiara apertamente (es. il cappuccio di Dullahan non scende mai, in nessun contesto, costituendo il fulcro della sua identità). In tal caso va dichiarato costante e ribadito in tutti gli outfit.

---

## 2. Coerenza Visiva della Famiglia Douglas

Scelta stilistica canonica approvata: i maschi della famiglia Douglas condividono un "family look" riconoscibile nelle generazioni e nei prompt visivi:
- Capelli scuri, lunghi e arruffati (o sfumati con precisione sulle tempie come nel taglio militare di Malachia) per accomodare le orecchie da lupo del Partial Shift e coprire totalmente la zona temporale umana;
- Palette calda al tramonto e sfondo/ambientazione di Blackwood City (palme, architettura costiera, legno di cedro, mogano, pietra e luci calde);
- Struttura facciale affine e marcata ("The Douglas Face", con l'eccezione di Noah che eredita i colori oro/zaffiro Bloodmoon).

*Nota:* Mantenere comunque elementi distintivi propri per ciascun membro (motivi e stile dei tatuaggi tribali/runici, cicatrici, accessori contestuali, tonalità degli occhi).

---

## 3. Anatomia Demi-Umani: Tassonomia a 31 Specie (SopakcoSauce / WyvernChat), Orecchie Singole & Invarianti Rigorose (Sierra & Scarlett)

Il progetto adotta come benchmark e standard tassonomico vincolante la **Classificazione Ufficiale a 31 Categorie per Specie Non-Umane** di WyvernChat / SopakcoSauce Docs, archiviata integralmente in [knowledge/External_References/SOPAKCOSAUCE_NON_HUMAN_CHARACTER_TEMPLATES.md](knowledge/External_References/SOPAKCOSAUCE_NON_HUMAN_CHARACTER_TEMPLATES.md).

**I demi-umani e le entità non-umane ereditano esclusivamente i tratti biologici, locomotori e sensoriali della specifica classe animale di appartenenza, conformemente ai rispettivi template PList/SBF:**
- **Mammiferi (Lupi, Cani, Gatti, Orsi, Bovini, Roditori):** possiedono un solo paio di orecchie, quelle animali della loro specie sulla sommità del capo (lupine/canine, feline, bovine orizzontali con morbida peluria, orse arrotondate), e la rispettiva coda. Non hanno orecchie umane aggiuntive ai lati della testa.
- **Rettili, Lamie & Naga (es. Sierra Cruz):** **DIVIETO ASSOLUTO DI ORECCHIE MAMMIFERE/LUPINE O PELLICCIA.** Mappatura sul template `lamia_naga`: i serpenti e i rettili non possiedono padiglioni auricolari esterni da mammifero. L'apparato uditivo è rettiliano: membrana timpanica liscia integrata nelle squame o creste/alette sensoriali squamate lisce prive di pelo lungo le tempie, capaci di percepire vibrazioni del suolo e risonanze termiche/acustiche. È tassativamente vietato descrivere orecchie da lupo o ciuffi di pelo su Sierra.
- **Acquatici & Cefalopodi (es. Prof. Moreau):** Mappatura su `merfolk` / `anthro`: tentacoli lombari, pelle screziata, branchie vestigiali, privi di padiglioni auricolari esterni mammiferi.
- **Pure Positive Framing nei Testi Narrativi:** È tassativamente vietato inserire frasi negative di diniego anatomico (*"no human ears"*, *"senza orecchie umane"*, *"prive di orecchie ai lati"*) all'interno di schede JED+, lorebook, greeting, outfits o scenari. L'anatomia va descritta unicamente in termini positivi (*"singolo paio di orecchie da lupo tra i capelli"*, *"fessure uditive rettiliane squamate lungo le tempie"*). La clausola negativa `No orecchie umane` è riservata esclusivamente ai prompt tecnici di generazione visiva Imagen.
- **Positive Framing per Personaggi a Base Umana:** Per personaggi umani o mortali shifters, non descrivere mai l'assenza di tratti animali né affermare negativamente o ridondantemente che hanno orecchie o corporatura umane. I tratti umani si esprimono naturalmente attraverso la fisionomia ordinaria, evitando formule come `100% human`, `ordinary human ears` o `interamente umana`.
- **Minotauri & Centauri:** Mappatura su `minotaurs` (busto umanoide, testa di toro con corna robuste, zoccoli, labirinto) e `centaurs` (busto umanoide su corpo equino quadrupede a 4 zampe, locomozione al galoppo, coda equina). Mai attribuire zampe equine a minotauri o corpi bovini a centauri.
- **Succubi & Incubi (es. Scarlett Rose, Father Revazhael):** Mappatura su `succubus_incubus`: corna (scarlatte o d'ebano), ali membranose/da pipistrello, coda prensile con punta a picca, nutrizione erotica/emotiva consensuale.
- **Sierra Cruz (Lamia — Locomozione, Livrea & Rigore Serpentine):**
  - Possiede **capelli color arcobaleno**, occhi rosa confetto con pupille verticali a fessura, lingua biforcuta, fossette termosensibili (pit organs), zanne velenifere retrattili, e membrana timpanica liscia/creste sensoriali squamate lungo le tempie (**zero orecchie da lupo o da mammifero**).
  - Dai fianchi in giù, la parte inferiore del corpo è interamente quella di un serpente di 4 metri **color arcobaleno con scaglie iridescenti** (`rainbow-colored hair` e `4-meter rainbow-colored serpentine tail covered in shimmering iridescent scales`).
  - **Divieto Assoluto di Termini Bipedi:** Non possiede gambe né piedi. È tassativamente vietato usare per Sierra termini o verbi come *gambe*, *piedi*, *ginocchia*, *scarpe*, *pantaloni*, *camminare* o *fare passi* (`legs`, `feet`, `knees`, `shoes`, `walk`, `step`, `stand on feet`). Sierra si muove esclusivamente strisciando, scivolando e avvolgendosi sulle sue spire (`slithers`, `glides`, `coils`).
- **Scarlett Rose (Succubus — Palette Rosa Confetto & Corna Scarlatte):**
  - Possiede **capelli rosa confetto** (`candy-pink`), **occhi rosa confetto** abbinati e **due corna scarlatte** che spuntano visibilmente tra i capelli sopra le tempie, oltre alle ali scure da succubus e alla coda prensile con punta a picca.
- **Marchi Divini dei Gemelli (Mani & Sol) & Distinzione Titoli Cosmici (Maniulfr vs Solulfr):** I marchi celestiali risiedono **esclusivamente sulle anche**: Alyssa porta il Marchio Runico di Máni (mezzaluna argentata con glifi lunari sub-dermici) **unicamente sull'anca sinistra**; Jasper porta il Marchio Runico di Sól (sole nero radioso con glifi fiammeggianti sub-dermici) **unicamente sull'anca destra**. È vietato disperdere marchi multipli su mani, petto, nuca, clavicola o cuore (condividono soltanto la Runa di Nascita **Mannaz** `ᛗ` a inchiostro di ferro freddo sul polso sinistro, secondo il calendario runico Elder Futhark per data di nascita: Gemelli 22 apr = `Mannaz`, Erik 31 ott = `Hagalaz`, Noah 5 ott = `Gebo`, Edric 25 feb = `Sowilo`, Wulfnic 21 dic = `Jera`, Elizabeth 14 lug = `Uruz`, Malachia 10 ago = `Thurisaz`, Logan 12 gen = `Eihwaz`). Inoltre, il titolo sacro **Sólúlfr** (Lupo del Sole) appartiene **esclusivamente a Svartr (Jasper)**; per Hvít (Alyssa) il titolo divino correlato a Máni è **Mániúlfr** (Maniulf / Lupo della Luna Bianca).

---

## 4. Stile Visivo Definitivo Argon / Gemini (Workflow Ufficiale di Progetto)

Tutte le immagini dei personaggi, delle Personas e dei relativi Outfit sono generate con il workflow **Argon (Visual Anchor `<IMAGE_0>`) + Gemini Imagen**, codificato dalle sessioni ufficiali (`699ca946550ec63b` e `cacb36df583d0db9`).

### A. Ancora Biometrica (`<IMAGE_0>`)
Ogni personaggio parte da un ritratto/figura base creato con **Argon** (`<IMAGE_0>`) che fissa in modo immutabile:
- Fisionomia del volto, cicatrici, barba/rasatura e colore degli occhi;
- Altezza e proporzioni muscolari;
- Colore, forma e posizione delle due orecchie da lupo sulla sommità del capo e della coda da lupo.

### B. Schema Input Utente e Formato JED+ v2.0 Multiline PList a 6 Sezioni Fisse (Italiano)
Ogni descrizione di outfit o appearance (su Character Card `/mine`, World Characters e User Personas) adotta obbligatoriamente lo **Schema JED+ v2.0 Multiline PList** (una chiave `UPPERCASE_KEY: valore;` per riga dentro parentesi quadre `[...]`), con `OUTFIT_NAME` e `SLOT_CONTEXT` seguiti dalle 6 sezioni canoniche:

```text
[OUTFIT_NAME: Nome dell'Outfit;
SLOT_CONTEXT: Casual / Daily | Business / Campus | Gala / Formal | Party / Club | Beach / Terme | Sleep / Nightwear | Nude / Anatomical | Hybrid Shift / Mutation | Full Shift / Beast Form;
ABBIGLIAMENTO: Capi, tessuti, colori e vestibilita' calibrata su altezza in cm e stazza. OBBLIGATORIO per ogni capo inferiore vestito: "con apertura/fessura/asola lombare posteriore personalizzata/rinforzata/sartoriale da cui fuoriesce liberamente la folta coda da lupo [colore]". Per Hybrid Shift: "Nessuno. Forma ibrida bipede di [X] cm ([Y'Z\"]) di altezza...". Per Full Shift: "Nessuno. Forma quadrupede completa da lupo gigante della Founding Bloodline...";
ACCESSORI: Cinture, fondine, armi, occhiali, borse, strumenti, auricolari tattici, o "Nessuno";
SCARPE: Calzature dettagliate, "Piedi nudi...", o "Zampe posteriori digitigradi con cuscinetti neri gommati e artigli...";
GIOIELLI: Anello con sigillo della casata Douglas, torque, bracciali di giuramento, orologi, catene e tatuaggi runici/tribali visibili (es. Thurisaz per Malachia, Gebo per Noah, Mannaz per Alyssa e Jasper, Hagalaz per Erik, Eihwaz per Logan, Sowilo per Edric, Jera per Wulfnic, Uruz per Elizabeth sul polso sinistro; oppure rune sub-dermiche bioluminescenti in forma Hybrid Shift);
TRUCCO: Espressione facciale, texture della pelle (sudore, olio d'officina, cicatrici), lunghezza barba/rasatura, colore occhi, zanne/muso in forma mutata;
ACCONCIATURA: Colore, taglio, prodotto di styling, copertura completa della zona temporale umana e postura delle "Orecchie lupine singole [colore]" sulla sommita' del capo]
```

**Vincolo Altezze Canoniche negli Outfits:** Ogni riferimento all'altezza in `ABBIGLIAMENTO:` deve rispettare tassativamente la matrice canonica (`Alyssa = 155 cm / 5'1"`, `Edric = 158 cm`, `Zefir = 178 cm`, `Jasper = 193 cm`, `Noah = 197 cm`, `Logan = 198 cm`, `Mac = 204 cm`, `Malachia = 208 cm`, `Erik = 213 cm`, `Wulfnic = 220 cm`, `Ut = 240 cm`). È vietato attribuire ad Alyssa `165 cm` o altezze diverse da `155 cm`.

### C. Formula Prompt Interno di Generazione (Pittura Digitale Semi-Realistica Argon)
1. **Medium ed Estetica:** *"Un'illustrazione digitale a figura intera, in stile pittura semi-realistica e ricca di dettagli"* (oppure *"Fotografia naturalistica, con grana naturale e dettagli nitidi"*), con enfasi sulle trame materiche (lana grezza, pelle di cervo, lino, cotone, metallo battuto), profondità di campo ridotta (*sfondo sfocato*) e illuminazione atmosferica calda o notturna.
2. **Inquadratura e Posa:** Sempre **a figura intera (`a figura intera`)**, ad altezza occhi, in posa frontale di tre quarti o di spalle di tre quarti mentre guarda sopra la spalla (per mostrare simultaneamente il volto/petto e l'uscita della coda dall'asola lombare posteriore dei pantaloni).
3. **Blindatura Anti-Orecchie Umane & Regola Auricolare:**
   - Includere sempre: *"La zona laterale della testa, dove si troverebbero le orecchie umane, è interamente e fittamente coperta dai capelli / dalle trecce / dalle basette, garantendo che non vi sia alcuna orecchia o traccia di anatomia umana visibile."*
   - Quando un personaggio indossa un auricolare radio di sicurezza (es. Malachia), il tubicino acustico trasparente sale dietro la nuca e **si innesta direttamente alla base dell'orecchia lupina sulla sommità del capo**, mai sulla tempia umana.
4. **Clausola Negativa Finale Obbligatoria:**
   `No orecchie umane. No auricolari [se non previsti]. No modifiche alle orecchie da lupo o alla coda, coerenti con <IMAGE_0>.`

---

## 5. Standard Minimo 9 Outfits per Scheda Personaggio

Ogni character card redatta o aggiornata nel repository deve includere nel campo `outfits` **un minimo assoluto di 9 outfit contestuali**, strutturati rigorosamente secondo lo schema a 6 sezioni (Abbigliamento, Accessori, Scarpe, Gioielli, Trucco, Acconciatura) con apertura lombare rinforzata per la coda:

1. **`casual`**: Abbigliamento quotidiano, relax a casa, abiti da strada/tempo libero informale.
2. **`business / campus`**: Abbigliamento per frequenza accademica (campus SUCC) o abito professionale/aziendale di rappresentanza (ufficio, lavoro, cancelleria).
3. **`gala / formal`**: Abito di alta sartoria per cene di casata, ricevimenti solenni, galà ufficiali o cerimonie di branco.
4. **`party / club`**: Nightlife, serate in discoteca o lounge bar esclusivi (es. The Verve, Solarton club scene).
5. **`beach / terme`**: Costume da bagno, costume termale o abbigliamento balneare da sorgente calda/spiaggia/piscina della tenuta.
6. **`sleep`**: Abbigliamento da notte, pigiama leggero, boxer o intimo per dormire.
7. **`nude`**: Nudo completo anatomico, con descrizione canonica e rigorosa di corporatura, cicatrici, genitali e tatuaggi/rune sub-dermiche.
8. **`hybrid shift / mutation`**: Forma ibrida bipede da combattimento (per licantropi LSE: Hybrid Shift mastodontico con pelliccia, muso allungato e artigli; per altre razze/mutanti: forma da battaglia o mutazione parziale).
9. **`full shift / other`**: Forma bestiale integrale a quattro zampe (per shifters: lupo gigante ancestrale; per non-shifters: uniforme operativa da campo specialistica o forma secondaria).

---

## 5. Sfondi per Fascia Oraria (Time of Day Backgrounds) e Tag Regista
- **4 Periodi Canonici:** Le Location supportano immagini differenziate per `dawn`, `day`, `dusk` e `night`.
- **Tag di Scena `[bg: LocationName]`:** Nella narrazione di Game Master, Assistant e bot in Visual Novel Mode, il cambio di scena deve utilizzare il tag `[bg: Nome Location]` (es. `[bg: Campus Suite Moonflower]`). L'engine di Wyvern sincronizza automaticamente lo sfondo con l'ora calcolata dall'AI Time Tracking senza forzature manuali.
