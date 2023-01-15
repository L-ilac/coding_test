# ! 접근법
# ! 모든 수 대해서 좋은 수의 조건에 부합하는지 검사한다.
# ! 배열에서 검사하고자하는 수를 제외하여 새로운 배열을 만들고, 배열을 정렬한 상태에서 투포인터를 이용하여 조건을 검사한다.
# ! 배열이 정렬되어있기때문에, 배열의 양 끝단에서부터 포인터의 위치를 조정하면서 값을 구하면 해당 수에 대한 검사를 마친다.
# ! 두개의 포인터가 서로 엇갈릴 때까지 조건을 만족하지 못하면, 해당 수는 좋은 수가 아닌 것.
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
