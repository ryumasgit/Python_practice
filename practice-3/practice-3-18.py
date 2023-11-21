#問題3-18: ポイントカード
import math

sheets = 3
point = 0
numbers = []
sheet_data = [[1,1024],[11,2048],[21,4196]]

for i in range(sheets):
    day, money = sheet_data[i]
    numbers = [int(number) for number in str(day)]
    if 5 in numbers:
        point += math.floor(money * 0.05)
    elif 3 in numbers:
        point += math.floor(money * 0.03)
    else:
        point += math.floor(money * 0.01)

print(point)