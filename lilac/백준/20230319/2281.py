n, m = map(int, input().split())

names = []

for _ in range(n):
    names.append(int(input()))


# ! dp[i] => i번째 이름이 가장 처음 쓰는 이름일 댸, 남게되는 칸의 수의 제곱의 합의 최솟값
dp = [0] * n


for i in range(n-2, -1, -1):
    length = 0
    length += names[i]

    dp[i] = (m-length)**2 + dp[i+1]

    for j in range(i+1, n):
        length += 1
        length += names[j]

        if length > m:
            break

        tmp = (m-length)**2

        if j == n-1:
            dp[i] = 0
        else:
            dp[i] = min(tmp + dp[j+1], dp[i])

print(dp)
print(dp[0])
