from collections import deque

n,m = map(int,input().split())

maze = []

for _ in range(n):
	maze.append([int(i) for i in input()])

queue = deque()

start = (0,0)
goal = (n-1,m-1)
success_flag = False
step = 0

x_dir = [-1,1,0,0]
y_dir = [0,0,-1,1]

queue.append(start)

while queue:
	tmp = queue.popleft()
	print(tmp)

	if tmp[0] == goal[0] and tmp[1] == goal[1]:
		print("YOU REACHED TO THE GOAL!")
		print(maze[tmp[0]][tmp[1]])
		success_flag = True
		break

	for i in range(4):
		if tmp[0]+x_dir[i] < 0 or tmp[1]+y_dir[i] < 0 or tmp[0]+x_dir[i] >= n  or tmp[1]+y_dir[i] >= m:
			continue

		if maze[tmp[0]+x_dir[i]][tmp[1]+y_dir[i]] == 0:
			continue

		# 이미 지나친 지점임을 처리하는 로직이 필요함.
		if maze[tmp[0]+x_dir[i]][tmp[1]+y_dir[i]] != 1 or (tmp[0]+x_dir[i],tmp[1]+y_dir[i]) == start:
			continue
		
		maze[tmp[0]+x_dir[i]][tmp[1]+y_dir[i]] = maze[tmp[0]][tmp[1]] +1
		queue.append((tmp[0]+x_dir[i],tmp[1]+y_dir[i]))

if success_flag == False:
	print("No Route for Goal!")

# 예시 답안

n,m = map(int,input().split())

graph = []

for i in range(n):
	graph.append(list(map(int,input())))


dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
	queue = deque()
	queue.append((x,y))

	while queue:
		x,y = queue.popleft()

		for i in range(4):
			nx = x + dx[i]
			ny = y + dy[i]

			if nx < 0 or ny < 0 or nx >= n or ny >= m:
				continue
			
			if graph[nx][ny] == 0:
				continue
			
			# 해당 노드를 처음으로 방문하는 경우에만 최단거리 기록 (시작지점은 검사안함)
			if graph[nx][nx] == 1 and """(nx,ny) != (0,0)""":
				graph[nx][ny] = graph[x][y] + 1
				queue.append((nx,ny))

	return graph[n-1][m-1]


print(bfs(0,0))