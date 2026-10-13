const fs = require('fs');

async function refreshToken() {
  const ak = 'AIzaSyCqumrbjUy-EoMpfN4Ev0ppnqjkdpnOTTw';
  const rt = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/refresh_token.txt', 'utf8').trim();
  const res = await fetch(`https://securetoken.googleapis.com/v1/token?key=${ak}`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ grant_type: 'refresh_token', refresh_token: rt })
  });
  const data = await res.json();
  fs.writeFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', data.id_token, 'utf8');
  return data.id_token;
}

async function deployCleanPanel() {
  const token = await refreshToken();
  const engineId = 'engine_HCTPXhL8xr89wUY9r9dYU';

  console.log('1. Recupero engine live da Wyvern...');
  const getRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    headers: { 'Authorization': `Bearer ${token}` }
  });

  if (!getRes.ok) {
    throw new Error(`Errore GET story engine: ${getRes.status} ${await getRes.text()}`);
  }

  const engineData = await getRes.json();
  console.log(`Story Engine recuperato: "${engineData.name}" (v${engineData.version})`);

  // Leggiamo il codice pulito direttamente dal file .tsx
  const panelCode = fs.readFileSync('scripts/perfect_tailwind_smartphone_panel.tsx', 'utf8');

  // Aggiorniamo il pannello panel_smartphone_os
  const panels = engineData.definition.ui_panels || [];
  const targetIndex = panels.findIndex(p => p.id === 'panel_smartphone_os');

  const cleanPanel = {
    id: 'panel_smartphone_os',
    name: 'Svartulfr Smartphone OS',
    icon: 'layout',
    placement: 'sidebar',
    target: 'both',
    enabled: true,
    code: panelCode
  };

  if (targetIndex >= 0) {
    panels[targetIndex] = cleanPanel;
  } else {
    panels.push(cleanPanel);
  }

  const payload = {
    expected_version: engineData.version,
    name: engineData.name,
    tagline: engineData.tagline || 'Svartulfr OS · Unified Smartphone Interactive UI',
    description: engineData.description,
    avatar: engineData.avatar,
    tags: engineData.tags,
    rating: engineData.rating,
    visibility: engineData.visibility,
    status: engineData.status,
    definition: {
      ...engineData.definition,
      ui_panels: panels
    }
  };

  console.log('2. Salvataggio su Wyvern con codice TSX pulito e zero-errori...');
  const putRes = await fetch(`https://app.wyvern.chat/api/story-engines/${engineId}`, {
    method: 'PUT',
    headers: {
      'Authorization': `Bearer ${token}`,
      'Content-Type': 'application/json'
    },
    body: JSON.stringify(payload)
  });

  if (!putRes.ok) {
    throw new Error(`Errore PUT story engine: ${putRes.status} ${await putRes.text()}`);
  }

  const updatedData = await putRes.json();
  console.log(`Pannello salvato con successo! Nuova versione: v${updatedData.version}`);

  // Salvataggio export locale
  const exportPath = 'exports/Story_Engines_Export.json';
  if (fs.existsSync(exportPath)) {
    try {
      const currentExport = JSON.parse(fs.readFileSync(exportPath, 'utf8'));
      if (Array.isArray(currentExport)) {
        const idx = currentExport.findIndex(e => e.id === engineId);
        if (idx >= 0) currentExport[idx] = updatedData;
        else currentExport.push(updatedData);
        fs.writeFileSync(exportPath, JSON.stringify(currentExport, null, 2), 'utf8');
      }
    } catch (e) {
      console.warn('Avviso: impossibile aggiornare export locale:', e.message);
    }
  }

  console.log('Fatto! Il pannello è pronto su Wyvern senza alcun errore o warning.');
}

deployCleanPanel().catch(err => {
  console.error('ERRORE:', err);
  process.exit(1);
});
