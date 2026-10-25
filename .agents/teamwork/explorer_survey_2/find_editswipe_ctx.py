import re

content = open('scratch/81904-87bfa0aca229c4ac.js', encoding='utf-8', errors='ignore').read()

idx = content.find('editSwipe(e,t);tb')
print("Snippet around editSwipe(e,t);tb:")
print(content[max(0, idx - 1000):min(len(content), idx + 500)])
