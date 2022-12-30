# 표준 라이브러리란 특정한 프로그래밍 언어에서 자주 사용되는 표준 소스코드를 미리 구현해 놓은 라이브러리임.

import 없이 바로 사용할 수 있는 함수들.
from collections import deque
1. 내장함수
input print sum min max eval sorted

eval(): 인자로 수학 수식이 문자열 형식으로 들어오면 해당 수식을 계산한 결과를 반환한다.

sorted(): 인자로 iterable 객체가 들어오면, 이를 정렬한 결과를 반환한다.
sorted(객체, reverse= ?): reverse로 오름차순 or 내림차순 선택
sorted(객체, key= ?): 정렬 기준(key 속성)을 설정할 수 있다.  # key는 lambda식 사용

 2. itertools  # 반복되는 데이터를 처리하는 기능을 포함하는 라이브러리
주로 combinations, permutations 2개를 제일 유용하게 사용함.
-> from itertools import permutations/combinations/product/combinations_with_replacement

permutations(순열) -> iterable 객체에서 특정 개수의 데이터를 뽑아 일렬로 나열하는 모든 경우의 수를 계산해줌(순서 중요)
Ex. result = list(permutations(data, 뽑을 갯수))

combinations(조합) -> permutations과 똑같이 데이터를 뽑아 나열하나 순서를 고려하지않음.
Ex. result = list(combinations(data, 뽑을 갯수))

product(중복순열) -> 중복을 허용하여 순열의 과정을 수행
Ex. result = list(product(data, repeat=뽑을 갯수))
# repeat 생략하면 안됌

combinations_with_replacement -> 중복 조합
Ex. result = list(combinations_with_replacement(data, 뽑을 갯수))


4개 모두 클래스이므로 객체 초기화 이후에 리스트로 변환하여 사용해야한다.


3. heapq  # Heap 기능을 위해 사용, 우선순위 큐 기능을 구현할 때 사용
# PrioirityQueue 라이브러리도 있지만, 보통 heapq가 더 빠름
# 파이썬의 Heap은 Min Heap으로 구성되어있음

heapq.heappush(리스트, 값) -> 힙에 원소 넣기(리스트에 자동으로 heap을 구성하도록 들어감)

heapq.heappop() -> 힙에서 원소 꺼내기

# 기본적으로 Min Heap이므로 Max Heap은 부호를 바꿔서 넣고 뺀다.

heapq.heapify(list) -> 기존에 데이터가 들어가있는 list를 힙의 형태로 정렬 시켜줌.


4. bisect  # 이진 탐색 구현용 라이브러리, 정렬된 배열에서 사용
bisect_left(리스트, 삽입하려는 값): 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(리스트, 삽입하려는 값): 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 오른쪽 인덱스를 반환
# 직접 리스트에 삽입하는게 아님. 삽입은 list.insert()로 넣을 수 있다.

5. collections  # 유용한 자료구조를 제공하는 표준 라이브러리.

deque -> 덱(양방향 큐)


덱으로 큐를 구현해야함(Queue 라이브 러리가 있지만, 일반적인 큐 자료구조를 구현하는 라이브러리가 아님, 양방향으로 뺄수 있기 때문에 큐, 스택 둘다 구현 가능)

덱은 인덱싱, 슬라이싱을 사용할 수 없다.

deque 은 list()로 변경하면 list로 사용 가능

deque.appendleft(x) -> 맨 첫번째에 원소 넣기
deque.append(x) -> 맨 마지막에 원소 넣기
deque.popleft(x) -> 맨 첫번째 원소 빼기
deque.pop(x) -> 맨 마지막 원소 빼기

Counter -> 카운터

등장 횟수를 세는 기능을 제공함, iterable 객체(list, dict, set, str, bytes, tuple, range)가 주어졌을 때, 해당 객체 내부의 원소가 몇번 씩 등장했는지 알려줌.(원소별 등장횟수)

Ex)
from collections import Counter

counter=Counter(iterable 객체)
counter[원소] -> 원소가 iterable 객체에 등장하는 횟수 반환


6. math  # 자주 사용되는 수학적인 기능을 포함하는 라이브러리

import math

math.factorial(x) -> x! 값 반환
math.sqrt(x) -> x 제곱근 반환(루트 x)
math.gcd(x, y) -> x, y의 최대공약수 반환
math.e -> 자연상수
math.pi -> 파이
