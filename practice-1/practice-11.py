# 問題11: 線形代数
# 与えられた2つのベクトルの内積を計算するプログラムを書いてください。ベクトルはリストや配列として与えられ、内積の結果を返す関数を実装してください。内積は、対応する要素同士を掛け合わせて総和を取る操作です。

vectorA = [3, 4, 5]
vectorB = [1, 2, 3]

def vector_calculation(v1, v2):
    num = len(v1)
    inner = 0
    for i in range(num):
        inner += v1[i] * v2[i]
    return inner

print(vector_calculation(vectorA, vectorB))