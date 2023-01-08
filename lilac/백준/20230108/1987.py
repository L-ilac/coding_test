# 좌측 상단에서 시작해서, 말이 최대한 몇 칸을 지날 수 있는지를 구하는 프로그램을 작성
# 이동하는 경로에 중복적인 알파벳이 들어갈 수 없음
import sys
r, c = map(int, input().split())
# ! sys.setrecursionlimit(10000) 없어도 맞음
board = []

# ! visited를 배열로 쓰지않고, 다른 자료형을 사용하면 시간초과남
visited = [False] * 26  # 이미 방문한 알파벳을 담을 리스트
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(r):
    board.append(list(input()))

max_steps = 1

# ! dfs는 pypy로 만 통과함.


def dfs(x, y, steps):
    global max_steps
    max_steps = max(max_steps, steps)

    for dx, dy in d:
        new_x, new_y = x+dx, y+dy
        if 0 <= new_x <= r-1 and 0 <= new_y <= c-1:
            if not visited[ord(board[new_x][new_y]) - ord('A')]:
                visited[ord(board[new_x][new_y]) - ord('A')] = True
                dfs(new_x, new_y, steps+1)
                # ! 백트래킹을 위한 코드
                visited[ord(board[new_x][new_y]) - ord('A')] = False


start_x, start_y = 0, 0

visited[ord(board[start_x][start_y])-ord('A')] = True
dfs(start_x, start_y, 1)

print(max_steps)

#! sol2 bfs

r, c = map(int, input().split())
q = set()
board = []
d = [(0, 1), (0, -1), (1, 0), (-1, 0)]

for _ in range(r):
    board.append(list(input()))

q.add((0, 0, board[0][0]))


answer = 1
while q:
    now_x, now_y, route = q.pop()
    answer = max(answer, len(route))

    for dx, dy in d:
        new_x, new_y = now_x + dx, now_y + dy
        if 0 <= new_x <= r-1 and 0 <= new_y <= c-1:
            if board[new_x][new_y] not in route:
                q.add((new_x, new_y, route+board[new_x][new_y]))


print(answer)

'''
bfs를 그냥 queue로 짰을때, 시간초과가 나는 이유는 동일한 알파벳구성을 가진 경로가 여러개일 수 있기 때문이다.
set을 이용해서 (x좌표, y좌표, 지나온경로) 의 형태로 중복을 점검하기 때문에 여러개의 경로가 하나로 통합되는 경우가 있다.
ex. a(0,0)->b(0,1)->c(1,1) / a(0,0)->b(1,0)->c(1,1) 은 서로 다른 경로지만, (1,1,abc)에 의해 합쳐진다.
즉, 여러개의 경로가 합쳐진 이후에는 합쳐진 지점으로부터의 탐색만 하면 되므로, 중복된 탐색을 막을 수 있다.

abcd

bcde

cdef

defg

'''

# ! bfs와 dfs의 수행시간이 차이가 3배정도 나는데, 그 이유 또한 위에 bfs는 중복적인 탐색을 하지 않는데, dfs는 그냥 전부 다 탐색하기 떄문
