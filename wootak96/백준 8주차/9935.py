import sys

s=sys.stdin.readline().rstrip()
bomb=sys.stdin.readline().rstrip()
bomb=list(bomb)
x=bomb[-1]

stack=[]
for i in s:
    stack.append(i)


    if i==x:
        if stack[-len(bomb):]==bomb:
            for i in range(len(bomb)):
                stack.pop()
if stack==[]:
    print("FRULA")
else:
    print("".join(map(str,stack)))
