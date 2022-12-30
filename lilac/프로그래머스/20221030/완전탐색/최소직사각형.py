def solution(sizes):
    answer = 0
    long = 0
    short = 0

    for size in sizes:
        if size[0] > size[1]:
            pass
        else:  # 가로가 세로보다 짧으면 두 값을 바꿔서 취급
            size[0], size[1] = size[1], size[0]

        long = max(long, size[0])  # 가로길이 중에 제일 큰 값
        short = max(short, size[1])  # 세로길이 중에 제일 큰 값

    answer = long * short  # 지갑 크기

    return answer

# 한 줄에 끝내는법
# return max(max(x) for x in sizes) * max(min(x) for x in sizes)
