# 問題2-11: 行きたいライブのスケジュール
A_lists = [12,14,15,26,27,28]
B_lists = [12,13,14,15,27]
output = []
A_priority = True
for day in range(1, 32):
    if day in A_lists and day in B_lists:
        if A_priority:
            A_priority = False
            output.append("A")
        else:
            A_priority = True
            output.append("B")
    elif day in A_lists:
        output.append("A")
    elif day in B_lists:
        output.append("B")
    else:
        output.append("x")

for day in output:
    print(day)