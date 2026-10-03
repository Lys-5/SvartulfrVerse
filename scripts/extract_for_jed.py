import json
import re

def convert_to_jed(char_data):
    name = char_data.get('name', 'Unknown')
    desc = char_data.get('description', '')
    personality = char_data.get('personality', '')
    scenario = char_data.get('scenario', '')
    
    # Simple extraction logic for demonstration
    # In a real scenario, this would use an LLM or more complex parsing.
    # Since I just need to compile the data for the LLM to process, 
    # I will just structure the raw text into a single markdown string
    # for each character so that I (or a subagent) can process it easily.
    
    combined_text = f"NAME: {name}\n\nDESCRIPTION:\n{desc}\n\nPERSONALITY:\n{personality}\n\nSCENARIO:\n{scenario}\n"
    return combined_text

def main():
    try:
        with open('scraped_characters_batch.json', 'r', encoding='utf-8') as f:
            data = json.load(f)
    except Exception as e:
        print("Error loading scraped JSON:", e)
        return

    # Names of the 14 NPCs
    npcs_14 = ["Oskar", "Fade Greymoor", "Vincent Campbell", "Casey Brown", "Barkley Rogers", 
               "Tate", "Nikolaj Jökull", "Janice Thompson", "Jared Thompson", "Roland Vickers", 
               "Finnegan", "Andrew", "Mackenzie", "Stan Davies Jr"]
               
    group_a = ["Rozalia", "Ruby Valerius", "Vesna", "Mikan", "Ginger", "Orion", "Henrey", "Aria Xenthon", "Tori", "River"]
    
    # We will just dump the relevant JSON objects into manageable chunks for the LLM to process
    
    def find_char(name_query):
        for k, v in data.items():
            if name_query.lower() in k.lower():
                return v
        return None

    def dump_group(names, filename):
        found = {}
        for n in names:
            c = find_char(n)
            if c:
                found[c['name']] = c
            else:
                print(f"Warning: {n} not found in scraped data")
        
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(found, f, indent=2, ensure_ascii=False)
        print(f"Saved {len(found)} characters to {filename}")

    dump_group(npcs_14, 'docs/14_NPCs_Raw.json')
    dump_group(group_a, 'docs/GroupA_Raw.json')

if __name__ == '__main__':
    main()
