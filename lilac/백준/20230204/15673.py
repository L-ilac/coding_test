n = int(input())

p = list(map(int, input().split()))

# 두 그룹을 골라서 고른 그룹의 스터성 지수의 곱.
# best 2그룹 곱하거나, worst 2그룹 곱하기.

# worst[i] = i번째 사람이 포함되는 팀 중 가장 스타성 지수의 합이 가장 낮은 팀
# best[i] = i번째 사람이 포함되는 팀 중 가장 스타성 지수의 합이 가장 높은 팀

worst = [0] * (n+1)
best = [0] * (n+1)


for i in range(1, n+1):
    best[i] = max(p[i-1], best[i-1]+p[i-1])

    worst[i] = min(p[i-1], worst[i-1]+p[i-1])

print(best)
print(worst)
