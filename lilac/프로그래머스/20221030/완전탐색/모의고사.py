def solution(answers):
    tmp = []

    p1 = [1, 2, 3, 4, 5]  # 5개 주기
    p1_score = 0

    p2 = [2, 1, 2, 3, 2, 4, 2, 5]  # 8개 주기
    p2_score = 0

    p3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]  # 10개 주기
    p3_score = 0

    # enumerate를 적극적으로 사용하자.
    for idx, answer in enumerate(answers):  # (문제번호, 답)의 형식으로 이용
        if p1[idx % len(p1)] == answer:
            p1_score += 1
        if p2[idx % len(p2)] == answer:
            p2_score += 1
        if p3[idx % len(p3)] == answer:
            p3_score += 1

    scores = [p1_score, p2_score, p3_score]
    top_score = max(scores)
    print(top_score)

    for idx, score in enumerate(scores):
        if score == top_score:
            tmp.append(idx+1)

    tmp.sort()

#     for answer in answers:

#         if p1[i%5] == answer:
#             p1_score[0] += 1

#         if p2[i%8] == answer:
#             p2_score[0] += 1

#         if p3[i%10] == answer:
#             p3_score[0] += 1

#         i += 1

#         if i == 40:
#             i = 0

#     scores = [p1_score, p2_score, p3_score]
#     scores.sort(key=lambda x : (-x[0],x[1]))

#     top_score = scores[0][0]

#     for score in scores:
#         if score[0] == top_score:
#                 tmp.append(score[1])

    return tmp
