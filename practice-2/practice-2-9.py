# 問題2-9: 残り物の量

amount, first_sales, second_sales = 1,80.0,40.0
first_sales, second_sales = (100 - first_sales), (100 - second_sales)
first_sales, second_sales = (first_sales / 100), (second_sales / 100)

initial_unsold_amount = amount * first_sales
last_unsold_amount = initial_unsold_amount * second_sales
print(last_unsold_amount)