# 問題4: 素数の判定
# 指定された整数が素数であるかどうかを判定するプログラムを書いてください。素数であれば true を、そうでなければ false を返す関数を実装してください。

import math

def prime_number(target):
    square_root = int(math.sqrt(target))
    for i in range(2,square_root + 1):
        if target % i == 0:
            return False
    return True

target = 101
print(prime_number(target))