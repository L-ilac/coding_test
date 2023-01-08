# bfs 또는 dfs를 통해 주어진 보드에서 영역의 갯수를 구하는 문제
#! 매우 기초적인 문제


from collections import deque
import sys
sys.setrecursionlimit(10000)  # ? dfs로 푸는 경우에 필요한 재귀함수 깊이 설정(최대 깊이 50 * 50)

# 총 테스트 케이스 갯수
t = int(input())
test = []

# 맵 세팅
for _ in range(t):
    # 가로, 세로, 배추의 갯수
    m, n, k = map(int, input().split())
    board = [[0] * m for _ in range(n)]
    for _ in range(k):
        # 배추가 심어진 위치
        x, y = map(int, input().split())
        board[y][x] = 1

    test.append(board)


# * BFS 풀이
def bfs(i, j, board, visited):
    m, n = len(board[0]), len(board)
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append((i, j))

    # 출발점을 기준으로 인접하여 방문 가능한 모든 노드 방문
    while q:
        now_x, now_y = q.popleft()

        for dx, dy in d:
            new_x, new_y = now_x+dx, now_y+dy

            if 0 <= new_x <= m-1 and 0 <= new_y <= n-1:
                if board[new_y][new_x] == 1 and not visited[new_y][new_x]:
                    visited[new_y][new_x] = True
                    q.append((new_x, new_y))


# * dfs 풀이
def dfs(x, y, board, visited):
    m, n = len(board[0]), len(board)
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

    for dx, dy in d:
        new_x, new_y = x+dx, y+dy

        if 0 <= new_x <= m-1 and 0 <= new_y <= n-1:
            if board[new_y][new_x] == 1 and not visited[new_y][new_x]:
                visited[new_y][new_x] = True
                dfs(new_x, new_y, board, visited)


for t in test:
    cnt = 0
    m, n = len(t[0]), len(t)
    visited = [[False] * m for _ in range(n)]

    for i in range(m):
        for j in range(n):
            if t[j][i] == 1 and not visited[j][i]:
                visited[j][i] = True
                #dfs(i, j, t, visited)
                bfs(i, j, t, visited)
                cnt += 1

    print(cnt)
