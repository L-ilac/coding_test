import sys
INF = sys.maxsize
n = int(input())
graph = [list(map(int, input().split())) for _ in range(n)]

# dp[현재 위치한 도시][지금까지 방문한 도시]
# dp : 현재까지 방문한 도시들을 지나가는데 쓰인 비용 x
# dp : 아직 방문하지 않은 도시들을 모두 거쳐 다시 시작점으로 돌아가는데 드는 최소 비용

dp = [[-1 for _ in range(1 << n)]
      for _ in range(n)]  # ! dp 초기값을 INF로 하면 안되는 이유 밑에 적어놓음


def tfs(cur, visited):
    # print(cur, visited)

    if dp[cur][visited] != -1:  # 이미 최소 비용이 계산되어 있다면
        return dp[cur][visited]  # 출력

    if visited == (1 << n)-1:  # 모든 도시를 방문했다면 ex 1111 -> 0번,1번,2번,3번 도시 모두 방문
        if graph[cur][0]:  # 출발점으로 돌아갈 경로가 있다면
            dp[cur][visited] = graph[cur][0]
            return graph[cur][0]  # 출력

        else:
            dp[cur][visited] = INF  # dp 업데이트
            return INF  # 없다면 무한대 출력

    # ! 현재 도시 cur와 지금까지 방문한 visited를 기준으로 그 다음에 이어질 여러가지 경로중 가장 최솟값을 구하는 것이므로, min_dist = INF 로 사용한다.
    min_dist = INF

    for i in range(1, n):  # 모든 도시 탐방
        # 가는 경로가 있거나 방문하지 않은 도시라면

        if graph[cur][i] == 0:
            continue
        if visited & (1 << i):
            continue

        # ! 한 점을 기준으로 도달할 수 있는 모든 경로를 다 탐색하고 나오면, 최종적으로 최솟값이 min_dist에 저장된다.
        min_dist = min(min_dist, graph[cur][i] + tfs(i, visited | (1 << i)))

        # dp[3][1001] = dp[1][1011] + graph[3][0]
        # ! 사용할 수 없는 이유, dp 초기화를 -1로 해놔서 값이 안바뀜, 그렇다고 dp 초기화 값을 INF로 바꾸고, 위의 17line의 조건도 INF로 바꾸면, 시간초과 남
        # dp[cur][visited] = min(dp[cur][visited],  graph[cur][i] + tfs(i, visited | (1 << i)))

    dp[cur][visited] = min_dist  # dp 업데이트

    # return dp[cur][visited]
    return min_dist  # 최소 거리


print(tfs(0, 1))  # 0번 출발지에서 시작,  1 = 0001을 의미 0번에서 출발했으니깐


# ! 기본적으로 dfs의 구조를 띄고 있는 점을 명심할 것.
# ! dfs의 결과로 반환되는 값을 dp를 갱신하는데 사용한다.
