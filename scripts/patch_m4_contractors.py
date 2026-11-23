#!/usr/bin/env python3
"""
Patch script for Milestone 4:
Applies standard RPG headers, age alignments, traits, and 9 contextual outfits to all 8 Contractor cards.
"""

import json
from pathlib import Path

FINAL = Path(__file__).resolve().parent.parent / "FINAL"

# -----------------------------------------------------------------------------
# 1. JASPER CONTRACTOR CARDS
# -----------------------------------------------------------------------------
jasper_rpg_block = """

RPG STATS & TRAITS:
[LEVEL: 2; ARC_LEVEL: 3.8 (Spikes 4.2+ with #07); SPECIES: Licantropo (Werewolf Enigma) (STR +3, PER +2, END +3, INT +1); OCCUPATION: Technomancer / Cyber-Mage (PER +3, END -1, INT +4, AGI +1); CLASS: DDM Contractor #08 (Solulfr)]
[STATS: STR 22; PER 26; END 24; CHA 14; INT 30; AGI 18; LCK 12]
TRAITS:
- Enigma Biology (STR +2, END +2): Dense muscular and skeletal structure, superhuman physical power, canine baculum and knot.
- Founding Bloodline (STR +1, END +2, CHA +2): Direct lineage of the historic founding families. Exemplifies generational leadership, formidable vitality, and undisputed ancestral authority.
- Pureblood Lineage (PER +1, END +1, CHA +1): Unbroken aristocratic heritage preserving refined lupine senses, noble poise, and genetic consistency across centuries.
- Technomantic Data Resonance (STR -1, PER +2, INT +3): Capacita di percepire il flusso di bit e la fibra ottica come tessuto eterico vivo, canalizzando incantesimi attraverso circuiti elettronici e reti digitali.
- Tech Savvy (INT +2): Digital expertise, drone piloting, systems intrusion, and DCC tech.
- Mastermind (PER +1, CHA -1, INT +2): Superior strategic planning, legal and corporate cunning, and long-range tactical foresight.
- Familiar Soulbound Synergy (PER +2, CHA +1, INT +2): Legame simbiotico profondo con un compagno animale sovrannaturale, con condivisione di percezione sensoriale e risonanza aurica.
- Lupine Senses (PER +2): Acute scent tracking and predatory hearing.
- Partial Shift Mastery (PER +1, AGI +1): Flawless daily command over lupine partial transformations (ears, tail, claws, scent tracking) without losing emotional composure.
- Regenerative Factor (END +2): Cellular rapid healing closing lacerations and physical wounds in minutes.
- Silver Allergy (END -2): Severe physiological vulnerability and tissue rejection to refined silver.
- Dungeon Veteran (STR +1, INT +1): Hardened survivor of reality tears, dungeons, and spatial breaches.
- The Weight He Carries (END +1, CHA -1, INT +1): Haunted by solemn secrets, profound grief, or the heavy burden of duty that hardens internal resolve.
- Immortal Contractor (END +2, LCK +1): Functionally immortal entity bound to The Cause in Voidspace.
- Rebel Heart / Underground (STR +1, CHA -1, AGI +1): Defiance of high-society pretenses, affinity for grease, bikes, counter-culture, and subterranean music."""

jasper_terme_outfit = {
    "id": "ddm_terme_08",
    "name": "beach / terme",
    "image_url": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2ff0fec6-331a-459a-74f3-33ffb35d4100/public",
    "description": "Abbigliamento: Boxer da bagno tecnici neri idrorepellenti a vita bassa con asola elastica posteriore rinforzata per la coda lupina. Torso nudo scolpito e compatto da 198 cm, spalle possenti segnate da venature runiche e muscolatura Enigma densa.\nAccessori: Asciugamano scuro in microfibra Voidspace ripiegato sulla spalla.\nScarpe: Ciabatte anatomiche nere in polimero antiscivolo.\nGioielli: Piastrina identificativa DDM #08 al collo e tatuaggio Gebo al polso sinistro; marchio di Sol sull'anca destra esposto alla luce termale.\nTrucco: Gocce d'acqua termale sul petto e sulle clavicole; sguardo verde menta rilassato e vigile.\nAcconciatura: Capelli castano-caramello umidi e spettinati all'indietro; orecchie lupine fulve con punte nere e doppi anelli d'argento erette a captare ogni eco nei vapori.",
    "avatar_transparent": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/1846eda2-faea-4df6-b465-ca6114b9e800/public",
    "avatar_transparent_source": "https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/2ff0fec6-331a-459a-74f3-33ffb35d4100/public"
}

def patch_jasper(filepath):
    if not filepath.exists():
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        card = json.load(f)
    
    # Canonical height fix
    card['description'] = card['description'].replace(
        'HEIGHT: 198 cm (6\'6" Partial), 230 cm (7\'6" Hybrid);',
        'HEIGHT: 193 cm Base (6\'4") / 198 cm Enigma Partial (6\'6"), 230 cm (7\'6") Hybrid;'
    )
    if 'RPG STATS & TRAITS:' not in card['description']:
        card['description'] += jasper_rpg_block

    for o in card.get('outfits', []):
        if 'nude' in o.get('name', '').lower():
            o['name'] = 'nude'

    if len(card.get('outfits', [])) == 8:
        card['outfits'].append(jasper_terme_outfit)

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    print(f"Patched {filepath.name}: {len(card['outfits'])} outfits")

# -----------------------------------------------------------------------------
# 2. ADAM VALENCIA (CONTRACTOR #02A)
# -----------------------------------------------------------------------------
adam_rpg_block = """

RPG STATS & TRAITS:
[LEVEL: 4; ARC_LEVEL: 3.5 [medicated] / 4.2 [raw]; SPECIES: Immortal Contractor (Arctic Wolf) (STR +2, PER +3, END +2, AGI +2); OCCUPATION: Co-Head of Anomalous Objects and Creatures (A.O.C.) (PER +3, INT +2, CHA +2); CLASS: Dual Construct Combatant & Environmental Manipulator]
[STATS: STR 18; PER 22; END 18; CHA 16; INT 20; AGI 20; LCK 14]
TRAITS:
- Dual Construct Vessel: Single soul split across two separate bodies (#02A and #02H) with continuous telepathic resonance and emotional symbiosis.
- Arctic Wolf Shifter: Supernatural lupine agility, enhanced cold resistance, and pure white predatory stealth.
- Environmental Architect: Active manipulation of terrain, structural matter, and spatial layouts during breach containment.
- Blade Virtuoso: Lethal dual-wielding swordsmanship honed across centuries of close-quarters combat.
- Sarcastic Charisma: Easy-going American charm and sardonic humor masking ancient trauma and identity dysmorphia.
- Council Emotional Suppressants: Chemically dampened emotional peaks to maintain stable 3.5 ARC levels and avoid destructive 4.2 spikes.
- Immortal Contractor: Functionally immortal biology impervious to mortal aging, diseases, and standard fatal wounds.
- The Weight He Carries: Centuries of erased memories and Council wipes fighting to preserve genuine personhood alongside Hana."""

adam_outfits = [
    {
        "id": "adam_casual",
        "name": "casual",
        "description": "Abbigliamento: Felpa oversize antracite scuro con cappuccio arrotolato sui gomiti, t-shirt grafica consumata, jeans scuri elasticizzati con asola posteriore per la coda lupina e stivaletti in pelle nera vissuta.\nAccessori: Bracciale in cuoio e acciaio al polso destro.\nScarpe: Stivaletti stringati in pelle nera con suola ammortizzata.\nGioielli: Sottile catenina d'argento e anello d'acciaio; cicatrice 'II' alla nuca.\nTrucco: Leggera barba incolta di tre giorni ben curata; occhi eterocromatici rosa e blu vigili.\nAcconciatura: Capelli bianco candido arruffati che ricadono sulle spalle attorno a un paio di orecchie lupine bianche."
    },
    {
        "id": "adam_business",
        "name": "business / mission",
        "description": "Abbigliamento: Giacca operativa DDM A.O.C. in Void-Weave bianco fumo e grigio antracite con patch '#02A' sulla spalla, maglia tecnica traspirante, pantaloni cargo modulari antistrappo con asola rinforzata per la coda e foderi dorsali per lame corte.\nAccessori: Doppia fondina dorsale a sgancio rapido per lame in lega anomala; cintura tattica con fiale di soppressori emozionali.\nScarpe: Anfibi tattici scuri rinforzati con suola fonoassorbente.\nGioielli: Piastrina d'acciaio DDM #02A al collo.\nTrucco: Naturale, concentrato e rilassato; lievi riflessi eterei negli occhi eterocromatici.\nAcconciatura: Capelli bianchi parzialmente legati dietro la nuca, lasciando libere le orecchie da lupo artico."
    },
    {
        "id": "adam_formal",
        "name": "gala / formal",
        "description": "Abbigliamento: Abito sartoriale due pezzi nero ossidiana con rever in seta avorio, camicia bianca elegante sbottonata al primo bottone, pantaloni su misura sagomati posteriormente per la coda e scarpe stringate lucide.\nAccessori: Orologio da polso vintage in platino con indicatore di deviazione dimensionale.\nScarpe: Scarpe stringate in vernice nera.\nGioielli: Anello sigillo con incisione romana 'II' all'anulare sinistro.\nTrucco: Viso pulito e curato, sguardo bicolore brillante e sorriso sornione.\nAcconciatura: Capelli bianco candido pettinati all'indietro con ciuffi morbidi attorno alle orecchie lupine erette."
    },
    {
        "id": "adam_party",
        "name": "party / club",
        "description": "Abbigliamento: Camicia di seta nera aperta sul petto atletico, pantaloni in pelle nera aderenti con apertura sacrale per la coda, cintura borchiata in argento e stivali bassi a punta.\nAccessori: Bracciali rigidi in argento ossidato e ciondolo a prisma.\nScarpe: Stivaletti alla caviglia in cuoio nero lucido.\nGioielli: Catenina d'argento con piccolo pendente e orecchini a cerchio.\nTrucco: Bagliori luminescenti accentuati nelle iridi rosa e blu sotto le luci stroboscopiche.\nAcconciatura: Capelli bianchi disordinati e ribelli dal fascino magnetico."
    },
    {
        "id": "adam_beach",
        "name": "beach / terme",
        "description": "Abbigliamento: Boxer da bagno sportivi color grigio fumo con dettagli grafici bianchi e asola posteriore rinforzata per la coda. Torso nudo atletico e tonico da 188 cm (6'2\") per 88 kg solcato da antiche cicatrici.\nAccessori: Telo mare in microfibra scura DDM poggiato sulla spalla.\nScarpe: Ciabatte da piscina ergonomiche nere.\nGioielli: Catenina con piastrina identificativa DDM #02A e cicatrice 'II' alla nuca esposta al sole.\nTrucco: Gocce d'acqua che scorrono sul petto; sguardo limpido e divertito.\nAcconciatura: Capelli bianchi bagnati tirati all'indietro con orecchie lupine chiare scosse dall'acqua."
    },
    {
        "id": "adam_sleep",
        "name": "sleep",
        "description": "Abbigliamento: Pantaloni da pigiama morbidi in cotone antracite a vita elasticizzata con apertura per la coda, torso nudo, comodo e disteso sul divano del penthouse DDM accanto ad Hana.\nAccessori: Nessuno.\nScarpe: Nessuna, a piedi nudi.\nGioielli: Nessuno.\nTrucco: Espressione rilassata, assopita e priva di tensioni.\nAcconciatura: Capelli bianchi morbidamente sparsi sul cuscino."
    },
    {
        "id": "adam_nude",
        "name": "nude",
        "description": "Abbigliamento: Nessuno. Completo nudo anatomico naturale. Corporatura atletica europea possente e scolpita da 188 cm (6'2\") per 88 kg, con spalle larghe, pettorali cesellati, addome definito a otto tasselli e braccia muscolose segnate da antiche cicatrici di battaglia.\nAccessori: Nessuno.\nScarpe: Nessuna. Piedi nudi agili e silenziosi con pianta plantare callosa.\nGioielli: Cicatrice a forma di numero romano 'II' impressa alla base della nuca; nessun gioiello metallico.\nTrucco: Carnagione chiara con leggera barba incolta curata; occhi eterocromatici luminescenti (uno rosa e uno blu) che brillano lievemente nell'oscurita; zanne lupine affilate; anatomia genitale maschile sana, naturale e non censurata.\nAcconciatura: Capelli bianco puro spettinati che scendono fino alle spalle; singolo paio di orecchie da lupo artico bianco erette e mobili sulla sommita del capo; morbida e folta coda da lupo artico bianco che spunta naturale dall'apertura sacrale."
    },
    {
        "id": "adam_hybrid",
        "name": "hybrid shift / mutation",
        "description": "Abbigliamento: Nessuno indosso; abiti lacerati dalla metamorfosi. Forma ibrida bipede da lupo artico possente di 220 cm di statura con densa pelliccia bianco candido, muso lupino allungato, zanne micidiali e artigli affilati capaci di fendere metallo e roccia.\nAccessori: Nessuno.\nScarpe: Zampe plantari con cuscinetti neri induriti e artigli retrattili.\nGioielli: Segno 'II' visibile sottopelle tra i peli della nuca.\nTrucco: Iridi rosa e blu incandescenti cariche di risonanza ARC; respiro che gela l'aria circostante.\nAcconciatura: Folta criniera candida che circonda il collo e le spalle taurine; orecchie lupine erette."
    },
    {
        "id": "adam_fullshift",
        "name": "full shift / other",
        "description": "Abbigliamento: Nessuno. Forma quadrupede lupina completa da lupo artico (Canis lupus arctos) di taglia superiore alla norma, con fitto mantello serico bianco candido che isola dal vuoto termico, passo silenzioso, occhi eterocromatici rosa e blu attenti e corporatura muscolosa da predatore instancabile.\nAccessori: Nessuno.\nScarpe: Zampe da lupo artico con artigli da presa su neve e superfici lisce.\nGioielli: Nessuno.\nTrucco: Fisionomia da lupo artico con tartufo nero umido e dentatura ferale intatta.\nAcconciatura: Doppio mantello fitto e compatto con folta coda candida che bilancia ogni scatto."
    }
]

def patch_adam(filepath):
    if not filepath.exists():
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        card = json.load(f)
    
    # Age update
    card['description'] = card['description'].replace(
        'AGE: Centuries-old (Born Medieval Europe);',
        'AGE: 28 at mortal death (Centuries-old Contractor);'
    )
    if 'RPG STATS & TRAITS:' not in card['description']:
        card['description'] += adam_rpg_block

    card['outfits'] = adam_outfits
    card['default_outfit'] = 'adam_casual'

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    print(f"Patched {filepath.name}: {len(card['outfits'])} outfits")

# -----------------------------------------------------------------------------
# 3. HANA VALENCIA (CONTRACTOR #02H)
# -----------------------------------------------------------------------------
hana_rpg_block = """

RPG STATS & TRAITS:
[LEVEL: 4; ARC_LEVEL: 3.5 [medicated] / 4.2 [raw]; SPECIES: Immortal Contractor (Arctic Wolf) (STR +2, PER +3, END +2, AGI +2); OCCUPATION: Co-Head of Anomalous Objects and Creatures (A.O.C.) (PER +3, INT +2, CHA +2); CLASS: Dual Construct Retrieval Specialist & Spatial Slicer]
[STATS: STR 16; PER 24; END 18; CHA 16; INT 22; AGI 20; LCK 14]
TRAITS:
- Dual Construct Vessel: Single soul split across two separate bodies (#02H and #02A) with continuous telepathic resonance and emotional symbiosis.
- Arctic Wolf Shifter: Supernatural lupine agility, enhanced cold resistance, and pure white predatory stealth.
- Cross-Dimensional Retrieval: Slicing reality boundaries to locate, snatch, and quarantine volatile anomalous objects and artifacts.
- Blade Virtuoso: Fast, precision dual-blade martial arts combined with spatial acceleration.
- Fierce Loyalty: Protective, volatile temperament defending her A.O.C. ACE family and her other half Adam with unyielding ferocity.
- Council Emotional Suppressants: Chemically dampened emotional peaks to maintain stable 3.5 ARC levels and avoid destructive 4.2 spikes.
- Immortal Contractor: Functionally immortal biology impervious to mortal aging, diseases, and standard fatal wounds.
- The Weight She Carries: Centuries of erased memories and Council wipes fighting to preserve genuine personhood alongside Adam."""

hana_outfits = [
    {
        "id": "hana_casual",
        "name": "casual",
        "description": "Abbigliamento: Maglione oversize in maglia color panna morbida che scivola su una spalla, leggings neri elasticizzati con asola posteriore per la coda bianca, stivaletti bassi scuri e collanina sottile in argento.\nAccessori: Borsa a tracolla compatta con scomparto schermato per oggetti anomali.\nScarpe: Stivaletti bassi in pelle nera con cerniera laterale.\nGioielli: Sottile collana in argento con ciondolo geometrico; cicatrice 'II' alla nuca.\nTrucco: Acqua e sapone con balsamo labbra trasparente; occhi eterocromatici rosa e blu intensi.\nAcconciatura: Lunghi capelli bianco candido sciolti in morbide onde attorno a due orecchie lupine bianche erette."
    },
    {
        "id": "hana_business",
        "name": "business / mission",
        "description": "Abbigliamento: Tuta operativa DDM A.O.C. in Void-Weave bianco latte e ardesia con patch '#02H' sulla spalla, colletto alto rinforzato, imbracatura modulare con foderi per lame da lancio e fiale di stasi dimensionale, pantaloni tattici con asola rinforzata per la coda.\nAccessori: Guanti tattici rinforzati con polpastrelli conduttivi per sigilli dimensionali; visore ARC.\nScarpe: Anfibi tattici leggeri neri con battistrada antiscivolo.\nGioielli: Piastrina identificativa DDM #02H al collo.\nTrucco: Sguardo vigile e severo; lievi riflessi rosa e blu sulle pupille.\nAcconciatura: Capelli bianchi raccolti in una coda alta elegante tra le orecchie da lupo artico."
    },
    {
        "id": "hana_formal",
        "name": "gala / formal",
        "description": "Abbigliamento: Abito da sera lungo fino a terra in seta grigio perla con scollatura all'americana, schiena scoperta sagomata per la coda lupina bianca e spacco laterale profondo, abbinato a stole di velluto scuro.\nAccessori: Pochette rigida in platino schermato.\nScarpe: Décolleté nere a tacco medio.\nGioielli: Orecchini pendenti in platino con zaffiri blu e tormaline rosa; anello con numero romano 'II'.\nTrucco: Make-up sobrio ed elegante con eyeliner sottile e labbra color ciliegia chiaro.\nAcconciatura: Elegante chignon morbido alla nuca che lascia scoperte le orecchie lupine candide."
    },
    {
        "id": "hana_party",
        "name": "party / club",
        "description": "Abbigliamento: Top corto a corsetto in velluto nero scollato, giacchino in pelle corta scura, minigonna in denim grigio con asola posteriore per la coda e stivali alti al ginocchio.\nAccessori: Choker in pelle nera con anellino argentato al collo.\nScarpe: Stivali alti al ginocchio in morbida pelle nera.\nGioielli: Cerchietti sottili in argento appuntati sull'orecchio lupino sinistro.\nTrucco: Ombretto fumé leggero che esalta la disparita cromatica delle iridi rosa e blu.\nAcconciatura: Capelli bianchi ondulati lasciati liberi lungo la schiena."
    },
    {
        "id": "hana_beach",
        "name": "beach / terme",
        "description": "Abbigliamento: Bikini sportivo a due pezzi color ardesia e bianco con fascia elastica sicura, che evidenzia la silhouette tonica e femminile da 180 cm (5'11\") per 65 kg; asola di sostegno per la coda lupina.\nAccessori: Pareo leggero trasparente legato al fianco e occhiali da sole scuri.\nScarpe: Sandali bassi minimalisti.\nGioielli: Piastrina DDM #02H e cicatrice 'II' esposta sulla nuca chiara.\nTrucco: Viso fresco e bagnato da spruzzi d'acqua; labbra idratate.\nAcconciatura: Capelli bianchi raccolti in una treccia morbida che scende lungo la spalla."
    },
    {
        "id": "hana_sleep",
        "name": "sleep",
        "description": "Abbigliamento: Canotta morbida in seta grigio fumo e pantaloncini da notte elasticizzati con ampia asola posteriore per la coda, rilassata sul letto matrimoniale del penthouse DDM accanto ad Adam.\nAccessori: Nessuno.\nScarpe: Nessuna, a piedi nudi.\nGioielli: Nessuno.\nTrucco: Completamente struccata, viso dolce e lineamenti distesi nel riposo.\nAcconciatura: Capelli bianchi sciolti a ventaglio sul cuscino."
    },
    {
        "id": "hana_nude",
        "name": "nude",
        "description": "Abbigliamento: Nessuno. Completo nudo anatomico naturale. Silhouette femminile atletica, tonica e sinuosa da 180 cm (5'11\") per 65 kg, con curve armoniose, seno pieno e sodo, addome piatto e gambe lunghe e scattanti temprate da secoli di addestramento acrobatico.\nAccessori: Nessuno.\nScarpe: Nessuna. Piedi nudi aggraziati e veloci con pianta curata.\nGioielli: Cicatrice a forma di numero romano 'II' impressa alla base della nuca; nessun monile.\nTrucco: Pelle serica color avorio immacolata; occhi eterocromatici magnetici (uno rosa e uno blu) che scintillano con bagliori eterei; labbra naturalmente rosee e zanne affilate; anatomia genitale femminile sana, proporzionata e non censurata.\nAcconciatura: Lunghi capelli bianco candido setosi che ricadono morbidi fino a meta schiena; singolo paio di soffici orecchie da lupo artico bianco mobili sul capo; folta e candida coda lupina espressiva che spunta naturale dall'osso sacro."
    },
    {
        "id": "hana_hybrid",
        "name": "hybrid shift / mutation",
        "description": "Abbigliamento: Nessuno indosso. Forma licantropica ibrida bipede di 205 cm con manto fitto color bianco serico, muscolatura flessuosa ed elastica, zanne da predatrice artica, artigli ricurvi d'ebano e riflessi spaziali azzurri lungo le braccia.\nAccessori: Nessuno.\nScarpe: Zampe posteriori digitigradi con cuscinetti plantari scuri e artigli micidiali.\nGioielli: Marchio 'II' bioluminescente tra i peli candidi della nuca.\nTrucco: Bagliori ipnotici rosa e blu negli occhi a fessura; respiro vaporoso e freddo.\nAcconciatura: Criniera vaporosa bianca serica attorno al collo; orecchie lupine erette."
    },
    {
        "id": "hana_fullshift",
        "name": "full shift / other",
        "description": "Abbigliamento: Nessuno. Forma quadrupede lupina completa da lupa artica (Canis lupus arctos) elegante e letale, con doppio mantello bianco latte lucente, silhouette scattante, occhi penetranti rosa e blu e passo vellutato capace di percorrere fratture dimensionali.\nAccessori: Nessuno.\nScarpe: Cuscinetti plantari soffici e artigli da caccia artica.\nGioielli: Nessuno.\nTrucco: Profilo ferale nobile con tartufo scuro umido e zanne candide affilate.\nAcconciatura: Manto fitto uniforme con foltissima coda candida a pennacchio."
    }
]

def patch_hana(filepath):
    if not filepath.exists():
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        card = json.load(f)
    
    # Age update
    card['description'] = card['description'].replace(
        'AGE: Centuries-old (Born Medieval Europe);',
        'AGE: 28 at mortal death (Centuries-old Contractor);'
    )
    if 'RPG STATS & TRAITS:' not in card['description']:
        card['description'] += hana_rpg_block

    card['outfits'] = hana_outfits
    card['default_outfit'] = 'hana_casual'

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    print(f"Patched {filepath.name}: {len(card['outfits'])} outfits")

# -----------------------------------------------------------------------------
# 4. DULLAHAN (CONTRACTOR #04)
# -----------------------------------------------------------------------------
dullahan_rpg_block = """

RPG STATS & TRAITS:
[LEVEL: 5; ARC_LEVEL: 4.5; SPECIES: Immortal Contractor (Irish Wolfhound) (STR +3, END +3, CHA -1, INT +1); OCCUPATION: Head of the Euclidean Division (PER +3, INT +3, AGI +1); CLASS: Spatial Weaver & Reality Executioner]
[STATS: STR 22; PER 22; END 24; CHA 10; INT 22; AGI 16; LCK 14]
TRAITS:
- Headless Humanoid & Void Mist: Decapitated physiology crowned by a perpetual vortex of shifting black mist under his executioner's hood.
- Irish Wolfhound Shifter: Immense, towering canine power, colossal bone density, and ancient tracking instinct.
- Euclidean Reality Bending: Sovereign mastery over non-Euclidean space, folding distances, repairing spatial tears, and trapping anomalies.
- Executioner's Hook-Axe: Summoned spectral black-iron hook-axe capable of cleaving dimensional seams and physical matter alike.
- Laconic Dominance: Unflappable, crass, and completely unimpressed demeanor that radiates quiet dread to subordinates and enemies.
- Feline Sanctuary: Soft paternal affection toward domestic cats and kittens, harboring dozens within his HQ residence alongside ACEs Bartholomew and Madge.
- Immortal Contractor: Functionally immortal existence immune to mortal decay, fatal injuries, and temporal erasure.
- The Hood Never Drops: Absolute existential rule preserving his headless vortex hidden beneath cloth and shadow in all contexts."""

dullahan_outfits = [
    {
        "id": "dullahan_casual",
        "name": "casual",
        "description": "Abbigliamento: Felpa grigia sportiva oversize da allenatore con cappuccio pesante tirato avanti a coprire il collo fumoso, pantaloni sportivi neri larghi con asola per la coda canina e scarpe da ginnastica robuste.\nAccessori: Fischietto metallico al collo appoggiato sopra la sciarpa scura; gattino tigrato accucciato nella tasca a marsupio.\nScarpe: Scarpe da ginnastica nere a suola larga ammortizzata.\nGioielli: Nessuno.\nTrucco: Nessun volto visibile; densa nebbia nera che ribolle lentamente sotto il cappuccio.\nAcconciatura: Nessun capello; orecchie canine da Irish Wolfhound grigie che spuntano dalle aperture laterali del cappuccio."
    },
    {
        "id": "dullahan_business",
        "name": "business / mission",
        "description": "Abbigliamento: Pastrano lungo da boia in pesante tela dimensionale antracite idrorepellente con collo rigido rialzato, cappuccio da esecutore cucito a mano da cui fuoriesce fumo nero, pantaloni da lavoro in tessuto corazzato con asola per la coda e stivali rinforzati.\nAccessori: Ascia da boia ad uncino in ferro abissale assicurata alla schiena con cinghie di cuoio grezzo.\nScarpe: Stivali da combattimento pesanti in cuoio nero con puntale rinforzato.\nGioielli: Marchio a numero romano 'IV' inciso sulla scapola sinistra.\nTrucco: Nessuna testa anatomica; solo il vortice di nebbia scura che pulsa nell'ombra.\nAcconciatura: Orecchie da Irish Wolfhound grigio topo che spuntano dal cappuccio scuro."
    },
    {
        "id": "dullahan_formal",
        "name": "gala / formal",
        "description": "Abbigliamento: Completo tre pezzi sartoriale nero notte tagliato su misura per la sua colossale stazza di 203 cm, camicia scura con cravatta di seta grigia avvolta alla base del fumo del collo, giacca con apertura posteriore discreta per la coda e scarpe eleganti lucidate.\nAccessori: Bastone da passeggio con impugnatura in ferro a forma di uncino.\nScarpe: Scarpe stringate eleganti in pelle nera lucidata.\nGioielli: Gemelli in argento scuro incisi col numero romano IV.\nTrucco: Presenza imponente e silenziosa avvolta da nebbia scura sotto il cappuccio sartoriale di velluto nero.\nAcconciatura: Orecchie da levriero irlandese grigie composte ai lati del cappuccio."
    },
    {
        "id": "dullahan_party",
        "name": "party / club",
        "description": "Abbigliamento: Giubbotto da motociclista in pesante pelle nera screpolata con maniche arrotolate sulle braccia possenti, t-shirt nera con cappuccio leggero, jeans scuri usurati con passante per la coda e stivali da rissa.\nAccessori: Tirapugni in ferro sagomato nella tasca destra.\nScarpe: Stivali pesanti da biker con fibbie metalliche.\nGioielli: Catenella di ferro che pende dal passante della cintura.\nTrucco: Vortice di nebbia nera illuminato occasionalmente da riflessi violetti sotto le luci del club.\nAcconciatura: Orecchie canine scure sporgenti dal cappuccio in pelle."
    },
    {
        "id": "dullahan_beach",
        "name": "beach / terme",
        "description": "Abbigliamento: Boxer da bagno larghi in tessuto tecnico antracite con asola lombare per la coda e un ampio poncho impermeabile con cappuccio scuro calato sul collo fumoso (teme e detesta l'acqua alta, resta sul bordo asciutto).\nAccessori: Grande asciugamano scuro e ciotola con latte per i gatti del seguito.\nScarpe: Sandali ergonomici da spiaggia neri.\nGioielli: Cicatrici da battaglia sulle spalle e marchio IV visibile sulla schiena.\nTrucco: Fumo denso che sbuffa lentamente dal collo riparato dal poncho.\nAcconciatura: Orecchie da wolfhound che spuntano vigili dal cappuccio del poncho."
    },
    {
        "id": "dullahan_sleep",
        "name": "sleep",
        "description": "Abbigliamento: Pantaloni da riposo larghi in flanella scura a quadri con asola per la coda, maglietta a maniche lunghe nera e cappuccio leggero morbido calato sul collo, disteso sul letto circondato da gatti addormentati.\nAccessori: Nessuno.\nScarpe: Nessuna, a piedi nudi.\nGioielli: Nessuno.\nTrucco: Nebbia nera pigra e immobile nel sonno.\nAcconciatura: Orecchie canine grigie rilassate ai lati del cappuccio."
    },
    {
        "id": "dullahan_nude",
        "name": "nude",
        "description": "Abbigliamento: Nessuno indosso sul corpo. Colossale e pesante corporatura maschile da 203 cm (6'8\") per 120 kg di muscolatura massiccia, petto villoso grigio, spalle titaniche e addome scolpito segnato da antiche cicatrici.\nAccessori: Nessuno tranne il perpetuo cappuccio scuro sollevato che cela la sommità della nuca.\nScarpe: Nessuna. Piedi nudi larghi e potenti con callosita plantare.\nGioielli: Numero romano 'IV' inciso profondamente sulla scapola sinistra; nessuna decorazione superflua.\nTrucco: Pelle grigio cenere ruvida; privo di testa anatomica: dalla base del collo reciso emana un lento e denso vortice di fumo e nebbia nera eterea che riempie il cappuccio; genitali maschili sani, proporzionati e non censurati.\nAcconciatura: Nessuna capigliatura o volto umano; morbide orecchie canine da Irish Wolfhound grigie che spuntano foniche attraverso le aperture laterali del cappuccio; folta coda canina grigio ferro visibile dall'apertura sacrale."
    },
    {
        "id": "dullahan_hybrid",
        "name": "hybrid shift / mutation",
        "description": "Abbigliamento: Brandelli di tessuto nero attorno alle spalle. Mastodontica forma ibrida canina bipede di 250 cm ricoperta di ispido pelo grigio acciaio, spalle taurine, collo reciso che erompe fumo nero abissale in cui si aprono fauci spettrali zannute capaci di ghermire varchi dimensionali.\nAccessori: Nessuno.\nScarpe: Zampe inferiori canine imponenti con cuscinetti neri e artigli ricurvi.\nGioielli: Marchio IV che pulsa di luce spettrale sulla scapola.\nTrucco: Vortice di fumo nero denso che ingloba la parte superiore del torso.\nAcconciatura: Pelliccia grigia ruvida su tutto il corpo; grandi orecchie canine erette nel fumo."
    },
    {
        "id": "dullahan_fullshift",
        "name": "full shift / other",
        "description": "Abbigliamento: Nessuno. Colossale levriero irlandese quadrupede (Canis familiaris) alto oltre un metro e dieci al garrese, dal folto pelo ruvido grigio topo, occhi velati di nebbia scura, muso nobile e potente e passo silenzioso e maestoso capace di scivolare tra le pieghe della realta.\nAccessori: Nessuno.\nScarpe: Zampe canine poderose con artigli scuri.\nGioielli: Nessuno.\nTrucco: Fisionomia da Irish Wolfhound gigante con muso fiero e dentatura ferale.\nAcconciatura: Pelo ruvido e compatto con folta coda che scende fino ai garretti."
    }
]

def patch_dullahan(filepath):
    if not filepath.exists():
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        card = json.load(f)
    
    # Age update
    card['description'] = card['description'].replace(
        'AGE: Centuries-old (Born 1700s France, Earth-121789);',
        'AGE: 34 at mortal death (Centuries-old Contractor, Born 1700s);'
    )
    if 'RPG STATS & TRAITS:' not in card['description']:
        card['description'] += dullahan_rpg_block

    card['outfits'] = dullahan_outfits
    card['default_outfit'] = 'dullahan_casual'

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    print(f"Patched {filepath.name}: {len(card['outfits'])} outfits")

# -----------------------------------------------------------------------------
# 5. FENRIR (CONTRACTOR #06)
# -----------------------------------------------------------------------------
fenrir_rpg_block = """

RPG STATS & TRAITS:
[LEVEL: 3; ARC_LEVEL: 4.0; SPECIES: Immortal Contractor (Eastern Kingsnake) (STR +3, PER +3, END +3, CHA -2); OCCUPATION: Squad Leader of LAZARUS [Black Ops] (STR +2, PER +3, AGI +2); CLASS: Super-Soldier & Kinetic Operative]
[STATS: STR 22; PER 24; END 22; CHA 6; INT 16; AGI 22; LCK 10]
TRAITS:
- Cybernetic Super-Soldier Biology: Genetically engineered dense musculature, pain-dampening neural circuits, and synthetic bone lacing from Earth-9898.
- Eastern Kingsnake Shifter: Cold-blooded stealth, constricting muscular force, and complete immunity to organic and synthetic toxins.
- Psychokinetic Force: Raw telekinetic vector manipulation capable of crushing armored bulkheads and detonating kinetic shields.
- Blind Thermal/Vibrational Echolocation: Sightless milky eyes paired with pit organs and cranial sensors reading body heat, acoustic pulses, and seismic tremors.
- Corpse-Like Stillness: Eerie lack of involuntary twitches, resting heartbeat, or breathing unless consciously activated for speech.
- Sole ACE Dependency: Extreme emotional attachment and protective fixation exclusively anchored to his assigned ACE.
- Immortal Contractor: Functionally immortal biology impervious to radiation, vacuum exposure, and catastrophic cellular trauma.
- Living Weapon Complex: Complete self-perception as an expendable military instrument, coping with bandages and tactical discipline."""

fenrir_outfits = [
    {
        "id": "fenrir_casual",
        "name": "casual",
        "description": "Abbigliamento: Felpa smanicata nera con cappuccio morbido, canotta scura attillata, bende di lino bianco avvolte attorno a mani e avambracci, pantaloni cargo neri affusolati e stivaletti leggeri da combattimento.\nAccessori: Fasce compressive da polso e bende pulite di ricambio.\nScarpe: Stivaletti bassi in gomma e cordura nera fonoassorbente.\nGioielli: Nessuno.\nTrucco: Pelle cadaverica pallida; occhi ciechi lattiginosi impassibili; immobilità assoluta.\nAcconciatura: Capelli corvini tagliati cortissimi a sfumatura militare lungo le tempie."
    },
    {
        "id": "fenrir_business",
        "name": "business / mission",
        "description": "Abbigliamento: Armatura pressurizzata da infiltrazione LAZARUS Black Ops in nanotessuto nero opaco con pannelli deflettori termici, sigillo '#06' invisibile a infrarossi, foderi integrati per coltelli da combattimento e cintura porta-cariche cinetiche.\nAccessori: Visore termico tattico disattivabile e maschera con respiratore filtrante.\nScarpe: Stivali tattici magnetici silenziati.\nGioielli: Numero romano 'VI' marchiato a fuoco alla base della spina dorsale.\nTrucco: Sguardo cieco che scruta il vuoto attraverso campi termici.\nAcconciatura: Capelli neri rasati corti e puliti."
    },
    {
        "id": "fenrir_formal",
        "name": "gala / formal",
        "description": "Abbigliamento: Uniforme militare cerimoniale scura a collo alto con chiusura diagonale a bottoni argentati, spalline rigide nere con profilo argento, pantaloni d'ordinanza stirati e stivali alti tirati a lucido.\nAccessori: Guanti neri eleganti in pelle sottile che celano le bende alle mani.\nScarpe: Stivali da parata militari neri specchiati.\nGioielli: Spilla metallica con numero romano 'VI' appuntata sul petto sinistro.\nTrucco: Portamento ieratico, privo di respiro o movimenti involontari.\nAcconciatura: Capelli corvini pettinati con disciplina marziale."
    },
    {
        "id": "fenrir_party",
        "name": "party / club",
        "description": "Abbigliamento: Giacca di pelle nera minimalista dal taglio asciutto indossata sopra una maglietta scura a scollo tondo, jeans scuri grezzi e stivali bassi con fibbie brunite.\nAccessori: Mani fasciate con garze nere.\nScarpe: Stivaletti in cuoio scuro.\nGioielli: Nessuno.\nTrucco: Viso scolpito nel marmo pallido, occhi vitrei freddi e insensibili agli stimoli luminosi.\nAcconciatura: Taglio militare corto nero pece."
    },
    {
        "id": "fenrir_beach",
        "name": "beach / terme",
        "description": "Abbigliamento: Pantaloncini da bagno aderenti in neoprene nero idrofobico; torso nudo colossale, marmoreo e segnato da innesti sub-dermici lungo le costole e le scapole.\nAccessori: Bende impermeabili sulle mani.\nScarpe: Sandali minimalisti neri antiscivolo.\nGioielli: Marchio 'VI' impresso sulla colonna vertebrale esposto alla luce.\nTrucco: Pelle cadaverica che non si abbronza; fossette termosensibili lungo le tempie che assorbono il calore circostante.\nAcconciatura: Capelli scuri corti bagnati e composti sul cranio."
    },
    {
        "id": "fenrir_sleep",
        "name": "sleep",
        "description": "Abbigliamento: Boxer scuri in cotone leggero, torso nudo freddo, sdraiato rigidamente sulla branda spoglia della sua stanza accanto al suo unico ACE di fiducia.\nAccessori: Nessuno.\nScarpe: Nessuna, a piedi nudi.\nGioielli: Nessuno.\nTrucco: Immobilità totale, battito cardiaco rallentato a frequenze minime.\nAcconciatura: Capelli neri corti a contatto col cuscino militare."
    },
    {
        "id": "fenrir_nude",
        "name": "nude",
        "description": "Abbigliamento: Nessuno. Completo nudo anatomico naturale. Silhouette slanciata, alta e spaventosamente muscolosa da 203 cm (6'8\") per 105 kg, con pelle pallida come marmo freddo, priva di peli corporei e solcata da cicatrici chirurgiche e innesti sub-dermici.\nAccessori: Nessuno.\nScarpe: Nessuna. Piedi nudi silenziosi e stabili con dita prensili.\nGioielli: Marchio a numero romano 'VI' inciso alla base della colonna vertebrale; bende protettive rimosse.\nTrucco: Pelle gelida priva di rossore; occhi lattiginosi e ciechi dal fascino inquietante; fossette termosensibili e membrana timpanica liscia lungo le tempie conformi all'anatomia rettiliana; anatomia genitale maschile sana, naturale e non censurata.\nAcconciatura: Capelli corvini tagliati cortissimi a sfumatura militare; privo di orecchie esterne mammifere conforme alla fisiologia ofidica; pelle squamata liscia alla base della schiena che degrada morbida."
    },
    {
        "id": "fenrir_hybrid",
        "name": "hybrid shift / mutation",
        "description": "Abbigliamento: Nessuno. Forma ibrida bipede da serpente predatore di 240 cm con pelle interamente rivestita di scaglie nero lucido con riflessi azzurri, collo e torso dalla possente muscolatura costrittrice, occhi termici incandescenti e artigli a uncino.\nAccessori: Nessuno.\nScarpe: Nessuna, scaglie plantari spesse e silenziose.\nGioielli: Marchio VI integrato nella tessitura delle squame dorsali.\nTrucco: Lingua biforcuta che saggia l'aria percependo feromoni e calore a chilometri di distanza.\nAcconciatura: Nessun capello; testa idrodinamica ofidica protetta da placche cornee nere."
    },
    {
        "id": "fenrir_fullshift",
        "name": "full shift / other",
        "description": "Abbigliamento: Nessuno. Colossale serpente reale quadrimetrico (Lampropeltis getula) dalle scaglie nero pece lucide con anelli chiari, locomozione silenziosa e fluida a spire, immune a qualsiasi veleno e forza di stritolamento sovrumana.\nAccessori: Nessuno.\nScarpe: Nessuna, movimento rettilineo a spire sul pavimento.\nGioielli: Nessuno.\nTrucco: Fisionomia ofidica perfetta con fossette sensoriali e zanne velenifere retrattili.\nAcconciatura: Nessuna; pelle squamata iridescente e compatta."
    }
]

def patch_fenrir(filepath):
    if not filepath.exists():
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        card = json.load(f)
    
    # Age update
    card['description'] = card['description'].replace(
        'AGE: Centuries-old (Died 2210 on Earth-9898);',
        'AGE: 26 at mortal death (Centuries-old Contractor, Died 2210);'
    )
    if 'RPG STATS & TRAITS:' not in card['description']:
        card['description'] += fenrir_rpg_block

    card['outfits'] = fenrir_outfits
    card['default_outfit'] = 'fenrir_casual'

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    print(f"Patched {filepath.name}: {len(card['outfits'])} outfits")

# -----------------------------------------------------------------------------
# 6. JOHAN JAKOBSEN (CONTRACTOR #05)
# -----------------------------------------------------------------------------
johan_rpg_block = """

RPG STATS & TRAITS:
[LEVEL: 4; ARC_LEVEL: 3.9; SPECIES: Immortal Contractor (Brown Rat) (STR -1, PER +3, END +1, INT +5); OCCUPATION: Director of Supernatural Research (PER +2, INT +4, CHA -1); CLASS: Anomaly Scientist & Reality Synthesizer]
[STATS: STR 10; PER 22; END 16; CHA 8; INT 34; AGI 18; LCK 16]
TRAITS:
- Genius Polymath (IQ 208): Encyclopedic memory, supernatural deduction, and rapid comprehension of multidimensional physics and arcane tech.
- Brown Rat Shifter: Rodent agility, hyper-acute auditory and olfactory tracking, and involuntary shifting when panicking.
- Subversive Manipulator: Timid, stuttering exterior masking cold, predatory scientific pragmatism that outmaneuvers rivals.
- Reality Tear Analysis: Expert diagnostic mastery over dimensional breaches, planar resonance, and anti-SERAPHIM weaponry.
- Chronic Agoraphobia & Animal Phobia: Intense anxiety in open spaces and an ironic, crippling terror of rodents and large predators.
- Antiseptic Hygiene Obsession: Compulsive hand sanitization, pristine sterile lab attire, and distaste for vulgarity and grime.
- Immortal Contractor: Functionally immortal intellect preserved across centuries of unhindered, amoral research.
- The Rat's Guilt: Lingering memory of his mortal demise in Aarhus, driving him to hoard data to avoid being trapped again."""

johan_outfits = [
    {
        "id": "johan_casual",
        "name": "casual",
        "description": "Abbigliamento: Casacca da laboratorio verde menta chiaro e pantaloni chirurgici coordinati, maglietta intima bianca a maniche lunghe con apertura posteriore per la coda da ratto e zoccoli sanitari bianchi antiscivolo.\nAccessori: Occhiali da vista sottili a montatura metallica; boccetta tascabile di disinfettante per le mani.\nScarpe: Zoccoli professionali bianchi in gomma sterilizzabile.\nGioielli: Nessuno.\nTrucco: Carnagione pallida e scavata con occhiaie scure pronunciate; sguardo nero febbrile e vigile.\nAcconciatura: Lunghi capelli corvini disordinati e radi che ricadono sul collo tra due piccole orecchie da topo bruno."
    },
    {
        "id": "johan_business",
        "name": "business / mission",
        "description": "Abbigliamento: Camice bianco da laboratorio sterilizzato con patch ricamata '#05' sul taschino, camicia a bottoni grigio antracite ben abbottonata, pantaloni sartoriali scuri con asola posteriore per la coda e guanti in lattice sintetico scuro.\nAccessori: Tablet analitico per diagnostica ARC e campionatori sterili in fiale sigillate.\nScarpe: Scarpe stringate in pelle nera con suola in gomma silenziosa.\nGioielli: Penna stilografica in titanio nel taschino.\nTrucco: Espressione analitica e distaccata, tic nervosi alle dita quando non indossa i guanti.\nAcconciatura: Capelli neri legati in una coda bassa per evitare contaminazioni nel laboratorio."
    },
    {
        "id": "johan_formal",
        "name": "gala / formal",
        "description": "Abbigliamento: Abito scandinavo a tre pezzi grigio fumo dal taglio minimale e asciutto, camicia bianca stirata inamidata con colletto chiuso, cravatta sottile nera, pantaloni con asola discreta per la coda e scarpe eleganti spazzolate.\nAccessori: Orologio da taschino minimale in acciaio opaco.\nScarpe: Scarpe eleganti nere lisce.\nGioielli: Fermacravatta semplice in argento.\nTrucco: Viso pulito e pallido con postura tesa e leggermente curva per il disagio sociale.\nAcconciatura: Capelli corvini pettinati con gel leggero all'indietro lasciando scoperte le orecchie da ratto."
    },
    {
        "id": "johan_party",
        "name": "party / club",
        "description": "Abbigliamento: Cardigan oversize beige sabbia a maglia fine indossato sopra una t-shirt scura morbida, pantaloni in velluto a coste color talpa e scarpe comode; postura ritrosa che cerca l'angolo piu appartato della sala.\nAccessori: Taccuino tascabile ad anelli e penna a sfera.\nScarpe: Mocassini comodi scuri.\nGioielli: Nessuno.\nTrucco: Sguardo furtivo e inquieto dietro le lenti sottili.\nAcconciatura: Capelli scuri scompigliati e cadenti sugli occhi."
    },
    {
        "id": "johan_beach",
        "name": "beach / terme",
        "description": "Abbigliamento: Boxer da bagno blu navy a vita media con asola lombare per la coda; torso magro e allampanato da 185 cm per 68 kg con pelle diafana che non sopporta la luce diretta, seduto sui gradini delle vasche termali DDM.\nAccessori: Accappatoio in spugna bianca e flacone di lozione idratante protettiva.\nScarpe: Ciabatte da piscina in gomma blu.\nGioielli: Nessuno.\nTrucco: Gocce di condensa sulla fronte pallida; sguardo ansioso rivolto verso le uscite.\nAcconciatura: Capelli bagnati neri incollati alla nuca."
    },
    {
        "id": "johan_sleep",
        "name": "sleep",
        "description": "Abbigliamento: T-shirt morbida in cotone grigio slavato e pantaloni larghi da pigiama a righe bianche e blu con asola per la coda, raggomitolato in posizione fetale sul letto singolo dello studio.\nAccessori: Nessuno.\nScarpe: Nessuna, a piedi nudi.\nGioielli: Nessuno.\nTrucco: Occhi chiusi ma palpebre che tremano lievemente per i calcoli mentali continui.\nAcconciatura: Capelli corvini arruffati sul cuscino."
    },
    {
        "id": "johan_nude",
        "name": "nude",
        "description": "Abbigliamento: Nessuno. Completo nudo anatomico naturale. Corporatura longilinea, esile e scarna da 185 cm (6'1\") per 68 kg, con pelle pallida quasi traslucida segnata da occhiaie e costole visibili sotto la cassa toracica.\nAccessori: Occhiali da vista sottili a montatura metallica posati sul comodino.\nScarpe: Nessuna. Piedi nudi magri e pallidi con pianta sensibile.\nGioielli: Nessun gioiello; pelle priva di tatuaggi o decorazioni.\nTrucco: Viso scavato, labbra sottili e sguardo nero intenso e febbrile dietro cerchi scuri di veglia; orecchie da topo brune arrotondate e semitrasparenti sul capo; anatomia genitale maschile sana, naturale e non censurata.\nAcconciatura: Lunghi capelli corvini disordinati e radi che ricadono sul collo; sottile e lunga coda glabra da ratto bruno che spunta dall'incavo lombare naturale."
    },
    {
        "id": "johan_hybrid",
        "name": "hybrid shift / mutation",
        "description": "Abbigliamento: Nessuno. Forma ibrida bipede wererat di 175 cm ricoperta di rada pelliccia setosa color cannella, muso allungato con vibrisse ipersensibili, zanne incisive ricurve affilatissime e zampe anteriori ad altissima destrezza chirurgica.\nAccessori: Nessuno.\nScarpe: Zampe inferiori con unghie ricurve per scalare condotti e pareti verticali.\nGioielli: Nessuno.\nTrucco: Occhi a perlina neri che riflettono la luce nell'oscurita; udito fine sintonizzato sui battiti cardiaci.\nAcconciatura: Pelliccia bruno-dorata rada sul cranio allungato; orecchie da ratto traslucide."
    },
    {
        "id": "johan_fullshift",
        "name": "full shift / other",
        "description": "Abbigliamento: Nessuno. Piccolo ratto bruno norvegese (Rattus norvegicus domestica) dal mantello lucido cannella e bianco, occhi neri intelligenti, riflessi rapidissimi e capacità di infiltrazione microscopica nelle fessure della DDM.\nAccessori: Nessuno.\nScarpe: Nessuna, zampette rosa agili e silenziose.\nGioielli: Nessuno.\nTrucco: Fisionomia da roditore da laboratorio con vibrisse frementi.\nAcconciatura: Pelliccia corta uniforme con lunga coda rosa glabra."
    }
]

def patch_johan(filepath):
    if not filepath.exists():
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        card = json.load(f)
    
    # Age update
    card['description'] = card['description'].replace(
        'AGE: Centuries-old (Appears early 30s, Died 2002 at 28 in Aarhus, Denmark);',
        'AGE: 28 at mortal death (Appears early 30s, Died 2002 at 28);'
    )
    if 'RPG STATS & TRAITS:' not in card['description']:
        card['description'] += johan_rpg_block

    card['outfits'] = johan_outfits
    card['default_outfit'] = 'johan_casual'

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    print(f"Patched {filepath.name}: {len(card['outfits'])} outfits")

# -----------------------------------------------------------------------------
# 7. LUKA SUTTER (CONTRACTOR #03)
# -----------------------------------------------------------------------------
luka_rpg_block = """

RPG STATS & TRAITS:
[LEVEL: 5; ARC_LEVEL: 3.8; SPECIES: Immortal Contractor (Black Bear) (STR +4, END +3, INT +1, CHA -1); OCCUPATION: Head of Security & Defense / PMC Forces (STR +3, PER +2, END +2); CLASS: Heavy Vanguard & Ferromagnetic Juggernaut]
[STATS: STR 26; PER 20; END 24; CHA 10; INT 18; AGI 16; LCK 12]
TRAITS:
- G.A.I.A. Cyber-Military Augmentation: Heavy skeletal carbon-reinforcements, dermal ballistic sub-plating, and neural fire-control implants from Earth-19098.
- Black Bear Shifter: Colossal ursine physical mass, bone-shattering swatting power, and apex predatory territorial drive.
- Ferromagnetic Metal Manipulation: Bending, superheating, and hurtling high-velocity ferrous shrapnel and heavy kinetic armaments.
- Veteran Military Officer: Decisive, battle-tested tactical command over DDM private military units and orbital strike protocols.
- Severe Claustrophobia: Panic-induced aggression in tight, confined, or subterranean spaces stemming from his orbital airlock execution.
- Chain-Smoker Regeneration: Continuous tobacco consumption neutralized instantly by rapid Contractor lung and tissue regeneration.
- Immortal Contractor: Indestructible physical vanguard enduring artillery impacts and void decompression.
- Blood Grudge against SERAPHIM: Relentless, vengeful hatred against SERAPHIM operatives following the slaughter of his previous ACE squad."""

luka_outfits = [
    {
        "id": "luka_casual",
        "name": "casual",
        "description": "Abbigliamento: Canotta a coste verde oliva militare scollata sul petto villoso, pantaloni mimetici da combattimento con tasche per caricatori e asola per la coda ursina, stivali d'ordinanza con cerniera laterale e sigaro serrato tra i denti.\nAccessori: Piastrina militare G.A.I.A. e accendino al plasma in metallo pesante.\nScarpe: Anfibi d'ordinanza in cuoio nero con suola chiodata.\nGioielli: Anello in acciaio nero zigrinato al pollice destro.\nTrucco: Cicatrice a forma di X sulla guancia destra ben evidente; sguardo nocciola fiero e sprezzante.\nAcconciatura: Capelli cremisi corti e arruffati; folte orecchie tondeggianti da orso nero tra i capelli."
    },
    {
        "id": "luka_business",
        "name": "business / mission",
        "description": "Abbigliamento: Corazza d'assalto pesante DDM PMC in composito magnetico e leghe di titanio con stemma '#03' sul pettorale, tuta pressurizzata ignifuga sottostante con apertura posteriore per la coda e imbracatura di supporto cinetico.\nAccessori: Guanti corazzati magnetici per accelerare proiettili ferromagnetici; cartucciera pesante a tracolla.\nScarpe: Stivali esoscheletrici con servomotori di supporto.\nGioielli: Piastrina DDM #03 al collo.\nTrucco: Tratti duri e minacciosi da comandante di sfondamento; fumo di sigaro che si disperde nell'aria.\nAcconciatura: Capelli rossi tenuti corti per non interferire con i sensori della corazza."
    },
    {
        "id": "luka_formal",
        "name": "gala / formal",
        "description": "Abbigliamento: Alta uniforme da ufficiale della G.A.I.A. in panno cremisi e nero carbone con bottoni dorati, spalline rigide con gradi da comandante, cordelline dorate sul petto, pantaloni d'ordinanza con banda laterale dorata e asola per la coda.\nAccessori: Sciabola d'onore a lama magnetica al fianco sinistro.\nScarpe: Stivali da cavalleria alti in cuoio nero tirati a specchio.\nGioielli: Medaglie al valore dell'esercito imperiale astrale.\nTrucco: Portamento eretto e possente, espressione burbera ma impeccabile.\nAcconciatura: Capelli cremisi pettinati all'indietro con cura tra le orecchie da orso nero."
    },
    {
        "id": "luka_party",
        "name": "party / club",
        "description": "Abbigliamento: Camicia in denim pesante nero con bottoni metallici a pressione aperta sul petto massiccio, giacca da motociclista in pelle consumata, jeans neri resistenti con asola per la coda e stivali da rissa.\nAccessori: Pacchetto di sigarette e fiaschetta metallica nella tasca interna.\nScarpe: Stivali in pelle con fibbie metalliche.\nGioielli: Bracciale a maglie spesse in titanio ferromagnetico.\nTrucco: Sorriso feroce e beffardo illuminato dal riverbero delle luci del bancone.\nAcconciatura: Capelli cremisi ribelli e spettinati."
    },
    {
        "id": "luka_beach",
        "name": "beach / terme",
        "description": "Abbigliamento: Boxer da bagno mimetici militari pesanti con coulisse rinforzata e asola per la coda; torso colossale da 193 cm (6'4\") per 122 kg di pura massa ursina, petto ricoperto di pelo scuro e braccia scolpite.\nAccessori: Telo militare scuro e occhiali da sole balistici.\nScarpe: Ciabatte da campo in gomma nera spessa.\nGioielli: Piastrina militare G.A.I.A. al collo e cicatrice a X esposta sulla guancia.\nTrucco: Gocce d'acqua che evaporano sul torso accaldato; sigaro sempre acceso tra le labbra.\nAcconciatura: Capelli rossi bagnati e orecchie da orso che scrollano via l'acqua."
    },
    {
        "id": "luka_sleep",
        "name": "sleep",
        "description": "Abbigliamento: Pantaloncini da riposo neri in cotone pesante a vita elastica con apertura per la coda, torso nudo, sdraiato pesantemente sul letto matrimoniale rinforzato del suo alloggio con le finestre aperte sul cosmo.\nAccessori: Portacenere in metallo sul comodino.\nScarpe: Nessuna, a piedi nudi.\nGioielli: Nessuno.\nTrucco: Respiro profondo e rumoroso, sonno pesante da predatore in letargo.\nAcconciatura: Capelli cremisi sparsi sul cuscino scuro."
    },
    {
        "id": "luka_nude",
        "name": "nude",
        "description": "Abbigliamento: Nessuno. Completo nudo anatomico naturale. Mastodontica corporatura iper-muscolosa da 193 cm (6'4\") per 122 kg di pura potenza ursina e innesti militari, con pettorali massicci, spalle larghe come una roccia e dorso segnato da vecchie cicatrici da scheggia.\nAccessori: Nessuno.\nScarpe: Nessuna. Piedi nudi pesanti e saldi al suolo con pianta callosa.\nGioielli: Cicatrice a forma di X sulla guancia destra; nessuna catenina superflua.\nTrucco: Sguardo fiero color nocciola, mascella squadrata con barba incolta ispida; orecchie da orso nero arrotondate e folte sulla sommità del capo; anatomia maschile imponente, proporzionata e non censurata.\nAcconciatura: Capelli cremisi corti e arruffati; folto pelo bruno-nero sparso sul petto possente; coda corta e tozza da orso nero che spunta naturale dall'osso sacro."
    },
    {
        "id": "luka_hybrid",
        "name": "hybrid shift / mutation",
        "description": "Abbigliamento: Nessuno. Forma licantropica ibrida bipede ursina Ursa Major di 260 cm ricoperta di densa pelliccia nera corvina, spalle titaniche, fauci spalancate con zanne d'acciaio, artigli ricurvi ferromagnetici carichi di scintille cinetiche e forza d'urto inarrestabile.\nAccessori: Nessuno.\nScarpe: Zampe posteriori plantari ursine devastanti.\nGioielli: Nessuno.\nTrucco: Occhi nocciola che bruciano d'ira feroce; ruggito tonante che fa vibrare le paratie metalliche.\nAcconciatura: Pelliccia densa su tutto il cranio e la groppa; orecchie ursine piegate all'indietro."
    },
    {
        "id": "luka_fullshift",
        "name": "full shift / other",
        "description": "Abbigliamento: Nessuno. Colossale orso nero americano quadrupede (Ursus americanus) di oltre 400 kg di massa muscolare compatta, folto mantello lucente nero pece, forza di scavo e abbattimento titanica e passo pesante e felpato.\nAccessori: Nessuno.\nScarpe: Zampe ursine poderose con artigli scuri non retrattili da sfondamento.\nGioielli: Nessuno.\nTrucco: Muso robusto con tartufo scuro umido e dentatura micidiale.\nAcconciatura: Folto pelo compatto su tutto il corpo con coda corta nascosta dal manto."
    }
]

def patch_luka(filepath):
    if not filepath.exists():
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        card = json.load(f)
    
    # Age update
    card['description'] = card['description'].replace(
        'AGE: Centuries-old (Born 2461 on Earth-19098, Contract 2508);',
        'AGE: 32 at mortal death (Centuries-old Contractor, Born 2461, Contract 2508);'
    )
    if 'RPG STATS & TRAITS:' not in card['description']:
        card['description'] += luka_rpg_block

    card['outfits'] = luka_outfits
    card['default_outfit'] = 'luka_casual'

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    print(f"Patched {filepath.name}: {len(card['outfits'])} outfits")

# -----------------------------------------------------------------------------
# 8. RICHARD WHITLOCK (CONTRACTOR #01)
# -----------------------------------------------------------------------------
richard_rpg_block = """

RPG STATS & TRAITS:
[LEVEL: 8; ARC_LEVEL: 4.6; SPECIES: Immortal Contractor (Lion) (STR +4, PER +2, END +3, CHA +3); OCCUPATION: De Facto Leader of Contractors & Council Liaison (STR +2, CHA +3, INT +2); CLASS: Royal Paladin & Pyrotic Warlord]
[STATS: STR 24; PER 20; END 24; CHA 24; INT 20; AGI 16; LCK 16]
TRAITS:
- Knight's Code of Chivalry: Rigid chivalric honor, protective paternal duty, and absolute intolerance for dishonor and disloyalty.
- Lion Shifter: Sovereign leonine presence, deafening territorial roar, and predatory apex combat instincts.
- Pyrokinesis & Temperature Mastery: Spontaneous ignition, radiant solar heatwaves, and flame manipulation radiating from his aura.
- Compulsion of Obedience: Imposing authoritative command voice that compels subordinates and lesser wills into mandatory compliance.
- Council Liaison Authority: Sole Contractor authorized to speak directly before The Council and negotiate tactical deployments.
- Paternal Protector Instinct: Deep, brooding personal responsibility for every Contractor and ACE under DDM employ.
- Immortal Contractor: Ancient, unyielding endurance impervious to blade thrusts, hanging, and centuries of relentless battle.
- Curse of the Dawnstar: Tragic loophole of his contract preventing him from being present at the exact fatal moment of his charges' death."""

richard_outfits = [
    {
        "id": "richard_casual",
        "name": "casual",
        "description": "Abbigliamento: Maglione a collo alto in pesante lana grigia intrecciata, pantaloni sartoriali in lana pettinata color fumo con asola posteriore per la coda leonina, mocassini in cuoio scuro morbido e aroma di legno di cedro e pipa.\nAccessori: Pipa in legno intagliato e accendino d'ottone.\nScarpe: Mocassini comodi in cuoio marrone scuro.\nGioielli: Anello d'oro massiccio con sigillo del Leone di Starfall all'anulare sinistro.\nTrucco: Lineamenti maturi e severi solcati da rughe d'espressione nobili; barba grigia ben rifinita.\nAcconciatura: Capelli grigi corti e ordinati attorno a due orecchie leonine dorate sulla sommità del capo."
    },
    {
        "id": "richard_business",
        "name": "business / mission",
        "description": "Abbigliamento: Corazza da cavaliere della DDM in acciaio brunito con incisioni dorate del leone sul pettorale e sigillo '#01', sopravveste in panno cremisi rinforzato con apertura per la coda, spallacci scanalati e stivali da guerra rinforzati.\nAccessori: Spadone a due mani con lama forgiata in metallo solare assicurato al cinturone dorsale.\nScarpe: Stivali corazzati pesanti con speroni d'ottone.\nGioielli: Spilla metallica col leone reale sul mantello.\nTrucco: Sguardo azzurro glaciale e risoluto, fiamme vive che brillano nei momenti di comando.\nAcconciatura: Capelli grigi composti sotto la celata rialzata; orecchie da leone erette e attente."
    },
    {
        "id": "richard_formal",
        "name": "gala / formal",
        "description": "Abbigliamento: Farsetto cerimoniale nobiliare in velluto cremisi cupo e broccato dorato con alamari in filo d'oro, camicia di lino bianco candido a colletto alto, pantaloni neri su misura con asola per la coda e stivali alti da cavaliere lucidi.\nAccessori: Mantello da capitano della Guardia Reale bordato di pelliccia dorata fissato con catena d'oro.\nScarpe: Stivali da parata in cuoio lucidato a specchio.\nGioielli: Anello sigillo reale e collare d'onore della Casata Starfall.\nTrucco: Portamento imponente, austero e regale che incute rispetto immediato.\nAcconciatura: Capelli grigi composti e criniera leonina dorata corta che sfuma sulle spalle."
    },
    {
        "id": "richard_party",
        "name": "party / club",
        "description": "Abbigliamento: Giacca da sera scura in cuoio martellato su camicia di seta nera aperta al colletto, pantaloni scuri dal taglio classico con asola per la coda e scarpe stringate eleganti in pelle nera.\nAccessori: Boccale di birra scura artigianale stretto con mano ferma.\nScarpe: Scarpe stringate in pelle scura lucida.\nGioielli: Anello d'oro col sigillo del Leone.\nTrucco: Sorriso raro e severo, sguardo calmo e protettivo verso i compagni piu giovani.\nAcconciatura: Capelli grigi curati che lasciano libere le orecchie leonine dorate."
    },
    {
        "id": "richard_beach",
        "name": "beach / terme",
        "description": "Abbigliamento: Boxer da bagno classici in tessuto bordeaux scuro con cordoncino dorato e asola posteriore per la coda leonina; torso maturo, possente e muscoloso da 193 cm (6'4\") per 110 kg percorso da cicatrici d'arma bianca e dal segno della corda al collo.\nAccessori: Ampio telo da bagno color rubino sulle spalle larghe.\nScarpe: Sandali da riposo in cuoio scuro.\nGioielli: Anello Starfall all'anulare sinistro.\nTrucco: Vapori caldi che avvolgono la figura maestosa senza offuscarne l'aura vigile.\nAcconciatura: Capelli grigi umidi all'indietro; orecchie leonine che percepiscono ogni eco circostante."
    },
    {
        "id": "richard_sleep",
        "name": "sleep",
        "description": "Abbigliamento: Pantaloni morbidi da notte in cotone pesante grigio antracite con asola posteriore per la coda leonina, torso nudo maturo e potente, disteso composto sul letto a baldacchino dell'ala medievale della DDM.\nAccessori: Nessuno.\nScarpe: Nessuna, a piedi nudi.\nGioielli: Nessuno.\nTrucco: Viso rilassato nel sonno severo da vecchio soldato.\nAcconciatura: Capelli grigi corti morbidamente adagiati sul cuscino."
    },
    {
        "id": "richard_nude",
        "name": "nude",
        "description": "Abbigliamento: Nessuno. Completo nudo anatomico naturale. Nobile e imponente corporatura da 193 cm (6'4\") per 110 kg, muscolosa e temprata da secoli di guerra, con spalle larghe, petto possente segnato da cicatrici di spada e una marcata cicatrice circolare da corda attorno al collo.\nAccessori: Nessuno.\nScarpe: Nessuna. Piedi nudi saldi e callosi con pianta robusta.\nGioielli: Anello d'oro con sigillo del Leone di Starfall all'anulare sinistro.\nTrucco: Lineamenti fieri e severi segnati dal tempo; barba grigia corta e curata; occhi azzurro chiaro penetranti e nobili; anatomia maschile matura, sana e non censurata.\nAcconciatura: Capelli grigi corti e composti; orecchie leonine dorate arrotondate sul capo; folta coda leonina con ciuffo scuro finale che ricade fluida dall'osso sacro."
    },
    {
        "id": "richard_hybrid",
        "name": "hybrid shift / mutation",
        "description": "Abbigliamento: Nessuno. Forma ibrida bipede leonina Starfall Lion Warlord di 245 cm con maestosa e folta criniera dorata e fulva, spalle taurine, zanne micidiali, artigli d'acciaio retrattili e aura ardente di fiamme dorate pronte a divampare.\nAccessori: Nessuno.\nScarpe: Zampe leonine possenti con cuscinetti scuri e artigli micidiali.\nGioielli: Anello Starfall inglobato nella possente zampa sinistra.\nTrucco: Occhi azzurri infuocati carichi di autorità e calore solare; ruggito solenne.\nAcconciatura: Maestosa criniera dorata e fulva che circonda il capo e il petto possente."
    },
    {
        "id": "richard_fullshift",
        "name": "full shift / other",
        "description": "Abbigliamento: Nessuno. Maestoso leone maschio quadrupede (Panthera leo) dalla folta criniera dorata e fulva, muscolatura elastica e possente, ruggito scuotiterra capace di imporre obbedienza e occhi azzurri splendenti come zaffiri nobili.\nAccessori: Nessuno.\nScarpe: Zampe feline titaniche con artigli retrattili affilati come rasoi.\nGioielli: Nessuno.\nTrucco: Fisionomia da leone sovrano con vibrisse imponenti e fauci possenti.\nAcconciatura: Criniera leonina foltissima con coda terminante in un ciuffo scuro e compatto."
    }
]

def patch_richard(filepath):
    if not filepath.exists():
        return
    with open(filepath, 'r', encoding='utf-8') as f:
        card = json.load(f)
    
    # Age update
    card['description'] = card['description'].replace(
        'AGE: Centuries-old (Appears late 40s, Born Kingdom of Starfall);',
        'AGE: 47 at mortal death (Appears late 40s, Centuries-old Contractor);'
    )
    if 'RPG STATS & TRAITS:' not in card['description']:
        card['description'] += richard_rpg_block

    card['outfits'] = richard_outfits
    card['default_outfit'] = 'richard_casual'

    with open(filepath, 'w', encoding='utf-8') as f:
        json.dump(card, f, indent=2, ensure_ascii=False)
    print(f"Patched {filepath.name}: {len(card['outfits'])} outfits")

def main():
    print("=== Patching Jasper Cards ===")
    patch_jasper(FINAL / "Jasper_Contractor_card.json")
    patch_jasper(FINAL / "Jasper_DDM_Contractor_card.json")

    print("\n=== Patching 7 Contractor Cards ===")
    patch_adam(FINAL / "Adam_Valencia_card.json")
    patch_hana(FINAL / "Hana_Valencia_card.json")
    patch_dullahan(FINAL / "Dullahan_card.json")
    patch_fenrir(FINAL / "Fenrir_card.json")
    patch_johan(FINAL / "Johan_Jakobsen_card.json")
    patch_luka(FINAL / "Luka_Sutter_card.json")
    patch_richard(FINAL / "Richard_Whitlock_card.json")

    print("\nAll cards patched successfully.")

if __name__ == "__main__":
    main()
