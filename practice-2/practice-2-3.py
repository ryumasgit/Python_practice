# 問題2-3: このリストに対して，要素の出現数を格納した辞書num2freqを作成し，出力してください．これはnum2freq[要素] = 出現数となるような辞書で，例えばnum2freq[1] = 3です．
nums = [1,2,4,3,2,1,5,1]

num2frep = {}
for num in nums:
    num2frep[num] = num2frep.get(num, 0) + 1

num2frep_list = list(num2frep.items())
num2frep_sorted = sorted(num2frep_list, key=lambda x:x[0])
print(num2frep_sorted)