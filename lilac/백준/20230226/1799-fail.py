import copy


board_size = int(input())

board = []

for _ in range(board_size):
    board.append(list(map(int, input().split())))

d = [(1, 1), (1, -1), (-1, 1), (-1, -1)]  # ! 대각선 4방향

# ! 비숍의 위치를 기준으로 대각선 방향의 모든 값을

# ! 체스보드의 모든 칸이 0인지 판단


def board_allzero():
    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 1:
                return False

    return True


def set_bishop(x, y):
    d = [(1, 1), (1, -1), (-1, 1), (-1, -1)]
    board[x][y] = 0

    changed = []
    changed.append((x, y))

    for dx, dy in d:

        new_x, new_y = x+dx, y+dy

        while 0 <= new_x <= board_size-1 and 0 <= new_y <= board_size-1:
            if board[new_x][new_y] != 0:
                board[new_x][new_y] = 0
                changed.append((new_x, new_y))

            new_x += dx
            new_y += dy
    return changed


answer = 0


def solve(bishop_cnt):
    global answer

    if board_allzero():
        answer = max(answer, bishop_cnt)
        return

    for i in range(board_size):
        for j in range(board_size):
            if board[i][j] == 1:
                changed = set_bishop(i, j)
                solve(bishop_cnt+1)

                for x, y in changed:
                    board[x][y] = 1


solve(0)
print(answer)

# ! 완전 탐색을 통한 백트래킹으로 풀면 시간 초과
