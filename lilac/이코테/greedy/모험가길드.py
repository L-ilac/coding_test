import sys
n = int(input())

people = list(map(int, sys.stdin.readline().split()))


# 공포도가 낮은 사람부터 접근
people.sort()

total_group_num = 0
group = 0
# 1 2 2 2 3
for p in people:
    group += 1

    if group == p:
        total_group_num += 1
        group = 0


print(total_group_num)
