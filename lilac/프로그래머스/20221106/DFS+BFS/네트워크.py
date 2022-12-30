def dfs(graph, node, visited):
    visited[node] = True  # 현재 노드 방문처리

    for i in graph[node]:  # 현재 노드와 연결된 모든 다른 노드에 대해
        if not visited[i]:  # 방문하지 않은 노드가 있다면
            dfs(graph, i, visited)  # 재귀적으로 dfs 수행


def solution(n, computers):
    answer = 0
    visited = [False] * n
    stack = []
    graph = {}

    # graph setting -> 그래프 세팅 안해도 되는 방법은 없나?
    for i in range(0, n):
        tmp = []
        for j in range(0, n):
            if computers[i][j] == 1 and i != j:
                tmp.append(j)
        graph[i] = tmp

    # 모든 네트워크가 방문될 때까지 수행
    for i in range(n):
        if visited[i]:  # 만약 dfs에 의해 방문처리 되었다면, 이미 밑에서 카운트 되었으므로 다음 노드로 넘어간다.
            continue
        else:
            dfs(graph, i, visited)  # i node 를 기준으로 연결된 모든 그래프를 방문처리
            answer += 1  # 하나의 네트워크 카운트

    return answer
