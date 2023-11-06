#問題3-4: 平方根の和算

number = 0
for i in range(1,609):
    number += (i ** (1/2))
    if number > 10000:
        print(i)
        break