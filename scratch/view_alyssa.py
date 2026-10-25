
lines = open('scratch/all_greetings_dump.txt', encoding='utf-8').readlines()
alyssa_start = False
for line in lines:
    if 'Svartulfr_Scenario_SUCC_Route_Alyssa.json' in line:
        alyssa_start = True
    elif 'Svartulfr_Scenario_SUCC_Route_Jasper.json' in line:
        alyssa_start = False
    if alyssa_start:
        print(line, end='')
