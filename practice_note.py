from itertools import product


a = [1, 2, 3]
b = [4, 5, 6]

print(list(product(a, b)))


[(1, 4), (1, 5), (1, 6), (2, 4), (2, 5), (2, 6), (3, 4), (3, 5), (3, 6)]
