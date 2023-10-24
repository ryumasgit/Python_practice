# 問題24: 7以上7777777以下の7の倍数を全て書き出したとき、数字「7」は何回現れるか。

start = 7
end = 7777777
count = 0

for number in range(start, end+1, start):
    count += str(number).count("7")

print(count)