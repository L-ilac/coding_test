from collections import deque
import sys
import heapq
# ! 각 섬을 연결할 수 있는 가장 짧은 다리의 길이를 구한다.
# ! 섬을 연결할 수 없거나 길이가 1이면 길이는 inf

# ! 다리 길이를 전부 구한 뒤에, minimum spanning tree
n, m = map(int, input().split())


def bfs_get_island(start, island_num):

    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()
    q.append(start)

    visited[start[0]][start[1]] = True

    while q:
        now_x, now_y = q.popleft()
        board[now_x][now_y] = island_num

        for dx, dy in d:
            new_x, new_y = now_x+dx, now_y + dy

            if 0 <= new_x <= n-1 and 0 <= new_y <= m-1:
                if not visited[new_x][new_y] and board[new_x][new_y] != 0:
                    visited[new_x][new_y] = True
                    q.append((new_x, new_y))


board = []
for _ in range(n):
    board.append(list(map(int, input().split())))

visited = [[False]*m for _ in range(n)]

islands = []
island_num = 1
for i in range(n):
    for j in range(m):
        if not visited[i][j] and board[i][j] != 0:
            bfs_get_island((i, j), island_num)
            island_num += 1


# ! 섬 간의 최단으로 연결할 수 있는 다리의 길이
distance = [[sys.maxsize]*(island_num-1) for _ in range(island_num-1)]

d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
for i in range(n):
    for j in range(m):
        if board[i][j] != 0:
            for dx, dy in d:

                new_x, new_y = i+dx, j+dy

                while 0 <= new_x <= n-1 and 0 <= new_y <= m-1 and board[new_x][new_y] == 0:
                    # print(new_x, new_y)
                    new_x += dx
                    new_y += dy

                if new_x > n-1 or new_x < 0 or new_y > m-1 or new_y < 0:
                    continue

                if board[i][j] != board[new_x][new_y] and board[new_x][new_y] != 0:
                    dist = max(abs(new_x-i)-1, abs(new_y-j)-1)

                    if dist == 1:
                        pass
                    else:
                        distance[board[i][j]-1][board[new_x][new_y]-1] = min(
                            distance[board[i][j]-1][board[new_x][new_y]-1], dist)
                        distance[board[new_x][new_y]-1][board[i][j]-1] = min(
                            distance[board[new_x][new_y]-1][board[i][j]-1], dist)

edges = []
for i in range(island_num-1):
    for j in range(island_num-1):
        if distance[i][j] != sys.maxsize:
            heapq.heappush(edges, (distance[i][j], i, j))


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


# print(distance)
# print(edges)


parent = [i for i in range(island_num-1)]
total = 0


cnt = 0
while edges:
    cost, a, b = heapq.heappop(edges)

    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        cnt += 1
        total += cost

    if cnt == island_num-2:
        break

# ! 한번 더 find_parent를 돌려줘야함
# for i in range(island_num-1):
#     find_parent(parent, i)

# print(parent)

if cnt == island_num-2:
    print(total)
else:
    print(-1)
