# n = int(input())

# nums = set()
# nums.add(1)


# for i in range(n):
#     tmp = sorted(list(nums))[i]
#     nums.add(tmp*2)
#     nums.add(tmp*3)
#     nums.add(tmp*5)

# print(sorted(list(nums))[n-1])


import sys

# n번째 못생긴 수 출력
n = int(sys.stdin.readline())

ugly = [0] * n  # 못생긴 수를 담기 위한 테이블 (1차원 DP 테이블)
ugly[0] = 1  # 첫 번째 못생긴 수는 1

# 몇 번쨰 인덱스까지 2, 3, 5배한 결과를 다뤘는지
i2 = i3 = i5 = 0

# 다음으로 다뤄야하는 곱셈 값
next2, next3, next5 = 2, 3, 5

# 1부터 n까지의 못생긴 수들을 찾기
for l in range(1, n):

    # 다음으로 다뤄야하는 곱셈 값들 중 최솟값을 l번째 인덱스에 저장
    ugly[l] = min(next2, next3, next5)

    # 현재 i2 인덱스 값에 2배를 곱한 값은 업데이트 되었으므로,
    # 다음 i2 인덱스 값에 2배를 곱한 값이 무엇인지 임시 저장
    if ugly[l] == next2:
        i2 += 1
        next2 = ugly[i2] * 2

    # 현재 i3 인덱스 값에 3배를 곱한 값은 업데이트 되었으므로,
    # 다음 i3 인덱스 값에 3배를 곱한 값이 무엇인지 임시 저장
    if ugly[l] == next3:
        i3 += 1
        next3 = ugly[i3] * 3

    # 현재 i5 인덱스 값에 5배를 곱한 값은 업데이트 되었으므로,
    # 다음 i5 인덱스 값에 5배를 곱한 값이 무엇인지 임시 저장
    if ugly[l] == next5:
        i5 += 1
        next5 = ugly[i5] * 5


# n번째 못생긴 수를 출력
print(ugly[n - 1])
