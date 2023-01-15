import heapq
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


# ! 다익스트라 알고리즘
# * 그래프 탐색에서 노드를 잇는 간선의 가중치가 모두 양수일 경우 사용할 수 있다.
# * 특정 출발점을 기준으로 나머지 모든 점까지의 최단거리를 구하는 알고리즘
# * 그리디하게 접근하기 떄문에, 낮은 시간복잡도를 가지는 알고리즘이다. + 그리디하게 접근하기 위해 heapq를 사용하여 구현한다.

q = []
distance = [1e9] * n
distance[start] = 0
heapq.heappush(q, (0, start))  # 출발점 넣기

while q:
    # * heapq를 이용하여 가장 가중치가 작은 노드부터 검사한다.
    dist, now = heapq.heappop(q)

    # ! 현재 확인하고 있는 노드가 최단거리를 갱신하는데 영향을 주지 않을 경우에는 넘긴다.
    if dist > distance[now]:
        continue

    # * now에 연결된 모든 노드에 대하여
    for i, weight in graph[now]:
        tmp = dist + weight

        # * 현재 새롭게 계산한 거리가 기존에 저장되어있던 최단거리보다 짧으면, 갱신해야함
        if tmp < distance[i]:
            distance[i] = tmp
            heapq.heappush(q, (tmp, i))


# ! 벨만포드 알고리즘
# * 그래프 탐색에서 노드를 잇는 간선의 가중치 중 음수값이 있을 경우 사용한다.
# * 기본적으로는 특정 출발점을 기준으로 나머지 모든 점까지의 최단거리를 구하는 알고리즘
# ? 특징으로는, 음수 순환이 존재하는 그래프일 경우, 최단거리를 구할 수 없는데(-inf를 향해 계속 갱신되기 떄문에), 음수 순환을 detect 할 수 있다.

distance = [1e9] * n
distance[start] = 0  # * 출발점에 해당하는 노드 설정

# * n개 노드에 대해 n번 반복
for i in range(n):
    # * 매 반복마다 모든 간선 확인
    for edge in edges:
        dep, dst, cost = edge

        # * dep까지의 거리가 한번이라도 계산된 적이 있다면(distance[dep] != 1e9), 출발점에서 dep까지 갈 수 있는 경로가 있다는 의미
        # ! start -> dep -> dst 경로의 값을 최솟값으로 갱신가능할 수 있다면, 갱신해준다.
        # ? start->dep + dep->dst VS start->dst
        if distance[dep] != 1e9 and distance[dep] + cost < distance[dst]:
            distance[dst] = distance[dep] + cost

            # ! 음수순환이 있는지 체크하는 코드
            # ! 음수순환이 없는 그래프라면 n번째 루프에서 최솟값을 갱신하는 경우가 없음.
            # ! if문이 true를 반환했다는건, 최솟값으로 갱신된다는 것이고, 그게 n-1번의 루프 이후(n번째 루프부터) 라면, 음수순환이 존재하므로 최소비용계산 불가
            if i == n-1:
                return True

return False

# ! 위상정렬
# * '순서가 정해져있는 작업'을 차례로 수행해야 할 때 그 순서를 결정해주기 위해 사용하는 알고리즘
indgree 배열을 이용해서 자기 자신으로 들어오는 간선이 몇개인지 체크하고, indgree가 0이 되는 요소부터 수행한다.
indgree 배열의 변동성을 체크하는 것이 가장 중요함

# ! dfs
# * 깊이 우선 탐색 -> 최대로 깊이 들어갈 수 있는 만큼 탐색하기 때문에, 재귀적으로 함수를 호출해서 들어가거나 스택을 사용

# ! bfs
# * 너비 우선 탐색 -> 같은 거리에 있는 모든 노드를 전부 탐색하기 떄문에, 최단거리를 구할 때 유리함, 큐를 사용

# ! 크루스칼 알고리즘 (minimum spanning tree)


# ! bisect  # 이진 탐색 구현용 라이브러리, 정렬된 배열에서 사용
bisect_left(리스트, 삽입하려는 값):  # * 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(리스트, 삽입하려는 값):  # * 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 오른쪽 인덱스를 반환
