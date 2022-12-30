# 재귀 호출시 재귀 깊이 설정
import sys
sys.setrecursionlimit(10**6) 


arr=[]
while True:
    try:
        n=int(input())
        arr.append(n)
        
    except:
        break

def dfs(start, end):

    # 종료 조건
    if start > end:
        return

    temp = end + 1

    # 루트보다 큰 값 있나 찾기, 있으면 오른쪽 서브트리로 탐색, 없으면 넘어감
    for i in range(start + 1, end + 1):
        if arr[start] < arr[i]:
            temp = i
            break

    #후위 순회
    dfs(start + 1, temp - 1) # 왼쪽 서브트리 탐색
    dfs(temp, end) # 오른쪽 서브트리 탐색
    print(arr[start]) # 루트 출력

dfs(0,len(arr)-1)
