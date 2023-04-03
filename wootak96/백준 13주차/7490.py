import copy

k=int(input())
for _ in range(k):
    n=int(input())
    arr=[]

    for i in range(1,2*n):
        if i%2==1:
            arr.append(i//2+1)
        else:
            arr.append(0)

    temp=[]        
    li=len(arr)
    def cal(index):
        if index>=li-1:
            x=copy.deepcopy(arr)
        
            temp.append(x)
            return 
        
        arr[index]=" "
        cal(index+2)
        arr[index]="+"
        cal(index+2)
        arr[index]="-"
        cal(index+2)


    cal(1)

    for arr in temp:    
        x=copy.deepcopy(arr)
        cnt=0
        for i in range(li-2,0,-2):
            if arr[i]==" ":
                cnt+=1
                arr[i]="+"
                arr[i-1]=(10**cnt)*arr[i-1]+arr[i+1]
                arr[i+1]=0
            else:
                cnt=0
    
        for i in range(1,li,2):
            if arr[i]=="+":
                arr[i+1]=arr[i-1]+arr[i+1]
            elif arr[i]=="-":
                arr[i+1]=arr[i-1]-arr[i+1]
        

        if arr[-1]==0:
            print("".join(map(str,x)))
    print()
