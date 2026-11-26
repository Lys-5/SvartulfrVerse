import json
import subprocess
import sys
from pathlib import Path

# Add repo root to path
repo_root = Path(__file__).resolve().parent.parent.parent.parent
sys.path.insert(0, str(repo_root))

from scripts.verify_npc_schema_contract import compile_wyvern_avatar_regex

# Test cases matching scratch/test_compiler.js plus adversarial edge cases
test_cases = [
    {
        "name": "Erik Douglas",
        "info": {
            "first_name": "Erik",
            "middle_names": ["Ulfr"],
            "last_name": "Douglas",
            "nicknames": ["The Old Wolf", "Pack Leader"],
            "titles": ["Lord", "Alpha"]
        },
        "prefix": "",
        "delimiter": ":"
    },
    {
        "name": "Scarlett Rose",
        "info": {
            "first_name": "Scarlett",
            "last_name": "Rose",
            "nicknames": ["Red"]
        },
        "prefix": "",
        "delimiter": ":"
    },
    {
        "name": "Sierra Cruz (Empty Prefix)",
        "info": {
            "first_name": "Sierra",
            "last_name": "Cruz"
        },
        "prefix": "",
        "delimiter": ":"
    },
    {
        "name": "Sierra Cruz (=> Prefix)",
        "info": {
            "first_name": "Sierra",
            "last_name": "Cruz"
        },
        "prefix": "=>",
        "delimiter": ":"
    },
    {
        "name": "Jean-Luc Virtuoso (Hyphen & Quotes)",
        "info": {
            "first_name": "Jean-Luc",
            "middle_names": ["Pierre"],
            "last_name": "Virtuoso",
            "nicknames": ["Doctor 'Doc'", "The Sinner"],
            "titles": ["Doctor", "Master"]
        },
        "prefix": "",
        "delimiter": ":"
    },
    {
        "name": "Marcus O'Connor (Apostrophe)",
        "info": {
            "first_name": "Marcus",
            "last_name": "O'Connor",
            "nicknames": ["Mark", "Marky"]
        },
        "prefix": "",
        "delimiter": ":"
    },
    {
        "name": "Wulfnic Báleygr Bloodmoon (Accented Characters)",
        "info": {
            "first_name": "Wulfnic",
            "middle_names": ["Báleygr"],
            "last_name": "Bloodmoon",
            "nicknames": ["The Old King", "Firstborn"],
            "titles": ["Jarl"]
        },
        "prefix": "",
        "delimiter": ":"
    }
]

js_code = r"""
const fs = require('fs');

function i() {
  return '(?:\\([^()\\\\[\\\\]:\\\\r\\\\n]{1,80}\\\\)|\\\\[[^()\\\\[\\\\]:\\\\r\\\\n]{1,80}\\\\])';
}

function compileWyvernAvatarRegex(npcInfo, prefix = "", suffix = ":") {
  if (!npcInfo?.first_name?.trim()) return "";
  
  const s = e => e.normalize("NFC");
  const u = e => s(e)
    .replace(/[.*+?^${}()|[\]\\]/g, "\\$&")
    .replace(/['\u2018\u2019\u02BC\u201B\u2032]/g, "['‘’ʼ‛′]")
    .replace(/[-\u2010\u2011\u2012\u2013\u2014\u2212]/g, "[-‐‑‒–—−]");
  
  const d = prefix.trim() ? "(?<=^|[^\\p{L}\\p{N}_])" : "";
  const h = [];
  const p = "(?:\\*\\*)?";
  
  if (prefix.trim()) {
    h.push(p + u(prefix.trim()) + "\\s*" + p);
  } else {
    h.push("(?<=^|\\n)\\s*" + p);
  }
  
  if (Array.isArray(npcInfo?.titles) && npcInfo.titles.length > 0) {
    const t = npcInfo.titles.map(u).join("|");
    h.push("((" + t + ")\\s+)?");
  }
  
  const v = [];
  const addPattern = (pat, words, len) => {
    v.push({ pattern: pat, weight: 1e4 * words + len });
  };
  
  const g = npcInfo.first_name.trim();
  const m = npcInfo?.last_name?.trim() || null;
  const y = (npcInfo?.middle_names ?? []).map(e => e.trim()).filter(Boolean);
  const _ = y.length ? Math.max(...y.map(e => e.length)) : 0;
  const w = u(g);
  const C = m ? u(m) : null;
  const x = y.length ? y.map(u).join("|") : null;
  
  if (x && C) addPattern(`${w}\\s+(${x})\\s+${C}`, 3, g.length + _ + (m?.length || 0) + 2);
  if (C) {
    addPattern(`${w}\\s+${C}`, 2, g.length + m.length + 1);
    addPattern(`${C}\\s+${w}`, 2, g.length + m.length + 1);
  }
  if (x && C) addPattern(`${C}\\s+(${x})\\s+${w}`, 3, g.length + _ + (m?.length || 0) + 2);
  if (x) addPattern(`${w}\\s+(${x})`, 2, g.length + _ + 1);
  addPattern(w, 1, g.length);
  if (C) addPattern(C, 1, m.length);
  
  if (npcInfo?.nicknames && npcInfo.nicknames.length > 0) {
    npcInfo.nicknames.forEach(nick => {
      const t = nick.trim();
      const words = t.split(/\s+/).filter(Boolean).length || 1;
      if (nick.includes("'") || nick.includes('"')) {
        addPattern(u(nick), words, t.length);
      } else {
        addPattern(u(nick), words, t.length);
        addPattern("'" + u(nick) + "'", words, t.length + 2);
        addPattern('"' + u(nick) + '"', words, t.length + 2);
      }
    });
  }
  
  v.sort((a, b) => b.weight - a.weight);
  h.push(`${d}(?<coreName>${v.map(e => e.pattern).join("|")})(?=$|[^\\p{L}\\p{N}_])`);
  
  if (Array.isArray(npcInfo?.titles) && npcInfo.titles.length > 0) {
    const t = npcInfo.titles.map(u).join("|");
    h.push("(\\s+(" + t + "))?");
  }
  
  const S = i();
  const b = `(?:["'‘’“”][^"'‘’“”:\\n]{1,40}["'‘’“”]|${S}|\\p{Lu}[\\p{L}\\p{N}.'’\\-]*|(?:de|del|della|der|den|van|von|di|da|do|dos|das|la|le|les|du|bin|ibn|al|el|af|av|of|the|y|e|saint|st))`;
  h.push(`(?:\\s+${b}){0,6}`);
  
  if (suffix?.trim()) {
    h.push(`(?:\\*\\*)?\\s*${u(suffix.trim())}(?:\\*\\*(?=\\s|$))?`);
  }
  
  return h.join("");
}

const input = JSON.parse(process.argv[2]);
const res = input.map(tc => compileWyvernAvatarRegex(tc.info, tc.prefix, tc.delimiter));
process.stdout.write(JSON.stringify(res));
"""

proc = subprocess.run(
    ["node", "-e", js_code, json.dumps(test_cases, ensure_ascii=False)],
    capture_output=True,
    encoding="utf-8",
    check=True
)

node_results = json.loads(proc.stdout)

all_matched = True
for i, tc in enumerate(test_cases):
    py_res = compile_wyvern_avatar_regex(tc["info"], prefix=tc["prefix"], delimiter=tc["delimiter"])
    node_res = node_results[i]
    if py_res == node_res:
        print(f"[{i+1}/{len(test_cases)}] {tc['name']}: 100% IDENTICAL (len={len(py_res)})")
    else:
        print(f"[{i+1}/{len(test_cases)}] {tc['name']}: MISMATCH!")
        print("PYTHON:\n", py_res)
        print("NODEJS:\n", node_res)
        all_matched = False

if all_matched:
    print("\nSUCCESS: All 7 test cases match byte-for-byte between Node.js Module 93312 and Python compile_wyvern_avatar_regex!")
else:
    sys.exit(1)
