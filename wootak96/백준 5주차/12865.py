n,k = map(int,input().split())
temp = [list(map(int,input().split())) for _ in range(n)]
w,v = zip(*temp)
w = [0] + list(w)
v = [0] + list(v)
d = [0]*(k+1)
for i in range(1, n+1): # i : 배낭
    for j in range(k, 0, -1): # j : 무게
        if j-w[i] >= 0: #제한된 무게보다 물건 무게가 덜 다가면
            d[j] = max(d[j],d[j-w[i]]+v[i]) # i번째 물건을 넣지 않은 경우 vs 넣은 경우
print(d[k])
