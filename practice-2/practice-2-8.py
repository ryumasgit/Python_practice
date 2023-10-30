# 問題2-8: 大量出店

stores, months = 3,3
ini_costs, personnel_costs, profit = 1000,1000,50
sales_datas = [50,80,500]
count = 0

for store in range(stores):
    net_income = 0
    sales = sales_datas[store]
    if 0 > ((sales * profit) - (personnel_costs * months) - (ini_costs)):
        count += 1

print(count)