#問題3-3: 花のリース

flowers = 5
flower_a = ["b","a","a","a","b"]
flower_b = ["a","a","b","b","a"]

match = False

for i in range(flowers):
    temp = flower_b[-1]
    for k in range(flowers-1):
        flower_b[-1 - k] = flower_b[-2 - k]
    flower_b[0] = temp
    if flower_a == flower_b:
        match = True
        break

if match == True:
    print("Yes")
else:
    print("No")