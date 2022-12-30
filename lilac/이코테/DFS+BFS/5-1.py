stack = []

# 파이썬에서는 stack을 구현할 필요 없이 list를 append와 pop으로 사용함.
# append() : 스택에 데이터 넣기, pop() : 스택에서 데이터 빼기

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
stack.pop()
stack.append(1)
stack.append(4)
stack.pop()

print(stack) # 최하단 원소부터 출력
print(stack[::-1]) # 최상단 원소부터 출력