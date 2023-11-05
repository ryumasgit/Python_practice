#問題3-2: ハイアンドローゲーム

def judgement(parent_bottom,child_bottom):
    if parent_bottom < child_bottom:
        print("High")
    else:
        print("Low")
    
parent_top, parent_bottom = 5,1
child_card_data = [[7,2],[1,4]]
execution_count = 2

for i in range(execution_count):
    child_top, child_bottom = child_card_data[i]
    if parent_top > child_top:
        print("High")
    elif parent_top == child_top:
        judgement(parent_bottom,child_bottom)
    else:
        print("Low")