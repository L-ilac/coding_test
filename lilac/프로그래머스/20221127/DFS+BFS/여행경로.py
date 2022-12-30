# # dfs적 접근(주어진 티켓을 가지고 갈 수 있는 방향까지 전부 다 간 다음에, 모든 티켓을 다 사용 못하면? 롤백)
# # 1. ICN 에서 시작 + 모든 티켓을 사용해야함
# # 2. 도착 가능 지점이 2개 이상이면 알파벳이 빠른 공항 선택
# # 무작정 알파벳이 빠른 공항을 선택하면, 티켓을 모두 사용 못하는 경우가 생김
# #

# from collections import defaultdict # defaultdict()

# def solution(tickets):
#     answer = []
#     stack = []
#     airlines = defaultdict(list) # -> 사실상 티켓을 그래프 형태로 구현해 놓은 것.

#     for ticket in tickets:
#         airlines[ticket[0]].append(ticket[1]) # 중복이 있을 수 있음(동일한 티켓이 2개 이상인 경우)

#     for airport in airports:
#         airlines[airport].sort() # 알파벳 순 정렬

#     # 항상 출발은 ICN
#     departure = 'ICN'
#     arrival = [airport for airport in airports if airlines[airport]]
#     airlines[departure].pop(0)
#     stack.append((departure,arrival))

#     while any(airlines[airport] for airport in airports): # 티켓을 사용하면 사용한 티켓 삭제
#         # 다음에 가고자하는 항공편이 legal 한가? 하다면 그냥 넣고, 아니면 빼야함
#         break
#         departure = arrival
#         arrival = airlines[departure].pop()
#         if not airlines[arrival]: # 다음 목적지가 없는데, 티켓을 전부 사용하지 못했다면?


#             now = stack.pop()
#             break


#         print(airlines)
#     # 1. 모든 공항 조사
#     # 2. 공항별 도착지 조사(알파벳이 빠른 요소 먼저 접근하기 위함)
#     # 3. ticket을 모두 사용해야함()
#     return answer

import collections
answer = []
graph = collections.defaultdict(list)


def dfs(s):
    while graph[s]:
        dfs(graph[s].pop(0))
    answer.append(s)


def solution(tickets):

    for a, b in tickets:
        graph[a].append(b)
    for a, b in graph.items():
        graph[a].sort()

    dfs("ICN")

    return answer[::-1]
