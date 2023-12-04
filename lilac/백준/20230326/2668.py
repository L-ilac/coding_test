n = int(input())

nums = [0]

for _ in range(n):
    nums.append(int(input()))


def dfs(i, start):
    global flag

    visited[i] = True

    if nums[i] == start and visited[nums[i]]:
        flag = True

    if not visited[nums[i]]:
        dfs(nums[i], start)

    return flag


answer = set()
for i in range(1, n+1):

    visited = [False]*(n+1)
    flag = False

    if dfs(i, i):
        answer.update([i for i in range(1, n+1) if visited[i]])


print(len(answer))
answer = list(answer)
answer.sort()

for a in answer:
    print(a)
