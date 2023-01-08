import sys
n = int(input())


data = []

for _ in range(n):
    # 이름 국 영 수
    name, k, e, m = sys.stdin.readline().rstrip().split()
    data.append([name, int(k), int(e), int(m)])


data.sort(key=lambda x: (-x[1], x[2], -x[3], x[0]))

for i in data:
    print(i[0])
