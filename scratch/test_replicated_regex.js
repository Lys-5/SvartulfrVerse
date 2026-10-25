// Test the exact Wyvern regex generator from module 93312
function generateNpcRegex(npc_info, prefix = "", delimiter = ":") {
  if (!npc_info?.first_name?.trim()) return "";
  
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

  if (Array.isArray(npc_info?.titles) && npc_info.titles.length > 0) {
    const t = npc_info.titles.map(u).join("|");
    h.push("((" + t + ")\\s+)?");
  }

  const v = [];
  const f = (pattern, weightFactor, length) => {
    v.push({ pattern, weight: 10000 * weightFactor + length });
  };

  const g = npc_info.first_name.trim();
  const m = npc_info?.last_name?.trim() || null;
  const y = (npc_info?.middle_names ?? []).map(e => e.trim()).filter(Boolean);
  const _ = y.length ? Math.max(...y.map(e => e.length)) : 0;
  
  const w = u(g);
  const C = m ? u(m) : null;
  const x = y.length ? y.map(u).join("|") : null;

  if (x && C) f(`${w}\\s+(${x})\\s+${C}`, 3, g.length + _ + (m?.length ?? 0) + 2);
  if (C) {
    f(`${w}\\s+${C}`, 2, g.length + m.length + 1);
    f(`${C}\\s+${w}`, 2, g.length + m.length + 1);
  }
  if (x && C) f(`${C}\\s+(${x})\\s+${w}`, 3, g.length + _ + (m?.length ?? 0) + 2);
  if (x) f(`${w}\\s+(${x})`, 2, g.length + _ + 1);
  
  f(w, 1, g.length);
  if (C) f(C, 1, m.length);

  if (npc_info?.nicknames && npc_info.nicknames.length > 0) {
    npc_info.nicknames.forEach(e => {
      const t = e.trim();
      const n = t.split(/\s+/).filter(Boolean).length || 1;
      if (e.includes("'") || e.includes('"')) {
        f(u(e), n, t.length);
      } else {
        f(u(e), n, t.length);
        f("'" + u(e) + "'", n, t.length + 2);
        f('"' + u(e) + '"', n, t.length + 2);
      }
    });
  }

  v.sort((a, b) => b.weight - a.weight);
  
  h.push(`${d}(?<coreName>${v.map(e => e.pattern).join("|")})(?=$|[^\\p{L}\\p{N}_])`);

  if (Array.isArray(npc_info?.titles) && npc_info.titles.length > 0) {
    const t = npc_info.titles.map(u).join("|");
    h.push("(\\s+(" + t + "))?");
  }

  // Common title/prefix words and particles
  const S = "(?:\\([^()\\[\\]:\\r\\n]{1,80}\\)|\\[[^()\\[\\]:\\r\\n]{1,80}\\])";
  const b = `(?:["'‘’“”][^"'‘’“”:\\n]{1,40}["'‘’“”]|${S}|\\p{Lu}[\\p{L}\\p{N}.'’\\-]*|(?:de|del|della|der|den|van|von|di|da|do|dos|das|la|le|les|du|bin|ibn|al|el|af|av|of|the|y|e|saint|st))`;
  h.push(`(?:\\s+${b}){0,6}`);

  if (delimiter?.trim()) {
    h.push(`(?:\\*\\*)?\\s*${u(delimiter.trim())}(?:\\*\\*(?=\\s|$))?`);
  }

  return h.join("");
}

// Test with Scarlett Rose
const scarlett = {
  first_name: "Scarlett",
  last_name: "Rose",
  middle_names: [],
  nicknames: ["Scarlett"],
  titles: []
};

console.log("=== Generated Regex for Scarlett Rose ===");
console.log(generateNpcRegex(scarlett));

// Test with Alyssa
const alyssa = {
  first_name: "Alyssa",
  middle_names: ["Hvit"],
  last_name: "Douglas Bloodmoon",
  nicknames: ["Lys", "Little Moon", "Sunflower"],
  titles: ["The White Moon", "Mother of Wolves"]
};

console.log("\n=== Generated Regex for Alyssa ===");
console.log(generateNpcRegex(alyssa));
