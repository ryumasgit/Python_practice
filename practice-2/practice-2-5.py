# 問題2-5: 2つの集合A,Bの類似度を計算する方法として，Jaccard係数というものがあります．例えば，文章の類似度の指標として使われています．
# Jaccard(A,B)=|A∩B||A∪B|=AとBの積集合の要素数AとBの和集合の要素数
# 2つのリストが与えられている時，リストを集合と見なした時のJaccard係数の値を求めてください．
# 期待する出力：0.23076923076923078
list1 = [12,23,34,45,56,67,78,89]
list2 = [21,32,43,45,65,67,78,98]

A = set(list1)
B = set(list2)
top_list = A & B
bottom_list = A | B

print(len(top_list) / len(bottom_list))