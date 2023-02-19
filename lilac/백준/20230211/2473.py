import sys
n = int(input())
solutions = list(map(int, sys.stdin.readline().rstrip().split()))
solutions.sort()

answer_idx = [0, 0, 0]

min_sum = sys.maxsize

for i in range(0, n-2):
    fix = i
    left = i+1
    right = n-1

    while left < right:
        tmp_sum = solutions[fix] + solutions[left] + solutions[right]

        if abs(tmp_sum) < abs(min_sum):
            min_sum = tmp_sum
            answer_idx = [fix, left, right]

        if tmp_sum == 0:
            break

        elif tmp_sum > 0:
            right -= 1

        else:
            left += 1

    if min_sum == 0:
        break

answer = [solutions[answer_idx[0]],
          solutions[answer_idx[1]], solutions[answer_idx[2]]]

print(*answer)
