# 問題2-15: エレベーター

counts = 3
floor_data = [3,1,4]
now_floor = 1
total = 0

for i in range(counts):
    moved_to_floor = floor_data[i]
    absolute = now_floor - moved_to_floor
    total += abs(absolute)
    now_floor = moved_to_floor

print(total)