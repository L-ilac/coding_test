from collections import deque
import sys

# ! 입력값이 많아서 그냥 input쓰면 시간초과
n, m = map(int, sys.stdin.readline().split())

graph = [[] for _ in range(n+1)]

visited = [False] * (n+1)

for _ in range(m):
    u, v = map(int, sys.stdin.readline().split())
    graph[u].append(v)
    graph[v].append(u)


cnt = 0

for i in range(1, n+1):
    if not visited[i]:
        q = deque()
        q.append(i)
        visited[i] = True

        while q:
            now = q.popleft()

            for new in graph[now]:
                if not visited[new]:
                    visited[new] = True
                    q.append(new)

        cnt += 1

print(cnt)
