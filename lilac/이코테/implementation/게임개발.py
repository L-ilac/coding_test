n, m = map(int, input().split())
xpos, ypos, start_dir = map(int, input().split())

game_map = []
direction = [(-1, 0), (0, 1), (1, 0), (0, -1)]  # 북동남서
rotate_cnt = 0
visit_cnt = 0

for _ in range(n):
    game_map.append(list(map(int, input().split())))


# game_map[xpos][ypos] = -1
# visit_cnt += 1

while True:
    if rotate_cnt == 4:

        # 뒤 돌아가는 계산은 반대방향 값을 더하지 않고, 원래 방향 값을 빼는 것으로도 가능하다.
        # ? new_x = xpos - direction[start_dir]
        new_x, new_y = xpos + direction[(start_dir-2) %
                                        4][0], ypos + direction[(start_dir-2) % 4][1]

        if -1 < new_x < n and -1 < new_y < m:

            if game_map[new_x][new_y] == 1:
                break
            else:
                xpos, ypos = new_x, new_y
                rotate_cnt = 0
                continue
        else:
            break

    new_x, new_y = xpos + direction[(start_dir-1) %
                                    4][0], ypos + direction[(start_dir-1) % 4][1]

    if -1 < new_x < n and -1 < new_y < m:
        if game_map[new_x][new_y] == 0:  # 가보지 않은 곳이 있을 경우
            print(new_x, new_y)
            game_map[new_x][new_y] = -1  # 바다는 아니지만 이미 방문
            xpos, ypos = new_x, new_y
            visit_cnt += 1
            rotate_cnt = 0
            start_dir = (start_dir-1) % 4
        else:  # 이미 가본 곳이거나, 바다일 경우
            rotate_cnt += 1
            start_dir = (start_dir-1) % 4
    else:
        rotate_cnt += 1
        start_dir = (start_dir-1) % 4

print(game_map)
print(visit_cnt)
