a = input()
b = input()


# 삽입, 삭제, 교체

dp = [[0]*(len(b)+1) for _ in range(len(a)+1)]

for j in range(len(b)+1):
    dp[0][j] = j

for i in range(len(a)+1):
    dp[i][0] = i


for i in range(1, len(a)+1):
    for j in range(1, len(b)+1):
        if a[i-1] == b[j-1]:
            dp[i][j] = dp[i-1][j-1]
        else:
            dp[i][j] = 1 + min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

#! https://joyjangs.tistory.com/38 레벤슈타인 알고리즘
