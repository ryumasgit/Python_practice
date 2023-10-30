# 問題2-6: 渋滞の距離

input_data = [5,6,25,4]
car_value, separate_min_limit = 5,10
car_value = int(car_value)
separate_min_limit = int(separate_min_limit)

traffic_jam_length = 0

for i in range(car_value-1):
    separate = input_data[i]
    if separate <= separate_min_limit:
        traffic_jam_length += separate

print(traffic_jam_length)