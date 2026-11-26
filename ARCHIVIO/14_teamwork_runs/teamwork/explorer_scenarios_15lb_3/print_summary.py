import json

with open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_3\verification_results.json', encoding='utf-8') as f:
    data = json.load(f)

print(f"{'#':<3} | {'ID':<24} | {'Status':<6} | {'Title':<45} | {'Entries':<7} | {'Lexicon':<7} | {'Visibility':<10}")
print("-" * 115)
for i, lb in enumerate(data['lorebooks']):
    print(f"{i+1:<3} | {lb['id']:<24} | {lb['status']:<6} | {lb['title']:<45} | {lb['entries_count']:<7} | {lb['lexicon_count']:<7} | {str(lb['visibility']):<10}")
