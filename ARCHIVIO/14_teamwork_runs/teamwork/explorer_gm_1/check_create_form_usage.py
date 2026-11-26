import urllib.request
import re

url = 'https://app.wyvern.chat/_next/static/chunks/app/(content)/mine/page-4fad869ea17238ea.js'
req = urllib.request.Request(url, headers={'User-Agent': 'Mozilla/5.0'})
content = urllib.request.urlopen(req).read().decode('utf-8')

# Search for the function that creates the assistant modal or form
# In the module where `f` was defined, let's find the export name of `f`
pos = content.find('Assistant config created successfully')
# Look backwards for export list: a.d(t, { ... })
exp_pos = content.rfind('a.d(t,{', 0, pos)
print("Exports:", content[exp_pos:exp_pos+300])

# Now search where those exported functions are used in the chunk!
# Let's find matches for the export name of `f`
