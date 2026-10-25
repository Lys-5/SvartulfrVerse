import json
import uuid

def generate_id():
    return '_' + uuid.uuid4().hex[:21]

path_lb2 = 'FINAL/Svartulfr_Lorebook_II.json'
with open(path_lb2, 'r', encoding='utf-8') as f:
    data = json.load(f)

entries = data.get('entries', [])
lexicon = data.get('lexicon', [])

print(f"Initial Lorebook II counts: entries={len(entries)}, lexicon={len(lexicon)}")

# 1. Entry Frattura
entry_frattura = {
    'id': generate_id(),
    'name': "La Frattura: Lo Squarcio del Velo e l'Origine dei Dungeon Europei",
    'type': 'lore/concept',
    'keys': ['La Frattura', 'Squarcio del Velo', 'Frattura', 'Dungeon Europei', 'Fascia Desolata', 'Breccia del Velo', 'Velo', 'dopo-Frattura'],
    'secondary_keys': ['Dungeon', 'Varco', 'Otherworld', 'Voidspace', 'catacombe', 'incursione', 'anomalia', 'abisso', 'breccia'],
    'key_logic': 'AND_ANY',
    'content': """[EVENTO COSMICO E FENOMENOLOGIA: La Frattura e i Dungeon Europei]
Nel teatro continentale europeo e nel bacino del Mediterraneo, il collasso dimensionale noto globalmente come Squarcio del Velo (classificato nei sistemi DDM come Reality Tear Primaria) ha assunto il nome storico di 'La Frattura'. 
Questo trauma ha lacerato la membrana di separazione tra il piano terreno e i reami esotici di Otherworld e Voidspace, innescando una cascata di manifestazioni anomale:
1. Nascita dei Dungeon Ipogei: Antichi complessi di catacombe, cripte medievali, acquedotti romani e miniere abbandonate sono stati invasi da miasma arcanico grezzo, convertendosi in 'Dungeon' labirintici governati da distorsioni gravitazionali, trappole dimensionali e proliferazione di nuclei di mana (Dungeon Cores).
2. La Fascia Desolata: Fasce di territorio liminale contaminate dalle radiazioni del Voidspace, dove la realta consensuale perde coerenza e gli spiriti non pacificati restano intrappolati in un limbo di nebbia eterica.
3. I Cambiati e la Rinascita Arcana: L'onda d'urto ha risvegliato entita sopite del folklore arcaico e alterato geneticamente migliaia di civili (i 'Cambiati'), costringendo le autorita a istituire presidi di quarantena, albi per Operatori Spiritici e rifugi dedicati come il Santuario dei Ritornati.""",
    'selective': True,
    'priority': 2,
    'position': 'before_char',
    'enabled': True
}

# 2. Entry EXO & Le Furie
entry_exo = {
    'id': generate_id(),
    'name': 'EXO & Le Furie: Agenzie Europee di Contenimento Breccia',
    'type': 'organization/faction',
    'keys': ['EXO', 'European Xenological Operations', 'Le Furie', 'Furie', 'Operatori Spiritici', 'Squadra Furie', 'Cambiati'],
    'secondary_keys': ['Dungeon', 'agenti', 'breccia', 'contenimento', 'assalto', 'incursione', 'paramilitare', 'sicurezza'],
    'key_logic': 'AND_ANY',
    'content': """[ORGANIZZAZIONE PARAMILITARE: European Xenological Operations (EXO) e Unita Le Furie]
Sede Operativa: Milano e Roma, con presidi tattici lungo i principali focolai di Dungeon dell'Europa meridionale.
Ruolo Istituzionale: La EXO e la primaria corporazione paramilitare e multimediale incaricata del contenimento dei danni da Frattura, della bonifica dei Dungeon urbani e della neutralizzazione delle brecce dimensionali. Lavora in stretto coordinamento o in rivalita commerciale con realta globali come DDM Inc. e i mercenari di PERSEUS.
Struttura Operativa:
- Settore Operativo e PR: Impiega specialisti della numerologia, cartomanti di valutazione del rischio e celebri agenti di campo dotati di poteri cinetici e pirotecnici, le cui imprese di salvataggio sono spesso trasmesse sui media per rassicurare l'opinione pubblica.
- Le Furie (Tactical Incursion Strike Team): Squadra d'assalto speciale segreta e d'intervento rapido, composta da operatori da combattimento corpo a corpo, occultisti di supporto e mannari da breccia. Le Furie vengono mobilitate quando un Dungeon raggiunge lo stadio critico o quando entita aberranti fuggono dai livelli inferiori minacciando centri abitati.
- Rete di Supporto Civile: Si interfaccia con i registri degli Operatori Spiritici freelance e con organizzazioni territoriali di tutela per civili traumatizzati dal miasma del Velo.""",
    'selective': True,
    'priority': 2,
    'position': 'before_char',
    'enabled': True
}

# 3. Entry Bestiario del Velo
entry_bestiario = {
    'id': generate_id(),
    'name': 'Bestiario del Velo: Creature dei Dungeon Mediterranei',
    'type': 'creature',
    'keys': ['Bestiario del Velo', 'Alichini', 'Coblynau', 'Drakaina', 'Variaghi', 'Alseidi', 'Mostri del Velo', 'Creature Dungeon'],
    'secondary_keys': ['Dungeon', 'mostro', 'creatura', 'bestia', 'catacomba', 'caverna', 'combattimento', 'minaccia'],
    'key_logic': 'AND_ANY',
    'content': """[BESTIARIO DEI DUNGEON: Entita della Frattura e del Voidspace]
L'esposizione delle antiche terre mediterranee alle correnti dell'Otherworld ha risvegliato e mutato creature caratteristiche dell'ecosistema sotterraneo:
1. Alichini: Demoni alati del baratro e predatori notturni che nidificano nelle volte delle cattedrali ipogee e nei pozzi dei Dungeon. Attaccano in picchiata a sciami coordinati, sfruttando artigli intrisi di acido e un'agilita aerea letale in spazi angusti.
2. Coblynau e Coboldi di Miniera: Piccoli umanoidi sotterranei dalla pelle cinerea e dita rinforzate, ossessionati dall'estrazione di vene di mana solido e cristalli di Dungeon Core. Sebbene territoriali e propensi a scavare trappole a trabocchetto, possono essere negoziati se riforniti di minerali o cibo fresco.
3. Drakaina: Enormi serpi acquatiche anfibie con teste multiple o creste spinose che infestano i bacini di drenaggio e i condotti fognari contaminati dal miasma del Velo. Possiedono una corazza squamata impenetrabile alle armi convenzionali e secrezioni velenose altamente corrosive.
4. Alseidi Corrotte: Antiche ninfe dei boschi le cui radici sacre sono state toccate da una faglia di Reality Tear. Trasformate in esseri vegetali antropomorfi spietati, difendono i varchi boschivi con rampicanti perforanti e spore allucinogene.
5. Variaghi: Mercenari spietati e stalker mutati della Fascia Desolata. Umani o mezze-specie induriti dalla sopravvivenza al confine del Velo, armati di equipaggiamento recuperato nei Dungeon e disposti a tendere imboscate ai cacciatori impreparati.""",
    'selective': True,
    'priority': 2,
    'position': 'before_char',
    'enabled': True
}

entries.extend([entry_frattura, entry_exo, entry_bestiario])
lexicon.extend([entry_frattura, entry_exo, entry_bestiario])

with open(path_lb2, 'w', encoding='utf-8') as f:
    json.dump(data, f, indent=2, ensure_ascii=False)

print(f"Updated Lorebook II: entries={len(entries)}, lexicon={len(lexicon)}")
