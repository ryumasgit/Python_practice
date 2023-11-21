#問題3-19: 合言葉
password = "abc"
input_password = "bac"
password_list = list(password)
input_password_list = list(input_password)

if password != input_password:
    if set(password_list) == set(input_password_list):
        print("YES")
    else:
        print("NO")
else:
    print("NO")