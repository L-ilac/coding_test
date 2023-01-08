# bfs 풀이
# ! 기본적인 그래프 탐색 문제로, 영역의 갯수를 세는 문제. 1012번 문제와 동일하다.
from collections import deque

n = int(input())


board = []
visited = [[False] * n for _ in range(n)]

for _ in range(n):
    board.append(list(map(int, list(input()))))

result = []

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True

            cnt = 1

            while q:
                d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                now_x, now_y = q.popleft()

                for dx, dy in d:
                    new_x, new_y = now_x+dx, now_y+dy

                    if 0 <= new_x <= n-1 and 0 <= new_y <= n-1:
                        if board[new_x][new_y] == 1 and not visited[new_x][new_y]:
                            visited[new_x][new_y] = True
                            q.append((new_x, new_y))
                            cnt += 1

            result.append(cnt)

result.sort()

print(len(result))
for i in result:
    print(i)


# dfs로도 풀어봅시다. dfs + stack

for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            q = deque()
            q.append((i, j))
            visited[i][j] = True

            cnt = 1

            while q:
                d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
                now_x, now_y = q.pop()

                for dx, dy in d:
                    new_x, new_y = now_x+dx, now_y+dy

                    if 0 <= new_x <= n-1 and 0 <= new_y <= n-1:
                        if board[new_x][new_y] == 1 and not visited[new_x][new_y]:
                            visited[new_x][new_y] = True
                            q.append((new_x, new_y))
                            cnt += 1

            result.append(cnt)

# dfs + recursive
cnt = 1


def dfs(x, y):
    global cnt  # global을 안쓰고 풀순 없을까
    d = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    visited[x][y] = True

    for dx, dy in d:
        new_x, new_y = x+dx, y+dy

        if 0 <= new_x <= n-1 and 0 <= new_y <= n-1:
            if board[new_x][new_y] == 1 and not visited[new_x][new_y]:
                visited[new_x][new_y] = True
                cnt += 1
                dfs(new_x, new_y)


for i in range(n):
    for j in range(n):
        if board[i][j] == 1 and not visited[i][j]:
            dfs(i, j)  # dfs 함수가 총 몇개의 노드를 탐색했는지 반환해야함
            result.append(cnt)
            cnt = 1
