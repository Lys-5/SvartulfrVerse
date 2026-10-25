
lines = open('scratch/all_greetings_dump.txt', encoding='utf-8').readlines()
jasper_start = False
for line in lines:
    if 'Svartulfr_Scenario_SUCC_Route_Jasper.json' in line:
        jasper_start = True
    elif 'Svartulfr_Scenario_Underworld_Sindacato.json' in line:
        jasper_start = False
    if jasper_start:
        print(line, end='')
