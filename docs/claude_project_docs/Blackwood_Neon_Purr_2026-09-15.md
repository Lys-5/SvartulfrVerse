# Blackwood — Neon Purr, rivale di DJ Frequency (2026-09-15)

Una scheda nuova, dominio Blackwood (materiale creativo dell'utente, non canon esterno). World a 133 personaggi dopo l'inserimento (132 → 133).

- **Neon Purr** (vero nome Jasper Lane, tenuto privato salvo cerchia stretta), id locale `kN5szEYv3jwqvkK200R2T` — demi-umano gatto, popstar hyperpop australiano in tour, attualmente di passaggio a Blackwood City, rivale sul campo DJ/musicale di Jasper Douglas Bloodmoon (alias DJ Frequency).
- Nessun Intimacy Profile: la fonte non conteneva contenuto anatomico/kink esplicito, solo un arco romantico generico verso `{{user}}`, quindi resta nella prosa VOICE & BEHAVIOR senza bisogno di segregazione (§13.3).

## Cosa dice la fonte

Introduzione promozionale ATvision per Neon Purr: popstar australiano da Byron Bay, genere "bubble buff hyperpop", fisico da bodybuilder, capelli ombré viola-rosa, quattro gatti al seguito, manager Tilda "Tigress" Rowe, cugina Miki come tecnica LED. Include una sezione "Relationship Dynamic with `{{user}}`": una lite iniziale colpa sua, uno stan segreto con account fan anonimo, una canzone d'amore scritta su `{{user}}` e mai ammessa, pratiche di scuse davanti allo specchio.

## Cosa abbiamo scritto

**Purga standard §13** (arco romantico fisso, non tratta/non-consenso, quindi non serve l'estensione 14/09): rimossi integralmente lo stan segreto, l'account fan anonimo, la canzone d'amore, le prove di scuse specificamente rivolte a `{{user}}`. Il nucleo riusabile, cioè "si imbarazza terribilmente quando gli piace qualcuno, nasconde tutto dietro battute e bravata, prova le scuse allo specchio senza mai riuscirci bene", è stato mantenuto come tratto di personalità generico e non risolto, riusabile per futuri agganci narrativi senza puntare a nessun personaggio specifico.

**Conversione richiesta dall'utente**: Neon Purr diventa demi-umano gatto (unico paio di orecchie, coda, entrambe in tinta ombré viola-rosa coerente con i capelli) e viene reso rivale di Jasper Douglas Bloodmoon (DJ Frequency) sul campo musicale/DJ. La lite "colpa sua al 100%" della fonte originale, rivolta a `{{user}}`, è stata riscritta e reindirizzata su questa rivalità: la scintilla è una battuta scintillante e stupida di Neon sul set di Jasper al **The Verve** (Location già esistente nel World, il nightclub sotterraneo di Logan Douglas), non seguita da scuse ma da un rilancio, diventata da lì una faida di beat battle semi seria e ricorrente ogni volta che il tour di Neon passa da Blackwood.

**Attitudes reciproche aggiunte su entrambe le schede**: Neon Purr → Jasper Douglas Bloodmoon e Jasper Douglas Bloodmoon → Neon Purr, entrambe `rival`/intensity 60, rispetto reciproco sotto la superficie competitiva (mai dichiarato ad alta voce da nessuno dei due). Aggiunta anche l'Attitude obbligatoria verso Alyssa Douglas Bloodmoon (`stranger`/15, mai incontrati).

## Note minori

- **Nome reale**: mantenuto come dettaglio narrativo tenuto privato, MA volutamente escluso dai campi `keys`/`secondary_keys` della scheda (solo "Neon Purr" e "Neon"), per evitare collisioni di chiave con "Jasper Douglas Bloodmoon" e per preservare la segretezza del nome nel meccanismo di attivazione. Compare solo nella prosa BACKSTORY.
- **Contorno**: manager Tilda "Tigress" Rowe, cugina Miki, i quattro gatti (Luna, Chibi, Comet, Snaxx) mantenuti come personaggi di contorno nella prosa, non promossi a Character separate (nessuno di loro entra probabilmente in scena a breve, coerente con §7).
- **Età**: 25 anni dichiarati dalla fonte, nato 19 novembre 1998, data variata come da convenzione §9.6.

RPG Stats lasciate `NULL` (sistema in pausa, §8). Start Position = birthdate, nessuna End Position (vivo, contemporaneo).

## Verifica

`PRAGMA integrity_check` ok, conteggio World 133/133, zero `{{user}}`, zero em-dash, zero grassetto markdown, tutti gli outfit con chiave `avatar` presente, `default_outfit` valido, Attitudes risolte correttamente per id locale su entrambe le schede coinvolte (Neon Purr e Jasper Douglas Bloodmoon, ora a dieci Attitudes), nessuna collisione di chiavi con schede esistenti. Scritto sul dispositivo dopo conferma che Wyldfire fosse chiuso, nessun file `-wal`/`-shm` residuo trovato dopo la scrittura.
