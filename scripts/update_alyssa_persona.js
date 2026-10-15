const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const personaId = 'persona_1786335754946';
  const url = `https://app.wyvern.chat/api/user-personas/${personaId}`;

  console.log('1. Fetching fresh persona state...');
  const resGet = await fetch(url, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!resGet.ok) {
    throw new Error(`Failed to GET persona: ${resGet.status} ${resGet.statusText}`);
  }
  const current = await resGet.json();
  fs.writeFileSync('scratch/alyssa_persona_backup_before_appearances.json', JSON.stringify(current, null, 2));
  console.log('Backup saved.');

  // Load prepared payload from scratch/alyssa_persona_payload.json
  const prepared = JSON.parse(fs.readFileSync('scratch/alyssa_persona_payload.json', 'utf8'));

  // Extract lorebook string IDs to avoid 413 Payload Too Large
  const lorebookIds = (current.lorebooks || []).map(lb => lb.id || lb._id);

  // Build the clean update payload
  const payload = {
    name: current.name || 'Alyssa',
    importance: current.importance || 'high',
    avatar: current.avatar,
    title: current.title || 'The White Moon',
    comment: current.comment || 'Seven Hills Pack Princess & Dominant Omega Healer',
    pronoun_subjective: current.pronoun_subjective || 'she',
    pronoun_objective: current.pronoun_objective || 'her',
    pronoun_possessive_determiner: current.pronoun_possessive_determiner || 'her',
    pronoun_possessive_pronoun: current.pronoun_possessive_pronoun || 'hers',
    pronoun_reflexive: current.pronoun_reflexive || 'herself',
    lorebooks: lorebookIds,
    appearances: prepared.appearances,
    outfits: prepared.outfits,
    description: prepared.description,
    default_appearance: prepared.default_appearance,
    default_outfit: prepared.default_outfit
  };

  console.log('\n2. Sending PUT update with payload size:', JSON.stringify(payload).length, 'bytes...');
  const resPut = await fetch(url, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });

  console.log('PUT response status:', resPut.status, resPut.statusText);
  if (!resPut.ok) {
    const errText = await resPut.text();
    throw new Error(`PUT failed: ${resPut.status} ${errText}`);
  }
  const putResult = await resPut.json();
  console.log('PUT success! Updated persona id:', putResult.id || putResult.persona_id);

  console.log('\n3. Performing GET verification to confirm persistence...');
  const resVerify = await fetch(url, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!resVerify.ok) {
    throw new Error(`Verification GET failed: ${resVerify.status}`);
  }
  const verified = await resVerify.json();
  fs.writeFileSync('scratch/alyssa_persona_after_appearances.json', JSON.stringify(verified, null, 2));

  console.log('\n=== VERIFICATION RESULTS ===');
  console.log('Appearances count:', verified.appearances?.length);
  verified.appearances?.forEach(a => {
    console.log(` - Appearance [${a.name}] (id: ${a.id}): ${a.description.length} chars`);
    console.log(`   Preview: ${a.description.slice(0, 100).replace(/\n/g, ' ')}...`);
  });

  console.log('\nDefault Appearance:', verified.default_appearance);
  console.log('Default Outfit:', verified.default_outfit);

  const hybridOutfit = verified.outfits?.find(o => o.name.toLowerCase() === 'hybrid');
  const fullshiftOutfit = verified.outfits?.find(o => o.name.toLowerCase().includes('fullshift'));
  console.log(`\n - Outfit [hybrid]: ${hybridOutfit?.description.length} chars | Display override: ${hybridOutfit?.display_name_override}`);
  console.log(` - Outfit [fullshift]: ${fullshiftOutfit?.description.length} chars | Display override: ${fullshiftOutfit?.display_name_override}`);

  const headerLine = verified.description.split('\n')[0];
  console.log(`\n - Description header: ${headerLine.slice(0, 110)}...`);
  console.log(` - Description total length: ${verified.description.length} chars`);
  console.log(` - Attached lorebooks count: ${verified.lorebooks?.length}`);
  (verified.lorebooks || []).forEach(lb => console.log(`   * ${lb.name} (${lb.id})`));
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
