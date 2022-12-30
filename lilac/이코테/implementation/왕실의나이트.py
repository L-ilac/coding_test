knight_pos = input()

xpos, ypos = ord(knight_pos[0])-ord('a')+1, int(knight_pos[1])
knight_moves = [(-2, -1), (-2, 1), (2, -1), (2, 1),
                (-1, -2), (1, -2), (-1, 2), (1, 2)]
#UUL, UUR, DDL, DDR, LLU, LLD, RRU, RRD


cnt = 0
for m in knight_moves:
    new_x, new_y = xpos+m[0], ypos+m[1]

    if 0 < new_x < 9 and 0 < new_y < 9:
        cnt += 1

print(cnt)
