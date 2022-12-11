import itertools


def isPrime(number):  # 밑에서 0과 1을 제거하기 때문에 2부터 검사한다
    for i in range(2, number):
        if number % i == 0:
            return False

    return True


def solution(numbers):
    answer = 0

    # 가능한 숫자 조합 전부 만들기
    numbers = list(numbers)  # 숫자 문자열을 1개씩 띄워놓는다.
    new_numbers = []

    for i in range(1, len(numbers)+1):
        # 가능한 모든 경우의 수를 구함(문자열 숫자의 배치 순서도 중요하므로 순열)
        tmp = list(itertools.permutations(numbers, i))

        for item in tmp:
            new_numbers.append(''.join(item))  # 문자열을 모두 이어붙여서 숫자형태로 변환

    # 문자열을 숫자로 변환 ("01102" -> 1102 로 변환됌)
    new_numbers = list(map(int, new_numbers))
    new_numbers = list(set(new_numbers))  # 중복되는 값 제거

    if 0 in new_numbers:  # 0이 있다면 제거
        new_numbers.remove(0)

    if 1 in new_numbers:  # 1이 있다면 제거
        new_numbers.remove(1)

    # 소수 판별
    for number in new_numbers:
        if isPrime(number):
            answer += 1

    return answer
