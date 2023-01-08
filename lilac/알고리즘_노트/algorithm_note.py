# 종종 쓰이는 함수들을 정리해보자.
# ! itertools를 활용할 수 있다면 적극적으로 활용하자.
from itertools import combinations, permutations, product, combinations_with_replacement

# combinations(iterable, m) -> iterable 에서 m개 뽑아서 조합(순서 상관없음)
# permutations(iterable, m) -> iterable 에서 m개 뽑아서 순열(순서 상관있음)

# * combinations_with_replacement(iterable, m)-> iterable 에서 m개를 뽑아서 중복조합(순서 상관없음)
# ? 중복조합은 주어진 iterable에서 같은 값을 여러번 선택하는 것을 허용한 조합이다. 단, 조합이므로 순서를 신경쓰지 않는다.


#! product는 조금 결이 다르다.
# * product(*iterables, m) -> 여러 iterable들의 데카르트곱
# ? 주어진 모든 iterable에서 각각 m번씩 요소를 뽑아서 하나의 그룹으로 묶는다. 중복을 허용한다.
# ? 즉, product(iterable1, iterable2, iterable3, 4) 이면, iterable1,2,3 에서 각각 4개씩 중복을 허용하여 뽑아서 총 12개로 이루어진 그룹을 만든다.
# product로 중복순열을 수행하고 싶으면, iterable을 1개만 넣으면 된다.


# ! 2차원 배열 회전
def rotate_matrix(matrix):
    n = len(matrix)  # *행 갯수
    m = len(matrix[0])  # *열 갯수

    new_matrix = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            # ! 원본 행렬의 (x,y) 좌표의 값이 90도 회전시, 회전된 행렬의 (y,n-1-x) 위치로 간다.
            new_matrix[j][n-1-i] = matrix[i][j]


# ! iterable에 있는 문자열 이어 붙이기 -> join 함수 이용하기
a = ['a', 'b', 'c']
"".join(a)  # result : abc


# ! 조건부 표현식 (Conditional Expression)
# * 조건문을 만족하면 Success 저장, 실패시 Fail 저장
result = "Success" if (condition) else "Fail"

# * "a안에 있는 i 중에 뒤에 if 조건문을 만족하는 애들만 형식에 맞게 맞춰서 리스트에 넣겠다!"
result2 = [i for i in a if (condition)]

# ? result = [표현식 + 반복분 + 조건문]
# ? 1. 반복문에 해당되는 횟수와 변수에 대하여 2. 조건문을 만족하는 변수만 3. 표현식에 대입하여 나온 값으로 리스트에 저장.

# ! Loop
range(start, end, step)  # * start 부터 end-1 까지 step씩 증가하는 loop
# ? step, start는 생략 시 각각 1, 0이 default
# ? range(start,end) or range(end) or range(start,end,step) 중 1개의 형태로 사용

# ! global 키워드
# * 함수 안에서 함수 밖의 변수 데이터를 변경해야하는 경우,
# * 함수 안에서 global 키워드로 함수 밖의 변수를 지정하면,
# * 해당 함수에서는 지역변수를 만들지않고, 함수 바깥에 선언된 변수를 바로 참조하게됌.

# ! 데이터 입력 받기
input() or sys.stdin.readline().rstrip()  # 후자는 입력받는 데이터 양이 많을 때

# * 입력받은 문자열은 실제 코드에서 사용되는 형태로 변환해줘야하는 경우가 많음,
# * map,list,split(),rstrip() 등을 이용하여 적절히 변환할 것.

# ? f-string 문법
age = 10
print(f"I am {age}years old.")


# ! heapq -> Heap의 특성을 이용해 우선순위 큐로 사용
# ? 보통 (우선순위, 값) 형태로 넣어서 우선순위 큐로 사용 (기본 min힙, max힙은 -우선순위로 가능)

# * -> 힙에 원소 넣기(리스트에 자동으로 heap을 구성하도록 들어감)
heapq.heappush(list, value)

# * -> 힙에서 원소 꺼내기
heapq.heappop()

# * -> 기존에 데이터가 들어가있는 list를 힙의 형태로 정렬 시켜줌.
heapq.heapify(list)
