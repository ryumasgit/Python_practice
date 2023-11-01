# 問題2-13: ハンドルネームの生成
input_line = "PAizADEren"
input_line = list(input_line)

output = []
vowel = ["a","A","i","I","u","U","e","E","o","O"]

for string in input_line:
    if not  string in vowel:
        output.append(string)
        
output = "".join(output)
print(output)