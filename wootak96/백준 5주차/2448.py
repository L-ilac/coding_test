n=int(input())

# k : 가로 길이, n : 세로 길이
k=2*n-1 

graph=[[" " for _ in range(k)] for _ in range(n)]

# 최소단위인 3이 되면 그리고, 이외에는 재귀 실행
def draw(n,x,y):
    if n==3:
      # 삼각형의 꼭짓점이 그림 그리는 시작하는 시작점
        graph[x][y]="*"
        graph[x+1][y-1]="*"
        graph[x+1][y+1]="*"
        for j in range(5):
            graph[x+2][y-2+j]="*"

    else:
        # 삼각형의 꼭짓점이 재귀 시작하는 시작점
        nx=[x,x+n//2,x+n//2]                  
        ny=[y,y-(n//2),y+(n//2)]            
        
        for z in range(3):
            draw(n//2,nx[z],ny[z])

draw(n,0,k//2) 
for i in graph:
    print(''.join(map(str,i)))
