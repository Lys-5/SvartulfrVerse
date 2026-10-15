const fs = require('fs');

async function testPut() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const pid = 'persona_1786335754946';

  const r = await fetch(`https://app.wyvern.chat/api/user-personas/${pid}`, { headers: { 'Authorization': 'Bearer ' + token } });
  const p = await r.json();
  console.log('Original lorebooks count:', p.lorebooks ? p.lorebooks.length : 0);

  // Test with lorebooks mapped to IDs
  const payloadWithIds = {
    ...p,
    lorebooks: (p.lorebooks || []).map(lb => lb.id || lb._id)
  };
  console.log('Payload size with IDs:', JSON.stringify(payloadWithIds).length);

  const res = await fetch(`https://app.wyvern.chat/api/user-personas/${pid}`, {
    method: 'PUT',
    headers: { 'Authorization': 'Bearer ' + token, 'Content-Type': 'application/json' },
    body: JSON.stringify(payloadWithIds)
  });
  console.log('PUT status with IDs:', res.status);
  if (!res.ok) {
    console.log(await res.text());
  } else {
    const verified = await (await fetch(`https://app.wyvern.chat/api/user-personas/${pid}`, { headers: { 'Authorization': 'Bearer ' + token } })).json();
    console.log('Verified lorebooks count after PUT:', (verified.lorebooks || []).length);
  }
}

testPut().catch(console.error);
