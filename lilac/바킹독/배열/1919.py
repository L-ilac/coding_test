first = list(input())
second = list(input())


for i in first[:]:
    if i in second[:]:
        first.remove(i)
        second.remove(i)

print(len(first) + len(second))


# ! 다른 풀이 궁금
alphabet = [0] * 26
