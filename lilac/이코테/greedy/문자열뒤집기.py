s = input()

# 연속된 문자열이 몇개인지 구해야함

zeros = 0  # 연속된 0 덩어리 갯수
ones = 0  # 연속된 1 덩어리 갯수

for i in range(len(s)-1):
    if s[i] != s[i+1]:
        if s[i] == '0':
            zeros += 1
        else:
            ones += 1

if s[-1] == '0':
    zeros += 1
else:
    ones += 1

print(min(zeros, ones))
