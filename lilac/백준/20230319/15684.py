n, m, h = map(int, input().split())

# ! connect_info[h][a][b]  a번 세로선에서 b번 세로선으로 가는 가로선이 위에서 h번째 위치에 있음
connect_info = [[[False]*(n+1) for _ in range(n+1)] for _ in range(h+1)]


for _ in range(m):
    a, b = map(int, input().split())

    connect_info[a][b][b+1] = True
    connect_info[a][b+1][b] = True


board = [[]*h for _ in range(n)]


def dfs(xpos, ypos, start_point):
    if xpos == h+1:
        if ypos == start_point:
            return True
        else:
            return False

    # 오른쪽 방향으로 가로선이 있는 경우
    if connect_info[xpos][ypos][ypos+1]:
        dfs(xpos, ypos+1, start_point)
    # 왼쪽 방향으로 가로선이 있는 경우
    elif connect_info[xpos][ypos][ypos-1]:
        dfs(xpos, ypos-1, start_point)
    # 양쪽 모두 가로선이 없는 경우
    else:
        dfs(xpos+1, ypos, start_point)


flag = False
for i in range(n):
    if not dfs(0, i):
        flag = True
        break

if flag:
    print(-1)
else:
    pass
