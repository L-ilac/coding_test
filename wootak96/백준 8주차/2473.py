import sys
INF=sys.maxsize
n=int(input())
solution = list(map(int,input().split()))
solution.sort()
ans_li=[0,0,0]
ans=INF
for i in range(n-2):
    left=i+1 # 기준점 i보다 작은건 검사 안해도 되는 이유 : 이미 전부터 검사함 중복검사임
    right=n-1
    
    while left<right:
        temp_sum=solution[left]+solution[right]+solution[i]

        if temp_sum==0:
            ans_li=[solution[i],solution[left],solution[right]]
            ans_li.sort()
            print(*ans_li)
            exit()

        elif temp_sum>0:    
            if ans>abs(temp_sum):
                ans=abs(temp_sum)
                ans_li=[solution[i],solution[left],solution[right]]
                
            right-=1
        
        else:
            if ans>abs(temp_sum):
                ans=abs(temp_sum)
                ans_li=[solution[i],solution[left],solution[right]]
            left+=1

ans_li.sort()
print(*ans_li)
