const fs = require('fs');

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const worldId = '_CgYT8fHXpDC4crjmegQF7';
  const alyssaPersonaId = 'persona_1786335754946';
  const alyssaWorldCharId = '_MXcEC8Y6B3BNm3b1ttHj6';
  const npcLbId = '_LBkRWNpPxpdn6dxYaDU2b';

  console.log('=== STEP 1: DEPLOY ALYSSA (PERSONA, WORLD CARD, LOREBOOK) ===');

  // 1. UPDATE USER PERSONA
  console.log('\n1. Fetching Alyssa Persona...');
  const resP = await fetch(`https://app.wyvern.chat/api/user-personas/${alyssaPersonaId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  if (!resP.ok) throw new Error('Failed to fetch persona: ' + resP.status);
  const pData = await resP.json();

  const lines = pData.description.split('\n');
  const newHeader = '[NAME: Alyssa Hvit Douglas Bloodmoon; FIRST_NAME: Alyssa; MIDDLE_NAME: Hvit (Wolf Name, Presentation at 13); LAST_NAME: Douglas Bloodmoon; ALIASES: Lys, Little Moon, Sunflower, The White Moon, The Anchor; AGE: 19 (Born April 22, 2005); GENDER: Female (She/Her); SPECIES: Werewolf, Founding Bloodline; SECONDARY_SEX: Dominant Omega (White Moon); HOUSE: Bloodmoon and Douglas; PACK: Seven Hills; BIRTH_RUNE: Gebo (5th Day Wrist Inscription, Serpent Tooth & Cold Iron Ink, Twin Bond); SOCIAL_STATUS: Citizen, Core of Villa Douglas compound, Guild Member; OCCUPATION: 1st-year undergrad (SUCC) Pre-Med, Novice Healing Mage, Botanist, Field Medic in the Guild, Pack Mom designate (inheriting office from Elizabeth Duskwood at 21); HEIGHT: 155cm (5\'1"); BUILD: Petite hourglass frame (Bust: 95cm, Waist: 55cm, Hips: 95cm); HAIR: Caramel-chestnut waves to the tailbone; EYES: Mint-green doe eyes; FEATURES: Luminous skin, crescent moon birthmark on left hip (Mark of Mani), shared Gebo tattoo on left wrist with Jasper, pierced belly button and ears; SHIFTS: Active physical form defined by Appearance (Base, Hybrid, full-shift); SCENT: Wild honey, moonflower, and medicinal herbs]';
  lines[0] = newHeader;
  const updatedDesc = lines.join('\n');

  const pPayload = {
    name: 'Alyssa',
    importance: pData.importance || 'high',
    avatar: pData.avatar,
    title: 'The White Moon',
    comment: pData.comment || 'Seven Hills Pack Princess & Dominant Omega Healer',
    pronoun_subjective: pData.pronoun_subjective || 'she',
    pronoun_objective: pData.pronoun_objective || 'her',
    pronoun_possessive_determiner: pData.pronoun_possessive_determiner || 'her',
    pronoun_possessive_pronoun: pData.pronoun_possessive_pronoun || 'hers',
    pronoun_reflexive: pData.pronoun_reflexive || 'herself',
    lorebooks: (pData.lorebooks || []).map(lb => lb.id || lb._id),
    appearances: pData.appearances,
    outfits: pData.outfits,
    description: updatedDesc,
    default_appearance: pData.default_appearance,
    default_outfit: pData.default_outfit
  };

  const resPutP = await fetch(`https://app.wyvern.chat/api/user-personas/${alyssaPersonaId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(pPayload)
  });
  console.log('Alyssa Persona PUT status:', resPutP.status);

  // 2. UPDATE WORLD CHARACTER CARD
  console.log('\n2. Fetching Alyssa World Character Card...');
  const resC = await fetch(`https://app.wyvern.chat/api/worlds/characters/${alyssaWorldCharId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const cData = await resC.json();
  fs.writeFileSync('scratch/pre_update_alyssa_world_card.json', JSON.stringify(cData, null, 2));

  const cLines = (cData.long_summary || '').split('\n');
  cLines[0] = newHeader;
  const updatedCardSummary = cLines.join('\n');

  const cardPayload = {
    display_name: 'Alyssa Hvit Douglas Bloodmoon',
    first_name: 'Alyssa',
    middle_names: ['Hvit'],
    last_name: 'Douglas Bloodmoon',
    long_summary: updatedCardSummary
  };

  const resPutC = await fetch(`https://app.wyvern.chat/api/worlds/characters/${alyssaWorldCharId}`, {
    method: 'PUT',
    headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
    body: JSON.stringify(cardPayload)
  });
  console.log('Alyssa World Character PUT status:', resPutC.status);

  // 3. UPDATE NPC PRIMARY LOREBOOK ENTRY
  console.log('\n3. Fetching NPC Primary Lorebook...');
  const resLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });
  const lbData = await resLb.json();
  fs.writeFileSync('scratch/pre_update_npc_primary_for_alyssa.json', JSON.stringify(lbData, null, 2));

  let alyssaEntryUpdated = false;
  const updatedLexicon = lbData.lexicon.map(e => {
    if (e.name === 'Alyssa Douglas Bloodmoon' || (e.name && e.name.includes('Alyssa'))) {
      alyssaEntryUpdated = true;
      const eLines = (e.content || '').split('\n');
      eLines[0] = newHeader;
      return {
        ...e,
        name: 'Alyssa Hvit Douglas Bloodmoon',
        keys: ['Alyssa', 'Hvit', 'Alyssa Hvit', 'White Moon', 'Omega', 'twin sister'],
        content: eLines.join('\n')
      };
    }
    return e;
  });

  if (alyssaEntryUpdated) {
    const resPutLb = await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, {
      method: 'PUT',
      headers: { 'Authorization': `Bearer ${token}`, 'Content-Type': 'application/json' },
      body: JSON.stringify({ lexicon: updatedLexicon })
    });
    console.log('NPC Primary Lorebook PUT status (Alyssa):', resPutLb.status);
  } else {
    console.warn('Alyssa entry not found in NPC Primary Lorebook!');
  }

  // 4. VERIFY ALL 3 TARGETS
  console.log('\n=== VERIFICATION GET ===');
  const vP = await (await fetch(`https://app.wyvern.chat/api/user-personas/${alyssaPersonaId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  console.log('Verified Persona description header:');
  console.log(' ->', vP.description.split('\n')[0].slice(0, 110) + '...');

  const vC = await (await fetch(`https://app.wyvern.chat/api/worlds/characters/${alyssaWorldCharId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  console.log('Verified World Card:', vC.display_name, '| First:', vC.first_name, '| Middle:', vC.middle_names, '| Last:', vC.last_name);

  const vLb = await (await fetch(`https://app.wyvern.chat/api/lorebooks/${npcLbId}`, { headers: { 'Authorization': `Bearer ${token}` } })).json();
  const vAlyssaEntry = vLb.lexicon.find(e => e.name && e.name.includes('Alyssa'));
  console.log('Verified NPC Primary Entry:', vAlyssaEntry?.name, '| Keys:', vAlyssaEntry?.keys);
  console.log(' -> Header:', vAlyssaEntry?.content.split('\n')[0].slice(0, 100) + '...');
}

main().catch(err => {
  console.error('Fatal error:', err);
  process.exit(1);
});
