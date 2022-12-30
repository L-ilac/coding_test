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
