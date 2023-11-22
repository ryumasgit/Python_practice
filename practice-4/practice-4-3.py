#問題4-2: 嫌いな数字
persons, min_score = 5, 25
input_data = [[80,11],[20,1],[50,2],[70,0],[25,1]]
for i in range(persons):
    get_score, behind_time = input_data[i]
    score = get_score - (behind_time * 5)
    if score < 0:
        score = 0
    if score >= min_score:
        print(i+1)