x = int(input())

dp = [{1}]
while True:

    tmp = set()
    for k in dp[-1]:
        tmp.add(k+1)
        tmp.add(k*2)
        tmp.add(k*3)
        tmp.add(k*5)

    if x in tmp:
        print(len(dp))
        break

    dp.append(tmp)


# x = int(input())
# dp = [0] * (x+1)

# for i in range(2, x+1):
#     dp[i] = dp[i-1] + 1

#     if i % 2 == 0:
#         dp[i] = min(dp[i], dp[i//2] + 1)

#     if i % 3 == 0:
#         dp[i] = min(dp[i], dp[i//3] + 1)

#     if i % 5 == 0:
#         dp[i] = min(dp[i], dp[i//5] + 1)

# print(dp[x])
