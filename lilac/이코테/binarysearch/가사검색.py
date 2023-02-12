from bisect import bisect_right, bisect_left
from collections import defaultdict


def solution(words, queries):
    answer = []
    new_words = defaultdict(list)
    reversed_new_words = defaultdict(list)

    for w in words:
        new_words[len(w)].append(w)
        reversed_new_words[len(w)].append(w[::-1])

    for arr in new_words.values():
        arr.sort()

    for arr in reversed_new_words.values():
        arr.sort()

    for q in queries:

        length = len(q)

        if q[0] != '?':
            first = q.replace("?", "a")
            last = q.replace("?", "z")

            leftmost = bisect_left(new_words[length], first)
            rightmost = bisect_right(new_words[length], last)

            cnt = rightmost-leftmost

            answer.append(cnt)

        else:
            new_q = q[::-1]

            first = new_q.replace("?", "a")
            last = new_q.replace("?", "z")

            leftmost = bisect_left(reversed_new_words[length], first)
            rightmost = bisect_right(reversed_new_words[length], last)

            cnt = rightmost-leftmost

            answer.append(cnt)

    return answer


# ! 접미어를 뒤집어서 접두어로 검색하는 방법을 떠올렸으나, 복잡할거라 생각하고 시도 하지 않음.
# ! bisect를 이용해서 키워드에 포함되는 단어를 찾는 방법은 떠올렸음.
# ! dictionary를 이용하여 길이별로 단어를 분리하여 저장하고, 재사용을 가능하게 함.
