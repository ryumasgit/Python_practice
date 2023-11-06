#問題3-6: ログのフィルター

input_count = 5
input_pattern = "ai"
input_data = ["pizza","paiza","aizu","ai","sai"]
match = False

for i in range(input_count):
    string = input_data[i]
    if input_pattern in string:
        print(string)
        match = True

if match == False:
    print("None")