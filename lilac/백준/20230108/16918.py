# 규칙성을 찾아내거나, 주어진 횟수만큼 시뮬레이션을 돌린값을 내거나

import copy

# ! 규칙성을 찾아내서 반복되는 결과만 찾아서 반환할 경우
r, c, n = map(int, input().split())

board = []
bombs = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(r):
    data = list(input())
    board.append(data)
    for j in range(c):
        if data[j] == 'O':
            bombs.append((i, j))

# 초기 상태의 폭탄이 터진 상태
board2 = [['O']*c for _ in range(r)]
for b_x, b_y in bombs:
    board2[b_x][b_y] = '.'
    for dx, dy in d:
        new_x, new_y = b_x + dx, b_y + dy
        if 0 <= new_x <= r-1 and 0 <= new_y <= c-1:
            board2[new_x][new_y] = '.'

bombs2 = []
for i in range(r):
    for j in range(c):
        if board2[i][j] == 'O':
            bombs2.append((i, j))

board3 = [['O']*c for _ in range(r)]
for b_x, b_y in bombs2:
    board3[b_x][b_y] = '.'
    for dx, dy in d:
        new_x, new_y = b_x + dx, b_y + dy
        if 0 <= new_x <= r-1 and 0 <= new_y <= c-1:
            board3[new_x][new_y] = '.'


answer = board

if n == 1:
    answer = board
elif n % 2 == 0:
    answer = [['O'] * c for _ in range(r)]
elif n % 4 == 1:
    answer = board3
elif n % 4 == 3:
    answer = board2

for i in answer:
    print("".join(i))

# ! 그냥 n까지 시뮬레이션 돌리는 경우(sol2)
r, c, n = map(int, input().split())

board = []
full_board = [['O']*c for _ in range(r)]
bombs = []
d = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for i in range(r):
    board.append(list(input()))

answer = None

if n == 1:
    answer = board
else:
    if n % 2 == 0:
        answer = full_board
    else:
        for _ in range(3, n+1, 2):
            tmp = copy.deepcopy(full_board)
            # 현재 보드에 설치되어 있는 폭탄을 전부 터뜨린다.
            for i in range(r):
                for j in range(c):
                    if board[i][j] == 'O':
                        tmp[i][j] = '.'
                        for dx, dy in d:
                            new_x, new_y = i+dx, j+dy
                            if 0 <= new_x <= r-1 and 0 <= new_y <= c-1:
                                tmp[new_x][new_y] = '.'
            board = copy.deepcopy(tmp)

        answer = board

for i in answer:
    print("".join(i))
