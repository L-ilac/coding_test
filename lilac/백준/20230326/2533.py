from collections import defaultdict

n = int(input())


graph = [[] for _ in range(n+1)]

indegree = defaultdict(int)

for _ in range(n-1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

    indegree[u] += 1
    indegree[v] += 1


tmp = list(indegree.items())  #
tmp.sort(key=lambda x: x[1])

# print(tmp)


answer = 0
complete = set()
while tmp:
    now = tmp.pop()

    if now[0] in complete:
        continue

    indegree[now[0]] = 0
    complete.add(now[0])
    answer += 1

    for new in graph[now[0]]:
        indegree[new] -= 1

        if indegree[new] == 0:
            complete.add(new)

    if len(complete) == n:
        break

print(answer)


# # i번의 모든 친구가 전부 얼리 어답터라면,
# if indegree[i] == 0:
#     complete.add(i)
