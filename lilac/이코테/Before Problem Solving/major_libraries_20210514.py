4. bisect  # 이진 탐색 구현용 라이브러리, 정렬된 배열에서 사용
bisect_left(리스트, 삽입하려는 값): 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(리스트, 삽입하려는 값): 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 오른쪽 인덱스를 반환
# 직접 리스트에 삽입하는게 아님. 삽입은 list.insert()로 넣을 수 있다.


5. Counter -> 카운터

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
