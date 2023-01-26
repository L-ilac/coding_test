n = int(input())

dp = [0] * (n+1)
dp[0] = 1
dp[2] = 1


for i in range(4, n+1, 2):
    tmp = 0
    for j in range(0, i-1, 2):
        tmp += dp[j] * dp[i-2-j]

    dp[i] = tmp % 987654321

print(dp[n])

# ! 카탈란 수라는 수학적 개념이라고한다.
