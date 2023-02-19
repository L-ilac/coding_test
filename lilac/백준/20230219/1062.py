from itertools import combinations
n, k = map(int, input().split())

words = []
for _ in range(n):
    tmp = list(input())
    left = set(tmp[4:-4])

    for ch in "acint":
        left.discard(ch)

    words.append(list(left))

alphabet = {'b': 0, 'd': 1, 'e': 2, 'f': 3, 'g': 4, 'h': 5, 'j': 6, 'k': 7, 'l': 8, 'm': 9,
            'o': 10, 'p': 11, 'q': 12, 'r': 13, 's': 14, 'u': 15, 'v': 16, 'w': 17, 'x': 18, 'y': 19, 'z': 20}

max_read = 0

if k < 5:
    pass
else:
    for teach in combinations(list(alphabet.keys()), k-5):
        bitmask = 0
        for c in teach:
            bitmask = (bitmask | 1 << alphabet[c])  # ! 가르친 단어로 만든 비트마스크

        readable = 0

        for w in words:
            if all(bitmask == (bitmask | (1 << alphabet[c])) for c in w):
                readable += 1

        max_read = max(max_read, readable)

print(max_read)
