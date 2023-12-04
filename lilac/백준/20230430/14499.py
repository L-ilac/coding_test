from collections import deque

n, m, start_x, start_y, k = map(int, input().split())

board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

op = list(map(int, input().split()))

dice = [0, 0, 0, 0, 0, 0]
d = [(0, 1), (0, -1), (-1, 0), (1, 0)]

now_x, now_y = start_x, start_y

for i in op:
    new_x, new_y = now_x+d[i-1][0], now_y+d[i-1][1]

    if not (0 <= new_x <= n-1 and 0 <= new_y <= m-1):
        continue

    tmp = deque()

    if i == 3 or i == 4:
        tmp.append(dice[0])
        tmp.append(dice[1])
        tmp.append(dice[2])
        tmp.append(dice[3])

        # print(tmp)

        if i == 3:  # 북
            tmp.rotate(1)
        else:  # 남
            tmp.rotate(-1)

        if board[new_x][new_y] == 0:
            board[new_x][new_y] = tmp[1]
        else:
            tmp[1] = board[new_x][new_y]
            board[new_x][new_y] = 0

        dice[0] = tmp[0]
        dice[1] = tmp[1]
        dice[2] = tmp[2]
        dice[3] = tmp[3]

    else:
        tmp.append(dice[4])
        tmp.append(dice[1])
        tmp.append(dice[5])
        tmp.append(dice[3])

        if i == 1:  # 동
            tmp.rotate(-1)
        else:  # 서
            tmp.rotate(1)

        if board[new_x][new_y] == 0:
            board[new_x][new_y] = tmp[1]
        else:
            tmp[1] = board[new_x][new_y]
            board[new_x][new_y] = 0

        dice[4] = tmp[0]
        dice[1] = tmp[1]
        dice[5] = tmp[2]
        dice[3] = tmp[3]

    # print(dice)
    print(dice[3])
    now_x, now_y = new_x, new_y

# # ! 기존 주사위의 전개도 (1번에 해당하는 면이 바닥에 닿아있음)
#   2
# 4 1 3
#   5
#   6

# # 동쪽으로 움직이는 경우

#   2
# 1 3 6
#   5
#   4
# # 서쪽으로 움직이는 경우

#   2
# 6 4 1
#   5
#   3

# # 남쪽으로 움직이는 경우

#   1
# 4 5 3
#   6
#   2

# # 북쪽으로 움직이는 경우
#   6
# 4 2 3
#   1
#   5
