# 問題2-12: Leet文字列
input_line = "PAIZA"
input_line = list(input_line)

output = []
for i in input_line:
    if i == "A":
        output.append("4")
    elif i == "E":
        output.append("3")
    elif i == "G":
        output.append("6")
    elif i == "I":
        output.append("1")
    elif i == "O":
        output.append("0")
    elif i == "S":
        output.append("5")
    elif i == "Z":
        output.append("2")
    else:
        output.append(str(i))

output = "".join(output)
print(output)