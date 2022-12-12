# 용액

N = int(input())
lst = list(map(int, input().split()))

left, right = 0, N-1
res = float('inf')
res_l, res_r = 0, N-1

while left < right:
    tmp_sum = lst[left] + lst[right]
    if res > abs(tmp_sum):
        res = abs(tmp_sum)
        res_l, res_r = left, right

    if tmp_sum < 0:
        left += 1
    else:
        right -= 1

print(f"{lst[res_l]} {lst[res_r]}")