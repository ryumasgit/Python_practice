# 問題2-17: 黒電話
input_line = "9315-35-7398"
input_line_separate = input_line.split("-")
lists = [item for sublist in input_line_separate for item in sublist]

distance = {"0":12,"1":3,"2":4,"3":5,"4":6,"5":7,"6":8,"7":9,"8":10,"9":11}
values = 0

for i in lists:
    values += distance[i] * 2

print(values)