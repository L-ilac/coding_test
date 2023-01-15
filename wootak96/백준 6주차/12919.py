import sys
import copy
s=list(sys.stdin.readline().rstrip())
t=list(sys.stdin.readline().rstrip())

# 좋다1처럼 경우의 수가 하나로 정해진 문제가 아니라서 두 경우 모두 고려해야함

def cal(x):
    global s
    if len(s)==len(x):
        if s==x:
            print(1)
            exit()
        return
    x2=copy.deepcopy(x)
    
    # 카피본인 x2 만들어서 x와 x2에 각각 다른 경우의 수 진행
    if x[-1]=="A":
        x.pop()
        cal(x)
        
    if x2[0]=="B":
        x2=x2[::-1]
        x2.pop()
        cal(x2)
    

cal(t)
print(0)
