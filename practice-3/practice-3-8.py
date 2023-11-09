#問題3-8: 

xc, yc, r_1, r_2 = map(int, input().split())
cases = int(input())

for i in range(cases):
    x, y = map(int, input().split())
    x = abs(x)
    y = abs(y)
    if r_1 * 2 <= (x - xc) * 2 and r_2 * 2 >= (x - xc) * 2 and r_2 * 2 >= (y - yc):
        print("yes")
    else:
        print("no")