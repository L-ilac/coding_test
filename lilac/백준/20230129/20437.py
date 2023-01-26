from collections import defaultdict
import sys

t = int(sys.stdin.readline().rstrip())


for _ in range(t):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline().rstrip())

    shortest = sys.maxsize
    longest = 0

    alphabets = defaultdict(list)

    for idx, c in enumerate(w):
        alphabets[c].append(idx)

    for idx_list in alphabets.values():
        if len(idx_list) >= k:
            for i in range(0, len(idx_list)-k+1):
                shortest = min(shortest, idx_list[i+k-1]-idx_list[i]+1)

                longest = max(longest, idx_list[i+k-1]-idx_list[i]+1)

    if shortest == sys.maxsize:
        print(-1)
    else:
        print(shortest, longest)


# ! 이게 왜 슬라이딩 윈도우인지는.. 모르겠다.
# ! 후보가 될 수 있는 알파벳만 추려서 탐색하는게 시간초과를 피하는 길.
