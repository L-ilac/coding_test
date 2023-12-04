from itertools import product

op = ["+", "-", " "]

t = int(input())


for _ in range(t):

    n = int(input())

    answer = []

    for o in list(product(op, repeat=n-1)):
        cal = ""

        for i in range(0, n-1):
            cal += str(i+1)
            cal += o[i]

        cal += str(n)

        tmp = cal.replace(" ", "")

        if eval(tmp) == 0:
            answer.append(cal)

    answer.sort()

    for a in answer:
        print(a)

    print()
