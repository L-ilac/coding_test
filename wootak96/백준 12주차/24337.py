n,a,b=map(int,input().split())


if a+b>n+1:
    print(-1)
    exit()

if a!=1 and b!=1:
    if a>=b:
        a_building=[i for i in range(1,a+1)]
        b_building=[i for i in range(b-1,0,-1)]
        temp=[1 for i in range(n-(a+b)+1)]
        building=temp+a_building+b_building
        print(*building)
        
    elif a<b:
        b_building=[i for i in range(b,0,-1)]
        a_building = [i for i in range(1,a)]
        temp=[1 for i in range(n-(a+b)+1)]
        building=temp+a_building+b_building
        print(*building)
       
else:
    # b==1, a>b
    if a>=b:
        a_building=[i for i in range(1,a+1)]
        temp=[1 for i in range(n-(a+b)+1)]
        building=temp+a_building
        print(*building)
    
    # a==1, b>a
    elif b>a:
        b_building=[i for i in range(b-1,0,-1)]
        temp=[1 for i in range(n-(a+b)+1)]
        building=[b]+temp+b_building
        print(*building)
