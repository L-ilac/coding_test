n,m = map(int,input().split())
maze = []

for _ in range(n):
	maze.append([int(i) for i in input()])

start = (0,0)
goal = (n-1,m-1)
move_count = 0
dx = [-1,1,0,0]
dy = [0,0,-1,1]


def dfs(x,y):
	stack =[]

	stack.append((x-1,y-1))
	
	while stack:
		tmp = stack.pop()
		candidate = []

		for i in range(4):
			candidate.append((tmp[0]+dx[i],tmp[1]+dy[i]))

		for point in candidate:
			if point[0] <= -1 or point[0] >= n or point[1] <= -1 or point[1] >= m:
				candidiate.remove(point) # 미로 범위 벗어남
			if maze[point[0]][point[1]] == 0: # 괴물이 있는 곳은 못감. 움직임 X
				candidiate.remove(point)

			







def dfs_based_maze_Solve(x,y):
	global move_count
	print(move_count)
	print(x,y)
	if x <= -1 or x >= n or y <= -1 or y >= m: # 미로 범위 벗어남
		return False
	elif maze[x][y] == 0: # 괴물이 있는 곳은 못감. 움직임 X
		return False
	elif x == goal[0] and y == goal[1]: # 최종 목적지일 경우. 움직임 +1
		move_count += 1
		return True
	else:
		move_count += 1
		if dfs_based_maze_Solve(x+1,y) == True:
			print(move_count)
			exit()
		if dfs_based_maze_Solve(x,y+1) == True:
			print(move_count)
			exit()
		if dfs_based_maze_Solve(x-1,y) == True:
			print(move_count)
			exit()
		if dfs_based_maze_Solve(x,y-1) == True:
			print(move_count)
			exit()
	
	return False

# 우선순위는 오른쪽, 아래, 왼쪽, 위 순서
if dfs_based_maze_Solve(start[0],start[1]) == False:
		print("미로를 탈출할 수 있는 길이 없습니다.")
		
# comment. 우선순위를 통해 오른쪽 아래를 향해 가긴하지만, 이게 항상 best case를 보장하는지는 잘 모르겠음. 약간 greedy한 방법임. 위로 돌아가는 경우에는 해결할 수 없음.

"""
ex)
10111
11101
00001
00001
00001

# 반복 좌표
0 2
1 2
2 2
1 3
0 2
"""

재귀가 아닌 직접 스택을 이용하여 구현하면 가능할 듯. 주말이나 내일 하자