from collections import deque

n, m = map(int, input().split())

pos = list(map(int, input().split()))

q = deque([i for i in range(1, n + 1)])


min_answer = 0

for p in pos:
    r_cnt = 0
    while q[0] != p:
        q.rotate(1)
        r_cnt += 1

    q.rotate(-r_cnt)

    l_cnt = 0
    while q[0] != p:
        q.rotate(-1)
        l_cnt += 1

    q.rotate(l_cnt)

    if r_cnt > l_cnt:
        q.rotate(-l_cnt)
    else:
        q.rotate(r_cnt)

    q.popleft()

    min_answer += min(r_cnt, l_cnt)

print(min_answer)
