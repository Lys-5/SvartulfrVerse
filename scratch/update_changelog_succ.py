import re

new_changelog_entry = """## [20 Ottobre 2026] - Integrazione Lore SUCC, Solarton, Modern Fantasy & Il Ponte con Fabule Urbane (La Frattura / Voidspace / Dungeons)

- **Ponte Canonico "La Frattura" e Integrazione nel Voidspace Svartúlfr (`Svartulfr_Lorebook_II.json` — `_HfG7TeV6MJyj6bxMwxkpt`)**:
  - **La Frattura come Squarcio del Velo**: Formalizzato l'evento cataclismatico dello *Squarcio del Velo* (classificato dai monitor DDM come *Reality Tear Primaria*) che in Europa e nel bacino del Mediterraneo ha preso il nome storico di *La Frattura*, aprendo varchi permanenti verso l'Otherworld e il Voidspace e generando cripte instabili, labirinti ipogei (Dungeon) e la contaminata *Fascia Desolata*.
  - **Agenzia EXO & Unità Tattica Le Furie**: Introdotte la *European Xenological Operations (EXO)* per la messa in sicurezza e bonifica dei Dungeon urbani (operativa in parallelo con DDM Inc. e PERSEUS) e la squadra d'assalto rapido *Le Furie*, deputata al contenimento di brecce critiche e fughe di creature dell'abisso.
  - **Bestiario dei Dungeon Mediterranei**: Catalogate le creature folkloristiche risvegliate e mutate dal miasma del Velo: *Alichini* (demoni alati del baratro e predatori aerei), *Coblynau e Coboldi* (scavatori ipogei ossessionati da vene di mana solido e Dungeon Cores), *Drakaina* (serpi anfibie giganti nei condotti fognari), *Alseidi Corrotte* (spiriti vegetali territoriali e ostili), *Variaghi* (predoni e mercenari della Fascia Desolata).
  - Conteggio Lorebook II: incrementato da 139 a **142 voci** attive (`entries` e `lexicon` perfettamente sincronizzati).

- **Arricchimento Istituzionale, Demografico e Giuridico SUCC (`Svartulfr_Lorebook_III.json` — `_9zWTGqYJNJ4BCDMj8gfcD`)**:
  - **Demografia Accademica Ufficiale**: Integrata la tabella percentuale verificata (25.8% Weres, 24.0% Demi-umani, 13.3% Umani, 7.5% Vampiri, 5.0% Demoni, 4.9% Fae, 4.7% Ibridi, 4.0% Non-morti, 4.0% Umani dotati, <1% Criptidi).
  - **Gli 11 Corsi Sovrannaturali**: Formalizzate le declaratorie accademiche per *Alchemy*, *Necromancy*, *Applied Divination*, *Paranormal Psychology*, *Astral Studies*, *Potions*, *Cryptozoology*, *Supernatural/Human Relations*, *Environmental Magic*, *Vampiric Studies* e *Lycanthropy Studies*.
  - **Calendario Sportivo e Servizi di Campus**: Inserito il derby accademico settimanale fisso *Bulls vs Clams* (venerdì ore 19:00), la pista ghiaccio dei *Bears* capitanati da Vincent Campbell, i *Kelpies* (nuoto/tuffi), i *Phantoms* (basket con spettro di Coach Connors), le stanze riscaldate per studenti a sangue freddo in biblioteca e la manutenzione della Torre dell'Orologio.
  - **Nuova Voce sul Quadro Giuridico Modern Fantasy**: Introdotta la voce normativa comprendente il *Divieto Federale di Matrimonio Misto* tra umani e sovrannaturali, il *Registro Obbligatorio dei Demoni*, le tutele del *Supernatural Harm Act del 2001* e il vincolo tecnologico (assenza assoluta di robotica avanzata, androidi o cyborg).
  - Conteggio Lorebook III: incrementato da 35 a **36 voci** attive.

- **Rifinitura Topografica di Solarton (`Svartulfr_Location.json` — `_EjXxkmPVhpCXg8xABpFkK`)**:
  - **Bricklane Mall**: Inclusi i celebri esercizi indipendenti *Medusa's* (salone di acconciatura specializzato per capigliature di serpenti, piume e criniere) e *Yeti Shack* (granite e dolci termoregolatori).
  - **Sidewinders Bar & Nightclub**: Arricchito il retroterra storico di primo locale ad aver abbattuto le leggi anti-vampiriche dopo la Crisi Notturna del 1999.
  - **Solarton High School**: Documentato il programma di borse sportive, le ristrutturazioni di accessibilità per non-umanoidi e i ruoli docenti di Hank Thompson (Educazione Fisica) e Stanley Davies Sr. (Matematica).
  - Conteggio Location: confermato a **225 voci** attive.

- **Deploy Wyvern API & Mirroring Locale**:
  - Effettuato il mirroring di tutte le modifiche in `lorebooks/optimized/`.
  - Refreshed Bearer token tramite Firebase API e deploy completato con `HTTP 200 OK` per Lorebook II (`_HfG7TeV6MJyj6bxMwxkpt`), Lorebook III (`_9zWTGqYJNJ4BCDMj8gfcD`) e Location (`_EjXxkmPVhpCXg8xABpFkK`).
"""

with open('CHANGELOG.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert right after header
marker = "# Changelog di Progetto — Svartúlfr Verse\n\nTutte le modifiche, gli aggiornamenti di sistema, le revisioni di Lore, i deploy dello StoryEngine e gli interventi sulle entità del World (World, Lexicon, Locations, NPC, Rules) sono tracciati cronologicamente in questo documento per garantire persistenza e coerenza storica tra le sessioni.\n\n"

if marker in content:
    updated = content.replace(marker, marker + new_changelog_entry + "\n---\n\n")
else:
    # fallback
    lines = content.split('\n')
    header_end = 4
    updated = '\n'.join(lines[:header_end]) + '\n\n' + new_changelog_entry + '\n---\n\n' + '\n'.join(lines[header_end:])

with open('CHANGELOG.md', 'w', encoding='utf-8') as f:
    f.write(updated)

print("CHANGELOG.md updated successfully!")
