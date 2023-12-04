from collections import deque

n = int(input())

board = []

for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

dp = [[[0]*n for _ in range(n)] for _ in range(3)]

# ! dp[s][x][y] -> x,y에 파이프의 앞머리가 s상태(가로(0), 세로(1), 대각(2))로 놓여있을 수 있는 경우의 수

pipe_status = [0, 1, 2]  # 파이프가 놓여져 있는 상태 -> 가로, 세로, 대각선

# 초기 조건 -> 시작은 파이프의 머리가 (0,1)에 가로로 놓여있다.
dp[0][0][1] = 1

d = [[(0, 1), (1, 1)], [(1, 0), (1, 1)], [
    (0, 1), (1, 0), (1, 1)]]  # 파이프의 상태에 따른 이동가능 변위


for x in range(n):
    for y in range(n):
        for s in range(3):  # ! 순서 중요
            if dp[s][x][y] != 0:

                for dx, dy in d[s]:
                    new_x, new_y = x + dx, y + dy
                    new_s = 0

                    if dx == 1 and dy == 1:
                        new_s = 2
                    elif dx == 1 and dy == 0:
                        new_s = 1
                    else:
                        new_s = 0

                    if 0 <= new_x <= n-1 and 0 <= new_y <= n-1:
                        if new_s == 2:
                            if board[x+1][y] == 0 and board[x][y+1] == 0 and board[new_x][new_y] == 0:
                                dp[new_s][new_x][new_y] += dp[s][x][y]
                        else:
                            if board[new_x][new_y] == 0:
                                dp[new_s][new_x][new_y] += dp[s][x][y]


answer = dp[0][n-1][n-1] + dp[1][n-1][n-1] + dp[2][n-1][n-1]


# print(dp)
print(answer)


# # ! 좀 더 좋은 접근
# dp = [[[0]*3 for _ in range(n)] for _ in range(n)]
# dp[0][1][0] = 1

# for j in range(2, n):
#     if board[0][j] == 0:
#         dp[0][j][0] = dp[0][j-1][0]

# for i in range(1, n):
#     for j in range(1, n):
#         if board[i][j] == 0:
#             dp[i][j][0] = dp[i][j-1][0] + dp[i][j-1][2]
#             dp[i][j][1] = dp[i-1][j][1] + dp[i-1][j][2]
#         if board[i][j] == 0 and board[i-1][j] == board[i][j-1] == 0:
#             dp[i][j][2] = dp[i-1][j-1][0] + dp[i-1][j-1][1] + dp[i-1][j-1][2]
# print(sum([dp[n-1][n-1][i] for i in range(3)]))
