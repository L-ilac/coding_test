board_size = int(input())

board = []

right_up = [False] * (2*board_size - 1)
right_down = [False] * (2*board_size - 1)

for _ in range(board_size):
    board.append(list(map(int, input().split())))

answer = 0


def solve(i, j, bishop_cnt):
    global answer

    if board_size % 2 == 0:  # 짝수 일때,
        if j == board_size:
            i += 1
            j = 1
        elif j == board_size + 1:
            i += 1
            j = 0
    else:
        if j == board_size:
            i += 1
            j = 0

        elif j == board_size + 1:
            i += 1
            j = 1

    if i == board_size:
        answer = max(answer, bishop_cnt)
        return answer

    if board[i][j] == 1 and not right_up[i+j] and not right_down[j-i+board_size-1]:
        right_up[i+j] = True
        right_down[j-i+board_size-1] = True
        solve(i, j+2, bishop_cnt+1)
        right_up[i+j] = False
        right_down[j-i+board_size-1] = False

    solve(i, j+2, bishop_cnt)


solve(0, 0, 0)
ans1 = answer

answer = 0
solve(0, 1, 0)
ans2 = answer

print(ans1 + ans2)
