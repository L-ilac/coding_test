from collections import deque

n,m = map(int, input().split())

mold = []

for _ in range(n):
	mold.append([int(i) for i in input()])
	#mold.append(list(map(int,input)()))

count = 0
print(mold)

def bfs(xpos, ypos):
	queue = deque() # 1. 덱 생성

	if mold[xpos][ypos] == 0: # 2.입력된 점이 0인지 판단 (방문했는지)
		mold[xpos][ypos] = 1 # 방문 처리 
		
		#bfs routine
		#방문 안한 지점을 기준으로 bfs로 나머지 연결된 부분까지 싹다 방문처리 
		queue.append((xpos,ypos)) # 맨 처음 좌표 넣고

		while queue: # 큐가 빌 때까지
			tmp = queue.popleft() #  제일 앞에 꺼 빼서

			tmp_list = [] 
		
			# 앞의 점에 연결된 점 모두 임시 리스트에 넣기
			tmp_list.append((tmp[0]+1,tmp[1]))
			tmp_list.append((tmp[0]-1,tmp[1]))
			tmp_list.append((tmp[0],tmp[1]+1))
			tmp_list.append((tmp[0],tmp[1]-1))

			# 임시로 넣은 점들이 넣을 필요 없으면 안넣음.
			# 안넣는 조건은, 1. 범위를 벗어나는 점이거나, 이미 방문했거나.
			for p in tmp_list:
				if p[0] <= -1 or p[0] >= n or p[1] <= -1 or p[1] >= m:
					continue # 범위 벗어나는 점

				if mold[p[0]][p[1]] == 1 :
					continue # 이미 방문 or 애초에 막혀있는 칸
				
				#위에 두개 조건문에 의해서 안 걸러지면, 넣고 방문처리
				mold[p[0]][p[1]] = 1
				queue.append((p[0],p[1]))

			tmp_list.clear()

		return True

	return False # 방문 안했다면 함수 탈출

for i in range(n):
	for j in range(m):
		if bfs(i,j) == True:
			count += 1
		
print(count)