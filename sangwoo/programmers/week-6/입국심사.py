def solution(n, times):
    left = 1
    right = n * max(times)

    while left < right:
        mid = (left + right) // 2
        total = 0
        for time in times:
            total += (mid // time)
        
        if total >= n:
            right = mid
        else:
            left = mid + 1
    
    return left

print(solution(6, [7,10]))