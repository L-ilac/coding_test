# n = int(input())

# triangle = []

# for _ in range(n):
#     tmp = list(map(int, input().split()))
#     triangle.append(tmp)

# dp = [[0]*i for i in range(1, n+1)]
# dp[0][0] = triangle[0][0]


# for i in range(len(triangle)-1):
#     for j in range(len(triangle[i])):
#         dp[i+1][j] = max(dp[i+1][j], dp[i][j] + triangle[i+1][j])
#         dp[i+1][j+1] = max(dp[i+1][j+1], dp[i][j] + triangle[i+1][j+1])

# print(max(dp[-1]))


n = int(input())

dp = []
for _ in range(n):
    tmp = list(map(int, input().split()))
    dp.append(tmp)


for i in range(1, n):
    for j in range(len(dp[i])):

        if j == 0:
            up_left = 0
        else:
            up_left = dp[i-1][j-1]

        if j == len(dp[i])-1:
            up_right = 0
        else:
            up_right = dp[i-1][j]

        dp[i][j] += max(up_left, up_right)


print(max(dp[-1]))

# ! 위층을 기준으로 아래층으로 모두 더해줄건지, 아래층을 기준으로 위층에서 골라서 더할건지 결정해야함
