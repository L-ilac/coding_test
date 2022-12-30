def dfs(graph, v, visited): # v: 출발 node
	visited[v] = True
	print(v, end='')

	for i in graph[v]:
		if not visited[i]:
			dfs(graph,i,visited) #재귀적으로 dfs함. 재귀를 통해 깊이 갈수 있는 만큼 깊이감. 깊이의 한계가 오면 하나씩 함수가 return 되면서 깊이가 아직 남아있는 다음 node를 방문.



graph = [[],[2,3,8],[1,7],[1,4,5],[3,5],[3,4],[7],[2,6,8],[1,7]]
# 인접 리스트 방식 표현 (연결된 것만 표현)
# 일부러 node 들을 오름차순으로 정리해놓음. 숫자가 작은 node가 먼저 접근.

visited = [False] * 9 


dfs(graph,1,visited)