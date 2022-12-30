import sys
n = int(input())

moves = sys.stdin.readline().rstrip().split()
print(moves)

direction = {'U': (-1, 0),
             'D': (1, 0),
             'R': (0, 1),
             'L': (0, -1)}  # 상하좌우 UDLR

xpos, ypos = 1, 1

for m in moves:
    new_x, new_y = xpos + direction[m][0], ypos + direction[m][1]

    if 0 < new_x < n+1 and 0 < new_y < n+1:
        xpos = new_x
        ypos = new_y

print(xpos, ypos)
