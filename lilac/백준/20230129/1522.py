
# * 문자 a와 문자 b의 위치를 최소한으로 교환하여 모든 a를 연속되게 만들어야한다.
# ! 문자열에 포함된 b의 갯수를 세서, 교환하기 전 문자열안에 길이가 b의 갯수인 문자열 중 b가 제일 많이 포함된 문자열을 찾으면 됌.
# ! 위에서 찾은 문자열안의 a는 문자열안에 속하지않은 b와 위치를 변경해주면 되기 때문.

# ! 문자열이 원형임
# ! 슬라이딩 윈도우를 활용한 문제

s = input()
b_cnt = s.count('b')  # 문자열에 들어가있는 b 갯수

new_s = s + s[0:b_cnt-1]  # 원형을 적용한 새로운 문자열

# * a와 b의 위치를 교환하는 것이기 때문에, 최악의 경우라도 문자열 내의 b의 갯수를 넘을 수 없음
answer = b_cnt


if b_cnt == 0:
    pass
else:
    # ! 원형을 적용한 새로운 문자열을 사용하기 때문에, 기존 문자열의 길이 만큼만 검사하면 된다.
    for i in range(len(s)):
        tmp = new_s[i:i+b_cnt]
        a_cnt = tmp.count('a')

        answer = min(answer, a_cnt)

print(answer)
