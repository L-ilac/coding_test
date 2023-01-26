s = input()
w = input()

length = len(w)

i = 0
cnt = 0
while i < len(s):

    tmp = s[i:i+length]

    if tmp == w:
        cnt += 1
        i += length
    else:
        i += 1

print(cnt)
