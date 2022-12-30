# 먹을 수 있는 물고기가 1마리라면, 그 물고기를 먹으러간다.
# 먹을 수 있는 물고기가 1마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러간다. -> 거리가 가까운 물고기가 여러개라면, 가장 위에 있는 물고기(1) , 가장 왼쪽에 있는 물고기 (2)

# 접근법
# 1. 아기상어의 현위치를 기준으로 먹을수 있는 물고기를 모두 찾는다
# 2. 찾은 먹을 수 있는 물고기를, (거리, y좌표, x좌표) 순서 기준으로 정렬한다.
# 3. 정렬한 물고기들중 제일 우선순위가 높은 물고기를 먹고, 그 물고기가 있던 위치에서 다시 1~3을 반복한다.
# 3-1. 1~3번을 반복할 때마다, 아기상어가 움직인 거리를 최종답안에 더해준다.
# 3-2. 아기상어의 사이즈가 커질 수 있기 때문에, 물고기를 1마리 먹을 때마다, 아기상어의 크기가 커지지 않는지 체크한다.

# 사실 1번에서 현위치를 기준으로 먹을수 있는 물고기를 모두 찾으면 말 그대로 맵안의 모든 물고기를 찾기 때문에, 내가 접근했던 방법은 최초로 먹을 수 있는 물고기를 찾으면 그 물고기와 같은 거리값을 가진 위치만 조사하면 될거라고 생각했다. 왜냐하면, bfs를 이용해 탐색하기때문에, 아기상어는 본인의 시작 위치 기준으로 떨어진 거리 순서대로 맵을 탐색할 것이고, 따라서 탐색도중 먹을 수 있는 물고기를 찾았다는건, 그 물고기가 처음으로 찾은 먹을 수 있는 물고기라는 것이기 때문이다. 하지만, 처음으로 찾은 물고기와 같은 거리만큼 떨어져있는 다른 물고기가 존재할 수 있기때문에, 적어도 같은 거리에 있는 모든 노드에 대해서는 먹을 수 있는 물고기가 존재하는지 조사해야하고, 먹을 수 있는 물고기가 여러마리라면, 우선순위 기준(더 위에, 더 왼쪽에)을 적용해서 먹을 물고기를 정해야한다.

# 또한, 기존의 bfs와는 한번 지나갔던 경로를 다시 지나갈 수도 있으므로, 물고기를 먹는 시점에, 방문해서 true 처리 해주었던 위치를 모두 다시 false로 바꿔주고, 대신 물고기를 먹은 위치의 값을 물고기가 없다는 의미를 가진 0으로 바꿔줘야한다.


import sys
import heapq
from collections import deque, defaultdict

# 맵 사이즈  n * n
n = int(sys.stdin.readline())

answer = 0
graph = []
visited = [[False] * n for _ in range(n)]
direction = [(0, -1), (-1, 0), (0, 1),  (1, 0)]
start = None
fish_dict = defaultdict(int)

candidate_fish = []


# map setting
for _ in range(n):
    graph.append(list(map(int, sys.stdin.readline().split())))


# 먹을 수 있는 물고기가 존재하는가?
def edible_fish_num(shark_size):
    cnt = 0
    for fish_size, num in fish_dict.items():
        if fish_size < shark_size:
            cnt += num

    return cnt


# map setting
for i in range(n):
    for j in range(n):
        if graph[j][i] == 9:
            start = (i, j)
        else:
            if graph[j][i] > 0:
                fish_dict[graph[j][i]] += 1


# 초기 상어 사이즈
shk_size = 2

# 현재까지 먹은 물고기 수 카운트
eaten_fish = 0

q = deque()

# 출발점에는 아무 물고기도 없으므로 0 처리
graph[start[1]][start[0]] = 0

# 새로운 물고기를 찾아서 먹을 때까지는 출발점으로 돌아올 이유가 없음
visited[start[1]][start[0]] = True


# 큐에 넣을때 (이동거리, x좌표, y좌표) 순으로 넣어야 가까운 거리, 가장위, 가장 왼쪽 순으로 위치가 나열됌.
q.append((0, start[0], start[1]))


while q and edible_fish_num(shk_size) > 0:
    now_moves, now_x, now_y = q.popleft()  # 현재 방문하는 지점

    for dx, dy in direction:
        new_x, new_y = now_x + dx, now_y + dy  # 새롭게 탑색하고자 하는 노드

        # 최소한의 조건
        if -1 < new_x < n and -1 < new_y < n and not visited[new_y][new_x]:

            if graph[new_y][new_x] == 0:  # 물고기가 없는 빈 공간일 때
                visited[new_y][new_x] = True
                q.append((now_moves + 1, new_x, new_y))
            else:  # 물고기가 있을 때
                # 먹을 수 없는 물고기 일 때 (지나가지도 못함)
                if graph[new_y][new_x] > shk_size:
                    continue
                elif graph[new_y][new_x] == shk_size:  # 상어와 물고기가 같으면 먹지는 못하지만 지나갈 수는 있음
                    visited[new_y][new_x] = True
                    q.append((now_moves + 1, new_x, new_y))

                # TODO
                else:  # 먹을 수 있는 물고기 일 때, 같은 거리에 다른 물고기가 있는지 모두 찾아야함. 즉, 이 물고기가 먹을 수있는 가장 가까운 물고기에 적합한지 판단해야함
                    q.appendleft((now_moves, now_x, now_y))

                    #heapq.heappush(candidate_fish, (now_moves+1, new_y, new_x))

                    # 우선순위인 물고기를 골라내기 위한 heap
                    while q:
                        tmp_moves, tmp_x, tmp_y = q.popleft()

                        if tmp_moves != now_moves:
                            continue

                        for dx, dy in direction:
                            tmp_new_x, tmp_new_y = tmp_x + dx, tmp_y + dy

                            if -1 < tmp_new_x < n and -1 < tmp_new_y < n and not visited[tmp_new_y][tmp_new_x]:
                                if 0 < graph[tmp_new_y][tmp_new_x] < shk_size:  # 먹을 수 있는 물고기라면

                                    heapq.heappush(
                                        candidate_fish, (tmp_moves+1, tmp_new_y, tmp_new_x))

                    chosen_moves, chosen_y, chosen_x = heapq.heappop(
                        candidate_fish)  # 제일 우선순위 높은 자식
                    candidate_fish.clear()

                    print(chosen_x, chosen_y)

                    # 물고기 먹으면, 지금까지 온 길 모두 초기화(되돌아갈수도 있으니까)
                    del visited
                    visited = [[False] * n for _ in range(n)]

                    # 새로운 시작점
                    visited[chosen_y][chosen_x] = True
                    q.append((chosen_moves, chosen_x, chosen_y))

                    # 먹은 물고기수 +1
                    eaten_fish += 1

                    # 상어가 물고기를 자기 크기만큼 먹으면 +1
                    if eaten_fish == shk_size:
                        shk_size += 1
                        eaten_fish = 0

                    # 먹은 물고기 갯수 차감
                    fish_dict[graph[chosen_y][chosen_x]] -= 1
                    # 물고기를 먹으면 그 위치를 아무것도 없는 공간을 바꿔준다.
                    graph[chosen_y][chosen_x] = 0

                    answer = chosen_moves
                    break

print(answer)
