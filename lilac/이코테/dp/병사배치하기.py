n = int(input())

soldiers = list(map(int, input().split()))

dp = [1] * n


for i in range(n-1):
    for j in range(i+1, n):
        if soldiers[j] < soldiers[i]:
            dp[j] = max(dp[j], dp[i] + 1)

print(n-max(dp))


n = int(input())
s = list(map(int, input().split()))
dp = [1] * n


for i in range(n-1):
    for j in range(i+1, n):
        if s[i] > s[j]:
            dp[j] = max(dp[i]+1, dp[j])

print(dp)
print(n-max(dp))
