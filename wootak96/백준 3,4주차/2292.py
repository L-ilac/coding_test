n=int(input())

if n==1:
    print(1)
else:
    count=2
    num1=2
    num2=7
    while True:
        if n>=num1 and n<=num2:
            print(count)
            break
        else:
            num1=num1+6*(count-1)
            num2=num2+6*count
            count += 1
