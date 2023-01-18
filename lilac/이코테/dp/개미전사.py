n = int(input())
k = list(map(int, input().split()))

dp = [0] * n

dp[0] = k[0]
dp[1] = k[1]
#
for i in range(2, n):
    dp[i] = max(k[i] + dp[i-2], dp[i-1])

print(dp[-1])


# n = int(input())

# foods = list(map(int, input().split()))
# dp = [0]*n
# dp[0] = foods[0]
# ! dp[1] = foods[1] 아님
# !dp[1] = max(foods[0],foods[1])

# for i in range(3, n):
#     dp[i] = max(dp[i-1], foods[i]+dp[i-2])

# print(dp[-1])
