n = int(input())
m = int(input())

parent = [i for i in range(n)]


def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]


def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


board = []
for i in range(n):
    tmp = list(map(int, input().split()))
    for j in range(n):
        if tmp[j] == 1:
            if find_parent(parent, i) != find_parent(parent, j):
                union_parent(parent, i, j)

plan = list(map(int, input().split()))

# print(parent)
# print(plan)


flag = True


for i in range(len(plan)-1):
    if find_parent(parent, plan[i]-1) != find_parent(parent, plan[i+1]-1):
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
