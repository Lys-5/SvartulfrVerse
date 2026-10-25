
lines = open('scratch/all_greetings_dump.txt', encoding='utf-8').readlines()
villa_start = False
for line in lines:
    if 'Svartulfr_Scenario_Villa_Douglas.json' in line:
        villa_start = True
    if villa_start:
        print(line, end='')
