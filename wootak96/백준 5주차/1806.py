n,s=map(int,input().split())
a = list(map(int,input().split()))

left=right=0
sum=a[0]
ans=n+1
while left<=right and right<n:
    if sum<s:
        right += 1
        if right < n:
            sum += a[right]
    elif sum == s:
        ans = min(right-left+1,ans)
        right += 1
        if right < n:
            sum += a[right]
    elif sum > s:
        ans = min(right-left+1,ans)
        sum -= a[left]
        left += 1
        if left > right and left < n:
            right=left
            sum = a[left]
if ans > n:
    ans=0
print(ans)
