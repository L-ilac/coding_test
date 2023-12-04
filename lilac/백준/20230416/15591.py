from collections import defaultdict, deque
import sys

N, Q = map(int, sys.stdin.readline().rstrip().split())


usado = [[sys.maxsize] * (N+1) for _ in range(N+1)]
# 주어진 그래프에는 사이클이 없음
graph = defaultdict(list)

for _ in range(N-1):
    p, q, r = map(int, sys.stdin.readline().rstrip().split())

    graph[p].append((q, r))
    graph[q].append((p, r))


def bfs(start):
    visited = [False] * (N+1)

    q = deque()
    q.append(start)
    visited[start] = True

    while q:
        now = q.popleft()

        for next, cost in graph[now]:
            if not visited[next]:
                visited[next] = True
                usado[start][next] = min(usado[start][now], cost)
                q.append(next)


for i in range(1, N+1):
    bfs(i)

print(usado)

questions = []
for _ in range(Q):
    k, v = map(int, sys.stdin.readline().rstrip().split())
    questions.append((k, v))


for k, v in questions:
    tmp = [u for u in usado[v] if u >= k and u != sys.maxsize]
    print(len(tmp))
