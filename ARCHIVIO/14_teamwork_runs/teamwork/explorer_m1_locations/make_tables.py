import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(".agents/teamwork/explorer_m1_locations/catalog_188.json", "r", encoding="utf-8") as f:
    catalog = json.load(f)

# Group by Environment
env_groups = {}
for entry in catalog:
    env = entry["environment"]
    if env not in env_groups:
        env_groups[env] = []
    env_groups[env].append(entry)

out = []
for env_name in sorted(env_groups.keys()):
    locs = sorted(env_groups[env_name], key=lambda x: (x["depth"], x["name"]))
    out.append(f"### {env_name} ({len(locs)} Locations)\n")
    out.append("| # | Location Name | ID | Parent Location | Depth | Context Prose | Included Lexicon |")
    out.append("|---|---|---|---|---|:---:|---|")
    for idx, l in enumerate(locs, 1):
        parent_str = l["parent_name"] if l["parent_name"] != "None (Root)" else "*(Root)*"
        ctx_icon = "Yes" if l["has_context"] else "No"
        lex_str = ", ".join(l["inc_lex"]) if l["inc_lex"] else "None"
        out.append(f"| {idx} | **{l['name']}** | `{l['id']}` | {parent_str} | {l['depth']} | {ctx_icon} | {lex_str} |")
    out.append("\n")

with open(".agents/teamwork/explorer_m1_locations/catalog_tables.md", "w", encoding="utf-8") as f:
    f.write("\n".join(out))

print("Catalog tables written successfully.")
