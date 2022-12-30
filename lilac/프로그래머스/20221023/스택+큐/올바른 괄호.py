def solution1(s):
    answer = True
    stack = []

    for i in s:

        if i == '(':
            stack.append(i)  # '(' 면 스택에 무조건 넣고
        else:
            if not stack:  # 입력값이 ')' 인데 스택에 남아있는 짝지어줄 '('이 없으면 잘못된 괄호
                return False
            else:  # 짝지어줄 괄호가 있다면 맨뒤에서 pop
                stack.pop(len(stack)-1)

    if len(stack) != 0:  # 문자열을 전부 돌고 짝지어지지 못한 '(' 가 남아있다면 false
        return False
    else:
        return True


def solution2(s):
    answer = True
    flag = 0

    for i in s:
        if i == '(':
            flag += 1
        else:
            flag -= 1

        if flag < 0:
            answer = False
            return answer

    if flag > 0:
        return False

    return True
