# 問題23: かならず37になる問題

hundreds_place = 100
tens_place = 10
for i in range(1,10):
    top = (hundreds_place * i) + (tens_place * i) + i
    bottom = i * 3
    result = top / bottom
    print(result)