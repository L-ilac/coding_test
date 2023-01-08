
# ! 그려야하는 제일 작은 단위의 도형을 찾는다.
# ! 작은 단위의 도형이 어떻게 반복되는지 규칙성을 찾는다.
# ! 가장 작은 도형을 그리기 시작해야하는 시작점을 기준으로 잡고, 그 해당 점까지 재귀적으로 탐색한다.
n = int(input())
board = [[' '] * ((2*n)-1) for _ in range(n)]  # 주어진 입력값에 맞는 보드


def star(n, x, y):
    if n == 3:
        board[x][y] = '*'
        board[x+1][y-1] = '*'
        board[x+1][y+1] = '*'
        for i in range(y-2, y+3):
            board[x+2][i] = '*'

        return

    star(n//2, x, y)
    star(n//2, x+n//2, y-n//2)
    star(n//2, x+n//2, y+n//2)


star(n, 0, n-1)

for i in board:
    print("".join(i))


# ! 기발한 답

def transform(base):
    p = len(base)  # * p 만큼의 공백이 더해져야하는가?
    t = []
    for i in base:
        t.append(' ' * p + i + ' ' * p)
    for i in base:
        t.append(i + ' ' + i)
    return t


base = ['  *  ', ' * * ', '*****']
N = int(input())
while len(base) != N:
    base = transform(base)
for i in base:
    print(i)
