#問題4-5: 観光の計画
spot_executions = 3
staying_time = [2,1,4]
travel_time = [[0,3,2],[3,0,8],[2,8,0]]
input_data = [1,2,3,1]
move_executions = 4
init_spot = 0
total_time = 0

for i in range(move_executions):
    destination = input_data[i]
    if i == 0:
        init_spot = destination
    total_time += staying_time[destination-1]
    total_time += travel_time[init_spot-1][destination-1]
    init_spot = destination
print(total_time)