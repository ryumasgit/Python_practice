#問題3-14: IDを登録順に並べよう
import re
executions = 5
member_data = ["paiza1","pizza99","sushi100","kirishima813","beef1001"]
members = []
numbers = []
for i in range(executions):
    member = member_data[i]
    members.append(member)
    number = re.sub(r"\D", "", member)
    numbers.append(int(number))
    
sorted_numbers = sorted(numbers)

for i in sorted_numbers:
    result = numbers.index(i)
    print(members[result])