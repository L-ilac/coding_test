def solution(clothes):
    answer = 1
    dict_clothes = {}

    for cloth in clothes:
        if cloth[1] not in dict_clothes:
            dict_clothes[cloth[1]] = 1
        else:
            dict_clothes[cloth[1]] += 1

    print(dict_clothes.values())

    for value in dict_clothes.values():
        answer *= value+1

    return answer-1
