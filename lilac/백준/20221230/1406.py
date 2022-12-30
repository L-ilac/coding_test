# 입력된 명령어에 따라서 동작하는 에디터를 만들어야함.
# 명령에는 커서 움직임(좌,우) ,문자 삭제(커서 왼쪽), 문자 삽입(커서 왼쪽) 이 있음
<<<<<<< HEAD

# ! 두개의 리스트를 만들어서, 리스트1 | 커서 | 리스트2 의 형태로 문자열을 구성한다고 생각해야함

=======
# 두개의 리스트를 만들어서, 리스트1 | 커서 | 리스트2 의 형태로 문자열을 구성한다고 생각해야함
>>>>>>> b99453e (파일 재추가)
# 아이디어를 떠올리지 못하면 못풀었을듯;
# 문자열을 직접 넣었다가 뺐다가 하면 시간초과 -> ex) 길이 5의 문자열에 3번째에 새로운 문자를 넣을 때, 4~5를 다른곳에 저장하고 새로운 문자 넣고 다시 그 뒤에 붙이는 방식으로하면 시간초과
# 그냥 현재 문자열 상태를 한 리스트에다가 저장해놓으려는 방식으로 문제를 풀면, append(), pop() -> O(1) 인 함수 쓰더라고 시간 초과됌.
# pop, insert 쓰지 않고 풀어야함 -> 쓰면 시간 초과

<<<<<<< HEAD
import sys

=======

import sys
>>>>>>> b99453e (파일 재추가)

# 커서를 기준으로 왼쪽 문자열, 오른쪽 문자열이 따로 있다는 생각으로 접근해야함
left = list(sys.stdin.readline().rstrip())
right = []
n = int(sys.stdin.readline().rstrip())


for _ in range(n):
    c = sys.stdin.readline().split()

    if c[0] == 'L':
        if len(left) == 0:
            continue
        right.append(left.pop())
    elif c[0] == 'D':
        if len(right) == 0:
            continue
        left.append(right.pop())
    elif c[0] == 'P':
        left.append(c[1])
    else:
        if len(left) == 0:
            continue
        left.pop()

# right에는 문자열이 거꾸로 들어가있으므로 실제 출력 때는 뒤집어줘야함
right.reverse()

answer = "".join(left) + "".join(right)

print(answer)
