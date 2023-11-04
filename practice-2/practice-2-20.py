# 問題2-20: 節分ロボット

members_count = 5
ages_data = [10,20,30,40,50]
amount_data = [[2,4,10],[1,3,15]]

ages = [ages_data[i] for i in range(members_count)]

execution_count = 2

beans = [0] * members_count

for k in range(execution_count):
    start, end, amount = amount_data[k]
    start -= 1
    for i in range(start,end):
        age = ages[i]
        if beans[i] + amount <= age:
            beans[i] += amount
        else:
            beans[i] = age

for i in range(members_count):
    print(beans[i])