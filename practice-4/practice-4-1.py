#問題4-1: モンスターの進化

init_atk, init_def, init_agi = 100, 150, 200
executions = 3
input_data = [
  ["paizabird","100","200","130","180","80","120"],
  ["paizawolf","180","220","100","120","90","140"],
  ["paizasheep","80","110","150","220","170","250"]
]
parameters = []
monster_names = []

for i in range(executions):
    monster_name, min_atk, max_atk, min_def, max_def, min_agi, max_agi = input_data[i]
    parameters = [min_atk, max_atk, min_def, max_def, min_agi, max_agi]
    min_atk, max_atk, min_def, max_def, min_agi, max_agi = [int(parameter) for parameter in parameters]
    if min_atk <= init_atk <= max_atk and min_def <= init_def <= max_def and min_agi <= init_agi <= max_agi:
        monster_names.append(monster_name)

if monster_names:
    for name in monster_names:
        print(name)
else:
    print("no evolution")