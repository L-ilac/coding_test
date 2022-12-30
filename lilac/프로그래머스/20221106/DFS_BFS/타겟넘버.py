from itertools import product


def solution(numbers, target):
    answer = 0
    option = [1, -1]
    case = list(product(option, repeat=len(numbers)))

    for c in case:
        sum = 0
        for i in range(len(numbers)):
            sum += c[i]*numbers[i]

        if sum == target:
            answer += 1

    # l = [(x, -x) for x in numbers]
    # s = list(map(sum, product(*l)))

    return answer


def solution2(numbers, target):
    q = [0]
    for n in numbers:
        s = []
        for _ in range(len(q)):
            x = q.pop()
            s.append(x + n)
            s.append(x + n*(-1))
        q = s.copy()
    return q.count(target)


def dfs(nums, i, n, t):
    ret = 0
    if i == len(nums):
        if n == t:
            return 1
        else:
            return 0
    ret += dfs(nums, i+1, n+nums[i], t)
    ret += dfs(nums, i+1, n-nums[i], t)
    return ret


def solution3(numbers, target):
    answer = dfs(numbers, 0, 0, target)
    return answer
