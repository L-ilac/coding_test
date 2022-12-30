graph = [[] for _ in range(3)]

graph[0].append((1,7)) # 0번째 리스트에 튜플형태로 그래프 연결정보 삽입
# 해석방법 : Node 0 과 Node 1이 cost 7로 연결되어있다.
graph[0].append((2,5))

# Node 1의 연결정보
graph[1].append((0,7))

# Node 2의 연결정보
graph[2].append((0,5))