# 問題7: 再帰関数を使用した階乗の計算
# 再帰関数を使用して、指定された整数の階乗を計算するプログラムを書いてください。

def factorial(target):
    if target == 0:
        return 1
    elif target < 0:
        return "答えは無限です"
    else:
        return target * factorial(target - 1)

print(factorial(7))