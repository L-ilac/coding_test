s = list(input())

tmp = []
num = 0
for c in s:
    # if c.isalpha():
    #     tmp.append(c)

    if ord('A') <= ord(c) <= ord('Z'):
        tmp.append(c)
    else:
        num += int(c)

tmp.sort()

# 숫자가 아예 없을 수도 있다.
if num != 0:
    tmp.append(str(num))

answer = ''.join(tmp)
print(answer)

# ! isalph(), isnumeric, 등등... 유용한 함수
