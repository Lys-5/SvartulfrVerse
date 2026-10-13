const fs = require('fs');
const path = require('path');

const WORLD_ID = '_CgYT8fHXpDC4crjmegQF7';
const API_BASE = 'https://app.wyvern.chat/api';

function getAllImages(dir) {
  let res = [];
  function walk(d) {
    const list = fs.readdirSync(d);
    for (const f of list) {
      const full = path.join(d, f);
      const st = fs.statSync(full);
      if (st.isDirectory()) {
        walk(full);
      } else {
        const ext = path.extname(f).toLowerCase();
        if (['.png', '.jpg', '.jpeg', '.webp'].includes(ext)) {
          const rel = path.relative('.', full).replace(/\\/g, '/');
          res.push({
            filepath: full.replace(/\\/g, '/'),
            filename: f,
            relpath: rel,
            ext
          });
        }
      }
    }
  }
  if (fs.existsSync(dir)) walk(dir);
  return res;
}

function deriveMetadata(img) {
  const rel = img.relpath;
  const baseName = path.basename(img.filename, img.ext);
  
  // Format title: replace underscores/dashes with spaces, capitalize
  let title = baseName
    .replace(/[_-]+/g, ' ')
    .replace(/\b\w/g, c => c.toUpperCase());

  let type = 'artwork';
  let tags = [];

  if (rel.includes('characters/avatars_legacy')) {
    type = 'avatar';
    tags.push('character', 'legacy', 'avatar');
    title = `${title} (Legacy Avatar)`;
  } else if (rel.includes('characters/')) {
    type = 'character';
    tags.push('character');
  } else if (rel.includes('environments/')) {
    type = 'environment';
    tags.push('environment', 'location', 'background');
  } else if (rel.includes('lore_and_gods/')) {
    type = 'lore';
    tags.push('lore', 'deity', 'mythology');
  } else {
    tags.push('asset');
  }

  return { title, type, tags };
}

function getContentType(ext) {
  if (ext === '.webp') return 'image/webp';
  if (ext === '.png') return 'image/png';
  if (ext === '.jpg' || ext === '.jpeg') return 'image/jpeg';
  return 'application/octet-stream';
}

async function uploadImage(headers, img) {
  const size = fs.statSync(img.filepath).size;
  const contentType = getContentType(img.ext);
  const meta = deriveMetadata(img);

  // 1. Request Cloudflare upload URL
  const reqUrl = `${API_BASE}/cloudflare/request-upload-url`;
  const reqPayload = {
    metadata: {
      filename: img.filename,
      contentType,
      size,
      context: 'gallery',
      worldId: WORLD_ID
    }
  };

  const resp1 = await fetch(reqUrl, {
    method: 'POST',
    headers: { ...headers, 'Content-Type': 'application/json' },
    body: JSON.stringify(reqPayload)
  });

  if (!resp1.ok) {
    throw new Error(`Step 1 request URL failed (${resp1.status}): ${await resp1.text()}`);
  }

  const data1 = await resp1.json();
  const uploadURL = data1.uploadURL;
  const imageId = data1.id;

  // 2. Upload binary to Cloudflare
  const fileBytes = fs.readFileSync(img.filepath);
  const blob = new Blob([fileBytes], { type: contentType });
  const form = new FormData();
  form.append('file', blob, img.filename);

  const resp2 = await fetch(uploadURL, {
    method: 'POST',
    body: form
  });

  if (!resp2.ok) {
    throw new Error(`Step 2 binary upload failed (${resp2.status})`);
  }

  // 3. Register in World Gallery
  const publicURL = `https://imagedelivery.net/Dv4koOwHQU3XnXLqtl0aVQ/${imageId}/public`;
  const galPayload = {
    title: meta.title,
    description: `Asset from repository: ${img.relpath}`,
    imageURL: publicURL,
    type: meta.type,
    tags: meta.tags
  };

  const resp3 = await fetch(`${API_BASE}/worlds/${WORLD_ID}/gallery`, {
    method: 'POST',
    headers: { ...headers, 'Content-Type': 'application/json' },
    body: JSON.stringify(galPayload)
  });

  if (!resp3.ok) {
    throw new Error(`Step 3 gallery register failed (${resp3.status}): ${await resp3.text()}`);
  }

  const item = await resp3.json();
  return { id: item.id, title: meta.title, publicURL };
}

async function main() {
  const token = fs.readFileSync('C:/Users/mande/.gemini/antigravity/brain/74bb3384-9979-419b-80ab-c29e070cbffe/scratch/wyvern_token.txt', 'utf8').trim();
  const headers = { 'Authorization': 'Bearer ' + token, 'User-Agent': 'Mozilla/5.0' };

  // Fetch current gallery to avoid duplicates
  const curRes = await fetch(`${API_BASE}/worlds/${WORLD_ID}/gallery`, { headers });
  const curGallery = await curRes.json();
  const existingTitles = new Set(curGallery.map(g => g.title));
  console.log(`Current gallery count on server: ${curGallery.length}`);

  const allImages = getAllImages('asset');
  console.log(`Total images found on disk: ${allImages.length}`);

  const toUpload = allImages.filter(img => {
    const meta = deriveMetadata(img);
    return !existingTitles.has(meta.title);
  });
  console.log(`Images to upload: ${toUpload.length}`);

  let successCount = 0;
  let failCount = 0;

  for (let i = 0; i < toUpload.length; i++) {
    const img = toUpload[i];
    try {
      const res = await uploadImage(headers, img);
      successCount++;
      console.log(`[${i + 1}/${toUpload.length}] [OK] ${res.title} -> ${res.publicURL}`);
    } catch (e) {
      failCount++;
      console.error(`[${i + 1}/${toUpload.length}] [FAIL] ${img.relpath}: ${e.message}`);
    }

    // Small delay to prevent rate limits
    await new Promise(r => setTimeout(r, 200));
  }

  console.log(`\n=== BULK UPLOAD SUMMARY ===`);
  console.log(`Successfully uploaded: ${successCount}`);
  console.log(`Failed: ${failCount}`);

  // Fetch final count
  const finalRes = await fetch(`${API_BASE}/worlds/${WORLD_ID}/gallery`, { headers });
  const finalGallery = await finalRes.json();
  console.log(`Total World Gallery items on server: ${finalGallery.length}`);
}

main().catch(console.error);
