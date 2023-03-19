n=int(input())
numbers=list(map(int,input().split()))
numbers.sort()
if numbers[0]!=1:
    print(1)
    exit()
sum_=0
for i in range(n):
    if i==0:
        sum_+=numbers[i]
    else:
        if sum_+2<=numbers[i]:
            print(sum_+1)
            exit()
        else:
            sum_+=numbers[i]

print(sum_+1)
