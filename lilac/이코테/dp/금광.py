# t = int(input())

# move = [(1, 1), (0, 1), (-1, 1)]  # 오른아래, 오른, 오른위

# for _ in range(t):
#     n, m = map(int, input().split())

#     tmp = list(map(int, input().split()))
#     board = []

#     for i in range(0, len(tmp), 4):
#         board.append(tmp[i:i+m])

#     dp = [[0]*m for _ in range(n)]

#     for i in range(n):
#         dp[i][0] = board[i][0]

#     for j in range(m-1):
#         for i in range(n):
#             for dx, dy in move:
#                 newx, newy = i+dx, j+dy

#                 if 0 <= newx <= n-1 and 0 <= newy <= m-1:
#                     dp[newx][newy] = max(
#                         dp[newx][newy], board[newx][newy] + dp[i][j])

#     print(max([i[-1] for i in dp]))


# t = int(input())

# for _ in range(t):
#     n, m = map(int, input().split())
#     tmp = list(map(int, input().split()))

#     move = [(0, 1), (1, 1), (-1, 1)]
#     dp = [[0]*m for _ in range(n)]

#     board = []

#     for i in range(0, len(tmp), m):
#         board.append(tmp[i:i+m])

#     for i in range(n-1):
#         dp[i][0] = board[i][0]

#     print(board)
#     print(dp)

#     for j in range(m-1):
#         for i in range(n):

#             for dx, dy in move:
#                 newx, newy = i+dx, j+dy

#                 if 0 <= newx <= n-1 and 0 <= newy <= m-1:
#                     dp[newx][newy] = max(
#                         dp[newx][newy], dp[i][j] + board[newx][newy])

#     print(dp)
#     print(max([a[-1] for a in dp]))


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    tmp = list(map(int, input().split()))

    dp = []

    board = []

    for i in range(0, len(tmp), m):
        board.append(tmp[i:i+m])
        dp.append(tmp[i:i+m])

    # for i in range(n-1):
    #     dp[i][0] = board[i][0]

    print(board)
    print(dp)

    for j in range(1, m):
        for i in range(n):

            if i == 0:
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            if i == n-1:
                left_down = 0
            else:
                left_down = dp[i+1][j-1]

            left = dp[i][j-1]

            dp[i][j] = board[i][j] + max(left, left_down, left_up)

    print(dp)
    print(max([a[-1] for a in dp]))


# ! 이전 위치를 기준으로 다음 위치로 다 더해줄건지, 다음 위치를 기준으로 이전위치중에서 가장 큰값을 골라 더할것인지 결정
