import json
import pathlib
import re

SC_DIR = pathlib.Path('FINAL/scenarios')

def check_quotes_and_dialogue():
    files = sorted(SC_DIR.glob('*.json'))
    for f in files:
        data = json.loads(f.read_text(encoding='utf-8'))
        for g_i, g in enumerate(data.get('greetings', [])):
            for m_i, m in enumerate(g.get('messages', [])):
                c = m.get('content', '')
                # check for single quote speech / text messages
                sq = re.findall(r"'([A-Z\s.,!?-]{4,})'", c)
                if sq:
                    print(f"SINGLE QUOTES in {f.name} g[{g_i}] m[{m_i}] ({m.get('speaker_slot')}): {sq}")
                
                # check for any unquoted spoken text or weird punctuation
                # check if there are curly quotes
                if '“' in c or '”' in c:
                    print(f"CURLY DOUBLE QUOTES in {f.name} g[{g_i}] m[{m_i}]")
                if '‘' in c or '’' in c:
                    # check if curly single quote is used as dialogue quote
                    csq = re.findall(r"[‘']([^'’]{4,})[’']", c)
                    # might be apostrophes like Wulfnic's, let's filter apostrophes
                    for item in csq:
                        if len(item.split()) > 2:
                            print(f"POSSIBLE SINGLE QUOTE STRING in {f.name} g[{g_i}] m[{m_i}]: {item}")

if __name__ == '__main__':
    check_quotes_and_dialogue()
