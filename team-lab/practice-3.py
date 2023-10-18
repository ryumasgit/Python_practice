# 問題3: 条件分岐とループの組み合わせ
# 1から100までの整数をループで処理し、以下の条件に基づいて出力するプログラムを書いてください。
# 3の倍数の場合は "Fizz" を出力
# 5の倍数の場合は "Buzz" を出力
# 3の倍数かつ5の倍数の場合は "FizzBuzz" を出力
# 上記のいずれでもない場合はその数を出力

def FizzBuzz(target):
  if target % 15 == 0:
    return "FizzBuzz"
  elif target % 3 == 0:
    return "Fizz"
  elif target % 5 == 0:
    return "Buzz"
  else:
    return target

target = 15
print(FizzBuzz(target))