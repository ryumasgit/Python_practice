#問題3-15: 構造体の検索
class Student:
    def __init__(self, name, old, birth, state):
        self.name = name
        self.old = old
        self.birth = birth
        self.state = state

n = 3
datas = [["mako",13,"08/08","nara"],["megumi",14,"11/02","saitama"],["taisei",16,"12/04","nagano"]]

roster = [None] * n
for i in range(n):
    name, old, birth, state = datas[i]
    roster[i] = Student(name, old, birth, state)
    
k = 14
for student in roster:
    if student.old == k:
        print(student.name)
        break