#問題3-9: 板たおし
def max_score(board):
    rows = len(board) #4
    cols = len(board[0]) #4

    dp = [[0] * cols for _ in range(rows)]
    dp[-1] = board[-1]

    for i in range(rows -2,-1,-1):
        for j in range(cols):
            dp[i][j] = board[i][j] + max(dp[i + 1][j - 1] if j > 0 else 0,
                                          dp[i + 1][j],
                                          dp[i + 1][j + 1] if j < cols - 1 else 0)
    result = max(dp[0])
    return result

board = [
    [5,4,3,10],
    [1,3,0,6],
    [9,0,3,2],
    [3,5,1,3]
]

result = max_score(board)
print(result)