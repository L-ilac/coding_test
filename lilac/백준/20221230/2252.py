# 주어진 입력은 학생들의 순서를 단편적으로 알려주는 정보이다.
# 주어진 토대로 학생들을 줄세울것. 단편적인 정보만 있으므로, 답은 여러개일 수 있음
import sys
from collections import defaultdict, deque

n, m = map(int, sys.stdin.readline().split())
graph = defaultdict(list)
indegree = [0] * (n+1)
queue = deque()


for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)  # a는 b보다 앞에 있다.(topological sort)
    indegree[b] += 1

# 자기보다 앞선 사람이 없는 녀석 골라내기
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)

result = []

while queue:
    now = queue.popleft()
    result.append(now)

    for i in graph[now]:
        indegree[i] -= 1

        if indegree[i] == 0:
            queue.append(i)

print(*result)
