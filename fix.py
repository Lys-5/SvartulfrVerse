import os

with open(r'd:\SvartulfrVerse\docs\Douglas_Family_JED_Proposal.md', 'r', encoding='utf-8') as f:
    text = f.read()

# Fix mangled UTF-8 chars
text = text.replace('Ãš', 'Ú').replace('Ã³', 'ó').replace('Ã°', 'ð').replace('Ã¡', 'á').replace('Ãº', 'ú')

with open(r'd:\SvartulfrVerse\docs\Douglas_Family_JED_Proposal.md', 'w', encoding='utf-8') as f:
    f.write(text)
