import sys

N, K = map(int, input().split())
stuff = [[0,0]]
knapsack = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for _ in range(N):
    stuff.append(list(map(int, input().split())))


#냅색 문제 풀이
for i in range(1, N + 1):
    for j in range(1, K + 1):
        weight = stuff[i][0] 
        value = stuff[i][1]
       
        if j < weight:
            knapsack[i][j] = knapsack[i - 1][j] #weight보다 작으면 위의 값을 그대로 가져온다
        else: # 현재 가방에 넣을 수 있는 무게의 가치를 비교하는데, 현재 물건의 가치와 바로 이전의 이 현재 물건을 넣을 수 있는  무게의 가치를 더한 것과 , 현재 가방의 무게의 이전 물건의 가치중 높은 것을 선택!
            knapsack[i][j] = max(value + knapsack[i - 1][j - weight], knapsack[i - 1][j])

print(knapsack[N][K])