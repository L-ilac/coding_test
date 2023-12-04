n, k = map(int, input().split())

school = [[0] * 2 for _ in range(6)]  # * school[year][sex]


for _ in range(n):
    s, y = map(int, input().split())

    school[y - 1][s] += 1


answer = 0
for y in range(6):
    for s in range(2):
        if school[y][s] % k == 0:
            answer += school[y][s] // k
        else:
            answer += (school[y][s] // k) + 1


print(answer)

# ! 올림 사용
import math
math.ceil()
