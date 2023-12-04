from itertools import product

# 브루트 포스


def solution(users, emoticons):
    dc = [90, 80, 70, 60]
    prices = []

    for e in emoticons:
        tmp = []
        for r in dc:
            tmp.append((100-r, int((e/100)*r)))

        prices.append(tmp)

    bruteforce = list(product(*prices, repeat=1))

    answer = [-1, -1]

    for case in bruteforce:

        emoticon_plus = 0
        total_buy = 0

        for u in users:
            ratio, limit = u

            user_buy = 0

            for dc, price in case:
                if dc >= ratio:
                    user_buy += price

            if user_buy >= limit:
                emoticon_plus += 1
            else:
                total_buy += user_buy

        if answer[0] < emoticon_plus:
            answer = [emoticon_plus, total_buy]
        elif answer[0] == emoticon_plus:
            answer[1] = max(answer[1], total_buy)

    return answer


print(solution([[40, 10000], [25, 10000]], [7000, 9000]))
