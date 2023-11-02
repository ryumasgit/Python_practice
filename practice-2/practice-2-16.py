# 問題2-16: 多重パス回し

def calculation(player_list, source, target, count):
    if player_list[source] >= count:
        player_list[source] -= count
        player_list[target] += count
    else:
        player_list[target] += player_list[source]
        player_list[source] = 0

players = 3
player_list = []
ini_ball_data = [10,5,8]
send_ball_data = [[1,3,5],[3,2,3],[2,1,10]]

player_list = [ini_ball_data[i] for i in range(players)]

commands = 3

for k in range(commands):
    source, target, count = send_ball_data[k]
    calculation(player_list, source-1, target-1, count)

for value in player_list:
    print(value)