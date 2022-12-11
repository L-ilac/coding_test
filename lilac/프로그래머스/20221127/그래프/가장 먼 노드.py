# bfs로 depth 가 제일 깊은 층의 원소 갯수 찾으면 될듯?
from collections import deque


def solution(n, edge):
    answer = 0
    graph = [[] for _ in range(n+1)]  # 1~n 인덱스로 접근
    visited = [0] * (n+1)  # 방문 확인용

    queue = deque()
    same_depth = []

    # graph setting
    for e in edge:
        graph[e[0]].append(e[1])
        graph[e[1]].append(e[0])

    # bfs를 하되, 같은 depth에 있는 노드들은 한번에 모아서 넣음

    queue.append(1)  # 1번 노드 기준이므로 초기 1 넣음
    visited[1] = 1

    while queue:
        now = queue.popleft()
        print(now)

        for g in graph[now]:
            if visited[g] == 0:
                visited[g] = 1
                same_depth.append(g)  # 방문하지 않은 사람이 있으면 반복

        if not queue and same_depth:
            queue.extend(same_depth)
            answer = len(same_depth)
            same_depth.clear()

    return answer
