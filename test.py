def isPal(i, l):
    tmp = str(i)
    tmp = '0' * (l-len(str(i)))

    i = tmp + str(i)

    # print(i)

    target = list(i)
    length = len(target)

    for i in range(length//2):
        if target[i] != target[length-1-i]:
            return False

    return True


queries = [[0, 1, 0, 1], [1, 1, 1, 2]]

l = len(queries[0])
dp = [-1]*(10**l)


for i in range(10**l):
    if isPal(i, l):
        for j in range(l):
            if i+(10**j) < (10**l):
                dp[i+(10**j)] = 1


for i in range(10**l):
    if not isPal(i, l) and dp[i] != -1:
        for j in range(l):
            if i+(10**j) < (10**l) and dp[i+(10**j)] == -1 and not isPal(i+(10**j), l):
                dp[i+(10**j)] = -(dp[i]-1)

result = []

for q in queries:
    result.append(dp[int("".join(map(str, q)))])

print(result)
