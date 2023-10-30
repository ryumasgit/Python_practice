# 問題2-10: 古代の数式

input_line = ["<<//","////"]

value = 0

for string in input_line:
    one_place = string.count("/")
    ten_place = string.count("<")
    ten_place = ten_place * 10
    value += one_place + ten_place

print(value)