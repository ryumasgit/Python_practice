#問題4-3: 宿泊費と交通費

transportation_expenses, accommodation_fee, executions = 200, 300, 3
cost = 0
input_data = [[1,3],[4,6],[8,10]]
cost += transportation_expenses * 2

for i in range(executions):
    start, end = input_data[i]
    if i > 0:
        difference =  start - intern_end
        total_transportation_expenses = transportation_expenses * 2
        total_accommodation_fee = accommodation_fee * difference
        cost += min(total_transportation_expenses, total_accommodation_fee)
    intern_end = end

print(cost)