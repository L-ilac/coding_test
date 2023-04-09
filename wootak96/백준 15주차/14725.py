n=int(input())

li=[]

for _ in range(n):
    s,*a=map(str,input().split())
    li.append(a)

li.sort()

for i in range(n):
    if i==0:
        for j in range(len(li[i])):
            print("--"*j + li[i][j])
    else:
        x=min(len(li[i]),len(li[i-1]))
        count=0
        for j in range(x):
            if li[i][j]==li[i-1][j]:
                count+=1
            else:
                break

        for j in range(count,len(li[i])):
            print("--"*j + li[i][j])
