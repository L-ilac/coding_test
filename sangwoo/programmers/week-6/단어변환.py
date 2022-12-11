from collections import deque

def check_one_diff(origin, compared):
    diff = 0

    for i in range(len(origin)):
        if origin[i] != compared[i]:
            diff += 1
    
    if diff == 1:
        return 1
    return 0

def solution(begin, target, words):

    res = [float('inf')] * len(words)
    queue = deque([(begin, 0)])

    while queue:
        origin, cnt = queue.popleft()
        if origin == target:
            return cnt

        for i, word in enumerate(words):
            if check_one_diff(origin, word) and cnt < res[i]:
                queue.append((word, cnt+1))
                res[i] = cnt

    return 0

print(solution("hit","cog",["hot", "dot", "dog", "lot", "log", "cog"]))