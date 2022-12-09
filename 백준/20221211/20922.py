import sys
from collections import deque
n, k = map(int, input().split())

nums = list(map(int, sys.stdin.readline().split()))

q = deque()
limit = []
candidate = []
frequency = {}  # count 함수에 의한 시간초과를 막기위한 딕셔너리


def sol1():
    for n in nums:
        if n not in frequency:
            frequency[n] = 1
        else:
            frequency[n] += 1

        if frequency[n] > k:
            candidate.append(len(q))

            while True:
                tmp = q.popleft()
                frequency[tmp] -= 1
                if tmp == n:
                    break

        q.append(n)

    candidate.append(len(q))
    answer = max(candidate)

    print(answer)


# 투포인터로도 풀 수 있다.
def sol2():
    p = 0

    for i in range(n):
        if nums[i] not in frequency:
            frequency[nums[i]] = 1
        else:
            frequency[nums[i]] += 1

        if frequency[nums[i]] > k:
            candidate.append(i-p)

            while nums[p] != nums[i]:
                frequency[nums[p]] -= 1
                p += 1

            frequency[nums[p]] -= 1
            p += 1

    candidate.append(n-p)
    answer = max(candidate)

    print(answer)
