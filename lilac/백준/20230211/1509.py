
# 팰린드롬분할

import sys


s = list(input())
n = len(s)

ispalindrome = [[False]*n for _ in range(n)]

# ! ispalindrome[start_idx][end_idx] -> s의 start_idx에서 end_idx 까지 자른 문자열이 palindrome이면 True


# ! 길이 1의 문자열
for i in range(n):
    ispalindrome[i][i] = True

# ! 길이 2의 문자열
for i in range(n-1):
    if s[i] == s[i+1]:
        ispalindrome[i][i+1] = True

# ! 길이 3이상의 문자열

# ! 문자열 길이 i
for i in range(2, n):
    # ! 시작 위치 j
    for j in range(0, n-i):
        end = j + i

        if s[j] == s[j+i] and ispalindrome[j+1][j+i-1]:
            ispalindrome[j][j+i] = True


dp = [sys.maxsize] * (n+1)
dp[-1] = 0

for end in range(n):
    for start in range(end+1):
        if ispalindrome[start][end]:
            dp[end] = min(dp[end], dp[start-1]+1)


print(dp[n-1])
