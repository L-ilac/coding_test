import sys
sys.setrecursionlimit(10**5)

n,k=map(int,input().split())
mod=1000000007
def fac(n):
    if n==1:
        return 1

    else:
        k=1
        for i in range(1,n+1):
            k = (k*i)%mod

        return k

def square(n,k):
    if k==0:
        return 1
    elif k==1:
        return n
    
    else:
        temp=square(n,k//2)
        if k%2==1:
            return temp*temp*n % mod

        else:
            return  temp*temp % mod


temp1=fac(n)%mod
temp2=fac(n-k)*fac(k)%mod
temp3=square(temp2,mod-2)%mod

print(temp1*temp3%mod)
