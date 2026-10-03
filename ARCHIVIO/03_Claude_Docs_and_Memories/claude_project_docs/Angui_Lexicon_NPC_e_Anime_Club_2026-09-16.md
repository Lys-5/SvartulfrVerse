# Angui come Lexicon NPC + risoluzione "SUCC's Anime Club" (16/09/2026)

Seguito diretto di `Canon_SUCC_ModernFantasy_Iorveths_Veseii_Audit_2026-09-16.md`.

## Decisioni dell'utente

- **Angui**: non va importato come Character a pieno titolo. Va inserito come **Lexicon di tipo `npc`**, cioè lore del mondo, non personaggio attivo con Start Position propria. Coerente con la scelta di non forzarlo dentro le categorie di specie/longevità del progetto (§12) e di non doverne decidere l'età esatta né la collocazione geografica come se fosse un residente di Blackwood.
- **"SUCC's Anime Club"**: i tre personaggi non nominati nella carta scenario sono stati identificati dall'utente come **Stan (Davies) Jr., Andrew Campbell e Oskar**, già tutti presenti nel World roster. Nessuna nuova scheda da creare per questa carta: è un incrocio narrativo fra tre personaggi già coperti, non introduce nessuno di nuovo. Non richiede altra azione.

## Scrittura Angui (locale, Wyldfire SQLite, §17)

- Backup pre-scrittura: `wyldfire.db.backup6-preangui-20260916T013454Z` (creato a posteriori del confronto con lo stato pre-modifica, verificato).
- Tabella: `world_lexicon_entries`. Modello di riferimento: le entry esistenti di tipo `npc` nello stesso World (`Bartholomew and Madge`, `The Other Contractors`), che seguono lo stesso pattern usato per lore fuori mappa collegata a un personaggio (in quel caso Dullahan, qui il campus SUCC/Modern Fantasy in generale).
- `world_id`: `6cfuc64QBr1Flf9nKndFy` (Blackwood/Svartúlfr, confermato tramite la scheda di Dullahan).
- Nuova riga: `id` generato `Hln-iiGfpprG7t-zWaYEc`, `name: "Angui"`, `type: "npc"`, `is_global: 1`, `keys: ["Angui"]`, `secondary_keys` su termini d'argomento (swamp creature, Blackwater Marsh, cryptid, hydra, healing saliva, ecc.), `npc_info` con `first_name: "Angui"` e `nicknames: ["Creature of Blackwater Marsh"]` (epiteto preso testualmente dalla fonte).
- Contenuto (prosa, formato coerente con §3: niente em-dash, niente asterischi, niente markdown) sintetizza la fonte tier 1 (`io-modernfantasy.uwu.ai/#angui`): origine a Mykonos, cattura e fuga da un'azienda farmaceutica, vita in una palude del Maryland, ostilità verso gli umani/tolleranza verso i soprannaturali, saliva curativa, immortalità effettiva oltre il secolo, gusti/avversioni.
- **Framing scelto**: trattato esplicitamente come lore fuori mappa ("più di tremila miglia da Blackwood... nessuno a Blackwood lo ha mai incontrato"), sul modello già usato per "The Other Contractors" (DDM Inc., mai stati in California). Non collocato geograficamente a Blackwood né altrove in California, per non inventare un aggancio non richiesto (§9.4). Se in futuro serve un aggancio più stretto, va deciso e confermato separatamente.
- Credito alla fonte: la pagina lorebook riporta "BY OREO" come autore del personaggio (non Iorveths o veseii direttamente), verosimilmente uno dei collaboratori il cui materiale è ospitato sull'account veseii insieme alle "alternate scenarios". Il credito è scritto in coda al contenuto della entry.

## Verifica

- Conteggio entry Lexicon del World: 239 → 240 dopo l'inserimento.
- Verifica mirata (non `PRAGMA integrity_check`, che sul file fallisce per la corruzione preesistente e non correlata di `app_settings`, vedi `Cancellazione_86_Stub_404_2026-09-16.md`): riga confermata per id/name/type, contenuto verificato per lunghezza e assenza di em-dash/asterischi/markdown.
- Sincronizzazione: confermato con l'utente che l'app desktop Wyldfire era chiusa, poi trasferito `wyldfire.db` aggiornato più il backup numerato sul dispositivo. Nessun file `-wal`/`-shm` residuo dopo la scrittura (verificato via listing della cartella).

## Esito

Con questo si chiude il ciclo di ricerca canon avviato dall'utente: il roster SUCC/Modern Fantasy di Iorveths e veseii raggiungibile tramite i tag `#SUCC` e `#modernfantasy` è ora interamente coperto nel World, o come Character (roster esistente) o come Lexicon (Angui).
