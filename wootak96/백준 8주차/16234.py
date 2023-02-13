from collections import deque
dx = [0,0,1,-1]
dy = [1,-1,0,0]
def bfs(a, l, r):
    n = len(a)
    c = [[False]*n for _ in range(n)]
    ok = False
    for i in range(n):
        for j in range(n):
            if c[i][j] == False:
                q = deque()
                q.append((i,j))
                c[i][j] = True
                s = [(i,j)]
                total = a[i][j]
                while q:
                    x, y = q.popleft()
                    for k in range(4):
                        nx,ny = x+dx[k], y+dy[k]
                        if 0 <= nx < n and 0 <= ny < n and c[nx][ny] == False:
                            diff = abs(a[nx][ny] - a[x][y])
                            if l <= diff <= r:
                                q.append((nx,ny))
                                s.append((nx,ny))
                                c[nx][ny] = True
                                ok = True
                                total += a[nx][ny]
                val = total // len(s)
                for x, y in s:
                    a[x][y] = val
    return ok

n, l, r = map(int, input().split())
a = [list(map(int,input().split())) for _ in range(n)]
ans = 0
while True:
    if bfs(a,l,r):
        ans += 1
    else:
        break
print(ans)
