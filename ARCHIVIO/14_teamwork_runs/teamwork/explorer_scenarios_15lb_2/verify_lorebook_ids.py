import json

expected = [
    "_gwwCxCfQ6PQaLEjAQVpJL",
    "_HfG7TeV6MJyj6bxMwxkpt",
    "_9zWTGqYJNJ4BCDMj8gfcD",
    "_EjXxkmPVhpCXg8xABpFkK",
    "_Uht3Ckz44JBDrPnUHq7LV",
    "_zwEqgEEzh12X6gHVmMKKC",
    "_GV1KyHVY1RMbCnWgLkzDG",
    "_GbWJbkhgLzWexMHrjyUUc",
    "_FaVcHfmrqcaJq8pa3WmRw",
    "_BbrRgrcdGPMLEbBU2b6xk",
    "_gchmML4Q478zdFjhXf8rN",
    "_brNyzEdhzNAyxK8xC8hhm",
    "_YtKLMTwyMxNf1DNYqBx1t",
    "_b9HgpUXtAW8VmTy82BPDV",
    "_c8bEm1bWphwqFBXWRPrV8"
]

data = json.load(open(r'e:\repository\SvartulfrVerse\.agents\teamwork\explorer_scenarios_15lb_2\live_scenarios_inspection.json', encoding='utf-8'))
live_master_lbs = data["Master Scenario"]["lorebook_ids"]

print("Expected count:", len(expected))
print("Live Master count:", len(live_master_lbs))
print("Difference expected - live:", set(expected) - set(live_master_lbs))
print("Difference live - expected:", set(live_master_lbs) - set(expected))
