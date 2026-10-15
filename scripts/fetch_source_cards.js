const fs = require('fs');
const path = require('path');

async function fetchSourceCards() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

  const targets = [
    // Ukiyo Series
    { id: '_93Rrpm1bDdytjzBqAp99P', label: 'Radek, Goran & Kian (Ukiyo)' },
    { id: '_9AycMJGa4fjy6pn6kgxGj', label: 'Marek (Ukiyo)' },
    { id: '_HMJMqb4EYk2aqRk8FaDRL', label: 'Jaelyn (Ukiyo)' },
    { id: '_1AqYn9gmgWCxb4q7yJmWW', label: 'Neve (Ukiyo)' },
    { id: '_eGUwEF8WhCLA7xVbwYrq7', label: 'Bessie May (Luscious)' },
    // Crimsonmaw Pack
    { id: '_kLVWbeM4YHR3dg6YU7ETk', label: 'Liam O’Connor' },
    { id: '_1AbCPT1jkMH3gYfWcHJ1x', label: 'Hugh Rivers' },
    // Academy of Magic -> CUMS
    { id: '_QMEpqAWP3kMxKTdU9PNa1', label: 'Amerian de Vian' },
    { id: '_8CB4AMJXm1Ge3f7MJYwk7', label: 'Ashton Crowley' },
    { id: '_p3qddkrJfMG2aYDQVDgPE', label: 'Aeril Royen' },
    { id: '_WEpLtWNRkeUQX3G919FE2', label: 'Caien Vaelion' },
    { id: '_BnDXBfPK8KjAbjY8x2PRW', label: 'Lestat Oreven' },
    { id: '_fBDHAtQgFpxbKLDB2RKeU', label: 'Xaiden Nershatar' },
    { id: '_T2RUPxBw8NfW8YyzjNrEL', label: 'Zaire Ziisis' }
  ];

  const results = [];

  for (const t of targets) {
    try {
      const res = await fetch(`https://app.wyvern.chat/api/characters/${t.id}`, {
        headers: { 'Authorization': 'Bearer ' + token }
      });
      if (res.ok) {
        const char = await res.json();
        results.push({
          target: t,
          char: char
        });
      }
    } catch (err) {}
  }

  const scratchDir = path.join(__dirname, '..', 'scratch');
  if (!fs.existsSync(scratchDir)) fs.mkdirSync(scratchDir, { recursive: true });
  const dumpPath = path.join(scratchDir, 'source_cards_dump.json');
  fs.writeFileSync(dumpPath, JSON.stringify(results, null, 2), 'utf8');
  console.log(`Salvati ${results.length} sorgenti in ${dumpPath}`);
}

fetchSourceCards();
