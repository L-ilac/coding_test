from bisect import bisect_left, bisect_right
n, x = map(int, input().split())

nums = list(map(int, input().split()))

target = x
start = 0
end = n-1

last = 0
flag = False

while start <= end:
    mid = (start + end)//2

    if nums[mid] <= x:
        start = mid+1
        if nums[mid] == x:
            last = mid
            flag = True
    else:
        end = mid - 1


start = 0
end = n-1

first = 0
while start <= end:
    mid = (start + end)//2

    if nums[mid] >= x:
        end = mid - 1
        if nums[mid] == x:
            first = mid
            flag = True
    else:
        start = mid + 1


if flag:
    print(last-first + 1)
else:
    print(-1)


# ! bisect 를 이용한 풀이
f = bisect_left(nums, x)  # * 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 왼쪽 인덱스를 반환
l = bisect_right(nums, x)  # * 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 오른쪽 인덱스를 반환

# ! 배열에 찾고자하는 원소가 없다면, bisect_left와 bisect_right는 동일한 인덱스를 내뱉는다.
# * 배열에 없는 원소를 넣을 자리는 가장 왼쪽, 가장 오른쪽이 똑같기 떄문

result = print(l-f) if (l-f) != 0 else print(-1)
