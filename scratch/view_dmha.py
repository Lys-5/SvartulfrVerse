
lines = open('scratch/all_greetings_dump.txt', encoding='utf-8').readlines()
dmha_start = False
for line in lines:
    if 'Svartulfr_Scenario_DMHA_Dungeons.json' in line:
        dmha_start = True
    elif 'Svartulfr_Scenario_SUCC_Route_Alyssa.json' in line:
        dmha_start = False
    if dmha_start:
        print(line, end='')
