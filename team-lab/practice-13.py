# 繰り返しとスライスの問題
def sheep_count():
    sheep = ""
    for i in range(1,100001):
      sheep += str(i) + 'SHEEP'
    return sheep

result = sheep_count()
print(result[55555:55575])