# 問題17: 平方数
# 与えられた整数が平方数であるかどうかを判定するプログラムを書いてください。整数が平方数であればTrue、そうでなければFalseを返す関数を実装してください。平方数とは、他の整数の2乗で表せる数のことです。

def is_square_number(target):
    if (target ** (1/2)).is_integer():
        return True
    else:
        return False

target = 100
print(is_square_number(target))