import sys
from collections import defaultdict, deque
n = int(input())

cost = defaultdict(list)
graph = defaultdict(list)
indegree = [0] * (n+1)
time = [0] * (n+1)
queue = deque()


for idx in range(1, n+1):

    # 건물 짓는데 걸리는 시간, (먼저 건설되어야하는 건물), -1
    tmp = list(map(int, sys.stdin.readline().split()))

    cost[idx] = tmp[0]  # 건물 짓는데 걸리는 시간

    for b in tmp[1:-1]:  # 먼저 건설되어야하는 건물들에 대하여
        graph[b].append(idx)
        indegree[idx] += 1


# 먼저 지어져야할 건물이 없는 건물을 큐에 넣는다.
for i in range(1, n+1):
    if indegree[i] == 0:
        queue.append(i)


while queue:
    # 건물을 짓기 위해 필요한 시간은 (먼저 지어져야하는 건물 중 제일 오래 걸리는 시간) + (해당 건물을 짓는 시간) 이다.

    # 더 이상 먼저 지어져야할 건물이 없는 건물을 pop하고, 이 건물을 짓는데 걸리는 시간을 확정짓는다.
    # now에 해당하는 건물을 짓는데 걸리는 시간은 더 커질 요소가 없다.
    now = queue.popleft()
    time[now] += cost[now]

    # now를 짓는데 걸리는 시간은 확정되었으므로, now를 먼저 지어져야할 건물로 갖는 건물들에 대해 업데이트가 필요하다.
    for i in graph[now]:
        # now를 먼저 지어져야할 건물로 갖는 건물들은 now를 짓는데 걸리는 시간이 최대값인지 확인해야한다.
        # 예를 들어, 3을 짓기위해 1,2를 지어야하는데, 1이 1만큼, 2가 2만큼 걸린다면,
        # 여러건물을 동시에 지을수 있기 때문에 2만큼 걸린후 3을 지을 수 있다.
<<<<<<< HEAD
<<<<<<< HEAD
        # ! 일반적인 위상정렬 문제와 다른 포인트
=======
>>>>>>> b99453e (파일 재추가)
=======
        # ! 일반적인 위상정렬 문제와 다른 포인트
>>>>>>> 8785cd6 (20221230 스터디 문제 추가 주석)
        time[i] = max(time[i], time[now])

        # 먼저 지어져야하는 건물의 갯수를 하나 뺀다.(위상정렬과 동일)
        indegree[i] -= 1

        # 만약 먼저 지어야져하는 건물이 더 없다면, 자기 자신을 짓는 시간만 더해주면 되므로 큐에 넣는다.
        if indegree[i] == 0:
            queue.append(i)

for i in range(1, n+1):
    print(time[i])
