# 問題2-14: 繰り返し学習
input_amout = 4
input_strings = ["y n", "n y", "n n", "y y"]

pass_fail = []
number = 1

for i in range(input_amout):
    pass_fail.append(input_strings[i])

count = input_amout - pass_fail.count("y y")
print(count)

for string in pass_fail:
    if not string == "y y":
        print(number)
    number += 1