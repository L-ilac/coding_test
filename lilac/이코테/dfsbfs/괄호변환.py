def correct(u):
    stack = []

    for i in list(u):
        if i == '(':
            stack.append('(')
        else:
            if not stack:
                return False
            else:
                stack.pop()
    return True


def solution(p):
    if p == '':
        return ''

    u, v = '', ''
    balance = 0

    for i in range(len(p)):
        if p[i] == '(':
            balance += 1
        else:
            balance -= 1

        if balance == 0:
            u += p[0:i+1]
            v += p[i+1:]
            break

    if correct(u):
        return u+solution(v)
    else:
        tmp = '('
        tmp += solution(v)
        tmp += ')'
        u = u[1:-1]
        u = list(u)

        # 문자열 변경 로직
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('

        tmp += ''.join(u)

        return tmp


# ! short - circuit ㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋㅋ
