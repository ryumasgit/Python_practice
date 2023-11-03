# 問題2-18: 運賃計算

def calcurate(current_line,current_station,destination_line, destination_station,cost):
    fare = destination_station - current_station
    if fare < 0:
        fare = abs(fare)
        cost += input_data[current_line-1][current_station-1] - input_data[current_line-1][current_station-1 - fare]
        current_station = destination_station
    else:
        cost += input_data[current_line-1][current_station-1 + fare] - input_data[current_line-1][current_station-1]
        current_station = destination_station
    return cost,current_station
    
lines, stations = 3,4
input_datas = [[0,1,2,3,],[0,4,5,6,],[0,7,8,9]]
input_lines_and_stations = [[1,4],[3,2],[2,2]]
input_data = []
count = 3
current_line = 1
current_station = 1
cost = 0

for i in range(lines):
    line = input_datas[i]
    row = [int(x) for x in line]
    input_data.append(row)



for i in range(count):
    destination_line, destination_station = input_lines_and_stations[i]
    current_line = destination_line
    if current_station != destination_station:
        cost,current_station = calcurate(current_line,current_station,destination_line, destination_station,cost)

print(cost)