import os
import re
import glob

sync_dir = os.path.expandvars(r'%LOCALAPPDATA%\Google\Chrome\User Data\Default\Sync Data\LevelDB')
print(f"Scanning {sync_dir}...")

files = glob.glob(os.path.join(sync_dir, "*.ldb")) + glob.glob(os.path.join(sync_dir, "*.log"))
print(f"Found {len(files)} files.")

# Scan for URLs or bookmark titles
urls = set()
api_providers = set()

url_regex = re.compile(rb'https?://[a-zA-Z0-9\-\._~:/\?#\[\]@!$&\'\(\)\*\+,;=%]+')

for fpath in files:
    try:
        with open(fpath, 'rb') as f:
            content = f.read()
            # Find URLs
            for match in url_regex.finditer(content):
                url = match.group(0).decode('utf-8', errors='ignore')
                # Clean up url
                url = url.split('\x00')[0].split('\x01')[0]
                if any(k in url.lower() for k in ['api', 'ai', 'router', 'zhipu', 'openrouter', 'groq', 'studio', 'gemini', 'navy', 'together', 'fireworks', 'deepinfra', 'cohere', 'mistral', 'anthropic']):
                    if len(url) < 150 and not any(x in url for x in ['.png', '.jpg', '.css', '.js', 'google.com/search', 'github.com/google']):
                        urls.add(url)
    except Exception as e:
        print(f"Error {fpath}: {e}")

print(f"Found {len(urls)} relevant AI/API URLs:")
for u in sorted(urls):
    print(" -", u)
