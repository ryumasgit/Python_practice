# 問題21: しりとりの判定

input_line = 5
input_strings_1 = (("apPle"),("error"),("suBway"),("Zb"))
input_strings_2 = (("adijA"),("Akq"),("qZR"))
shiri = ""

for i in range(input_line):
    string = input_strings_1[i]
    if shiri:
        if string[0] != shiri:
            print(shiri,string[0])
            break
    if i == (input_line - 1):
        print("Yes")
    else:
        shiri = string[-1]


# input_lines = 5
# input_strings = [("apPle",), ("error",), ("suBway",), ("Zb",), ("adijA",), ("Akq",), ("qZR",)]
# shiri = ""
# valid = True

# for i, (string,) in enumerate(input_strings):
#     if shiri:  # しりとりが始まっている場合
#         if string[0] != shiri:  # 前の単語の末尾と新しい単語の先頭が一致しない場合
#             valid = False
#             break

#     shiri = string[-1]

# if valid and len(input_strings) == input_lines:
#     print("Yes")
# else:
#     print("No")