#問題4-2: 嫌いな数字
dont_like_number = "4"
executions = 5
input_data = ["101","204","301","401","501"]
number_list = []
result = []

for i in range(executions):
    number = input_data[i]
    number_list = list(number)

    if not dont_like_number in number_list:
        result.append(number)

if result:
    for number in result:
        print(number)
else:
    print("none")