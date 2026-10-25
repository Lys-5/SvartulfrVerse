// scratch/test_node_nc_parser.js
const fs = require('fs');

// Read live scenario and world characters
const scenario = JSON.parse(fs.readFileSync('FINAL/scenarios/Svartulfr_World_Scenario_SUCC_Welcome_Day.json', 'utf8'));
const modDump = JSON.parse(fs.readFileSync('scratch/mod93312_dump.json', 'utf8'));

// Extract WH function from module 93312
// In mod93312: n.d(t,{WH:function(){return m},YP:function(){return v}})
// Let's create the WH function in JS
function compileWH(charInfo, prefix = '=>', suffix = ':') {
  if (!charInfo || !charInfo.first_name || !charInfo.first_name.trim()) return '';
  const s = e => e.normalize('NFC');
  const u = e => s(e).replace(/[.*+?^${}()|[\]\\]/g, '\\$&')
                      .replace(/['\u2018\u2019\u02BC\u201B\u2032]/g, "['‘’ʼ‛′]")
                      .replace(/[-\u2010\u2011\u2012\u2013\u2014\u2212]/g, '[-‐‑‒–—−]');
  const d = prefix.trim() ? '(?<=^|[^\\p{L}\\p{N}_])' : '';
  const h = [];
  const p = '(?:\\*\\*)?';
  if (prefix.trim()) {
    h.push(p + u(prefix.trim()) + '\\s*' + p);
  } else {
    h.push('(?<=^|\\n)\\s*' + p);
  }
  if (Array.isArray(charInfo.titles) && charInfo.titles.length > 0) {
    const t = charInfo.titles.map(u).join('|');
    h.push(`((${t})\\s+)?`);
  }
  const v = [];
  const f = (pat, mult, len) => { v.push({ pattern: pat, weight: 10000 * mult + len }); };
  const g = charInfo.first_name.trim();
  const m = (charInfo.last_name || '').trim() || null;
  const y = (charInfo.middle_names || []).map(e => e.trim()).filter(Boolean);
  const _ = y.length ? Math.max(...y.map(e => e.length)) : 0;
  const w = u(g);
  const C = m ? u(m) : null;
  const x = y.length ? y.map(u).join('|') : null;

  if (x && C) f(`${w}\\s+(${x})\\s+${C}`, 3, g.length + _ + (m ? m.length : 0) + 2);
  if (C) {
    f(`${w}\\s+${C}`, 2, g.length + m.length + 1);
    f(`${C}\\s+${w}`, 2, g.length + m.length + 1);
  }
  if (x && C) f(`${C}\\s+(${x})\\s+${w}`, 3, g.length + _ + (m ? m.length : 0) + 2);
  if (x) f(`${w}\\s+(${x})`, 2, g.length + _ + 1);
  f(w, 1, g.length);
  if (C) f(C, 1, m.length);
  if (charInfo.nicknames && charInfo.nicknames.length > 0) {
    charInfo.nicknames.forEach(e => {
      const t = e.trim();
      const n = t.split(/\s+/).filter(Boolean).length || 1;
      if (e.includes("'") || e.includes('"')) {
        f(u(e), n, t.length);
      } else {
        f(u(e), n, t.length);
        f(`'${u(e)}'`, n, t.length + 2);
        f(`"${u(e)}"`, n, t.length + 2);
      }
    });
  }
  v.sort((a, b) => b.weight - a.weight);
  h.push(`${d}(?<coreName>${v.map(e => e.pattern).join('|')})(?=$|[^\\p{L}\\p{N}_])`);
  if (Array.isArray(charInfo.titles) && charInfo.titles.length > 0) {
    const t = charInfo.titles.map(u).join('|');
    h.push(`(\\s+(${t}))?`);
  }
  if (suffix && suffix.trim()) {
    h.push(`(?:\\*\\*)?\\s*${u(suffix.trim())}(?:\\*\\*(?=\\s|$))?`);
  }
  return '^' + h.join('');
}

// 13 Primary Characters
const CHARS = [
  { first_name: 'Erik', middle_names: ['Cornelius', 'Ulfr'], last_name: 'Douglas', nicknames: ['The Prime Alpha', 'The Patriarch'] },
  { first_name: 'Logan', middle_names: ['Dominic', 'Járn'], last_name: 'Douglas', nicknames: ['Uncle Logan', 'The Peacemaker'] },
  { first_name: 'Edric', middle_names: [], last_name: 'Douglas', nicknames: ['Ed', 'Pup'] },
  { first_name: 'Noah', middle_names: ['Loki'], last_name: 'Douglas Bloodmoon', nicknames: ['The Diplomat', 'The Fixer'] },
  { first_name: 'Malachia', middle_names: ['Björn'], last_name: 'Douglas Bloodmoon', nicknames: ['The Iron Shield', 'Mala'] },
  { first_name: 'Jasper', middle_names: ['Svartr'], last_name: 'Douglas Bloodmoon', nicknames: ['DJ Frequency', 'Shadow Wolf', 'Jasp'] },
  { first_name: 'Alyssa', middle_names: ['Hvit'], last_name: 'Douglas Bloodmoon', nicknames: ['White Moon', 'Lyssa', 'The Anchor'] },
  { first_name: 'Wulfnic', middle_names: ['Báleygr'], last_name: 'Bloodmoon', nicknames: ['The First Tusk', 'Primo Zanna', 'The Ancient'] },
  { first_name: 'Zefir', middle_names: [], last_name: 'Hvitskog', nicknames: ['White Ghost', 'Firstborn'] },
  { first_name: 'Mackenzie', middle_names: [], last_name: 'Sanchez-Rogers', nicknames: ['Mac'] },
  { first_name: 'Finnegan', middle_names: [], last_name: 'Novak', nicknames: ['Finn'] },
  { first_name: 'Sierra', middle_names: [], last_name: 'Cruz', nicknames: [] },
  { first_name: 'Scarlett', middle_names: [], last_name: 'Rose', nicknames: [] }
];

console.log('--- Testing Node.js V8 Regex Compilation for all 13 characters ---');
CHARS.forEach((c, i) => {
  const pat = compileWH(c, '=>', ':');
  const reg = new RegExp(pat, 'gimu');
  const testStr = `=>${c.first_name}:\n"Test line"`;
  const m = reg.exec(testStr);
  console.log(`[${i+1}] ${c.first_name}: pattern length ${pat.length} | Match on '${testStr.split('\n')[0]}': ${m ? 'PASS' : 'FAIL'}`);
  if (!m) {
    throw new Error(`Failed to match ${c.first_name}`);
  }
});

// Test Fallback regex for Narrator
const fallback = /^=>\s*([^:\n]{1,35}):\s*/gim;
const narrTest = '=>Narrator:\nNarration';
const narrM = fallback.exec(narrTest);
console.log(`Fallback regex match on '${narrTest.split('\n')[0]}': ${narrM && narrM[1] === 'Narrator' ? 'PASS' : 'FAIL'}`);

console.log('\n--- Node.js V8 execution completed successfully! ---');
