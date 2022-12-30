from collections import deque
n = int(input())  # 보드 크기 n*n
k = int(input())  # 사과 갯수

apples = []

for _ in range(k):
    apple_x, apple_y = map(int, input().split())
    apples.append((apple_x, apple_y))

l = int(input())

moves = []
for _ in range(l):
    x, c = input().split()
    moves.append((x, c))

moves = deque(moves)

# deque[0] -> 꼬리 , deque[-1] -> 머리
snake = [deque(), 1]  # 뱀을 이루는 점좌표들, 바라보는 방향(맨처음에는 동쪽)
snake[0].append((1, 1))

direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서 -> +1: 오른쪽 90, -1: 왼쪽 90

time = 0
while True:
    # 현재 뱀의 머리 위치
    now_x, now_y = snake[0][-1][0], snake[0][-1][1]
    # 뱀의 머리가 다음으로 움직여야할 위치
    new_x, new_y = now_x+direction[snake[1]][0], now_y + direction[snake[1]][1]

    # 보드를 벗어나지 않으면서, 자기 몸에 부딪히지 않을 경우
    if 1 <= new_x <= n and 1 <= new_y <= n and (new_x, new_y) not in snake[0]:
        # 새로운 곳으로 머리를 위치 시킴
        snake[0].append((new_x, new_y))
        print(new_x, new_y)

        # 이동한 칸에 사과가 있다면,
        if (new_x, new_y) in apples:
            # 사과는 없어지고, 꼬리는 움직이지 않음
            apples.remove((new_x, new_y))
        # 이동한 칸에 사과가 없다면,
        else:
            # 꼬리를 줄인다.
            snake[0].popleft()
    # 보드를 벗어났거나, 자기 몸에 부딪히는 경우
    else:
        time += 1
        print(time)
        break
    # 움직임이 끝나고 난후에 시간증가

    time += 1

    # 방향을 바꾸는 동작이 있다면?
    if moves and int(moves[0][0]) == time:
        x, c = moves.popleft()

        if c == 'L':
            snake[1] -= 1
            snake[1] %= 4
        else:
            snake[1] += 1
            snake[1] %= 4
