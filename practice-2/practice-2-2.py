# 問題2-2: 辞書の値のソート
dic = {'two':324, 'four':830, 'three':493, 'one':172, 'five':1024}

items_list = list(dic.items())
sorted_items_list = sorted(items_list, key=lambda x:x[1])
ans = [elem[0] for elem in sorted_items_list]
print(ans)