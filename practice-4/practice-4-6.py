#問題4-6: 観光の計画
x, y, r = 20,10,10
executions = 3
input_data = [[25,10],[20,15],[70,70]]

for i in range(executions):
    x_i, y_i = input_data[i]
    if (x_i - x) ** 2 + (y_i - y) ** 2 >= r ** 2:
        print("silent")
    else:
        print("noisy")