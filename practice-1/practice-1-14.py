# 問題14: 約数の総和
# 指定された整数の約数を見つけ、それらの総和を計算するプログラムを書いてください。

import math

def calculation_divisor_total(target):
    total = 0
    if target < 0:
        return "正の整数で指定して下さい。"
    else:
        for i in range(1, target + 1):
              if target % i == 0:
                  total += i
        return total

target = 109
print(calculation_divisor_total(target))