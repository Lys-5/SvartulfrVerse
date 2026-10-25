
lines = open('scratch/all_greetings_dump.txt', encoding='utf-8').readlines()
uw_start = False
for line in lines:
    if 'Svartulfr_Scenario_Underworld_Sindacato.json' in line:
        uw_start = True
    elif 'Svartulfr_Scenario_Villa_Douglas.json' in line:
        uw_start = False
    if uw_start:
        print(line, end='')
