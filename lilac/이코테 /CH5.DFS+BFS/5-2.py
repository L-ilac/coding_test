from collections import deque # 파이썬에서는 queue를 위해 deque 사용

queue = deque()

# append() : 큐에 데이터 넣기, pop() : 큐에서 데이터 빼기


queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft() # queue이므로 앞에서부터 뺀다.
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) 
print(queue[0]) # list와 동일하게 인덱스로 접근 가능
queue.reverse() # queue 뒤집기 : queue에 들어있는 원소들이 순서가 뒤집힘.
print(queue[3]) # 뒤집히기 전 0번째 인덱스에 있던 값


queueTolist = list(queue) #deque 객체를 리스트 자료형으로 변경할때 사용