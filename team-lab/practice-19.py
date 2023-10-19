# 問題19: 反復横跳び大会

n = 4
lists = [55,57,55,52]
records = []
for i in range(n):
    record = lists[i]
    records.append(record)

sorted_records = sorted(records, reverse=True)

ranks = {}
rank = 1
for record in sorted_records:
    if record not in ranks:
        ranks[record] = rank
    rank += 1

for record in records:
    rank = ranks[record]
    print(rank)