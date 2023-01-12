n = int(input())
nums = list(map(int, input().split()))


def bs(start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if nums[mid] == mid:
        return mid
    elif nums[mid] < mid:
        return bs(mid+1, end)
    else:
        return bs(start, mid-1)


result = bs(0, n-1)
if result is None:
    print(-1)
else:
    print(result)


# ! 이분탐색을 통해서 범위를 좁힐 때, 버려지는 범위가 절대 답이 될 수 없는 이유가 있어야한다.
# ? 이 문제 같은 경우 한쪽이 버려져야하는 이유를 못찾아서 제 시간내에 못품 -> 다시 풀때는 생각해볼 것
