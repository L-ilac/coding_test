import sys
INF=sys.maxsize
n=int(input())
graph = [list(map(int,input().split())) for _ in range(n)]

# dp[현재 위치한 도시][지금까지 방문한 도시]
# dp : 현재까지 방문한 도시들을 지나가는데 쓰인 비용 x 
# dp : 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 돌아가는데 드는 최소 비용

dp=[[-1 for _ in range(1<<n)] for _ in range(n)]
 


def tfs(cur,visited):

    if visited == (1<<n)-1 : # 모든 도시를 방문했다면 ex 1111 -> 0번,1번,2번,3번 도시 모두 방문
        if graph[cur][0]: # 출발점으로 돌아갈 경로가 있다면
            return graph[cur][0] # 출력
        
        else:
            dp[cur][visited]=graph[cur][0] # dp 업데이트
            return INF # 없다면 무한대 출력

    if dp[cur][visited] != -1: # 이미 최소 비용이 계산되어 있다면
        return dp[cur][visited] # 출력

    min_dist = INF
    for i in range(1,n): # 모든 도시 탐방
        if not visited & (1 << i) and graph[cur][i] != 0 : # 가는 경로가 있거나 방문하지 않은 도시라면
            min_dist = min(min_dist, graph[cur][i] + tfs(i,visited | (1 << i)))

            # dp[3][1001] = dp[1][1011] + graph[3][0]  

    dp[cur][visited] = min_dist # dp 업데이트
    return min_dist # 최소 거리 

print(tfs(0,1)) # 0번 출발지에서 시작,  1 = 0001을 의미 0번에서 출발했으니깐
