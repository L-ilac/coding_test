# 육각형의 확장이기 때문에, 육각형을 이루고 있는 벌집의 갯수가 수열 형태를 이룰 것으로 예상
# 육각형을 이루고 있는 벌집의 갯수 -> (한 변의 길이 - 1) * 6
# 1개 -> 6개 -> 12개 -> 18개 -> 24개 ....
# 입력으로 주어진 숫자가 몇번째 육각형에 있는지 구할 수 있다면, 그게 답.

n = int(input())

total_bee_house = 1
tmp = 6
answer = 1

while n > total_bee_house:
    total_bee_house += tmp
    tmp += 6
    answer += 1

print(answer)
