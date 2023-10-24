# 問題22: プレゼント応募企画の実施


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b // gcd(a, b)

input_line = ("5 2 4")
input_line = input_line.split()
input_line = [int(s) for s in input_line]
case_x = input_line[1]
case_y = input_line[2]
both_cases = lcm(case_x, case_y)

for i in range(1, input_line[0] + 1):
    if i % both_cases ==0:
        print("AB")
    elif i % case_x == 0:
        print("A")
    elif i % case_y == 0:
        print("B")
    else:
        print("N")