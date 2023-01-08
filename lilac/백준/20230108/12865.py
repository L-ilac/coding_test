# 평범한 배낭
# ! dp로 유명한 knapsack problem, 물건을 쪼갤수 없기 때문에, greedy가 아닌 dp로 풀어야함

n, k = map(int, input().split())  # 물품의 총수, 최대 무게

items = []

# (각 물품의 무게, 가치) 형태로 삽입
for _ in range(n):
    items.append((tuple(map(int, input().split()))))

# 가방이 수용할 수 있는 무게 0~k , 가방에 포함될 물건의 갯수 0~n 로 dp배열 구성
dp = [[0]*(k+1) for _ in range(n+1)]
# ! dp[i][j] -> 가방의 무게가 k이고, i번째 물건까지 가방에 포함할 수 있을 때, 얻을 수 있는 최대 가치


for i in range(n+1):
    for j in range(k+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        else:
            # 현재 넣으려는 물건이 가방의 크기보다 커서 아예 넣지를 못할때
            if items[i][0] > j:
                dp[i][j] = dp[i-1][j]
            else:
                # ! dp[i-1][j-items[i][1]] -> i번째 물품을 넣었을 때의 최대가치 = i번째 물품을 넣기위해 가방의 공간을 마련했을때의 최대 가치 (j-items[i][1]) + i번째 물품의 가치
                # ! dp[i-1][j] -> i번째 물품을 넣지않았을 때의 최대 가치
                # ! 둘중에 큰걸 고르면 된다.
                dp[i][j] = max(dp[i-1][j-items[i][1]], dp[i-1][j])


print(dp[-1][-1])
