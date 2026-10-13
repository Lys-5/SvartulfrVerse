const fs = require('fs');
const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();

async function testPut() {
  const locId = '_63BP7yfwEpEJbDgEqP2ew'; // Sugar Moon Bakery
  
  // 1. GET existing
  const getRes = await fetch(`https://app.wyvern.chat/api/worlds/locations/${locId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const existing = await getRes.json();
  console.log('GET existing name:', existing.name);
  console.log('GET existing property_config:', existing.property_config);
  console.log('GET existing marketplace_config:', existing.marketplace_config);
  console.log('GET existing jobs:', existing.jobs);

  // 2. Prepare payload
  const payload = {
    property_config: {
      enabled: false
    },
    marketplace_config: {
      enabled: true,
      name: "Sugar Moon Bakery",
      description: "Pasticceria artigianale di Arcadia famosa per dolci al miele di luna, pane fresco e infusi calmi per therianthropi.",
      buy_rate: 0.5,
      inventory: [
        {
          lexicon_entry_id: "_nKrK7KRNbpFHtg6f8QkLj",
          stock: 20,
          price_override: { "fbecc738-f9f7-4426-b8a1-a237b8ad922c": 8 }
        },
        {
          lexicon_entry_id: "_HFeBYyrcXfB1pcbDW8NC6",
          stock: 15,
          price_override: { "fbecc738-f9f7-4426-b8a1-a237b8ad922c": 6 }
        },
        {
          lexicon_entry_id: "_Xcgd9WWjX3GHMm7DkaLtw",
          stock: 25,
          price_override: { "fbecc738-f9f7-4426-b8a1-a237b8ad922c": 5 }
        },
        {
          lexicon_entry_id: "_NyLqqJg949nYc7wRKmx3Y",
          stock: 30,
          price_override: { "fbecc738-f9f7-4426-b8a1-a237b8ad922c": 4 }
        }
      ]
    },
    jobs: ["_tatXe1j7kFVmnKNzftMrE"]
  };

  // 3. PUT update
  const putRes = await fetch(`https://app.wyvern.chat/api/worlds/locations/${locId}`, {
    method: 'PUT',
    headers: {
      'Authorization': 'Bearer ' + token,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });
  console.log('PUT status:', putRes.status);
  const putData = await putRes.json();
  console.log('PUT response:', putData);

  // 4. Verify with fresh GET
  const verifyRes = await fetch(`https://app.wyvern.chat/api/worlds/locations/${locId}`, {
    headers: { 'Authorization': 'Bearer ' + token }
  });
  const verified = await verifyRes.json();
  console.log('VERIFY market enabled:', verified.marketplace_config?.enabled);
  console.log('VERIFY inventory count:', verified.marketplace_config?.inventory?.length);
  console.log('VERIFY jobs:', verified.jobs);
}

testPut().catch(console.error);
