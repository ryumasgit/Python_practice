#問題4-7: レポートの評価
persons, questions = 3,25
input_data = [[-2,17],[-7,20],[2,24]]

for i in range(persons):
    score = 0
    filing_date, correct_answers = input_data[i]
    point_allocation = 100 / questions
    score += correct_answers * point_allocation

    if filing_date > 0 and filing_date < 10:
        score = score * 0.8
    elif filing_date > 9:
        score = 0

    if score > 79:
        print("A")
    elif score < 80 and score > 69:
        print("B")
    elif score < 70 and score > 59:
        print("C")
    else:
        print("D")