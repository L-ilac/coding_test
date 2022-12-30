import sys
from collections import deque
# 위상 정렬 : 방향성을 가진 그래프, 내부에 순환이 없어야 함.
n, m = map(int, sys.stdin.readline().split())
graph = [[] for _ in range(n + 1)] # node 갯수 만큼 노드 간선 그래프 리스트 만들기
inDegree = [0 for _ in range(n + 1)] # node 갯수 만큼 차수 리스트
queue = deque() # 큐 생성
answer = []

# 입력 받아서 그래프 만들기, 차수 세기
for _ in range(m): # 비교한 갯수 만큼
    a, b = map(int, sys.stdin.readline().split()) # 작은 수 a, 큰수 b
    graph[a].append(b) # a 노드에 b 잇기
    inDegree[b] += 1 # 진입 차수 1 증가

# 진입 차수가 0인 노드를 queue 에 삽입
for i in range(1, n + 1): # 1 이상부터 노드 갯수 길이 만큼
    if inDegree[i] == 0: # 진입 차수가 0이면
        queue.append(i) # queue 에 삽입

# 삽입된 큐를 가지고
while queue: # 큐에 값이 있으면
    tmp = queue.popleft() # queue 에서 가장 왼쪽의 값 제거,
    answer.append(tmp)# 제거된 값 담기

    for i in graph[tmp]: # 큐에서 꺼낸 원소와 연결된 노드
        inDegree[i] -= 1 # 간선 제거
        if inDegree[i] == 0: # 제거한 후 진입차수가 0이면
            queue.append(i) # queue 에 삽입.

print(*answer) # list 의 모든 값 출력

