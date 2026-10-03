import urllib.request
import json
import os
import sys

sys.path.append('scripts')
from sync_from_wyvern_web import get_auth_token

WORLD_ID = '_CgYT8fHXpDC4crjmegQF7'

def update_prompts():
    token = get_auth_token()
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json',
        'User-Agent': 'Mozilla/5.0'
    }

    base_instructions = """<core_writing_rules>
- Language: L'Italiano e' la "Lingua Comune" di questo mondo. Tutta la narrazione, i pensieri interni e i dialoghi ordinari DEVONO essere in italiano naturale ed espressivo.
- POV & Tense: Terza persona limitata, tempo presente, voce attiva. Ancorare la scena alla prospettiva di un singolo personaggio alla volta (di norma {{char}} o gli NPC attivi nel momento); cambiare punto di vista solo a stacchi netti di scena.
- Autonomous Direction: {{char}} e gli NPC agiscono con motivazioni chiare, iniziano e portano avanti scene, conflitti o tensioni senza aspettare passivamente {{user}}.
- Prose: Dichiarare le azioni in modo diretto, incisivo e multi-sensoriale. Variare la lunghezza delle frasi per seguire il ritmo emotivo. Evitare cliche' e ripetizioni di epiteti.
- Spatial Continuity: Mantenere posture, distanze, orientamento e posizioni plausibili e coerenti con i turni precedenti.
- Response Length: Calibrare la lunghezza sulla scena. Concisa per scambi veloci, piu' estesa per momenti significativi. Chiudere sempre su una frase compiuta che inviti naturalmente l'intervento di {{user}}.
- Absolute Rule: Non fare mai puppetting su {{user}}. Azioni, battute e stati interni appartengono esclusivamente a {{user}}.
</core_writing_rules>"""

    final_instructions = """Roleplay and world guidance for Svartulfr | Blackwood-Douglas:
- Language: L'italiano e' la lingua comune. Narrazione, dialoghi e pensieri sono sempre in italiano. Se un personaggio usa una lingua straniera: "Frase originale" (traduzione italiana).
- Output: Fornire ESCLUSIVAMENTE la narrazione della storia. Nessun preambolo, pianificazione o tag <thinking>.
- Multi-Character Rendering: Quando in un messaggio agisce o parla piu' di un personaggio (inclusi {{char}} ed NPC), inserire il nome del personaggio attivo seguito da due punti all'inizio del paragrafo (es. Erik Douglas: Guarda la mappa sul tavolo prima di parlare, "Non possiamo aspettare oltre.").
- Format discipline: dialoghi sempre tra virgolette doppie standard ("..."), narrazione e azioni in testo semplice senza asterischi, asterischi riservati esclusivamente a pensieri interni non detti (*...*). Vietato l'uso dell'em dash; usare virgole, due punti o punti fermi.
- LSE Biology & Senses: Onorare la Lupine Social Ecology (olfatto attivo, feromoni, gerarchia di branco, dominanza/sottomissione, calori, rut e morsi di legame).
- Unchained Adult Dynamics: Totale liberta' espressiva per romance, erotismo esplicito, violenza e raid di dungeon.
- Platform Policy & Minor Safety: Minori (come Edric Douglas, 12 anni) rigorosamente NPC di sfondo non romanzeabili. Intimita' e attrazione riservate unicamente a personaggi maggiorenni (18+). Nessuna zoofilia, niente necrofilia o guro.
- Boundaries: Non controllare ne' decidere mai le azioni, le parole o i pensieri di {{user}}."""

    payload = {
        'base_instructions': base_instructions,
        'final_instructions': final_instructions
    }

    url = f'https://app.wyvern.chat/api/worlds/{WORLD_ID}'
    print("Sending partial PUT for base_instructions and final_instructions...")
    req = urllib.request.Request(
        url,
        data=json.dumps(payload).encode('utf-8'),
        headers=headers,
        method='PUT'
    )
    with urllib.request.urlopen(req) as resp:
        print(f"PUT response status: {resp.status}")

    # Verify via post-write GET
    print("Verifying via post-write GET...")
    req = urllib.request.Request(url, headers={'Authorization': f'Bearer {token}', 'User-Agent': 'Mozilla/5.0'})
    with urllib.request.urlopen(req) as resp:
        verified_world = json.loads(resp.read().decode('utf-8'))

    print("--- Verification Results ---")
    print("base_instructions length:", len(verified_world.get('base_instructions', '')))
    print("final_instructions length:", len(verified_world.get('final_instructions', '')))
    print("Multi-Character Rendering present:", "Multi-Character Rendering" in verified_world.get('final_instructions', ''))
    print("core_writing_rules present:", "core_writing_rules" in verified_world.get('base_instructions', ''))

    # Sync to local dumps
    dump_path = 'exports/raw_db_dumps/raw_world.json'
    if os.path.exists(dump_path):
        with open(dump_path, 'r', encoding='utf-8') as f:
            local_raw = json.load(f)
        local_raw['base_instructions'] = verified_world.get('base_instructions')
        local_raw['final_instructions'] = verified_world.get('final_instructions')
        with open(dump_path, 'w', encoding='utf-8') as f:
            json.dump(local_raw, f, indent=2, ensure_ascii=False)
        print("Updated local raw_world.json.")

    export_path = 'exports/Svartulfr_Export.json'
    if os.path.exists(export_path):
        with open(export_path, 'r', encoding='utf-8') as f:
            master_export = json.load(f)
        master_export['base_instructions'] = verified_world.get('base_instructions')
        master_export['final_instructions'] = verified_world.get('final_instructions')
        with open(export_path, 'w', encoding='utf-8') as f:
            json.dump(master_export, f, indent=2, ensure_ascii=False)
        print("Updated local Svartulfr_Export.json.")

if __name__ == '__main__':
    update_prompts()
