n = int(input())

board = []  # * board[i][j] -> i에서 j로 가는데 드는 비용

for _ in range(n):
    tmp = list(map(int, input().split()))
    board.append(tmp)

# 못풀었음
