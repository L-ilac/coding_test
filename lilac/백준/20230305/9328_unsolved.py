from collections import deque, defaultdict


def bfs(start_points, keys):
    d = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    q = deque()

    visited = [[False] * w for _ in range(h)]

    for x, y in start_points:
        q.append((x, y))
        visited[x][y] = True

    left_doors = defaultdict(set)  # ? 'A' : [문의 좌표]
    # stolen_docs = set()
    stolen_docs = 0

    # print(h, w)
    # print(start_points)
    # print(keys)

    while q:
        now_x, now_y = q.popleft()
        # print(now_x, now_y)

        for dx, dy in d:
            new_x, new_y = now_x+dx, now_y+dy

            if 0 <= new_x <= h-1 and 0 <= new_y <= w-1:
                if not visited[new_x][new_y] and board[new_x][new_y] != '*':

                    # ! 빈 공간이라면 그냥 갈수 있음
                    if board[new_x][new_y] == '.':
                        visited[new_x][new_y] = True
                        q.append((new_x, new_y))

                    # ! 훔칠 수 있는 문서라면 문서의 좌표를 저장
                    elif board[new_x][new_y] == '$':
                        # stolen_docs.add((new_x, new_y))
                        stolen_docs += 1
                        visited[new_x][new_y] = True
                        q.append((new_x, new_y))

                    # ! 문 또는 키를 만났을 때
                    elif board[new_x][new_y].isalpha():
                        # ! 문을 만났을 경우, 현재 있는 키로 열 수 있는지 판단한다. 못 열면, 남은 문에 추가
                        if board[new_x][new_y].isupper():
                            if board[new_x][new_y].lower() in keys:
                                visited[new_x][new_y] == True
                                q.append((new_x, new_y))
                            else:
                                # ! 방문하지 않은 문은 1번만 방문되어야함
                                left_doors[board[new_x][new_y]].add(
                                    (new_x, new_y))
                                visited[new_x][new_y] = True

                        # ! 키를 만났을 경우, 보유한 키에 추가하고, 추가된 키로 열 수 있는 문이 있는지 찾는다.
                        else:
                            keys.add(board[new_x][new_y])
                            visited[new_x][new_y] = True
                            q.append((new_x, new_y))

                            if left_doors[board[new_x][new_y].upper()]:
                                for x, y in left_doors[board[new_x][new_y].upper()]:
                                    q.append((x, y))
                                del left_doors[board[new_x][new_y].upper()]

    return stolen_docs


test_num = int(input())
for _ in range(test_num):
    h, w = map(int, input().split())

    start_point = []
    board = []
    for i in range(h):
        tmp = list(input())
        board.append(tmp)

    for i in range(h):
        if board[i][0] == '.':
            start_point.append((i, 0))

        if board[i][-1] == '.':
            start_point.append((i, w-1))

    for j in range(w):
        if board[0][j] == '.':
            start_point.append((0, j))

        if board[-1][j] == '.':
            start_point.append((h-1, j))

    tmp_key = input()

    keys = set()
    if tmp_key != '0':
        keys = set(list(tmp_key))

    ans = bfs(start_point, keys)

    print(ans)
