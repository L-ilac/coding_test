n=int(input())

chess_map=[]
black=[]
white=[]
color=[[0]*n for _ in range(n)]

for i in range(n):
    for j in range(n):
        # 검은칸은 True,흰칸은 False
        color[i][j]=(i % 2 == 0 and j % 2 == 0) or (i % 2 != 0 and j % 2 != 0)


for i in range(n):
    chess_map.append(list(map(int, input().split())))
    for j in range(n):
        # 비숍을 놓을 수 있는 칸이고 검은칸이면
        if chess_map[i][j]==1 and color[i][j]==True:
            black.append((i,j))
        # 비숍을 놓을 수 있는 칸이고 흰칸이면
        if chess_map[i][j]==1 and color[i][j]==False:
            white.append((i,j))

Black_cnt,White_cnt=0,0


isused01=[0]*(n*2-1) # 우상향 대각선 /
isused02=[0]*(n*2-1) # 좌상향 대각선 \

def check(bishop,index,count): # black,0,0    white,0,0
    global Black_cnt, White_cnt
    if index==len(bishop): # 모두 검사했으면 이제 최대값 확인
        rx,ry=bishop[index-1]
        # 검은칸이면 Black_cnt 최대값 
        if color[rx][ry]:
            Black_cnt=max(Black_cnt,count) # 다른 경우의 bcnt와 비교해서 최대값 갱신
        # 흰칸이면 White_cnt 최대값
        else:
            White_cnt=max(White_cnt,count) # 다른 경우의 wcnt와 비교해서 최대값 갱신
        return
    
    # black [(0, 0), (0, 4), (1, 1), (2, 0), (2, 2), (2, 4), (4, 0), (4, 2), (4, 4)]     
    # white [(0, 1), (0, 3), (3, 0), (4, 3)]
    x,y=bishop[index]
    if isused01[x+y] or isused02[x-y]: # 우상향 대각선이나 좌상향 대각선에 숫자가 있으면 다음으로 넘어감
        check(bishop,index+1,count)
    
    else: # 우상향 대각선, 좌상향 대각선에 숫자가 없는 경우
        
        # 지금 자리에 비숍을 놓는 경우
        isused01[x+y]=1
        isused02[x-y]=1
        check(bishop,index+1,count+1)
        # 안놓는 경우
        isused01[x+y]=0
        isused02[x-y]=0
        check(bishop,index+1,count)

if len(black)>0:
    check(black,0,0)
if len(white)>0:
    check(white,0,0)
print(Black_cnt+White_cnt)
