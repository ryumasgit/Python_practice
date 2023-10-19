# 問題9: ソートアルゴリズム
# バブルソート、クイックソート、またはマージソートなど、任意のソートアルゴリズムを実装し、整数の配列をソートするプログラムを書いてください。

def bubble_sort(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
              arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [64, 34, 25, 12, 22, 11, 90]
bubble_sort(arr)
print(arr)