#問題3-10: クジの当選番号
answer_num = [1,2,3,4,5]
num_data = [[1,2,5,4,3],[3,4,5,6,7],[6,7,8,9,10]]
executions = 3

for k in range(executions):
    my_num = num_data[k]
    count = 0
    for i in my_num:
        if i in answer_num:
            count += 1
    print(count)