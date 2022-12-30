import sys

n=int(input())
solution=list(map(int,input().split()))

left=0
right=n-1
ans_left=0
ans_right=0
_min=sys.maxsize

while left<right:
    _sum=solution[left]+solution[right]
    if _min > abs(_sum):
        _min=abs(_sum)
        ans_left = solution[left]
        ans_right = solution[right]


    if _sum>0:
        right -=1

    elif _sum<0:
        left  +=1
    
    else:
        break
print(ans_left,ans_right)
