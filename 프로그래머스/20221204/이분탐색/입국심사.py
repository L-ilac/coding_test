# 7 10 14 20 21 28 30 .... 이런 순으로 가다가 그냥 n번째 요소 return

def solution(n, times):
    answer = 0
    low = min(times)
    high = max(times) * n

    while low <= high:
        mid = (low+high)//2
        checked = 0

        for time in times:
            checked += mid//time

            # if checked >= n :
            #     break

        if checked >= n:
            answer = mid
            high = mid - 1
        else:
            low = mid + 1

    return answer
