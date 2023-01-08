from itertools import permutations
import sys
n = int(input())

numbers = list(map(int, input().split()))

operator = list(map(int, input().split()))  # + - * / 순

new_operator = []

for i in range(4):
    for _ in range(operator[i]):
        new_operator.append(i)

# ! 중복 제거해줄 것
operator_perms = list(set(permutations(new_operator, len(new_operator))))


max_val = -sys.maxsize
min_val = sys.maxsize

for perms in operator_perms:
    result = numbers[0]
    for i in range(len(numbers)-1):
        if perms[i] == 0:  # 더하기
            result += numbers[i+1]
        elif perms[i] == 1:  # 빼기
            result -= numbers[i+1]
        elif perms[i] == 2:  # 곱하기
            result *= numbers[i+1]
        elif perms[i] == 3:  # 나누기
            result = int(result/numbers[i+1])

    max_val = max(result, max_val)
    min_val = min(result, min_val)

print(max_val)
print(min_val)
