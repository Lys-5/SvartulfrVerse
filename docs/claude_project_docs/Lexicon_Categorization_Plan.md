---
Piano di ricategorizzazione Lexicon — creato 30/08/2026 (notte)
**Steps 1-3 ESEGUITI ED ESITO CONFERMATO il 30/08/2026 (notte, sessione successiva).** Tutte e 3 le
correzioni Global Entry sono state applicate direttamente sulla piattaforma live Wyvern e salvate con
successo. Anche le 6 nuove Lexicon entries "interazioni digitali/social" (vedi
`claude/Pending_Lexicon_Drafts_Digital_Social.md`) sono state create con successo nella stessa sessione.
Il mirror locale `D:\SvartulfrVerse\Wyvern\lexicon\by_folder\` è stato aggiornato di conseguenza.
---

## 0. Perché questo documento

Le guide ufficiali (`wiki.wyvern.chat/Advanced/Lexicon` e `wiki.wyvern.chat/Features/Worlds/Lexicon`)
sono state lette con successo tramite il browser pane dell'utente (sessione autenticata, non bloccata
da bot detection) in una sessione successiva a quella in cui è stato scritto questo piano — vedi la
nota metodologica più sotto. Il piano originale si basava solo su osservazione diretta in-app.

**CONFERMATO dalla wiki ufficiale**: "Global ON (default): the entry participates in the world-wide
keyword scan... Global OFF: the entry is invisible to keyword scanning. It will never activate on its
own... It can only appear if you explicitly add it to a location or environment's Included Lexicon
list." Questo ha confermato l'ipotesi di rischio per le 3 entry sotto e giustificato la correzione a
Global Entry: Yes invece di un collegamento esplicito a Included Lexicon (scelta più semplice e
comunque corretta dato che tutte e 3 sono concetti/eventi rilevanti ovunque nel World).

## 1. Verifiche prioritarie — ESEGUITE, TUTTE E 3 CORRETTE E CONFERMATE SALVATE

| # | Entry | Type | Esito |
|---|---|---|---|
| 10 | Il Viaggio di Wulfnic in America | MEMORY | Global Entry impostato a Yes. Salvato e confermato. |
| 11 | La Guerra di Fenris e l'Esilio dei Firstborn | EVENT | Global Entry impostato a Yes. Salvato e confermato. |
| 12 | Douglas Commercial Coalition (DCC) | CONCEPT | Global Entry impostato a Yes. Salvato e confermato. |

Mirror locale aggiornato in `Wyvern/lexicon/by_folder/HISTORY.md` (#10, #11) e
`Wyvern/lexicon/by_folder/JOB_AND_BUSINESS.md` (#12), con nota della correzione e data.

## 2. Audit di tipizzazione — tutte le 39 entry originarie (invariato, confermato corretto)

- **MEMORY** (16), **CREATURE** (4), **EVENT** (3), **ITEM** (1), **CONCEPT** (13), **LOCATION** (2).
  Totale: 39. Nessuna modifica necessaria oltre ai 3 fix Global Entry sopra.

Da questa base, +6 nuove entry create nella sessione successiva (Digital Interactions Chase/Jasper/
Iordan come MEMORY, SUCCbook/Pack-Family/Texting Styles come CONCEPT) portano il totale a **45**.

## 3. Miglioramento opzionale (non eseguito in questo giro): Solarton Locations / Campus Locations

Resta un task a parte, non incluso in questo giro. Le due entry Lexicon type Location (liste di luoghi
in prosa) restano candidate per la conversione in Location native separate (Regola #7 del progetto),
da valutare insieme a Lys quando si riprende il lavoro Location generale.

## 4. Checklist di esecuzione — AGGIORNATA

1. ~~Aprire "Il Viaggio di Wulfnic in America" (Lexicon), verificare/impostare Attached Character~~ →
   Non necessario: il fix corretto era Global Entry = Yes (confermato dalla wiki), non Attached Character.
   **FATTO.**
2. ~~Aprire "La Guerra di Fenris e l'Esilio dei Firstborn" (Lexicon)~~ → Global Entry = Yes. **FATTO.**
3. ~~Stesso controllo per "Douglas Commercial Coalition (DCC)"~~ → Global Entry = Yes. **FATTO.**
4. (Opzionale, task a parte) Discutere con Lys se e quando convertire Solarton Locations/Campus
   Locations in Location native. **NON ANCORA FATTO, bassa priorità.**
5. ~~Aggiornare `Wyvern/lexicon/by_folder/` in locale con eventuali modifiche fatte~~ → **FATTO**,
   inclusi i 3 fix Global Entry, le 6 nuove entry, lo spostamento manuale delle 4 entry
   Uncategorized→Chars Details fatto da Lys, e l'aggiornamento dell'entry Jasper (nome d'arte
   DJ Frequency + sezione SoundCloud/Spotify).

## 5. Task rimasti aperti (bassa priorità)

- Position field hygiene check: la wiki conferma le opzioni Before Char / After Char / In Chat; la UI
  live mostra "Before Core Prompt" per le entry ispezionate finora. Da confermare che tutte le 45 entry
  abbiano un Position coerente col loro scopo (nessuna verifica sistematica ancora fatta).
- Conversione Solarton Locations/Campus Locations in Location native (vedi §3).
