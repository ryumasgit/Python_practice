#問題3-1: 台風の接近

load_count, precipitation_limit = 3,200
data_set = [[100,200,20],[100,20,20],[500,20,20]]

precipitations = []
for k in range(load_count):
     data = data_set[k]
     precipitations.append(data)

precipitations = [list(map(int,x)) for x in zip(*precipitations)]

result = ""

for i, sublist in enumerate(precipitations):
    if all(value < precipitation_limit for value in sublist):
        if result:
            result += " "
        result += str(i + 1)
         
if result:
    print(result)
else:
    print("wait")