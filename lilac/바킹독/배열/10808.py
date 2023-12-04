s = input()

alphabet = [0] * (ord("z") - ord("a") + 1)

for c in s:
    alphabet[ord("z") - ord(c)] += 1

alphabet.reverse()

print(*alphabet)


# ! 다른 방법?