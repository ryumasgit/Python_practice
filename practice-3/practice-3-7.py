#問題3-7: 

def ride(gondola,people):
    if gondola >= people:
        return people, 0
    else:
        people -= gondola
        return gondola, people
        
gondola, group = map(int, input().split())

gondolas = []
result = []
for i in range(gondola):
    gondolas.append(int(input()))
    result.append(int(0))

peoples = []
for i in range(group):
    peoples.append(int(input()))

k = 0
for people in peoples:
    value, left = ride(gondolas[k],people)
    result[k] += value
    if k+1 >= gondola:
        K = 0
    else:
        k += 1
    result[k] += left

for i in result:
    print(i)