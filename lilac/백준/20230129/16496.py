n = int(input())

nums = list(map(int, input().split()))

new_nums = []

for idx, n in enumerate(nums):
    new_n = str(n)*10
    new_nums.append((int(new_n[:10]), idx))


new_nums.sort(reverse=True)


result = ''
for i in range(len(new_nums)):
    result += str(nums[new_nums[i][1]])

if int(result) == 0:
    result = '0'

print(result)
