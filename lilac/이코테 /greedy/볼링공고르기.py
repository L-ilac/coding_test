n, m = map(int, input().split())

balls = list(map(int, input().split()))

cnt = 0
for i in range(1, m+1):
    for b in balls:
        if b != i:
            cnt += balls.count(i)

print(cnt//2)
