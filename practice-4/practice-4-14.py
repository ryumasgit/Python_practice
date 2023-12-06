#問題4-11: 下桁ルール
Bob_data, Alice_data = 75,81

Alice_data = list(map(int, str(Alice_data)))
Bob_data = list(map(int, str(Bob_data)))

Alice_sum = sum(Alice_data)
Bob_sum = sum(Bob_data)

Alice_sum = list(map(int, str(Alice_sum)))
Bob_sum = list(map(int, str(Bob_sum)))

if Alice_sum[-1] > Bob_sum[-1]:
    print("Alice")
elif Alice_sum[-1] < Bob_sum[-1]:
    print("Bob")
else:
    print("Draw")