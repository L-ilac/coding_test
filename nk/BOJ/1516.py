from collections import deque
import sys

N = int(input()) # N 입력받기
graph = [[] for _ in range(N + 1)] # 노드와 간선의 정보 
inDegree = [0 for _ in range(N + 1)] # 각 노드의 진입 차수 리스트
time = [0 for _ in range(N + 1)] # 각 노드 건물 짓는데 걸리는 시간
answer = [0 for _ in range(N + 1)] # 정답리스트
queue = deque() # 큐 생성


for i in range(1, N+1):
    tmp_list = list(map(int, sys.stdin.readline().split()))[:-1] # -1 전까지 받은 값 저장
    time[i] = tmp_list[0] # 건물 짓는데 걸리는 시간 저장
    for tmp in tmp_list[1:]: # 연결된 리스트를 저장하기 위하여 반복문 생성
        graph[tmp].append(i) # 먼저 지어져야하는 노드에 자신을 추가
        inDegree[i] += 1 # 자신에 연결된 차수 높이기

for i in range(1, N+1):
    if inDegree[i] == 0: # 진입차수가 0일때 
        queue.append(i) # queue 에 건물 번호 넣어주기

while queue:
    data = queue.popleft() # 큐의 맨 왼쪽에 있는 데이터(건물 번호) 꺼내기 
    # 건물 짓는데 걸리는 시간 (선수 건물 짓기 + 현재 건물 짓기)
    answer[data] += time[data] # 건물을 짓는데 걸리는 시간 더하기

    for x in graph[data]: # 현재값과 연결된 노드를 탐색하며
        inDegree[x] -= 1 # 간선의 갯수 -1 
        answer[x] = max(answer[x], answer[data]) # x 건물을 짓기 전에 먼저 지어야 하는 선수 건물 짓는데 걸리는 시간으로 갱신
        if inDegree[x] == 0: # 진입 차수가 0 일때
            queue.append(x) # 큐에 현재 건물 번호 넣어주기

# 출력
for i in range(1, N+1): # 건물 하나씩 건물이 완성되기까지 걸리는 최소 시간 
    print(answer[i]) # 출력


