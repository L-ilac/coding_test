# 맨 앞자리 숫자로 비교(다르다면)
# 맨 앞자리 숫자가 같다면, 제한 조건이 1000 이하이기 때문에, 케이스가 총 3가지
# 1. 한자리 vs 두자리 -> 한자리 숫자를 복사해서 늘리면됌 4 43 -> 4(4) 43
# 2. 한자리 vs 세자리 -> 1번과 동일 4 463 -> 4(44) < 463
# 3. 두자리 vs 세자리 -> 두자리 숫자와 세자리 숫자를 각각 복사해서 늘려서 4자리까지만 비교 -> 45 454 -> [45(45)] [454(4]54)
# 하지만 한자리, 두자리, 세자리 모두가 나올 경우가 있기 때문에, 마음 편하게 3종류 모두 4자리까지 늘려서 비교하는게 모든 케이스를 다 커버함.

def solution(numbers):
    answer = ''
    tmp = ''
    new_numbers = []

    for num in numbers:  # 숫자를 최소 4자리까지는 늘려서 슬라이싱해서 사용
        new_num = str(num)*4
        new_numbers.append((num, int(new_num[:4])))  # 원본과 늘린 문자열 둘다 필요함

    new_numbers.sort(key=lambda x: -x[1])  # 4자리 늘린 값으로 정렬

    answer = ''.join(str(x[0]) for x in new_numbers)  # 정렬한 순서대로 이어붙이기

    if int(answer) == 0:  # 최종 결과물이 0000... 이라면 0으로 처리
        answer = '0'

    return answer


# comparator를 이용한 방법은?

solution([6, 10, 2])
