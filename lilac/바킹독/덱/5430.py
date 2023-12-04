from collections import deque
import sys

t = int(input())


for _ in range(t):
    p = list(input())
    n = int(input())
    direction = 1

    tmp = sys.stdin.readline().rstrip()[1:-1]

    if tmp:
        nums = deque(tmp.split(","))
    else:
        nums = deque()

    flag = True

    for c in p:
        if c == "R":
            direction *= -1
        elif c == "D":
            if len(nums) == 0:
                flag = False
                break
            else:
                if direction == 1:
                    nums.popleft()
                elif direction == -1:
                    nums.pop()

    if direction == -1:
        nums.reverse()

    if flag:
        print("[" + ",".join(nums) + "]")
    else:
        print("error")


# ! reverse()를 매번 수행할 경우 시간초과로 이어짐. reverse()를 직접 수행하는 대신 방향만 저장하는게 핵심
