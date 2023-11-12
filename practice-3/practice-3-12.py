#問題3-12: スラックアウト
h, w = 4, 3
board_data = [["oxo"],["oox"],["oxo"],["xxx"]]
score_data = [[1,2,3],[4,5,6],[7,8,9],[10,11,12]]

board = []
for i in range(h):
    strings = board_data[i]
    for string in strings:
        board.extend(string)
    
score_list = []
for i in range(h):
    score = score_data[i]
    score_list.extend(score)

counter = 0    
for i in range(len(board)):
    if board[i] == "o":
        counter += score_list[i]
        
print(counter)