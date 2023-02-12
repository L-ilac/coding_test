from collections import deque

s = deque(list(input()))

explode = input()

stack = []

while s:
    c = s.popleft()

    stack.append(c)

    if stack[-1] == explode[-1]:
        tmp = "".join(stack[-len(explode):])  # ! 리스트 슬라이싱은 생각보다 시간이 많이든다.
        if tmp == explode:
            for _ in range(len(explode)):
                stack.pop()
            # del stack[-len(explode):]


result = "".join(stack)

if result == "":
    print("FRULA")
else:
    print(result)
