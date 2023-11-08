#問題3-7: ゴンドラ

def ride(gondola, people):
    if gondola >= people:
        return people, 0
    else:
        return gondola, people - gondola

gondola, group = 3,3
gondolas = [5,5,5]
result = [0,0,0]
peoples = []
people_data = [6,5,3]
for i in range(group):
    peoples.append(people_data[i])

k = 0

for people in peoples:
    value, left = ride(gondolas[k], people)
    result[k] += value
    left_people = left

    while left_people > 0:
        k += 1
        if k >= gondola:
            k = 0
        value, left = ride(gondolas[k], left_people)
        result[k] += value
        left_people = left
    k += 1
    if k >= gondola:
        k = 0

for i in result:
    print(i)