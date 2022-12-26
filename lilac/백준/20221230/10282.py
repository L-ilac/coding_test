# import sys
# import heapq

# test_case_num = int(input())
# test_case = []

# # 시스템 상에서 표현할 수 있는 최댓값
# inf = sys.maxsize


# # 감염되는데 걸리는 시간을 업데이트하는 다익스트라 알고리즘 수행 함수
# def dijkstra(node_num, start, graph):
#     # 해킹된 컴퓨터로부터 출발하여, 모든 컴퓨터가 감염되기까지 걸리는 시간을 저장하는 리스트
#     infected_time = [inf] * (node_num+1)

#     queue = []  # 힙을 사용해서 다익스트라 알고리즘을 구현하기때문에 힙으로 사용할 리스트

#     # 시작점을 기준으로 알고리즘을 수행하는데, 시작점은 비용이 0이다.
#     heapq.heappush(queue, (0, start))  # (컴퓨터까지 도달하기 위한 현재까지의 비용, 컴퓨터 번호)

#     # 출발지 -> 출발지 는 비용이 0이다.
#     infected_time[start] = 0

#     # 큐가 빌 때까지, 비용(시간)을 업데이트 한다.
#     while queue:

#         # 컴퓨터까지 도달하기 위한 현재까지의 비용, 컴퓨터 번호
#         t, now = heapq.heappop(queue)

#         # 기존에 now 까지의 최단거리가 지금 꺼낸 now까지의 거리보다 짧다면, 업데이트 할 필요 없음.
#         if infected_time[now] < t:
#             continue

#         # now에서 갈 수 있는 모든 노드에 대해 거리를 줄일 수 있는지 시도한다.
#         for i in graph[now]:
#             # i는 (노드번호, 비용) 의 형태로 저장되어 있는데, now -> i[0] 까지 이동하는 비용이 i[1]이라는 뜻이다.

#             # 출발점 -> now 까지의 비용 + now -> i[0] 까지의 비용 = 출발점 -> i[0] 까지의 비용
#             tmp = t + i[1]

#             # 위에서 계산한 값이 저장되어 있는 최단거리보다 짧다면, 업데이트 해주면된다.
#             if tmp < infected_time[i[0]]:
#                 infected_time[i[0]] = tmp
#                 # 업데이트하면서 출발점으로부터 특정 지점까지의 최단거리가 변경되었기 때문에,
#                 # 변경된 값에 의해 또다른 변경을 야기할 수 있으므로, 큐에 변경된 요소를 넣는다.
#                 # 야기된 변경이 있는지 없는지는, line 31에서 판단한다.
#                 heapq.heappush(queue, (tmp, i[0]))

#     total_hacked = 0
#     total_time = 0

#     for i in range(1, node_num+1):
#         # infected_time 값이 inf인 컴퓨터들은 처음 해킹된 컴퓨터로부터 도달할 수 없는 컴퓨터이다.(의존성이 존재하지 않음)
#         if infected_time[i] != inf:
#             total_hacked += 1
#             # 처음 해킹된 컴퓨터로 도달할 수 있는 모든 컴퓨터들이 전부 감염되는 시간을 구하려면, 감염된 컴퓨터들중 가장 오래 걸린 값을 선택하면 된다.
#             total_time = max(total_time, infected_time[i])

#     print(total_hacked, total_time)


# # 테스트 케이스 입력
# for _ in range(test_case_num):

#     # 컴퓨터 개수 n, 의존성 개수 d, 해킹당한 컴퓨터 번호 c
#     n, d, c = map(int, sys.stdin.readline().split())

#     # 의존성을 그래프 형태로 저장(인접 리스트 방식 사용) -> 딕셔너리 형태로 해도 상관없음(defaultdict(list))
#     dependency = [[] for i in range(n+1)]
#     for _ in range(d):

#         # 컴퓨터 a가 b를 의존하며, b가 감염되면 s초 후에 a도 감염된다.(b -> a로 가는데 s초 걸린다 로 해석할 수 있음)
#         a, b, s = map(int, sys.stdin.readline().split())
#         # b에서 a로 가는 경로가 존재하고(단방향), s만큼의 비용이 든다.
#         dependency[b].append((a, s))

#     # 테스트 케이스가 여러개이므로, 관련된 데이터들을 리스트 하나에 묶는다.
#     # 컴퓨터 개수 n, 해킹당한 컴퓨터 번호 c, 컴퓨터들간의 의존성을 담은 그래프 dependency
#     test_case.append([n, c, dependency])


# # 여러 개의 테스트 케이스들에 대해서 다익스트라 알고리즘 수행
# # 가장 처음 해킹당한 컴퓨터를 시작점으로 도달할 수 있는(감염될 수 있는) 모든 컴퓨터에 대해 감염되는데 걸리는 시간을 계산한다.
# for case in test_case:
#     dijkstra(case[0], case[1], case[2])  # 컴퓨터 개수, 해킹당한 컴퓨터 번호 , 의존성 그래프


import sys
import heapq
from collections import defaultdict

test_cases = []
test_case_num = int(input())  # 테스트 케이스 갯수
inf = sys.maxsize


def solve(start, graph, node_num):
    hacked_time = [inf] * (node_num + 1)
    q = []

    hacked_time[start] = 0
    heapq.heappush(q, (0, start))

    while q:
        current_time, now = heapq.heappop(q)

        if current_time < hacked_time[now]:
            continue

        for node in graph[now]:
            tmp_time = current_time + node[1]

            if tmp_time < hacked_time[node[0]]:
                hacked_time[node[0]] = tmp_time
                heapq.heappush(q, (tmp_time, node[0]))

    total_hacked = 0
    total_time = 0

    for time in hacked_time:
        if time != inf:
            total_hacked += 1
            total_time = max(total_time, time)

    print(total_hacked, total_time)


for _ in range(test_case_num):
    n, d, c = map(int, sys.stdin.readline().split())

    dependency = defaultdict(list)
    for _ in range(d):
        a, b, s = map(int, sys.stdin.readline().split())
        dependency[b].append((a, s))

    test_cases.append([c, dependency, n])


for case in test_cases:
    solve(case[0], case[1], case[2])
