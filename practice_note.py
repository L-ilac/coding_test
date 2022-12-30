import heapq


data = [7, 2, 3]

q = []

for i in range(0, len(data)):
    heapq.heappush(q, (i+1, data[i]))

print(q)

heapq.heappop(q)

print(q)
