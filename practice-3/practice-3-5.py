#問題3-5: ポイント払い

ini_money, ride_count = 2000, 5
fare_data = [300,500,300,100,100]
points = 0

for i in range(ride_count):
    fare = fare_data[i]
    if points >= fare:
        points -= fare
    else:
        ini_money -= fare
        points += int(fare * 0.1)
    print(ini_money, points)