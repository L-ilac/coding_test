# 문제 : 트리를 전위 순회한 결과가 주어졌을 때, 동일한 트리로 후위 순회한 결과를 출력하라.

# 이진 트리 순회 방식은 루트를 몇번째 순서에 순회하느냐에 따라 3종류로 나뉜다.
# preorder(루트 -> 왼쪽 자식 -> 오른쪽 자식), inorder(왼쪽 자식 -> 루트 -> 오른쪽 자식), postorder(왼쪽 자식 -> 오른쪽 자식 -> 루트)

# 문제 접근법
# 1. preorder로 주어진 입력으로, 실제 이진탐색 트리를 구성하기 위해서는 그냥 순서대로 트리에 노드를 집어 넣으면 됌.
# 2. 그러므로 입력을 순서대로 트리에 노드로 삽입해서 원본 트리를 구성함.
# 3. 2번에서 구성된 트리로 postorder 수행
import sys
# 문제에서 총 노드의 갯수가 10000개 이하라고 했으므로, 최대 재귀 깊이를 늘려준다. -> 테스트해보니까 10002는 통과 10001까지는 재귀깊이 에러 -> 왜....? 노드 최대 10000개 + 메인함수 스택?
sys.setrecursionlimit(100000)

# 트리의 노드


class Node:
    def __init__(self, num) -> None:
        self.left = None
        self.right = None
        self.key = num

# 트리(간략하게 루트와 트리에 노드를 추가하는 함수만 만들었음)


class Tree:
    def __init__(self) -> None:
        self.root = None

    def setRoot(self, node):
        self.root = node

    def addNode(self, node):
        if self.root is None:  # 루트가 비어 있다면
            self.root = node
        else:  # 루트가 비어있지 않다면

            # 루트에서 부터 시작해서, 현재 삽입하려고하는 노드가 어느 위치에 들어가야하는지 자리를 찾기 위해 반복문 사용
            now = self.root
            while True:
                if now.key > node.key:
                    if now.left is None:
                        now.left = node
                        break
                    now = now.left
                else:
                    if now.right is None:
                        now.right = node
                        break
                    now = now.right


bst = Tree()
# 다른 문제처럼 입력의 갯수가 초기에 주어지는게 아니라, eof(end of file)가 나오면 자동으로 입력을 멈추도록 코드를 짜야함.(문제에서 요구하는바)
while True:
    try:
        num = int(input())
        new_node = Node(num)
        bst.addNode(new_node)
    except:
        break

# 보통 트리가 주어졌을 때, postorder 함수는 다음과 같다. 결국 밑에 있는 트리를 구성하지 않고 해결한 답변들도 재귀적으로 함수를 부르는 순서는 똑같다.


def postorder(root):
    if root is None:
        return
    postorder(root.left)
    postorder(root.right)
    print(root.key)


# solution2
preorder = []


def postorder2(start, end):
    if start >= end:
        return

    # 루트보다 큰 값이 존재하지 않을 경우, 맨 앞의 값이 루트이고 그 뒤에 모든 값들이 루트의 왼쪽 서브 트리임을 알 수 있다.
    if preorder[end - 1] <= preorder[start]:
        postorder2(start + 1, end)
        print(preorder[start])
        return

    mid = 0
    for i in range(start + 1, end):
        if preorder[start] < preorder[i]:
            mid = i
            break

    # 후위 순회의 전형적인 순서 (왼쪽 -> 오른쪽 -> 루트)
    postorder2(start + 1, mid)
    postorder2(mid, end)
    print(preorder[start])


postorder2(0, len(preorder))


def postorder3(first, end):
    if first > end:
        return
    mid = end+1   # 루트보다 큰 값이 존재하지 않을 경우를 대비

    # 어느 위치에서 왼쪽 서브트리와 오른쪽 서브트리로 갈라지는지 찾기 위한 반복문
    for i in range(first+1, end+1):
        if preorder[first] < preorder[i]:
            mid = i
            break

    postorder3(first+1, mid-1)
    postorder3(mid, end)
    # 주어진 입력이 전위 순회이기 때문에 preorder[start] 위치에 있는 값이 트리에서 루트에 해당한다.
    print(preorder[first])


postorder3(0, len(preorder)-1)
