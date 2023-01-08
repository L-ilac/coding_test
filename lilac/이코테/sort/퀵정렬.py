a = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]


def quick(arr, start, end):

    if start >= end:
        return

    pivot = start
    left = start+1
    right = end

    while left <= right:

        # ! 조건문 순서 안지키면 에러남 -> short circuit
        while left <= end and arr[left] <= arr[pivot]:
            left += 1

        while right > start and arr[right] >= arr[pivot]:
            right -= 1

        if left > right:
            arr[right], arr[pivot] = arr[pivot], arr[right]
        else:
            arr[right], arr[left] = arr[left], arr[right]

    # 마지막으로 설정된 right가 pivot이 되는 값이 위치하는 인덱스이고, 고정된다.
    quick(arr, start, right-1)
    quick(arr, right+1, end)


quick(a, 0, len(a)-1)
print(a)
