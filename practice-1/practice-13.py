# 問題13: 繰り返しとスライスの問題

def string_count():
    string = ""
    for i in range(1,501):
      string += str(i) + 'Hello'
    return string

result = string_count()
print(result[100:175])