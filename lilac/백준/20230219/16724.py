from collections import deque

# ! bfs + union-find
# ! 주어진 지도안에 사이클이 몇개 있는가 찾는 문제


def bfs(start):
    d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    cycle = set()
    start_x, start_y = start

    q = deque()
    q.append((start_x, start_y))

    visited[start_x][start_y] = True

    while q:
        now_x, now_y = q.popleft()
        c = now_x, now_y
        cycle.add(c)

        # print(c)

        dx, dy = d[board[now_x][now_y]]
        new_x, new_y = now_x + dx, now_y + dy
        p = new_x, new_y

        # print(c, p)

        # ! 새롭게 방문하는 노드가 이미 방문한 적 있다면, 그냥 기존 사이클에 합치면 된다.
        if visited[new_x][new_y] and p not in cycle:
            union_parent(parent, c, p)
            return False

        # ! 새롭게 방문하는 노드가 방문한 적 없다면, 기존에 없었던 사이클이라는 뜻

        visited[new_x][new_y] = True
        q.append((new_x, new_y))

        # ! 사이클이 형성되었다면,
        if find_parent(parent, c) == find_parent(parent, p):
            break
        else:
            union_parent(parent, c, p)

    return True

    # ! q에 들어간 모든 원소가 처리되서 나온건지, visited[True] 에 의해 나온건지 분기가 필요함.


n, m = map(int, input().split())

board = []
for i in range(n):
    tmp = list(input())
    board.append(tmp)

# print(board)

parent = [[(i, j) for j in range(m)] for i in range(n)]


def find_parent(parent, p):
    if parent[p[0]][p[1]] != p:
        parent[p[0]][p[1]] = find_parent(parent, parent[p[0]][p[1]])
    return parent[p[0]][p[1]]


def union_parent(parent, c, p):
    c = find_parent(parent, c)
    p = find_parent(parent, p)

    parent[c[0]][c[1]] = p


visited = [[False]*m for _ in range(n)]

cycle = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j]:
            if bfs((i, j)):
                cycle += 1

            # print()

# print(parent)
print(cycle)


# ! 방향이 하나로 고정되어있어서 bfs가 아닌 dfs로 푸는게 더 수월 했을 듯.
