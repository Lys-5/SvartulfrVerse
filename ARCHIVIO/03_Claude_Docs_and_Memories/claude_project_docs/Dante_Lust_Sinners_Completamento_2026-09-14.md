# Dante "Lust" (Sinners) — Completamento 2026-09-14

Prima scheda lavorata della cartella Los Angeles / gruppo Sinners, da import grezzo JanitorAI fornito dall'utente in chat.

## Epurazione da `{{user}}`

Il materiale sorgente conteneva un arco romantico/sessuale completo verso `{{user}}` ("Dante's current favorite"), inclusi tre blocchi di esempio in-character costruiti specificamente attorno a `{{user}}` come partner (scena di gelosia al bar, crollo emotivo alla porta, scena esplicita di gruppo). Applicata l'Estensione 14/09 di §13: tutto questo materiale è stato escluso integralmente, non trascritto e ripulito. Portato avanti solo ciò che è indipendente da `{{user}}`: aspetto, personalità, il locale (The Inferno), il ruolo nei Sinners, le relazioni con Jean-Luc/Roxie/Siobhan, il tema centrale dell'insicurezza da validazione.

Il contenuto NSFW esplicito (turn-ons, dinamiche a letto, anatomia) è stato spostato in un Intimacy Profile separato in Lexicon (`_2C3KXHRw9xyMzRqA9YDYE`), registro a blocchi (stile Erik) scelto perché la sessualità di Dante è strutturalmente legata al suo trauma di validazione, non un tratto isolato. Misure anatomiche numeriche convertite in descrittori qualitativi ("modest in scale" invece della cifra esatta), come da convenzione di progetto.

L'uso di Ambrosia sui clienti del locale per abbassarne le inibizioni è stato mantenuto come tratto di backstory/caratterizzazione generale del suo modus operandi professionale (non è contenuto rivolto a `{{user}}` né una scena giocabile), coerente con la lettura di Dante come figura antagonista dei Sinners.

## Età

Fonte diceva solo "appears 25, in reality much older, won't admit his age", con un riferimento diretto e personale agli anni '20 come incubo già navigato. Proposta a discrezione (§9.7): 350 anni, nato il 14 giugno 1674. Confermata dall'utente prima della scrittura. `birthdate` e `start_timeline_position` entrambi a 7420104 ore (World Clock), coincidenti, inferiori a `world_age` (10486470).

## Relazioni

Jean-Luc Virtuoso (`_U7CH86RKPVkCjMtQnGX1j`): romantic_interest, intensity 85, cotta non corrisposta e rapporto di subordinazione.
Roxie (`_H9h9jKxeX6cEDqyNRa141`): wary, intensity 55, paura mista ad attrazione.
Siobhan (`_Hk2RdTkz6XFmWW88TEraB`): friend, intensity 65, amicizia tossica basata su gossip condiviso.
Alyssa e Jasper: stranger, intensity 15 (mai incontrati, come da §16).

Nota: queste tre schede (Jean-Luc, Roxie, Siobhan) sono ancora placeholder vuoti sul World. Le Attitudes di Dante puntano già ai loro ID corretti, pronte per quando verranno lavorate; andrà aggiunta la reciproca su ciascuna quando arriva il turno.

## Pipeline

JED+ completo (long_summary), summary PList, display_description, pronomi, 5 outfit con Default Outfit impostato (Inferno Floor), 5 Dialogue Examples riscritti senza `{{user}}` (Jean-Luc, Siobhan, Roxie, il locale, un momento di vulnerabilità in solitudine), final_instructions con la riga di disciplina di formato, Global Character ON. RPG Stats non toccate (sistema in pausa, §8).

Verificato con GET autenticata fresca dopo la scrittura: zero `{{user}}`, zero em-dash, zero grassetto, tutti i campi presenti, birthdate/start coincidenti.
