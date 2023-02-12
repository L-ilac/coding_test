s = input()
w = input()

length = len(w)

i = 0  # 인덱스

cnt = 0  # 단어가 몇번 등장하는지 카운트

while i < len(s):

    tmp = s[i:i+length]

    if tmp == w:
        cnt += 1
        # ! 중복되지 않게 세기 위해서 단어의 길이만큼을 인덱스에 더해준다.
        i += length
    else:
        i += 1

print(cnt)
