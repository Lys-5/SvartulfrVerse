import json
import os
import re
import pathlib
import sys
import secrets
import string

# Ensure UTF-8 output
sys.stdout.reconfigure(encoding='utf-8')

ROOT = pathlib.Path(__file__).resolve().parent.parent
FINAL = ROOT / 'FINAL'
OPT = ROOT / 'lorebooks' / 'optimized'
PERSONAS = FINAL / 'personas'

def generate_nanoid(length=21):
    alphabet = string.ascii_letters + string.digits + '_-'
    return ''.join(secrets.choice(alphabet) for _ in range(length))

def clean_prophecy_and_intimacy(desc, char_name):
    # Strip prophecy from Alyssa / Jasper narrative
    for p_header in [
        'THE WHITE MOON, SVARTR & THE NORSE PROPHECY:',
        'THE SOLAR SHADOW, SVARTR SOLULF & THE NORSE PROPHECY:'
    ]:
        pos_p = desc.find(p_header)
        if pos_p != -1:
            # find next header
            next_headers = ['THE MOONLIGHT SHE BRINGS:', 'THE BURDEN HE CARRIES:', 'SEXUALITY & INTIMACY:']
            next_pos = -1
            for nh in next_headers:
                np = desc.find(nh, pos_p)
                if np != -1 and (next_pos == -1 or np < next_pos):
                    next_pos = np
            if next_pos != -1:
                desc = desc[:pos_p].rstrip() + '\n\n' + desc[next_pos:]
            else:
                desc = desc[:pos_p].rstrip()

    # Strip SEXUALITY & INTIMACY, SIGNATURE, RPG STATS from prose description
    pos_sex = desc.find('SEXUALITY & INTIMACY:')
    if pos_sex != -1:
        desc = desc[:pos_sex].strip()
        
    return desc

def main():
    print("=== 1. Reading Alyssa and Jasper Personas and Cards ===")
    with open(PERSONAS / 'Alyssa_Persona.json', 'r', encoding='utf-8') as f:
        alyssa_p = json.load(f)
    with open(PERSONAS / 'Jasper_Persona.json', 'r', encoding='utf-8') as f:
        jasper_p = json.load(f)
        
    alyssa_desc = alyssa_p['description']
    jasper_desc = jasper_p['description']
    
    # Extract Alyssa Intimacy
    pos_a_sex = alyssa_desc.find('SEXUALITY & INTIMACY:')
    pos_a_items = alyssa_desc.find('SIGNATURE ITEMS & VEHICLE:', pos_a_sex)
    alyssa_intimacy = alyssa_desc[pos_a_sex:pos_a_items].strip() if pos_a_items != -1 else alyssa_desc[pos_a_sex:].strip()
    
    # Extract Jasper Intimacy
    pos_j_sex = jasper_desc.find('SEXUALITY & INTIMACY:')
    pos_j_items = jasper_desc.find('SIGNATURE ITEMS & VEHICLE:', pos_j_sex)
    jasper_intimacy = jasper_desc[pos_j_sex:pos_j_items].strip() if pos_j_items != -1 else jasper_desc[pos_j_sex:].strip()

    # Extract Prophecy Text
    pos_p1 = alyssa_desc.find('THE WHITE MOON, SVARTR & THE NORSE PROPHECY:')
    pos_p1_end = alyssa_desc.find('THE MOONLIGHT SHE BRINGS:', pos_p1)
    alyssa_prophecy_text = alyssa_desc[pos_p1:pos_p1_end].strip()

    pos_p2 = jasper_desc.find('THE SOLAR SHADOW, SVARTR SOLULF & THE NORSE PROPHECY:')
    pos_p2_end = jasper_desc.find('THE BURDEN HE CARRIES:', pos_p2)
    jasper_prophecy_text = jasper_desc[pos_p2:pos_p2_end].strip()

    # Extract Card Intimacies
    card_files = [
        ('Erik_Douglas_card.json', 'Erik Douglas'),
        ('Malachia_Douglas_Bloodmoon_card.json', 'Malachia Douglas'),
        ('Logan_Douglas_card.json', 'Logan Douglas'),
        ('Noah_Douglas_Bloodmoon_card.json', 'Noah Douglas'),
        ('Mackenzie_Sanchez_Rogers_card.json', 'Mackenzie Sanchez-Rogers'),
        ('Wulfnic_Bloodmoon_card.json', 'Wulfnic Bloodmoon'),
    ]
    
    card_intimacies = {}
    for cfile, cname in card_files:
        with open(FINAL / cfile, 'r', encoding='utf-8') as f:
            cdata = json.load(f)
            cdesc = cdata.get('description', '')
        pos_s = cdesc.find('SEXUALITY & INTIMACY:')
        if pos_s != -1:
            pos_e = cdesc.find('SIGNATURE', pos_s)
            if pos_e == -1: pos_e = cdesc.find('RPG STATS', pos_s)
            c_intimacy = cdesc[pos_s:pos_e].strip() if pos_e != -1 else cdesc[pos_s:].strip()
            card_intimacies[cname] = c_intimacy

    print("Extracted intimacies for all characters.")

    # 2. Build the 12 Lexicon Entries
    new_entries = []

    # Entry 1: LSE: Teologia Fenririana & Il Ciclo Millenario della Luna Bianca
    entry_teol = {
        "entry_id": generate_nanoid(),
        "name": "LSE: Teologia Fenririana & Il Ciclo Millenario della Luna Bianca",
        "type": "lore/concept",
        "keys": ["religione lse", "teologia fenririana", "luna bianca", "white moon", "hvit", "arianne", "nixara", "mani", "hati", "culto lupino", "folklore lse", "nine firstborn", "nove primogeniti"],
        "secondary_keys": [],
        "selective": False,
        "key_logic": "AND_ANY",
        "scan_persona": True,
        "whole_words_only": True,
        "enableEntryHighlighting": True,
        "ignored_characters": [],
        "ignored_personas": [],
        "content": """[LORE & MITOLOGIA LSE: TEOLOGIA FENRIRIANA & IL CICLO DELLA LUNA BIANCA]

La religione e la cosmologia sacra dei licantropi LSE (Lupine Social Ecology) e del Clan Svartulfr affondano le radici nella consacrazione divina avvenuta nell'864 d.C., quando Fenris benedisse i Nove Guerrieri Vichinghi guidati da Wulfnic Baleygr (i Nove Primogeniti). Accanto ai guerrieri discesero sulla terra due personificazioni cosmiche: Mani (la Luna, legata ad Hati) e Sol (il Sole, legata a Skoll).

IL CICLO DELLE QUATTRO LUNE BIANCHE (Mani Reincarnata):
1. Hvit, la Prima (The Original): Nata da Mani e Hati con occhi bianco-argentei radiosi, fu la prima compagna condivisa di tutti e Nove i Primogeniti (Wulfnic, Ut, Zefir, Sigvaldi, Svartr, Brandr, Kari, Runolfr e Garmr), donando a ciascuno una discendenza sacra. Durante la Guerra dei Pantheon (il Falso Ragnarok), sepolse sei compagni prima di seguire i superstiti (Wulfnic, Ut, Zefir) in America, spegnendosi un secolo dopo.
2. Arianne, la Seconda: Nata nel villaggio la notte esatta della morte di Hvit. A diciannove anni fu reclamata da Wulfnic nella prima Grande Caccia e condivisa con Ut e Zefir. Visse per secoli al loro fianco, morendo nel 1975 dando alla luce Nixara.
3. Nixara, la Terza: Nata direttamente come figlia biologica di Wulfnic, spezzo il ciclo antico: Wulfnic non pote mai prenderla come compagna. Fu la prima Luna Bianca a scegliere un compagno al di fuori del Sangue Divino, Erik Douglas, prima di morire di parto nel 2005.
4. Alyssa, la Quarta (Hvit Rinata): Nata nel 2005 da Erik e Nixara, porta negli occhi il bagliore bianco-argento di Hvit e nel sangue la memoria ancestrale delle tre che l'hanno preceduta. Invece di essere condivisa tra i Primogeniti come nei secoli arcaici, incarna il voto pacifista assoluto del nuovo millennio, custodita e venerata dall'intera dinastia."""
    }
    new_entries.append(entry_teol)

    # Entry 2: LSE: La Profezia dei Lupi Gemelli (Hvit Solulf & Svartr Solulf)
    entry_prof = {
        "entry_id": generate_nanoid(),
        "name": "LSE: La Profezia dei Lupi Gemelli (Hvit Solulf & Svartr Solulf)",
        "type": "lore/concept",
        "keys": ["profezia lse", "norse prophecy", "profezia gemelli", "hvit solulf", "svartr solulf", "sole nero", "black sun", "lupi gemelli", "bastion", "re dei lupi", "antico norreno", "falso ragnarok"],
        "secondary_keys": [],
        "selective": False,
        "key_logic": "AND_ANY",
        "scan_persona": True,
        "whole_words_only": True,
        "enableEntryHighlighting": True,
        "ignored_characters": [],
        "ignored_personas": [],
        "content": """[PROFEZIA & FOLKLORE LSE: I LUPI GEMELLI & LA CADUTA DEI PRIMI]

Un'antichissima profezia in antico norreno, tramandata oralmente tra i sacerdoti del Clan Svartulfr e incisa su steli di ferro freddo, recita:

"Tha er tungl ok sol risa saman i dreyra,
mun old hinna Fyrstu lida undir lok,
ok Vigit mun verda Konungr
eptir eitt hundrad ok fimm tigi vetra."

(Traduzione: "Quando la luna e il sole sorgeranno insieme nel sangue, l'era dei Primi giungera alla fine, e il Bastione diverra Re dopo centocinquanta inverni.")

SIGNIFICATO SACRO E DINAMICA COSMICA:
Per oltre mille anni, la profezia e rimasta incompleta: Hvit si e reincarnata quattro volte come Luna Bianca, mentre Svartr Solulf (il Lupo del Sole Nero, incarnazione di Sol e Skoll, nonche il piu spietato tra i Nove Fratelli caduto nel Falso Ragnarok attorno al 1000 d.C.) e rimasto dormiente nel vuoto eterico.
Nel 2005, la profezia si e compiuta con la nascita dei gemelli Alyssa e Jasper Douglas Bloodmoon:
- Alyssa incarna la Luna Bianca (Hvit Solulf), custode di vita, pace e guarigione.
- Jasper incarna il Sole Nero (Svartr Solulf), ombra protettrice, tecnomante e guardiano digitale.
La loro nascita contemporanea segna l'avvicinarsi della fine dell'era dei Primogeniti millenari (Wulfnic, Ut, Zefir) e l'ascesa definitiva della Casata Douglas come Bastione regale del mondo licantropo."""
    }
    new_entries.append(entry_prof)

    # Entry 3: LSE: Il Marchio Solare & I Poteri Risvegliati di Jasper (Svartr)
    entry_pot_j = {
        "entry_id": generate_nanoid(),
        "name": "LSE: Il Marchio Solare & I Poteri Risvegliati di Jasper (Svartr)",
        "type": "ability",
        "keys": ["marchio solare", "solar brand", "poteri jasper", "tecnomanzia solare", "sole nero", "black sun", "svartr", "runa sol", "solar flame", "tecnomanzia"],
        "secondary_keys": [],
        "selective": False,
        "key_logic": "AND_ANY",
        "scan_persona": True,
        "whole_words_only": True,
        "enableEntryHighlighting": True,
        "ignored_characters": [],
        "ignored_personas": [],
        "content": """[ABILITA & MARCHI SACRI: IL MARCHIO DEL SOLE NERO (JASPER / SVARTR)]

Jasper porta impresso sul dorso della mano destra, sul petto e sulla nuca il Marchio Runico di Sol (il Sole Nero di Skoll), retaggio dell'anima guerriera di Svartr Solulf. I suoi poteri awakened comprendono:
1. Tecnomanzia Solare & Sintesi Neurale: Capacita di interfacciare il proprio sistema nervoso direttamente con flussi ottici, circuiti quantistici e mainframe DCC, manipolando codice e crittografia via telepatia hardware.
2. Reindirizzamento Termico e Cinetico: Assorbimento di calore ed energia d'impatto con scarica esplosiva solare attraverso gli artigli o i circuiti.
3. Ombra Eterica Predatoria: Quando i suoi occhi virano all'oro fuso ardente (sguardo di Svartr), Jasper manifesta un'aura di soppressione letale, capace di paralizzare predatori e macchine da guerra.
4. Sincronia Gemellare (Gebo Bond): Collegamento empatico e biologico istantaneo con la sorella gemella Alyssa; condivisione di percezione sensoriale e allerta vitale a qualsiasi distanza."""
    }
    new_entries.append(entry_pot_j)

    # Entry 4: LSE: Il Marchio Lunare & L'Aura Pacificatrice di Alyssa (Hvit)
    entry_pot_a = {
        "entry_id": generate_nanoid(),
        "name": "LSE: Il Marchio Lunare & L'Aura Pacificatrice di Alyssa (Hvit)",
        "type": "ability",
        "keys": ["marchio lunare", "lunar brand", "poteri alyssa", "aura pacificatrice", "pacifist aura", "luna bianca", "runa mani", "white moon aura", "guarigione lunare"],
        "secondary_keys": [],
        "selective": False,
        "key_logic": "AND_ANY",
        "scan_persona": True,
        "whole_words_only": True,
        "enableEntryHighlighting": True,
        "ignored_characters": [],
        "ignored_personas": [],
        "content": """[ABILITA & MARCHI SACRI: IL MARCHIO DELLA LUNA BIANCA (ALYSSA / HVIT)]

Alyssa porta sulla clavicola sinistra, sul cuore e sul fianco il Marchio Runico di Mani (la Luna Bianca di Hati), sigillo di reincarnazione della Madre Lunare. I suoi poteri awakened comprendono:
1. Aura Pacificatrice Assoluta (The Calming Light): Un campo feromonale ed eterico che disarma istantaneamente l'aggressivita, spegnendo la furia cieca (Berserker Rage), le tensioni Alpha/Omega e l'istinto omicida in chiunque le sia vicino.
2. Rigenerazione Cellulare e Chiaroveggenza: Spontanea accelerazione della guarigione tissutale e guarigione ematica attraverso il tocco e la magia botanica.
3. Sguardo Bianco-Argenteo: Nei momenti di connessione spirituale, i suoi occhi passano dal verde menta al bianco-argento luminoso di Hvit, rivelando le intenzioni dell'anima e svelando illusioni.
4. Sincronia Gemellare (Gebo Bond): Connessione sacra incisa a inchiostro di ferro freddo sul polso con Jasper; Alyssa avverte immediatamente qualsiasi sofferenza, alterazione o minaccia rivolta al fratello gemello."""
    }
    new_entries.append(entry_pot_a)

    # Entry 5: Alyssa Intimacy Memory
    entry_mem_a = {
        "entry_id": generate_nanoid(),
        "name": "Alyssa Douglas: Profilo Intimo & Dinamiche Sessuali",
        "type": "memory",
        "keys": ["alyssa intimita", "alyssa intimacy", "alyssa sessualita", "alyssa sesso", "alyssa kink", "alyssa profile intimo"],
        "secondary_keys": [],
        "selective": False,
        "key_logic": "AND_ANY",
        "scan_persona": True,
        "whole_words_only": True,
        "enableEntryHighlighting": True,
        "ignored_characters": [],
        "ignored_personas": [],
        "content": f"[PROFILO INTIMO & MEMORIA SESSUALE: ALYSSA DOUGLAS BLOODMOON]\n\n{alyssa_intimacy}"
    }
    new_entries.append(entry_mem_a)

    # Entry 6: Jasper Intimacy Memory
    entry_mem_j = {
        "entry_id": generate_nanoid(),
        "name": "Jasper Douglas: Profilo Intimo & Dinamiche Sessuali",
        "type": "memory",
        "keys": ["jasper intimita", "jasper intimacy", "jasper sessualita", "jasper sesso", "jasper kink", "jasper profile intimo"],
        "secondary_keys": [],
        "selective": False,
        "key_logic": "AND_ANY",
        "scan_persona": True,
        "whole_words_only": True,
        "enableEntryHighlighting": True,
        "ignored_characters": [],
        "ignored_personas": [],
        "content": f"[PROFILO INTIMO & MEMORIA SESSUALE: JASPER DOUGLAS BLOODMOON]\n\n{jasper_intimacy}"
    }
    new_entries.append(entry_mem_j)

    # Entries 7-12: Character Cards Intimacy Memories
    for cname, ctext in card_intimacies.items():
        if len(ctext) > 50:
            low_name = cname.lower().split()[0]
            entry_c = {
                "entry_id": generate_nanoid(),
                "name": f"{cname}: Profilo Intimo & Dinamiche Sessuali",
                "type": "memory",
                "keys": [f"{low_name} intimita", f"{low_name} intimacy", f"{low_name} sessualita", f"{low_name} sesso", f"{low_name} kink"],
                "secondary_keys": [],
                "selective": False,
                "key_logic": "AND_ANY",
                "scan_persona": True,
                "whole_words_only": True,
                "enableEntryHighlighting": True,
                "ignored_characters": [],
                "ignored_personas": [],
                "content": f"[PROFILO INTIMO & MEMORIA SESSUALE: {cname.upper()}]\n\n{ctext}"
            }
            new_entries.append(entry_c)

    print(f"Total new Lexicon entries built: {len(new_entries)}")

    # 3. Add to FINAL/Svartulfr_Lorebook_I.json
    lb1_path = FINAL / 'Svartulfr_Lorebook_I.json'
    with open(lb1_path, 'r', encoding='utf-8') as f:
        lb1_data = json.load(f)
        
    existing_lex = lb1_data.get('lexicon', [])
    existing_ids = {e.get('name'): e.get('entry_id') for e in existing_lex}
    
    added_count = 0
    for ne in new_entries:
        if ne['name'] not in existing_ids:
            existing_lex.append(ne)
            added_count += 1
            
    lb1_data['lexicon'] = existing_lex
    lb1_data['entries'] = existing_lex
    
    with open(lb1_path, 'w', encoding='utf-8') as f:
        json.dump(lb1_data, f, ensure_ascii=False, indent=2)
    with open(OPT / 'Svartulfr_Lorebook_I.json', 'w', encoding='utf-8') as f:
        json.dump(lb1_data, f, ensure_ascii=False, indent=2)
        
    print(f"Added {added_count} new entries to Lorebook I (Total: {len(existing_lex)})")

    # 4. Streamline Alyssa and Jasper Personas
    clean_a = clean_prophecy_and_intimacy(alyssa_desc, 'Alyssa')
    clean_j = clean_prophecy_and_intimacy(jasper_desc, 'Jasper')
    
    alyssa_p['description'] = clean_a
    jasper_p['description'] = clean_j
    
    with open(PERSONAS / 'Alyssa_Persona.json', 'w', encoding='utf-8') as f:
        json.dump(alyssa_p, f, ensure_ascii=False, indent=2)
    with open(PERSONAS / 'Jasper_Persona.json', 'w', encoding='utf-8') as f:
        json.dump(jasper_p, f, ensure_ascii=False, indent=2)
        
    print(f"Alyssa Persona streamlined: {len(alyssa_desc)} -> {len(clean_a)} chars")
    print(f"Jasper Persona streamlined: {len(jasper_desc)} -> {len(clean_j)} chars")

    # 5. Streamline all Character Cards
    for cfile, cname in [('Jasper_Douglas_Bloodmoon_card.json', 'Jasper')] + card_files + [('Edric_Douglas_card.json', 'Edric')]:
        cpath = FINAL / cfile
        with open(cpath, 'r', encoding='utf-8') as f:
            cdata = json.load(f)
        orig_desc = cdata.get('description', '')
        streamlined_desc = clean_prophecy_and_intimacy(orig_desc, cname)
        cdata['description'] = streamlined_desc
        with open(cpath, 'w', encoding='utf-8') as f:
            json.dump(cdata, f, ensure_ascii=False, indent=2)
        print(f"{cfile}: {len(orig_desc)} -> {len(streamlined_desc)} chars")

    print("\n[SUCCESS] Local streamlining and lore extraction completed successfully!")

if __name__ == '__main__':
    main()
