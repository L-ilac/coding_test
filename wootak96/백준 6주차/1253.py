import copy
import sys
n=int(sys.stdin.readline())

num=list(map(int,input().split()))
num.sort()

ans=0
for target in range(n):
    left=0
    right=0
    # target은 포함 안되어야 하므로 카피본 만들어서 타겟 없는 리스트 새로 만듦
    new_num=copy.deepcopy(num)
    new_num.remove(num[target])
    
    left=0
    right=n-2
    while left<right:
        sum_=new_num[left]+new_num[right]

        if sum_==num[target]:
            ans+=1
            break

        elif sum_<num[target]:
            left+=1

        else:
            right-=1
print(ans)
