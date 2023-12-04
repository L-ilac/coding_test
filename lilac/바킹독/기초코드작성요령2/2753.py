year = int(input())


if year % 4 == 0 and year % 100 != 0:
    print(1)
elif year % 400 == 0:
    print(1)
else:
    print(0)


# ! 다른 방식의 코드 궁금
