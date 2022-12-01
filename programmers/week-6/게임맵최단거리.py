from collections import deque

def solution(maps):
    n, m = len(maps), len(maps[0])
    visited = [[-1] * m for _ in range(n)]

    # 남 동 북 서
    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    visited[0][0] = 1

    queue = deque([(0, 0)])
    while queue:
        x, y = queue.popleft()

        # if (x, y) == (n-1, m-1):
        #     break

        for i in range(4):
            tx = x + dx[i]
            ty = y + dy[i]

            if 0 <= tx < n and 0 <= ty < m and maps[tx][ty] == 1 and visited[tx][ty] == -1:    
                visited[tx][ty] = visited[x][y] + 1
                queue.append((tx, ty))

    return visited[n-1][m-1]

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,1],[0,0,0,0,1]]))