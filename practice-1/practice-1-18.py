# 問題18: 立法数
# 与えられた整数が立法数であるかどうかを判定するプログラムを書いてください。整数が立法数であればTrue、そうでなければFalseを返す関数を実装してください。立法数とは、他の整数の3乗で表せる数のことです。

def is_square_number(target):
    if (target ** (1/3)).is_integer():
        return True
    else:
        return False

target = 8
print(is_square_number(target))