num = 1

for _ in range(3):
    num *= int(input())

result = [0] * 10

for i in list(str(num)):
    result[int(i)] += 1


for i in result:
    print(i)
