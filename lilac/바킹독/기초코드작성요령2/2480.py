dice = list(map(int, input().split()))


if dice[0] != dice[1] != dice[2]:
    print(max(dice) * 100)
elif dice[0] == dice[1] and dice[1] != dice[2]:
    print(1000 + (dice[0] * 100))
elif dice[1] == dice[2] and dice[0] != dice[1]:
    print(1000 + (dice[1] * 100))
elif dice[0] == dice[2] and dice[2] != dice[1]:
    print(1000 + (dice[2] * 100))
else:
    print(10000 + (dice[0] * 1000))


# ! 정렬을 미리 해놓으면 편함. (별해)
