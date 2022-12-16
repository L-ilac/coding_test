# 로봇 청소기
N, M = map(int, input().split())
r, c, d = map(int, input().split())

direction = {
    0: [-1, 0], # 북 -> 서
    1: [0, 1], # 동 -> 북
    2: [1, 0], # 남 -> 동
    3: [0, -1] # 서 -> 남
}

zido = []
for _ in range(N):
    zido.append(list(map(int, input().split())))

res = 1
zido[r][c] = 2
while True:

    flag = 1
    for _ in range(4):
        ld = (d+3) % 4
        tr = r + direction[ld][0]
        tc = c + direction[ld][1]
        d = ld

        if 0 <= tr < N and 0 <= tc < M and zido[tr][tc] == 0:
            zido[tr][tc] = 2
            res += 1
            r, c = tr, tc
            flag = 0
            break

    if flag:
        rev_r = r - direction[d][0]
        rev_c = c - direction[d][1]

        if zido[rev_r][rev_c] == 1:
            break
        else:
            r, c = rev_r, rev_c    

print(res)