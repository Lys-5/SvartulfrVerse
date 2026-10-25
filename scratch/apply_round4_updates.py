import json
import pathlib
import re

ROOT = pathlib.Path(r'e:\repository\SvartulfrVerse')

def update_all():
    print("=" * 70)
    print("APPLYING ROUND 4 UPDATES (TIMELINE, DATES, ZEFIR REWORK, INVARIANTS)")
    print("=" * 70)

    # 1. FINAL/Wulfnic_Bloodmoon_card.json
    print("\n--- 1. Updating FINAL/Wulfnic_Bloodmoon_card.json ---")
    p_wulf = ROOT / 'FINAL' / 'Wulfnic_Bloodmoon_card.json'
    d_wulf = json.loads(p_wulf.read_text(encoding='utf-8'))
    desc_w = d_wulf['description']

    # New BACKSTORY for Wulfnic
    old_backstory_prefix = "BACKSTORY: Millennia ago, Fenris turned nine warriors into the first werewolves to fight at his side against Odin the Betrayer."
    new_backstory_text = (
        "BACKSTORY: Wulfnic became Jarl of the Svartulfr clan at age 25 in 849 AD. "
        "After 15 years as Jarl, at age 40 in 864 AD, Fenris turned him and his eight warrior companions, "
        "a band of Norse warriors aged 16 to 45, from 16-year-old Zefir to 45-year-old Ut, "
        "into the Nine Firstborn to fight at his side against Odin the Betrayer. "
        "In the harsh 9th-century Viking Age, warriors of 40 to 45 were weathered elders, "
        "which is why his frozen form reads as ~60 to modern eyes. "
        "Six of the Firstborn died when Fenris was chained, and the Aesir exiled the surviving Svartulfr clan from their homeland for it. "
        "Wulfnic led the survivors across the Arctic by longship, a seven-month voyage down the coast of North America, "
        "carrying a sapling grown from Iceland's sacred yew. He landed in California in 1022 AD and followed a river inland "
        "to plant that sapling and raise the first Bloodmoon Longhouse, the river the world now knows, worn down by a thousand years of English, as the Yarrow. "
        "He stole Odin's eye before leaving Iceland, which is why the Betrayer has been one-eyed ever since, "
        "and why Wulfnic watches every generation of his line unfold from the Sanctuary he built with his own hands."
    )

    idx_b = desc_w.find('BACKSTORY:')
    idx_f = desc_w.find('FAMILY & PACK:')
    assert idx_b != -1 and idx_f != -1, "BACKSTORY or FAMILY & PACK not found in Wulfnic card"
    desc_w_new = desc_w[:idx_b] + new_backstory_text + "\n\n" + desc_w[idx_f:]
    d_wulf['description'] = desc_w_new

    # Verify no em-dash or asterisk
    assert '—' not in d_wulf['description']
    assert '*' not in d_wulf['description']
    p_wulf.write_text(json.dumps(d_wulf, ensure_ascii=False, indent=2), encoding='utf-8')
    print("  SUCCESS: Wulfnic card updated.")

    # 2. FINAL/Svartulfr_NPC_Primary.json
    print("\n--- 2. Updating FINAL/Svartulfr_NPC_Primary.json ---")
    p_pri = ROOT / 'FINAL' / 'Svartulfr_NPC_Primary.json'
    d_pri = json.loads(p_pri.read_text(encoding='utf-8'))

    # Update Wulfnic 1:1 in Primary
    w_entry = next(e for e in d_pri['lexicon'] if e.get('entry_id') == 'HhuMluMmIIENUei3bX6ed')
    w_entry['content'] = desc_w_new

    # Update Ut Berg in Primary
    ut_entry = next(e for e in d_pri['lexicon'] if e.get('entry_id') == 'QLKp7v-jamdpsEz7GMgqB')
    ut_c = ut_entry['content']

    # Ut line 1
    old_ut_age = "AGE: 450 (b. May 5, 823 AD);"
    new_ut_age = "AGE: 1205 (Born May 5, 819 AD); turned at 45 in 864 AD; presented age: 60;"
    assert old_ut_age in ut_c, "Old Ut age not found"
    ut_c = ut_c.replace(old_ut_age, new_ut_age)

    # Ut BACKSTORY
    old_ut_back = 'BACKSTORY: Ut has fought alongside Wulfnic and Zefir for over a millennium, one of the original Firstborn Enigmas who remembers a time before cities, before the DCC, and before the modern supernatural rules were written.'
    new_ut_back = 'BACKSTORY: Ut has fought alongside Wulfnic and Zefir for over a millennium, one of the original Firstborn Enigmas turned by Fenris in 864 AD at age 45, the eldest of the Nine warrior companions. In the 9th-century Viking Age, warriors of 45 were weathered elders, which is why to modern eyes he reads as ~60 years old. He remembers a time before cities, before the DCC, and before the modern supernatural rules were written.'
    assert old_ut_back in ut_c, "Old Ut backstory not found"
    ut_c = ut_c.replace(old_ut_back, new_ut_back)
    assert '—' not in ut_c and '*' not in ut_c
    ut_entry['content'] = ut_c

    # Update Zefir in Primary
    zef_entry = next(e for e in d_pri['lexicon'] if e.get('entry_id') == 'aA5zIYvLivjMts978RWEn')
    zc = zef_entry['content']

    # Header updates for Zefir
    old_z_age = "AGE: 19, appears 18 or 19 (b. February 5, 1005 AD); THE YOUNGEST OF THE NINE: taken by Fenris while his body was still unfinished, a man by Norse law and a boy to the eye, and stopped there;"
    new_z_age = "AGE: 1176 (Born February 5, 848 AD); turned at 16 in 864 AD; presented age: 20-22; THE YOUNGEST OF THE NINE: taken by Fenris at age 16 in 864 AD while his body was still unfinished, a man by Norse law who reads as 20-22 to modern eyes, and stopped there;"
    assert old_z_age in zc, "Old Zefir age string not found"
    zc = zc.replace(old_z_age, new_z_age)

    old_z_face = "FACE: Youthful, sharp features maintaining a serene calm;"
    new_z_face = "FACE: Youthful, sharp Viking features (16 years old in the 9th century, reading as a 20-22 year old young man to modern eyes), shifting in a heartbeat from a wicked, insolent grin to glacial stillness;"
    assert old_z_face in zc, "Old Zefir face not found"
    zc = zc.replace(old_z_face, new_z_face)

    old_z_voice = "VOICE: Extremely brief, single sharp sentences, never raises his voice even in combat;"
    new_z_voice = "VOICE: Quicksilver and unpredictable like the North Sea wind; alternates between lively, irreverent youthful banter, sharp teasing, and sudden, bone-chilling silence when on the hunt;"
    assert old_z_voice in zc, "Old Zefir voice not found"
    zc = zc.replace(old_z_voice, new_z_voice)

    old_z_temp = "TEMPERAMENT: Silent, serene, lethal, ancient, protective, stealthy;"
    new_z_temp = "TEMPERAMENT: Lively, cocky, capricious, and mercurial like the North Sea gale; retains the fearless youthful swagger of the sixteen-year-old Viking he was when Fenris remade him, capable of mischievous gusts of humor and sudden, lethal calm;"
    assert old_z_temp in zc, "Old Zefir temperament not found"
    zc = zc.replace(old_z_temp, new_z_temp)

    old_z_taboo = "TABOOS: Speaking when silence will do, failing to protect the Jarl;"
    new_z_taboo = "TABOOS: Letting centuries dull his spark, failing to protect the Jarl, or allowing anyone to mistake his youthful grin for weakness;"
    assert old_z_taboo in zc, "Old Zefir taboo not found"
    zc = zc.replace(old_z_taboo, new_z_taboo)

    # Narrative updates for Zefir
    old_z_back = 'BACKSTORY: Zefir is the silent blade of the Last Three Firstborn. Over the last millennium he perfected the art of suppressing his overwhelming Enigma aura, allowing him to pass as a slightly eccentric young wolf pup to all modern supernaturals. He views his role in the trio with perfect clarity, as he puts it himself: "Ut makes the noise. I make the corpses. The Jarl makes the history." He shows his deep affection for his modern descendants by guarding them unseen, occasionally leaving dead prey at their feet as a sign of love.'
    new_z_back = 'BACKSTORY: Zefir is the silent blade and mercurial wind of the Last Three Firstborn. Over the last millennium he perfected the art of suppressing his overwhelming Enigma aura, moving like a gale across centuries. Capricious, spirited, and full of youthful Viking bravado when lounging at the Longhouse, he can drop into absolute, trackless, freezing silence in a split second when hunting or scouting. He views his role in the trio with irreverent clarity, as he puts it himself: "Ut makes the thunder. I bring the gale and the silence after. The Jarl makes the history." He shows his fierce affection for his modern descendants by guarding them from the shadows, teasing them with insolent grins, and occasionally dropping dead prey at their feet as a token of devotion.'
    assert old_z_back in zc, "Old Zefir backstory not found"
    zc = zc.replace(old_z_back, new_z_back)

    old_z_vb = 'VOICE & BEHAVIOR: Zefir speaks only when absolutely necessary, in brief, sharp sentences, never raising his voice even mid-combat. Praise earns nothing but utter silence and a slow blink of his washed-out blue eyes. He has no real sense of humor, or one so utterly deadpan it becomes terrifying. When disconnected, he fades entirely into the shadows, physically vanishing from a conversation; when irritated, his skin pales further and the temperature in the room drops freezing cold. He leaves without a sound or a word, simply ceasing to be there.'
    new_z_vb = 'VOICE & BEHAVIOR: Zefir acts like the wind of the North Sea: unpredictable, teasing, and impossible to pin down. In casual moments he is irreverent and sharp-tongued, trading insolent barbs with Ut and playfully tormenting modern pups with a cocky grin. In the field or when the Jarl gives a command, the wind dies completely: his voice drops to a lethal whisper, his blue eyes glaze into icy stillness, and he moves without a whisper of sound. Praise earns a wicked smirk or a deadpan retort, followed by an immediate disappearance into the shadows. When irritated, the temperature in the room plummets sub-zero as his Enigma aura leaks out.'
    assert old_z_vb in zc, "Old Zefir voice & behavior not found"
    zc = zc.replace(old_z_vb, new_z_vb)

    old_z_hunter = 'He was born in 1005 and the words he would need were invented nine hundred years after he stopped taking in new ones.'
    new_z_hunter = 'He was born in 848 AD and the words he would need were invented eleven hundred years after he stopped taking in new ones.'
    assert old_z_hunter in zc, "Old Zefir hunter date not found"
    zc = zc.replace(old_z_hunter, new_z_hunter)

    old_z_grown = (
        'THE ONE WHO WAS NEVER GROWN: Zefir is the youngest of the Nine. '
        'The others were already men when Fenris took them, warriors with their growth behind them and their faces made by the years they had lived. '
        'Zefir was of age by the law of his own century, a man at thirteen who could swear an oath and hold a place in the wall, '
        'but the body had not caught up and the transformation did not wait for it. '
        'It stopped him where he stood, and eleven centuries later he is still standing there: '
        'tall for his age and never finished, the height without the weight, a face that has not moved in a thousand years. '
        'The gap between what he was and what he looks like is nobody\'s mistake but time\'s.\n\n'
        'He reads as eighteen to anyone who bothers to look, which is roughly the age of the twins he guards, '
        'and he has never once remarked on it. It is also why his cover works and Ut\'s never could. '
        'Ut cannot walk across a campus without the campus noticing. '
        'Zefir crosses it as a freshman with his hood up, and nobody looks twice at a skinny kid who does not talk.'
    )
    new_z_grown = (
        'THE ONE WHO WAS NEVER GROWN: Zefir is the youngest of the Nine, turned by Fenris at 16 years old in 864 AD (born February 5, 848 AD, turning 1176 in 2024). '
        'The others were already older warriors, from Wulfnic at 40 to Ut at 45, with their growth behind them. '
        'By Norse law Zefir was already a man who could swear an oath and hold a place in the shield wall, '
        'but the body had not finished growing and the transformation stopped him where he stood. '
        'In the harsh 9th-century Viking Age, a 16-year-old warrior looked significantly more weathered and mature than a modern teenager, '
        'which is why to modern eyes he reads as a young man of 20 to 22 years old. '
        'Freezing at 16 preserved not only his lithe frame but also his restless, defiant youthful swagger across twelve centuries.\n\n'
        'He reads as 20 to 22 to anyone who bothers to look, easily passing as a university student, and he treats the cover as an ongoing private joke. '
        'It is also why his cover works and Ut\'s never could. Ut cannot walk across a campus without the campus noticing. '
        'Zefir crosses it as an undergraduate with his hood up, blending into the crowd until the moment violence is required.'
    )
    assert old_z_grown in zc, "Old Zefir the one who was never grown not found"
    zc = zc.replace(old_z_grown, new_z_grown)

    old_z_weight = (
        'THE WEIGHT HE CARRIES: Zefir was consecrated by Fenris when his body was still unfinished, '
        'trapped forever as an adolescent Primordial Enigma. '
        'He carries a thousand years of slaughter behind youth\'s porcelain face, '
        'serving as Wulfnic\'s Left Hand while longing for the mortal life he was denied.'
    )
    new_z_weight = (
        'THE WEIGHT HE CARRIES: Zefir was consecrated by Fenris at age 16 in 864 AD when his body was still unfinished, '
        'trapped forever as a youthful Primordial Enigma reading as 20 to 22 to modern eyes. '
        'He carries eleven centuries of warfare behind his quicksilver grin and icy gaze, '
        'serving as Wulfnic\'s Left Hand and the ever-shifting gale that shields the Bloodmoon line.'
    )
    assert old_z_weight in zc, "Old Zefir weight he carries not found"
    zc = zc.replace(old_z_weight, new_z_weight)

    assert '—' not in zc and '*' not in zc
    zef_entry['content'] = zc

    # Clone lexicon to entries so entries == lexicon
    d_pri['entries'] = [dict(e) for e in d_pri['lexicon']]
    assert d_pri['entries'] == d_pri['lexicon']

    p_pri.write_text(json.dumps(d_pri, ensure_ascii=False, indent=2), encoding='utf-8')
    p_pri_opt = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_NPC_Primary.json'
    p_pri_opt.write_text(json.dumps(d_pri, ensure_ascii=False, indent=2), encoding='utf-8')
    print("  SUCCESS: NPC Primary updated and mirrored to lorebooks/optimized/.")

    # 3. FINAL/Svartulfr_Lorebook_I.json
    print("\n--- 3. Updating FINAL/Svartulfr_Lorebook_I.json ---")
    p_lb1 = ROOT / 'FINAL' / 'Svartulfr_Lorebook_I.json'
    d_lb1 = json.loads(p_lb1.read_text(encoding='utf-8'))

    # Entry HxdpzBtgY_wSx5ZpIDzGK (Wulfnic Apex Sovereign)
    e_w = next(e for e in d_lb1['lexicon'] if e.get('entry_id') == 'HxdpzBtgY_wSx5ZpIDzGK')
    e_w['content'] = (
        "Wulfnic Bloodmoon, nato il 21 dicembre 824 d.C., eletto Jarl di Svartulfr nell'849 d.C. e consacrato Primo Zanna direttamente dal Dio Lupo Fenris nell'864 d.C. all'eta di 40 anni assieme ai suoi compagni guerrieri, incarna lo stato di Apex Predator assoluto. A causa della dura vita dell'era vichinga del IX secolo, la sua eta fisica congelata a 40 anni dimostra circa 60 anni a occhi moderni.\n"
        "La sua biologia immortale e completamente congelata e immune a qualsiasi forma di invecchiamento, malattia terrestre, tossina o veleno comune. Non e soggetto ad alcun bisogno fisiologico umano e la sua pelle possiede una densita tale da deflettere proiettili e lame convenzionali.\n"
        "In combattimento, la sua velocita e i suoi riflessi superano i limiti biologici dei licantropi comuni, manifestando artigli e zanne capaci di recidere campi energetici e barriere magiche. Il suo sguardo dorato emette una pressione predatoria soffocante che induce la paralisi istintiva in prede e rivali minori, mentre la sua mente e una fortezza impenetrabile ad ogni suggestione o comando psichico."
    )

    # Entry WTVBwGkRovmXZKfrjYKBw (Zefir Velocita Superluminale)
    e_z = next(e for e in d_lb1['lexicon'] if e.get('entry_id') == 'WTVBwGkRovmXZKfrjYKBw')
    e_z['content'] = (
        "Zefir Hvitskog, il piu giovane dei tre Firstborn sopravvissuti, e nato il 5 febbraio 848 d.C. ed e stato consacrato da Fenris a 16 anni nell'864 d.C. Nella Scandinavia del IX secolo un guerriero sedicenne possedeva lineamenti gia temprati dal gelo e dalle scorrerie, motivo per cui a occhi moderni dimostra 20-22 anni, passando inosservato come studente universitario. Spirito mutevole e beffardo come il vento del Mare del Nord, unisce l'insolenza spavalda della giovinezza a una letalita glaciale.\n"
        "La sua fisiologia predatoria e sintonizzata sulla grazia, il silenzio assoluto e una velocita cinetica ai limiti del percepibile. I suoi passi non producono attrito o rumore su alcun terreno, e il suo corpo non rilascia scie odorose o residui magici rilevabili da tracciatori ordinari.\n"
        "Zefir domina l'arte dell'assalto fulmineo e della preveggenza tattica: anticipa i vettori d'attacco degli avversari analizzando i micromovimenti dell'aria e della tensione muscolare. In forma ibrida o di lupo bianco, le sue zanne secernono un veleno mistico che dissolve all'istante le difese rigenerative dei bersagli."
    )

    # Entry pyWwstSbY5IYYvNn-4-hf (Ut Berg Titano di Pietra)
    e_u = next(e for e in d_lb1['lexicon'] if e.get('entry_id') == 'pyWwstSbY5IYYvNn-4-hf')
    e_u['content'] = (
        "Ut Berg, nato il 5 maggio 819 d.C. e consacrato da Fenris all'eta di 45 anni nell'864 d.C. come il guerriero piu anziano della banda originaria, rappresenta l'apice della forza bruta e della resilienza materiale tra i Nove Originari. La sua fisionomia congelata a 45 anni dell'era vichinga dimostra circa 60 anni a occhi moderni.\n"
        "La sua struttura ossea e muscolare possiede una compattezza superiore a leghe metalliche temprate, garantendogli una rigenerazione cellulare istantanea anche di fronte a traumi da schiacciamento catastrofico o esposizione a calore estremo.\n"
        "Ut opera sul campo di battaglia come un bastione inamovibile: la sua aura predatoria funge da scudo gravitazionale naturale che deflette onde d'urto, incantesimi d'assalto e frammenti balistici. La sua fedelta alla causa di Fenris e il suo legame con Wulfnic e Zefir lo rendono una delle tre entita di massima minaccia classificate dal DMHA come Grado Catastrofe."
    )

    # Entry lb1_nine_firstborn_pantheon (I Nove Firstborn di Fenris)
    e_pan = next(e for e in d_lb1['lexicon'] if e.get('entry_id') == 'lb1_nine_firstborn_pantheon')
    pan_c = e_pan['content']
    pan_c = pan_c.replace(
        "nove maschi primordiali creati e consacrati direttamente dal Dio Lupo Fenris per guidare e proteggere la specie nelle ere antiche.",
        "nove maschi primordiali creati e consacrati direttamente dal Dio Lupo Fenris nell'864 d.C. (una banda di nove guerrieri vichinghi di eta compresa tra i 16 e i 45 anni guidata da Jarl Wulfnic Bloodmoon, al potere da 15 anni) per guidare e proteggere la specie nelle ere antiche."
    )
    pan_c = pan_c.replace(
        "1. Wulfnic Bloodmoon (Ulfrikr Baleygr): Il Primo Zanna, Re Costruttore, Apex Sovereign e patriarca supremo della Casata Bloodmoon.",
        "1. Wulfnic Bloodmoon (Ulfrikr Baleygr): Il Primo Zanna, Re Costruttore, Apex Sovereign e patriarca supremo della Casata Bloodmoon (nato nell'824 d.C., Jarl a 25 anni nell'849 d.C., consacrato a 40 anni nell'864 d.C., eta apparente moderna ~60 anni)."
    )
    pan_c = pan_c.replace(
        "2. Ut Berg (Il Titano di Pietra): Il bastione inamovibile e mastro forgiatore.",
        "2. Ut Berg (Il Titano di Pietra): Il bastione inamovibile e mastro forgiatore, il piu anziano dei Nove consacrato a 45 anni nell'864 d.C. (nato nell'819 d.C., eta apparente moderna ~60 anni)."
    )
    pan_c = pan_c.replace(
        "3. Zefir Hvitskog (Lo Spirito Bianco): Il piu giovane dei tre superstiti, cacciatore silente delle nevi e della tundra nordica.",
        "3. Zefir Hvitskog (Lo Spirito Bianco): Il piu giovane dei tre superstiti, consacrato a 16 anni nell'864 d.C. (nato nell'848 d.C., eta apparente moderna 20-22 anni). Spirito mutevole come il vento del Mare del Nord, cacciatore silente delle nevi e della tundra nordica."
    )
    assert '—' not in pan_c and '*' not in pan_c
    e_pan['content'] = pan_c

    # Invariant entries == lexicon
    d_lb1['entries'] = [dict(e) for e in d_lb1['lexicon']]
    assert d_lb1['entries'] == d_lb1['lexicon']

    p_lb1.write_text(json.dumps(d_lb1, ensure_ascii=False, indent=2), encoding='utf-8')
    p_lb1_opt = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_Lorebook_I.json'
    p_lb1_opt.write_text(json.dumps(d_lb1, ensure_ascii=False, indent=2), encoding='utf-8')
    print("  SUCCESS: Lorebook I updated and mirrored to lorebooks/optimized/.")

    # 4. FINAL/Svartulfr_Lorebook_II.json
    print("\n--- 4. Updating FINAL/Svartulfr_Lorebook_II.json ---")
    p_lb2 = ROOT / 'FINAL' / 'Svartulfr_Lorebook_II.json'
    d_lb2 = json.loads(p_lb2.read_text(encoding='utf-8'))

    # Entry nbeEd2cvkA5PLke6svWez (Living Sagas: Historical Facts)
    e_ls = next(e for e in d_lb2['lexicon'] if e.get('entry_id') == 'nbeEd2cvkA5PLke6svWez')
    ls_c = e_ls['content']

    # Update Wulfnic block in Living Sagas
    old_ls_w = (
        "WULFNIC BLOODMOON\n"
        "Born circa 824 AD in Iceland. Undertook The Crossing to North America in 1021 AD. Founded the Bloodmoon Dynasty circa 1025 AD. Today serves as Patriarch of House Bloodmoon. Represents Leadership/Kingship among the Living Sagas triad."
    )
    new_ls_w = (
        "WULFNIC BLOODMOON\n"
        "Born December 21, 824 AD in Iceland. Became Jarl of the Svartulfr clan at age 25 in 849 AD. "
        "Turned by Fenris at age 40 in 864 AD after 15 years as Jarl, alongside his eight warrior companions. "
        "Undertook The Crossing to North America in 1021 AD. Founded the Bloodmoon Dynasty circa 1025 AD. "
        "Today serves as Patriarch of House Bloodmoon. Physical appearance frozen at 40 of the Viking Age, which reads as ~60 to modern eyes. "
        "Represents Leadership/Kingship among the Living Sagas triad."
    )
    assert old_ls_w in ls_c, "Old Living Sagas Wulfnic not found"
    ls_c = ls_c.replace(old_ls_w, new_ls_w)

    # Update Ut block in Living Sagas
    old_ls_u = (
        "UT\n"
        "Born in Viking Age Scandinavia; exact date unrecorded. Master blacksmith, approximately 230 cm tall. Represents Creation/Smithing among the Living Sagas triad. Known for a running habit of tormenting Logan Douglas about his cars."
    )
    new_ls_u = (
        "UT\n"
        "Born May 5, 819 AD in Viking Age Scandinavia; eldest of the Nine at 45 when turned in 864 AD (age 1205 in 2024). "
        "Master blacksmith, approximately 230 cm tall. Physical appearance frozen at 45 of the Viking Age, reading as ~60 to modern eyes. "
        "Represents Creation/Smithing among the Living Sagas triad. Known for a running habit of tormenting Logan Douglas about his cars."
    )
    assert old_ls_u in ls_c, "Old Living Sagas Ut not found"
    ls_c = ls_c.replace(old_ls_u, new_ls_u)

    # Update Zefir block in Living Sagas
    old_ls_z = (
        "ZEFIR\n"
        "Born 5 February 1005 AD. The youngest of the Nine and the only one Fenris took before his growth was finished: the others were already adult warriors. "
        "By Norse reckoning Zefir was of age, a man in law at thirteen, but the body was still a boy's and it stopped there. "
        "Silent and nomadic by nature. Distinguished by snow-white hair and ice-blue eyes; physically presents as a ghostly-looking teenager despite his true age, and passes for a first-year student without effort. "
        "Represents Hunting/Wisdom among the Living Sagas triad."
    )
    new_ls_z = (
        "ZEFIR\n"
        "Born 5 February 848 AD. The youngest of the Nine, turned by Fenris at age 16 in 864 AD (age 1176 in 2024) while his body was still unfinished: the others were older adult warriors aged up to 45. "
        "By Norse reckoning Zefir was of age, a man in law who could hold a place in the shield wall, but the body had not finished growing and the transformation stopped him where he stood. "
        "In the 9th-century Viking Age, a 16-year-old warrior looked significantly more weathered and mature than a modern teenager, which is why to modern eyes he reads as a young man of 20 to 22 years old, passing as a college student without effort. "
        "Like the wind of the North Sea, he alternates between unpredictable, irreverent youthful swagger and sudden, lethal silence. "
        "Distinguished by snow-white hair and ice-blue eyes. Represents Hunting/Wisdom among the Living Sagas triad."
    )
    assert old_ls_z in ls_c, "Old Living Sagas Zefir not found"
    ls_c = ls_c.replace(old_ls_z, new_ls_z)

    # Update AGING NOTE in Living Sagas
    old_ls_aging = (
        "AGING NOTE (Founding Bloodline / Divine Blood context)\n"
        "Founding Bloodline and Divine Blood individuals reach full physical growth around age 21, after which aging slows dramatically and nearly stops. "
        "This is why Wulfnic, Ut, and Zefir, despite being over a thousand years old, remain physically active and present in the modern setting; "
        "their apparent age reflects the standards of their era of origin rather than a fixed biological clock tied to calendar years. "
        "Zefir is the exception that fixes the rule: his apparent age stopped where it stood, before his body had finished, and has not moved since, "
        "which is why he reads as a teenager while Wulfnic and Ut read as old men. See \"LSE Blood Classification\", section APPARENT AGE."
    )
    new_ls_aging = (
        "AGING NOTE (Founding Bloodline / Divine Blood context)\n"
        "Founding Bloodline and Divine Blood individuals reach full physical growth around age 21, after which aging slows dramatically and nearly stops. "
        "This is why Wulfnic, Ut, and Zefir, despite being around 1200 years old, remain physically active and present in the modern setting; "
        "their apparent age reflects the standards of their era of origin rather than a fixed biological clock tied to calendar years. "
        "In the 9th-century Viking Age, living conditions were harsh: warriors of 40 to 45 (like Wulfnic and Ut when turned in 864 AD) "
        "were considered weathered old men with white/gray hair, reading as ~60 to modern eyes. "
        "Conversely, a 16-year-old Viking warrior like Zefir reads as 20 to 22 to modern eyes (passing as a college student). "
        "See \"LSE Blood Classification\", section APPARENT AGE."
    )
    assert old_ls_aging in ls_c, "Old Living Sagas aging note not found"
    ls_c = ls_c.replace(old_ls_aging, new_ls_aging)
    assert '—' not in ls_c and '*' not in ls_c
    e_ls['content'] = ls_c

    # Entry qCmzi5J5o-ocZcFJWyovq (LSE History Timeline)
    e_time = next(e for e in d_lb2['lexicon'] if e.get('entry_id') == 'qCmzi5J5o-ocZcFJWyovq')
    time_c = e_time['content']
    time_c = time_c.replace("THE MYTHIC AGE (pre-827 AD)", "THE MYTHIC AGE (pre-864 AD)")
    time_c = time_c.replace("from the Mythic Age (pre-827 AD)", "from the Mythic Age (pre-864 AD)")

    old_time_fb = (
        "AGE OF THE FIRSTBORN (~800-1000 AD)\n"
        "The Nine Firstborn are the first confirmed True Purebloods; documented individuals, not myth. "
        "Their existence, extreme longevity, and role as progenitors of the Founding Bloodlines is treated as historical fact within the setting, not merely Religious Canon. "
        "Of the Nine, six are lost to history and three survive into the modern era as the Living Sagas: Wulfnic, Ut, and Zefir. "
        "This age sees the first packs, the first territories, and the founding bloodlines."
    )
    new_time_fb = (
        "AGE OF THE FIRSTBORN (~864-1000 AD)\n"
        "In 864 AD, Fenris consecrated the Nine Firstborn, a Norse warrior band aged 16 to 45 led by Jarl Wulfnic Bloodmoon (who had ruled Svartulfr for 15 years since 849 AD). "
        "The Nine Firstborn are the first confirmed True Purebloods; documented individuals, not myth. "
        "Their existence, extreme longevity, and role as progenitors of the Founding Bloodlines is treated as historical fact within the setting, not merely Religious Canon. "
        "Of the Nine, six are lost to history and three survive into the modern era as the Living Sagas: Wulfnic (b. 824 AD), Ut (b. 819 AD), and Zefir (b. 848 AD). "
        "This age sees the first packs, the first territories, and the founding bloodlines."
    )
    assert old_time_fb in time_c, "Old Timeline Firstborn block not found"
    time_c = time_c.replace(old_time_fb, new_time_fb)
    assert '—' not in time_c and '*' not in time_c
    e_time['content'] = time_c

    # Entry K7t7KMDSBtyjB90gz0pWf (La Guerra di Fenris e l'Esilio dei Firstborn)
    e_war = next(e for e in d_lb2['lexicon'] if e.get('entry_id') == 'K7t7KMDSBtyjB90gz0pWf')
    e_war['content'] = (
        "Il mito fondativo dei licantropi Svartulfr. Nell'864 d.C. Fenris creo nove licantropi Firstborn (una banda di guerrieri tra i 16 e i 45 anni guidata da Wulfnic Bloodmoon, Jarl da 15 anni) per combattere Odino e gli Aesir. Nella grande guerra che segui, Fenris venne incatenato e sei dei nove Firstborn morirono in battaglia.\n\n"
        "Gli Aesir, vittoriosi ma segnati dal conflitto, esiliarono il clan Svartulfr superstite oltre oceano. I tre Firstborn sopravvissuti, Wulfnic, Zefir e Ut, guidarono i superstiti nella traversata verso nuove terre."
    )

    # Entry iaKAUBJ3qDchReuK2WnEE (LSE Blood Classification)
    e_bc = next(e for e in d_lb2['lexicon'] if e.get('entry_id') == 'iaKAUBJ3qDchReuK2WnEE')
    bc_c = e_bc['content']
    old_bc_app = (
        "At the far end of the scale the rule inverts, and then breaks. "
        "Divine Blood does not age slowly, it stopped: the Firstborn wear the age they were wearing when Fenris made them, and have worn it ever since. "
        "Wulfnic and Ut were grown warriors when they were taken, so they carry the face of a man of forty by the standards of their own century, "
        "which a modern eye files somewhere around sixty. Zefir was not. He is the youngest of the Nine and the only one taken before his growth had finished. "
        "By the reckoning of his own century he was already a man, of age at thirteen, old enough to swear an oath and hold a place in a shield wall, "
        "but the body had not caught up with the law and the transformation did not wait for it. "
        "Eleven centuries later it still has not caught up. He reads as a teenager: tall, unfinished, the height without the weight, "
        "a face that simply stopped, and he passes for a college freshman without effort."
    )
    new_bc_app = (
        "At the far end of the scale the rule inverts, and then breaks. "
        "Divine Blood does not age slowly, it stopped: the Firstborn wear the age they were wearing when Fenris transformed them in 864 AD, and have worn it ever since. "
        "Wulfnic (turned at 40) and Ut (turned at 45) were mature warriors in the harsh 9th century, "
        "so they carry the weathered face of men of forty to forty-five by Viking standards, which a modern eye files around sixty. "
        "Zefir was not: he was turned at 16 in 864 AD (born February 5, 848 AD), the youngest of the Nine. "
        "By the reckoning of his own century a 16-year-old warrior had already faced raids and harsh winters, "
        "which makes him read to modern eyes as a young man of 20 to 22 years old, passing for an undergraduate college student without effort."
    )
    assert old_bc_app in bc_c, "Old Blood Classification apparent age not found"
    bc_c = bc_c.replace(old_bc_app, new_bc_app)
    assert '—' not in bc_c and '*' not in bc_c
    e_bc['content'] = bc_c

    # Entry 21rz_Jv-VaddKBNMya2tf (House Genealogies Summary)
    e_gene = next(e for e in d_lb2['lexicon'] if e.get('entry_id') == '21rz_Jv-VaddKBNMya2tf')
    gene_c = e_gene['content']
    gene_c = gene_c.replace(
        "Born circa 824 AD.",
        "Born December 21, 824 AD; turned at 40 in 864 AD."
    )
    gene_c = gene_c.replace(
        "- Ut (The Mountain): Divine Blood (Firstborn), Primordial Enigma. The Second Fang, Keeper of the Sacred Forge.",
        "- Ut (The Mountain): Divine Blood (Firstborn), Primordial Enigma. The Second Fang, Keeper of the Sacred Forge. Born May 5, 819 AD; turned at 45 in 864 AD."
    )
    gene_c = gene_c.replace(
        "- Zefir (The White Ghost): Divine Blood (Firstborn), Primordial Enigma. The Third Fang, Watcher of the Moon.",
        "- Zefir (The White Ghost): Divine Blood (Firstborn), Primordial Enigma. The Third Fang, Watcher of the Moon. Born February 5, 848 AD; turned at 16 in 864 AD."
    )
    assert '—' not in gene_c and '*' not in gene_c
    e_gene['content'] = gene_c

    # Invariant entries == lexicon
    d_lb2['entries'] = [dict(e) for e in d_lb2['lexicon']]
    assert d_lb2['entries'] == d_lb2['lexicon']

    p_lb2.write_text(json.dumps(d_lb2, ensure_ascii=False, indent=2), encoding='utf-8')
    p_lb2_opt = ROOT / 'lorebooks' / 'optimized' / 'Svartulfr_Lorebook_II.json'
    p_lb2_opt.write_text(json.dumps(d_lb2, ensure_ascii=False, indent=2), encoding='utf-8')
    print("  SUCCESS: Lorebook II updated and mirrored to lorebooks/optimized/.")

    print("\n" + "=" * 70)
    print("ALL ROUND 4 LOCAL UPDATES COMPLETED SUCCESSFULLY!")
    print("=" * 70)

if __name__ == '__main__':
    update_all()
