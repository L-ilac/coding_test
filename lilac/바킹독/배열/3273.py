n = int(input())

nums = list(map(int, input().split()))

x = int(input())

# ! brute-force 불가

nums.sort()

left = 0
right = n - 1

answer = 0

while left < right:
    tmp = nums[left] + nums[right]

    if tmp == x:
        answer += 1
        left += 1
    elif tmp > x:
        right -= 1
    else:
        left += 1

print(answer)


# ! 투포인터 말고 다른 풀이 방법이 있나?