#問題3-11: ボールが入る箱
executoins, radius = 4, 2
box_data = [[6,6,6],[4,6,4],[6,1,1],[4,4,4]]

for i in range(executoins):
    box = box_data[i]
    min_length = min(box)
    if radius*2 <= min_length:
        print(i+1)