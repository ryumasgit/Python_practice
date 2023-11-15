#問題3-16: 工場の検品
import collections
genre, order = 3,5

order_data = [1,2,1,2,3]
init_data = [2,1,3,2,1]
order_list = []
init_list = []
for i in range(order):
    order_list.append(order_data[i])

for i in range(order):
    init_list.append(init_data[i])

order_count = collections.Counter(order_list)
init_count = collections.Counter(init_list)

if order_count == init_count:
    print("Yes")
else:
    print("No")