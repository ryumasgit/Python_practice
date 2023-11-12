#問題3-13: 株の売買
date, c_1, c_2 = 3, 100, 200
stock_price_data = [80, 80, 30]
profit = 0
shares_held = 0

for i in range(date):
    stock_price = stock_price_data[i]
    if i == date - 1:
        profit += stock_price * shares_held
        shares_held = 0
    elif stock_price <= c_1:
        profit -= stock_price
        shares_held += 1
    elif stock_price >= c_2 and shares_held > 0:
        profit += stock_price * shares_held
        shares_held = 0

print(profit)