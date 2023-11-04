# 問題2-19: 誤発注

input_line = 5
input_data = [1,4,6,2,1]
products = {}
for i in range(1,input_line+1):
    products[i] = products.get(i, 0)
    
for k in range(input_line):
    product = input_data[k]
    products[product] = products.get(product, 0) + 1

count = 0
for v in products.values():
    if v == 0:
        count += 1
print(count)