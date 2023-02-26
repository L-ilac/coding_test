from collections import deque
import sys


n, m = map(int, sys.stdin.readline().rstrip().split())

graph = [[] for _ in range(n+1)]
for _ in range(m):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


fac1, fac2 = map(int, sys.stdin.readline().rstrip().split())

# ! 경로상에 있는 다리 무게 제한중에 제일 작은 무게 구하기
# ! 한 공장에서 다른 공장으로 도달하는 경로를 bfs로 탐색하다가, 현재 설정된 중량을 못버티는 다리가 있으면 false
# ! 빠르게 도달하는게 목적이 아님.


def bfs(weight):
    q = deque()
    q.append([fac1, {fac1}])

    while q:
        now, visited = q.popleft()

        # ! 중량제한을 못버티는 다리 없이 도착지에 도달한 경우
        if now == fac2:
            return True

        for next, limit in graph[now]:
            if next not in visited:

                # ! 중량제한을 못버티는 다리가 있음
                if limit < weight:
                    continue

                visited.add(next)
                q.append([next, visited])

    # ! fac1 -> fac2 경로가 없다는 뜻
    return False


left = 0
right = 1000000000

answer = 0
while left <= right:
    mid = (left+right)//2

    # print(mid)

    if bfs(mid):
        left = mid + 1
        answer = mid
    else:
        right = mid - 1


print(answer)


# ? union_find 로 어떻게 풀지?
