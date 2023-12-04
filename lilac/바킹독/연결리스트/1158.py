from collections import deque


n, k = map(int, input().split())


nums = deque([str(i) for i in range(1, n + 1)])
answer = []


while nums:
    nums.rotate(-k + 1)
    answer.append(nums.popleft())


print("<", ", ".join(answer), ">", sep="")  # 출력 형식...?
