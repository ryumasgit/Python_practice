#問題3-8: 暴風域にいますか？

def check_position(xc, yc, r_1, r_2, x, y):
    distance_to_origin = (x - xc) ** 2 + (y - yc) ** 2
    r_1_squared = r_1 ** 2
    r_2_squared = r_2 ** 2

    if r_1_squared <= distance_to_origin <= r_2_squared:
        return True
    else:
        return False

xc, yc, r_1, r_2 = map(int, input().split())
cases = int(input())

for i in range(cases):
    x, y = map(int, input().split())
    if check_position(xc, yc, r_1, r_2, x, y):
        print("yes")
    else:
        print("no")