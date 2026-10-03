# Roster ufficiale Modern Fantasy: pagine "related" e sistemazione geografica (2026-09-15)

Su indicazione dell'utente, esplorate dal browser locale le tre pagine "related" collegate al roster Modern Fantasy (`io-modernfantasy.uwu.ai`), e applicata la decisione di collocazione geografica per i personaggi canon non ancora nel World.

## Pagine "related" esplorate

- **Supernatural Reserve Forces** (`#srf`): conferma che i quattro membri canon (Mjr. Graham Purcell, Lt. Miles Airhardt, Sgt. Rafael Callaway, Pvt. Kade Leavis) sono gli unici ufficiali. Tutti e quattro già presenti nel World, nessun nuovo personaggio da questa pagina.
- **The Underworld** (`#underworld`): pagina "Connections" con ruoli assegnati ai personaggi del sottobosco criminale: Alistair (Collector), Cato (Henchman), Damien (Private Detective), Everett (Fixer), Gianni (Bodyguard), Ilya (Mercenary), Romeo (Biker), Vasile (Hunter), più Ruaraidh (Leader) e Sully (Driver) sotto "Ballantine Family". Confermano i ruoli già scritti sulle schede esistenti (Damien, Everett, Cato, Alistair, Vasile, Ruaraidh, Sully). **Nota importante**: questa pagina raggruppa insieme, sotto lo stesso tema "Underworld", personaggi che nel nostro World abbiamo già collocato in domini diversi (es. Romeo "Gray" Dean è a Solarton, non Los Angeles), quindi il raggruppamento tematico dell'autore non implica automaticamente stessa città: non è stato usato come prova per rilocare nessuno.
- **Supernatural University of Central California** (SUCC, link esterno a `io-succ.uwu.ai`): dominio Solarton già ampiamente lavorato in sessioni precedenti, non toccato in questo giro (fuori scope per il compito Los Angeles del momento).

## Verifica coincidenza Gianni Luciano / Romeo

Gianni Luciano cita un fratello minore di nome "Romeo" nella propria fonte. Verificato contro la scheda esistente di **Romeo "Gray" Dean** (Solarton, Silver Bullets): specie diversa (manticora dichiarata per il fratello di Gianni vs werewolf per Gray), biografia diversa (Gray cresciuto da un padre alcolizzato bigotto a Solarton, non orfanotrofio toscano), nazionalità diversa. **Nessun collegamento reale, quasi certamente omonimia casuale**, non riportato come aggancio.

## Decisione di collocazione applicata

Per i dodici personaggi canon già catalogati in `Pending_Lorebook_ModernFantasy_12Personaggi_2026-09-15.md` (Angui, Cyrus Camden, Emil, Gianni Luciano, Ilya Volkov, Julian Bieri, Levi Graham, Milo Grayson, Nic Lucero, Rhett e Jayce, Vale Roberts): **nessuno di loro è ambientato a Los Angeles nella fonte originale** (Maryland, Londra, New York, Seattle, Oregon, Louisiana, o non specificato). Per decisione esplicita dell'utente, chi non è dichiaratamente a Los Angeles resta un **contatto esterno**, non una scheda Character piena: accorpati in un'unica entry Lexicon ricca (§7, "gruppo di personaggi off-world che nessuno incontrerà a breve"), scorporabile in schede singole solo se uno di loro entra davvero in scena.

**Eccezione: Ilya Volkov** ottiene anche un aggancio diretto sulla scheda di **Vero Walker** (già presente nel World), di cui è fratellastro per dichiarazione esplicita della fonte: ha scoperto Vero nella PMC rivale BLOODHOUND (Ilya lavora per LUNAR) e ha tentato di ucciderlo, fallendo. Aggiunta una nuova sezione FAMILY sulla scheda di Vero con questo dettaglio, prima assente. Resta comunque nella entry Lexicon contatti esterni, non ha una scheda propria.

**Garrett Locke**: nessuna azione necessaria, già completato e collocato a Bakersfield in una sessione precedente (`Bakersfield_Garrett_Locke_Dallas_Rhodes_2026-09-15.md`).

## Correzione di continuity: la base S.R.F. è a Los Angeles, non sulla East Coast

La scheda di **Miles Airhardt** riportava `POSTING: The East Coast SRF base`, in contraddizione con quanto già stabilito in `Import_Plan_AllContent.md` ("i 4 membri S.R.F. e la DCC Tower restano correttamente in LOS ANGELES, la base SRF... si trova fisicamente a Los Angeles") e con l'indicazione esplicita dell'utente in questa sessione: la base è **Fort MacArthur, al Porto di Los Angeles**, la stessa zona dove nel canon del World si trova già la Location "Molo 42" (San Pedro), ed è il luogo dove hanno prestato servizio Kaladin Nargathon e Marcus Thornfield (Gamma-7, poi S.R.F. dal 2009) e dove Nixara Bloodmoon lavorò come consulente psichiatrica per il personale sovrannaturale durante Project BlackWolf (canon già scritto in `Kaladin_Wild_Honey_Thread.md`).

Corretto:
- **Miles Airhardt**: `POSTING` cambiato da "The East Coast SRF base" a "Fort MacArthur, Port of Los Angeles".
- **Rafael Callaway, Kade Leavis, Graham Purcell**: aggiunto lo stesso campo `POSTING`, assente in precedenza (nessuna contraddizione da correggere, solo esplicitato per coerenza fra i quattro membri della squadra Alpha).
- **Nuova Location creata**: "Fort MacArthur", environment Los Angeles, parente di "Molo 42" nella stessa area del porto di San Pedro. Descrizione include il ruolo storico di Nixara e il passaggio di Kaladin/Marcus.

## Nuova entry Lexicon

**"Modern Fantasy: Contatti Esterni dell'Underworld"**, tipo `mob`, `is_global: true`, chiavi sui nomi dei dodici personaggi (undici voci, Rhett e Jayce condividono un'unica voce). Contenuto in prosa compatta, un paragrafo per personaggio, nessun contenuto anatomico/kink (nessuna delle fonti ne conteneva), nessun riferimento fisso al personaggio giocante.

## Verifica

`PRAGMA integrity_check` ok. Conteggio Character invariato a 134 (solo un UPDATE su Vero Walker, nessun nuovo Character creato). Lexicon passato da 221 a 222. Location Los Angeles passate da 7 a 8. Zero `{{user}}` (corretta una menzione letterale della stringa macro nella nota di provenienza della nuova entry Lexicon, che l'avrebbe fatta leggere a runtime come un riferimento vivo invece che come citazione), zero em-dash, zero grassetto markdown su tutti i campi toccati. Scritto sul dispositivo dopo conferma che Wyldfire fosse chiuso, nessun file `-wal`/`-shm` residuo.
