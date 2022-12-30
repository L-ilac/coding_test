# 입력받은 문자열을 이루는 문자의 갯수를 각각 세고, 가장 많이 나온 문자를 대문자로 반환한다.
# 가장 많이 나온 문자가 여러개일 경우에는 ? 반환

import heapq
from collections import defaultdict
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> b99453e (파일 재추가)
=======

>>>>>>> 8c3377f (123)
=======
>>>>>>> b99453e (파일 재추가)
=======

>>>>>>> 8c3377f (123)
count = defaultdict(int)

arr = []

# 문자 갯수 세기
for a in list(input().lower()):
    count[a] += 1

# 제일 많이 나온 문자를 세기위해 heapq 사용
for key, value in count.items():
    heapq.heappush(arr, (-value, key))

# 가장 많이 나온 문자
most1 = heapq.heappop(arr)

<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD
<<<<<<< HEAD

=======
>>>>>>> b99453e (파일 재추가)
=======

>>>>>>> 8c3377f (123)
=======
>>>>>>> b99453e (파일 재추가)
=======

>>>>>>> 8c3377f (123)
if arr:
    # 2번째로 가장 많이 나온 문자
    most2 = heapq.heappop(arr)

    # 가장 많이 나온 횟수가 동일할 때, ? 출력
    if most1[0] == most2[0]:
        print("?")
    else:
        print(most1[1].upper())

# 동일한 문자 1개로만 이루어진 문자열일 경우를 고려해야함
else:
    print(most1[1].upper())
