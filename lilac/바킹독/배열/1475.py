import math

n = input()

result = [0] * 10

for i in list(n):
    result[int(i)] += 1


result[6] += result[9]

if result[6] % 2 == 0:
    result[6] = result[6] // 2
else:
    result[6] = (result[6] // 2) + 1

result[9] = 0

print(max(result))



# ! 다른 풀이가 궁금
math.ceil()