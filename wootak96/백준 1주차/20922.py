n,k=map(int,input().split())
num=list(map(int,input().split()))

left,right=0,0

dic={}
ans=0
while right<n:
   
    if num[right] not in dic.keys():
        dic[num[right]]=1
        right+=1
    else:
       
        if  dic[num[right]]+1 > k:
            dic[num[left]]-=1
            left+=1
        else:
            dic[num[right]]+=1 
            right+=1
            
    ans=max(ans,right-left)

print(ans)
