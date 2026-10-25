const fs = require('fs');

// Extract the auto-generation function directly from module 93312
const modCode = fs.readFileSync('scratch/modules/93312.js', 'utf-8');

// We can construct the function in a sandboxed vm or eval
function i() {
  return '(?:\\([^()\\[\\]:\\r\\n]{1,80}\\)|\\[[^()\\[\\]:\\r\\n]{1,80}\\])';
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

// Test cases
const test1 = {
  first_name: "Erik",
  middle_names: ["Ulfr"],
  last_name: "Douglas",
  nicknames: ["The Old Wolf", "Pack Leader"],
  titles: ["Lord", "Alpha"]
};

console.log("=== TEST 1: Erik Douglas (prefix empty) ===");
console.log(compileWyvernAvatarRegex(test1, "", ":"));

console.log("\n=== TEST 2: Scarlett Rose (prefix empty) ===");
const test2 = {
  first_name: "Scarlett",
  last_name: "Rose",
  nicknames: ["Red"]
};
console.log(compileWyvernAvatarRegex(test2, "", ":"));

console.log("\n=== TEST 3: Sierra Cruz (prefix empty) ===");
const test3 = {
  first_name: "Sierra",
  last_name: "Cruz"
};
console.log(compileWyvernAvatarRegex(test3, "", ":"));

console.log("\n=== TEST 4: Sierra Cruz (prefix '=>') ===");
console.log(compileWyvernAvatarRegex(test3, "=>", ":"));
