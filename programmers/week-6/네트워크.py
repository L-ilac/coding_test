from collections import deque, defaultdict

def solution(n, computers):

    answer = 0
    graph = defaultdict(list)

    for i, com in enumerate(computers):
        for c in range(len(com)):
            if com[c] == 1 and c != i:
                graph[i].append(c)
    
    visited = [0] * n

    for i in range(n):
        if visited[i] == 0:
            visited[i] = 1
            queue = deque([i])

            while queue:
                x = queue.popleft()
                for node in graph[x]:
                    if visited[node] == 0:
                        visited[node] = 1
                        queue.append(node)
            
            answer += 1

    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))