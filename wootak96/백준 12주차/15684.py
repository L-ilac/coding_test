import sys

n,m,h=map(int,input().split())

ladder=[[False for _ in range(n)] for _ in range(h)]

for _ in range(m):
    a,b=map(int,sys.stdin.readline().split())
    ladder[a-1][b-1]=True

# 사다리를 검사하는 함수
def check():
    for start in range(n):
        k=start
        for i in range(h):
            if ladder[i][k]: # 오른쪽으로 이동하는 경우
                k+=1
            elif k>0 and ladder[i][k-1]: # 왼쪽으로 이동하는 경우
                k-=1
        if start != k: # 첫스타트 지점이랑 도착지점이 다르면
            return False
    return True
   

# 사다리를 추가로 놓을 수 있는 지점들 저장
can=[]
for i in range(h):
    for j in range(n-1):
        if ladder[i][j]==False:
            can.append([i,j])

            
g=len(can)
ans=sys.maxsize


def cal(cnt,index):
    global ans
     
    # 사다리 검사해서 도착조건 만족하면 ans값 갱신
    if check():
        if cnt<=3:
            ans=min(ans,cnt)
            return
        
    if cnt>=3:
        return

    if index>g-1:
        return
    
    i,j=can[index]

    if n==2:
        ladder[i][j]=True
        cal(cnt+1,index+1)
        ladder[i][j]=False
        cal(cnt,index+1)

    elif n==3:
        if j==0:
            if ladder[i][j+1]==False:
                ladder[i][j]=True
                cal(cnt+1,index+1)
                ladder[i][j]=False
                cal(cnt,index+1)
            else:
                cal(cnt,index+1)

        elif j==1:
            if ladder[i][j-1]==False:
                ladder[i][j]=True
                cal(cnt+1,index+1)
                ladder[i][j]=False
                cal(cnt,index+1)
            else:
                cal(cnt,index+1)
    
    else:
        if j==0:
            if ladder[i][j+1]==False:
                ladder[i][j]=True
                cal(cnt+1,index+1)
                ladder[i][j]=False
                cal(cnt,index+1)
            else:
                cal(cnt,index+1)

        elif j==n-2:
            if ladder[i][j-1]==False:
                ladder[i][j]=True
                cal(cnt+1,index+1)
                ladder[i][j]=False
                cal(cnt,index+1)
            else:
                cal(cnt,index+1)

        else:
            if ladder[i][j-1]==False and ladder[i][j+1]==False:
                ladder[i][j]=True
                cal(cnt+1,index+1)
                ladder[i][j]=False
                cal(cnt,index+1)
            else:
                cal(cnt,index+1)

if m==0:
    print(0)
    exit()

cal(0,0)
if ans<=3:
    print(ans)
else:
    print(-1)
