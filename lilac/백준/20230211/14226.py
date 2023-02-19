from collections import deque

s = int(input())

q = deque()  # ! (현재 화면의 이모티콘 갯수, 클립보드에 이모티콘 갯수, 시간)

visited = set()  # ! (현재화면 이모티콘 갯수, 클립보드의 이모티콘 갯수) 이미 처리한 적있으면 더 볼 필요가 없음.

q.append((1, 0, 0))  # ! 현재 화면의 이모티콘 갯수, 클립보드의 이모티콘 갯수, 시간


while q:
    onscreen, clipboard, time = q.popleft()

    if onscreen == s:
        print(time)
        break

    if (onscreen-1, clipboard) not in visited:
        q.append((onscreen-1, clipboard, time+1))
        visited.add((onscreen-1, clipboard))

    if (onscreen+clipboard, clipboard) not in visited:
        q.append((onscreen+clipboard, clipboard, time+1))
        visited.add((onscreen+clipboard, clipboard))

    if (onscreen, onscreen) not in visited:
        q.append((onscreen, onscreen, time+1))
        visited.add((onscreen, onscreen))
