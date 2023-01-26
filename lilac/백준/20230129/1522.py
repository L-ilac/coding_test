
# ! 슬라이딩 윈도우
# 문자열이 원형임

s = input()
b_cnt = s.count('b')  # 문자열에 들어가있는 b 갯수

new_s = s + s[0:b_cnt-1]  # 원형을 적용한 새로운 문자열

answer = b_cnt

if b_cnt == 0:
    pass
else:
    for i in range(len(s)):
        tmp = new_s[i:i+b_cnt]
        a_cnt = tmp.count('a')

        answer = min(answer, a_cnt)

print(answer)
