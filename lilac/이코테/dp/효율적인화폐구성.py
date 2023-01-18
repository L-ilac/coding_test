# n, m = map(int, input().split())


# coins = []

# for _ in range(n):
#     coins.append(int(input()))

# dp = [10001] * (m+1)

# # ! 0원은 동전이 하나도 없으면 된다.
# dp[0] = 0

# for c in coins:
#     for i in range(c, m+1):
#         dp[i] = min(dp[i-c]+1, dp[i])

# print(dp)
# print(dp[m])


n, m = map(int, input().split())

dp = [10001] * (m+1)

# ! dp[i] -> i원을 만드는데 필요한 동전의 최소 갯수

coins = []
for _ in range(n):
    coins.append(int(input()))


dp[0] = 0  # ! 0원은 동전이 한개도 없어도 만들 수 있는 금액임
for c in coins:
    # ! dp[c] = 1 <- 안되는 이유? 타겟 m이 화폐단위 c보다 작을 수도 있다.
    for i in range(c, m+1):
        dp[i] = min(dp[i], dp[i-c]+1)


print(dp[-1])
