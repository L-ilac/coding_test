dx = [-1,0,1,0]
dy = [0,1,0,-1]
n,m = map(int,input().split())
x,y,dir = map(int,input().split())
a = [list(map(int,input().split())) for _ in range(n)]
cnt = 0
while True:
    if a[x][y] == 0:
        a[x][y] = 2
    if a[x+1][y] != 0 and a[x-1][y] != 0 and a[x][y-1] != 0 and a[x][y+1] != 0:
        if a[x-dx[dir]][y-dy[dir]] == 1:
            break
        else:
            x -= dx[dir]
            y -= dy[dir]
    else:
        dir = (dir + 3) % 4
        if a[x+dx[dir]][y+dy[dir]] == 0:
            x += dx[dir]
            y += dy[dir]
for i in range(n):
    for j in range(m):
        if a[i][j] == 2:
            cnt += 1
print(cnt)
