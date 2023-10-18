# 問題1: 最大公約数 (GCD) の計算
# 最大公約数（Greatest Common Divisor, GCD）を求めるプログラムを書いてください。2つの整数を入力とし、それらの最大公約数を返す関数を実装してください。

def GCD(target1, target2):
    divior = []
    min_num = min(target1, target2)
    for i in range(2,min_num + 1):
        if target1 % i == 0 and target2 % i == 0:
            divior.append(i)
    return max(divior)

target1 = 12
target2 = 48
print(GCD(target1, target2))