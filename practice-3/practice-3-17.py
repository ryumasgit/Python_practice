#問題3-17: ローソク足
days = 5

opening_price = 0
closing_price = 0
high_price = 0
low_price = 0
price_data = [[11,14,16,10],[12,15,17,10],[13,11,14,11],[12,10,13,8],[11,13,14,10]]

for i in range(days):
    o, c, h, l = price_data[i]
    if i == 0:
        opening_price = o
        high_price = c
        low_price = l
    elif i == days-1:
        closing_price = c

    if h > high_price:
        high_price = h

    if l < low_price:
        low_price = l

print(opening_price,closing_price,high_price,low_price)