n = int(input())

array = []

def setting(data):
	return data[1]

for _ in range(n):
	data = input().split()
	array.append((data[0],int(data[1])))

array = sorted(array, key = setting)
# lambda 식을 이용한 방법 
# array = sorted(array, key = lambda student: student[1])

print(array)

