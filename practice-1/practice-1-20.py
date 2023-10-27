# 問題20: 時差ボケ

n = 3
data = ((7,5,12),(10,6,20),(12,3,8))
times = []

for i in range(n):
    input_list = data[i]
    time_a = input_list[0] + input_list[1]
    time_b = 24 - input_list[2]
    times.append(time_a + time_b)

max_time = max(times)
min_time = min(times)

print("1 日の時間が最も短いのは",min_time,"時間")
print("1 日の時間が最も長いのは",max_time,"時間")