n, k = map(int, input().split())

# ! dp[i][j] -> 숫자 i개를 더해서 j를 만드는 가짓수


dp = [[0]*(n+1) for _ in range(k+1)]

# 숫자 1개를 더해서 j를 만드는 가짓수
for j in range(0, n+1):
    dp[1][j] = 1

# 숫자 i개 더해서 0을 만드는 가짓수 -> 숫자를 몇개를 더하던 0을 만들려면 0만 있어야함
for i in range(1, k+1):
    dp[i][0] = 1


for i in range(2, k+1):
    for j in range(1, n+1):
        for s in range(0, j+1):
            # ! 모든 s에 대해, i-1개를 이용해 s를 만들었으므로, j-s를 하나 추가해주면 된다.
            dp[i][j] += dp[i-1][s]

        dp[i][j] %= 1000000000

print(dp[k][n])


#
