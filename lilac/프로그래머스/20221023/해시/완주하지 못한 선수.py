def sol1(participant, completion):
    dict_completion = dict.fromkeys(completion, 0)

    for name in completion:
        dict_completion[name] += 1

    for name in participant:
        if name not in dict_completion:
            answer = name
            break
        elif dict_completion[name] == 0:
            answer = name
            break
        dict_completion[name] -= 1


def sol2(participant, completion):
    dict_participant = dict.fromkeys(participant, 0)
    dict_completion = dict.fromkeys(completion, 0)

    for name in participant:
        dict_participant[name] += 1

    for name in completion:
        dict_completion[name] += 1

    for name in participant:
        if name not in dict_completion:
            answer = name
            break
        elif dict_participant[name] != dict_completion[name]:
            answer = name
            break
