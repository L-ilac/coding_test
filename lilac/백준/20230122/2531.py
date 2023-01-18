import sys
n, d, k, c = map(int, input().split())

sushi = []
for _ in range(n):
    sushi.append(int(sys.stdin.readline().rstrip()))

sushi += sushi[0:k-1]
answer = 0

for i in range(n):
    tmp = set(sushi[i:i+k])
    tmp.add(c)

    answer = max(answer, len(tmp))

print(answer)
