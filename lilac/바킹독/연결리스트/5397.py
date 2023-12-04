from collections import deque

t = int(input())


for _ in range(t):
    s = list(input())
    
    left = deque()
    right = deque()
    
    for c in s:
        if c == "<":
            if not left:
                continue
            right.appendleft(left.pop())
        elif c == ">":
            if not right:
                continue
            left.append(right.popleft())
        elif c == "-":
            if not left:
                continue
            left.pop()
        else:
            left.append(c)
            
    
    left_str = ''.join(left)
    right_str = ''.join(right)
    
    print(left_str+right_str)
