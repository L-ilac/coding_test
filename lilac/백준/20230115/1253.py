n = int(input())
nums = list(map(int, input().split()))

nums.sort()

cnt = 0
for i in range(len(nums)):
    new_nums = nums[:i] + nums[i+1:]
    target = nums[i]
    left = 0
    right = n-2

    while left < right:
        tmp = new_nums[left] + new_nums[right]

        if tmp == target:
            cnt += 1
            break
        elif tmp < target:
            left += 1
        else:
            right -= 1


# ! 좋은 수를 만드는 두 수의 조합은 여러개일 수 있다. 하지만, 하나만 찾고 해당 타켓에 대한 탐색은 그만해도 상관 없다.
# ! ex) -3 -1 2 3 5 에서 target 2일 경우, -3+5 , -1+3 둘다 2를 만들 수 있으므로, 2라는 좋은 수를 만드는 조합이 여러개인 것.
# ! 하나만 찾아도 그냥 break하면 된다. 하나만 찾고 break 하기 때문에, 문제가 간단해지는 것. 만약 좋은 수를 만드는 모든 조합 수를 세라고하면, 좀 복잡해질듯
