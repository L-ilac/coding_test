n = int(input())
nums = list(map(int, input().split()))


left = 0
right = 0


answer = 0
checked = [False] * 100001  # ! 선택된 수열에 특정 숫자가 포함되어있는지를 나타내는 배열


# ! right의 위치도 한번 이동하면 다시 되돌아오면 안된다.

for i in range(n):
    left = i  # ! 수열의 시작 인덱스(고정)

    while right < n and not checked[nums[right]]:
        checked[nums[right]] = True
        right += 1

    checked[nums[left]] = False
    answer += right - left


print(answer)
