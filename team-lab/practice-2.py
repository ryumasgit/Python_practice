# 問題2: フィボナッチ数列
# フィボナッチ数列を計算するプログラムを書いてください。指定された位置のフィボナッチ数を返す関数を実装してください。

def fibonacci_sequence(target):
    if target < 0:
        return "負の数は指定できません"
    elif target == 0:
        return 0
    elif target == 1:
        return 1
    else:
        num1 = 0
        num2 = 1
        
        for i in range(3,target + 1):
          num1, num2 = num2, num1 + num2
        return num2
      
print(fibonacci_sequence(-15))