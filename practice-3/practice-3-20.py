#問題3-20: RPGでお買い物
tool_count = 3
tools = [10,100,50]
input_data = [[1,5],[2,3],[3,1],[2,1],[1,3]]
init_money, executions = 300, 5

for i in range(executions):
    tools_index, pieces = input_data[i]
    total_price = tools[tools_index-1] * pieces
    if init_money >= total_price:
        init_money -= total_price
    
print(init_money)