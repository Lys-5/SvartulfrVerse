const fs = require('fs');

const tokenPath = 'C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt';
const token = fs.readFileSync(tokenPath, 'utf8').trim();
const worldId = '_CgYT8fHXpDC4crjmegQF7';

const cleanedExisting = JSON.parse(fs.readFileSync('scratch/cleaned_existing_lexicon.json', 'utf8'));
const filledEmpty = JSON.parse(fs.readFileSync('scratch/filled_empty_lexicon.json', 'utf8'));
const newEntries = JSON.parse(fs.readFileSync('scratch/new_lexicon_entries.json', 'utf8'));

async function putLexicon(id, body) {
  const url = `https://app.wyvern.chat/api/worlds/lexicon/${id}`;
  const res = await fetch(url, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(body)
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`PUT ${id} failed (${res.status}): ${text}`);
  }
  return await res.json();
}

async function postLexicon(body) {
  const url = `https://app.wyvern.chat/api/worlds/lexicon`;
  const res = await fetch(url, {
    method: 'POST',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({ ...body, world_id: worldId })
  });
  if (!res.ok) {
    const text = await res.text();
    throw new Error(`POST failed (${res.status}): ${text}`);
  }
  return await res.json();
}

async function run() {
  console.log('=== STEP 1: UPDATING CLEANED EXISTING ENTRIES (11) ===');
  for (const entry of cleanedExisting) {
    console.log(`Updating ${entry.name} (${entry.id})...`);
    await putLexicon(entry.id, { content: entry.content });
    console.log(`-> Updated successfully.`);
  }

  console.log('\n=== STEP 2: FILLING EMPTY ENTRIES (3) ===');
  for (const entry of filledEmpty) {
    console.log(`Filling ${entry.name} (${entry.id})...`);
    await putLexicon(entry.id, { content: entry.content });
    console.log(`-> Filled successfully.`);
  }

  console.log('\n=== STEP 3: POSTING NEW ENTRIES (3) ===');
  for (const entry of newEntries) {
    console.log(`Creating ${entry.name}...`);
    const created = await postLexicon(entry);
    console.log(`-> Created with ID: ${created.id || created._id}`);
  }

  console.log('\nALL LEXICON OPERATIONS COMPLETED SUCCESSFULLY!');
}

run().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
