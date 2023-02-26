from collections import defaultdict
import sys
n = int(input())

words = []
new_words = []
dict = defaultdict(set)

for i in range(n):
    word = sys.stdin.readline().rstrip()
    new_words.append((word, i))
    words.append(word)

new_words.sort()


def common(w1, w2):

    l = len(w1) if len(w1) < len(w2) else len(w2)
    common = ""
    for i in range(l):
        if w1[i] == w2[i]:
            common += w1[i]
        else:
            break

    return common


for i in range(len(new_words)-1):
    prefix = common(new_words[i][0], new_words[i+1][0])

    dict[prefix].add(new_words[i][1])
    dict[prefix].add(new_words[i+1][1])


prefixes = list(dict.keys())

# ! 접두사의 길이가 최대인 경우가 여러개 일때에는 입력되는 순서대로 제일 앞쪽에 있는 단어를 답으로 한다.
prefixes.sort(key=lambda x: (-len(x), min(list(dict[x]))))


tmp = list(dict[prefixes[0]])
tmp.sort()

print(words[tmp[0]])
print(words[tmp[1]])
