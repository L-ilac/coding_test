from collections import deque


def rotate(blocks):
    result = []
    max_x = max([x for x, y in blocks])

    for x, y in blocks:
        result.append([y, max_x-x])

    result.sort()
    return result


def getRotatedBlocks(blocks):
    result = []
    for block in blocks:
        tmp = []
        rotate90 = rotate(block)
        rotate180 = rotate(rotate90)
        rotate270 = rotate(rotate180)

        tmp.append(block)

        if block == rotate90:
            # continue
            pass
        elif block == rotate180:
            tmp.append(rotate90)
        else:
            tmp.append(rotate90)
            tmp.append(rotate180)
            tmp.append(rotate270)

        result.append(tmp)

    return result


def getBlocks(board, target):
    result = []
    board_size = len(board)
    direction = [(0, 1), (0, -1), (-1, 0), (1, 0)]  # 상하좌우
    queue = deque()

    for y in range(board_size):
        for x in range(board_size):
            if board[y][x] == target:
                block = []
                block.append([x, y])
                queue.append([x, y])
                board[y][x] = -1

                while queue:
                    cur_x, cur_y = queue.popleft()

                    for dir in direction:  # 상하좌우로 갈 수 있는지 모두 확인
                        new_point = [cur_x+dir[0], cur_y+dir[1]]

                        if -1 < new_point[0] < board_size and -1 < new_point[1] < board_size:

                            if board[new_point[1]][new_point[0]] == target:

                                queue.append(new_point)
                                board[new_point[1]][new_point[0]] = -1
                                block.append(new_point)

                min_x = min([x for x, y in block])
                min_y = min([y for x, y in block])

                for xy in block:
                    xy[0] -= min_x
                    xy[1] -= min_y

                block.sort()
                result.append(block)

    result.sort(key=lambda x: -len(x))
    return result


def matchBlocks(board, table):
    answer = 0
    for b in board[:]:
        for t in table[:]:
            if b in t:
                answer += len(b)
                board.remove(b)
                table.remove(t)
                break

    return answer


def solution(game_board, table):
    game_board.reverse()
    table.reverse()

    blocksfromboard = getBlocks(game_board, 0)
    blocksfromtable = getRotatedBlocks(getBlocks(table, 1))

    answer = matchBlocks(blocksfromboard, blocksfromtable)
    return answer
