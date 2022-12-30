def solution(nums):
    answer = 0

    pkmon_cnt = dict.fromkeys(nums, 0)

    for num in nums:
        pkmon_cnt[num] += 1

    print(pkmon_cnt)
    answer = len(nums)/2 if len(pkmon_cnt) > (len(nums)/2) else len(pkmon_cnt)

    # if len(pkmon_cnt) > (len(nums)/2):
    #     answer = (len(nums))/2
    # else:
    #     answer = len(pkmon_cnt)
    print(answer)

    return answer


nums = [3, 3, 3, 2, 2, 4]
solution(nums)
