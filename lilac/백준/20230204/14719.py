h, w = map(int, input().split())

blocks = list(map(int, input().split()))

result = 0

left = 0
right = 1

# 왼쪽 벽과 오른쪽 벽을 잡는다
# 벽의 안쪽에 있는 블록들은 무조건 양쪽 벽보다 높이가 낮거나 같아야함
# 가장 왼쪽 벽과 가장 오른쪽 벽은 신경 쓸 필요 없음


for i in range(1, len(blocks)-1):
    # i번째 인덱스를 기준으로 양쪽으로 가장 높은 벽들을 찾는다
    left_highest = max(blocks[:i])
    right_highest = max(blocks[i+1:])

    if min(left_highest, right_highest) - blocks[i] > 0:
        result += min(left_highest, right_highest) - blocks[i]

print(result)
