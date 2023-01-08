import sys
R, C, N = map(int, sys.stdin.readline().split())
board = [list(input().strip()) for i in range(R)]

if N <= 1: # 1초 이하면
    for x in board: print("".join(x)) # 원래 상태
elif N % 2 == 0 : # 짝수초 이면
    for x in range(R): print("O" * C)  # 모두다 폭탄을 갖고 있는 상태
else:
    board1 = [['O'] * C for i in range(R)] # 기존 그래프랑 비교하기 위한 board
    for x in  range(R):
        for y in range(C):
            if board[x][y] == 'O':  # 폭탄이 있을 때
                board1[x][y] = '.'  # 그자리에, 그와 붙어있는 곳에 .으로 처리
                if x-1 >= 0 : board1[x-1][y] = '.'
                if x+1 < R : board1[x+1][y] = '.'
                if y-1 >= 0: board1[x][y-1] = '.'
                if y+1 < C : board1[x][y+1] = '.'
    
    board2 = [['O'] * C for i in range(R)]
    for x in range(R):
        for y in range(C):
            if board1[x][y] == 'O':
                board2[x][y] = '.'  # 그자리에, 그와 붙어있는 곳에 .으로 처리
                if x-1 >= 0 : board2[x-1][y] = '.'
                if x+1 < R : board2[x+1][y] = '.'
                if y-1 >= 0: board2[x][y-1] = '.'
                if y+1 < C : board2[x][y+1] = '.'

    if N % 4 == 3: 
        for x in board1 : print(''.join(x))
    elif N % 4 == 1:
        for x in board2 : print(''.join(x))





