import urllib.request
import re
import json

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/assistants/%5Bid%5D/page-cbe4530944bdffb9.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

print("Assistant page chunk length:", len(content))

# Look for form fields, labels, validation schema (zod or yup or formik), default values
print("\n--- Form Fields / Form Labels ---")
for kw in ['title', 'kind', 'system_prompt', 'final_instructions', 'lorebook', 'avatar', 'description', 'narrator', 'sidechat', 'tags', 'visibility', 'rating']:
    matches = list(re.finditer(re.escape(kw), content))
    print(f"Keyword '{kw}': {len(matches)} matches")

# Find snippets around kind and options
for m in re.finditer(r'kind', content):
    idx = m.start()
    snip = content[max(0, idx-100):min(len(content), idx+200)]
    if any(t in snip for t in ['options', 'value', 'select', 'sidechat', 'narrator', 'label', 'schema']):
        print("\n[KIND SNIPPET]:", snip)

# Find snippets around lorebook
for m in re.finditer(r'lorebook', content, re.I):
    idx = m.start()
    print("\n[LOREBOOK SNIPPET]:", content[max(0, idx-100):min(len(content), idx+200)])

# Find defaultValues or form schema
for kw in ['defaultValues', 'resolver', 'z.object', 'createMutation', 'updateMutation', 'post', 'put']:
    for m in re.finditer(re.escape(kw), content):
        idx = m.start()
        print(f"\n[{kw} SNIPPET]:", content[max(0, idx-100):min(len(content), idx+200)])
