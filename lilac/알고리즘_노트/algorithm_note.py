import heapq
# 종종 쓰이는 함수들을 정리해보자.
# ! itertools를 활용할 수 있다면 적극적으로 활용하자.
from itertools import combinations, permutations, product, combinations_with_replacement

# combinations(iterable, m) -> iterable 에서 m개 뽑아서 조합(순서 상관없음)
# permutations(iterable, m) -> iterable 에서 m개 뽑아서 순열(순서 상관있음)

# * combinations_with_replacement(iterable, m)-> iterable 에서 m개를 뽑아서 중복조합(순서 상관없음)
# ? 중복조합은 주어진 iterable에서 같은 값을 여러번 선택하는 것을 허용한 조합이다. 단, 조합이므로 순서를 신경쓰지 않는다.


#! product는 조금 결이 다르다.
# * product(*iterables, repeat=m) -> 여러 iterable들의 데카르트곱
# ? 주어진 모든 iterable에서 각각 m번씩 요소를 뽑아서 하나의 그룹으로 묶는다. 중복을 허용한다.
# ? 즉, product(iterable1, iterable2, iterable3, 4) 이면, iterable1,2,3 에서 각각 4개씩 중복을 허용하여 뽑아서 총 12개로 이루어진 그룹을 만든다.
# product로 중복순열을 수행하고 싶으면, iterable을 1개만 넣으면 된다.



# ! 2차원 배열 회전 (시계방향)
def rotate_matrix(matrix):
    n = len(matrix)  # *행 갯수
    m = len(matrix[0])  # *열 갯수

    new_matrix = [[0]*n for _ in range(m)]

    for i in range(n):
        for j in range(m):
            # ! 원본 행렬의 (x,y) 좌표의 값이 90도 회전시, 회전된 행렬의 (y,n-1-x) 위치로 간다.
            new_matrix[j][n-1-i] = matrix[i][j]

# ! 어렵게 생각하지말자. 그림으로 그려서 기준점이었던 원점(0,0)이 우측 상단 or 좌측 하단으로 옮겨간다고 생각하자.


# ! iterable에 있는 문자열 이어 붙이기 -> join 함수 이용하기
a = ['a', 'b', 'c']
"".join(a)  # * result : abc
"_(구분자)".join(a) # * result : a_b_c -> iterable의 값과 값 사이에 구분자를 넣어서 하나의 문자열로 합침


# ! 조건부 표현식 (Conditional Expression)
# * 조건문을 만족하면 Success 저장, 실패시 Fail 저장
result = "Success" if (condition) else "Fail"

# * "a안에 있는 i 중에 뒤에 if 조건문을 만족하는 애들만 형식에 맞게 맞춰서 리스트에 넣겠다!"
result2 = [i for i in a if (condition)]

# ? result = [표현식 + 반복분 + 조건문]
# ? 1. 반복문에 해당되는 횟수와 변수에 대하여 2. 조건문을 만족하는 변수만 3. 표현식에 대입하여 나온 값으로 리스트에 저장.

# ! Loop
range(start, end, step)  # * start 부터 end-1 까지 step씩 증가하는 loop
# ? step, start는 생략 시 각각 1, 0이 default
# ? range(start,end) or range(end) or range(start,end,step) 중 1개의 형태로 사용

# ! global 키워드
# * 함수 안에서 함수 밖의 변수 데이터를 변경해야하는 경우,
# ! 함수 안에서 global 키워드로 함수 밖의 변수를 지정하면, (함수 안에서 밖의 변수를 global로 지정)
# * 해당 함수에서는 지역변수를 만들지않고, 함수 바깥에 선언된 변수를 바로 참조하게됌.

# ! 데이터 입력 받기
input() or sys.stdin.readline().rstrip()  # 후자는 입력받는 데이터 양이 많을 때

# * 입력받은 문자열은 실제 코드에서 사용되는 형태로 변환해줘야하는 경우가 많음,
# * map,list,split(),rstrip() 등을 이용하여 적절히 변환할 것.


# ? f-string 문법 -> 문자열 안에 변수를 넣어서 변수를 문자열로 자동 변환 시키는 것
age = 10
print(f"I am {age}years old.")


# ! heapq -> Heap의 특성을 이용해 우선순위 큐로 사용
# !!!!!!!! 보통 (우선순위, 값) 형태로 넣어서 우선순위 큐로 사용 (기본 min힙, max힙은 -우선순위로 가능)

# * -> 힙에 원소 넣기(리스트에 자동으로 heap을 구성하도록 들어감)
heapq.heappush(list, value)

# * -> 힙에서 원소 꺼내기
heapq.heappop()

# * -> 기존에 데이터가 들어가있는 list를 힙의 형태로 정렬 시켜줌. -> 정렬이라기보단 0번째 인덱스에 min or max 값이 들어있음(내부적으로 힙은 정렬된 형태를 갖지는 않기 때문)
heapq.heapify(list)



# ! 다익스트라 알고리즘
# * 그래프 탐색에서 노드를 잇는 간선의 가중치가 <"모두 양수"> 일 경우 사용할 수 있다.
# ! 특정 출발점을 기준으로 나머지 모든 점까지의 최단거리를 구하는 알고리즘 -> 특정 출발점 기준 -> 나머지 모든 점
# * 그리디하게 접근하기 떄문에, 낮은 시간복잡도를 가지는 알고리즘이다. + 그리디하게 접근하기 위해 heapq를 사용하여 구현한다.
# * 다익스트라 알고리즘에서 매번 "방문하지 않은 노드 중 가장 최단 거리가 짧은 노드를 선택"하는 과정을 반복하는 이유는,
# * 선택된 노드가 최단거리가 완전히 결정된 노드이기 때문이다. 최단거리가 완전히 결정된 노드는 더 이상 알고리즘을 반복해도 최단거리가 줄어들지 않는다.
# ! ex) 현재 최단거리가 가장 짧은 노드가 A라고 하자. 그리고 또 다른 노드 B가 있다고 하자.
# ! 그렇다면, 다음의 식은 간선이 양수라면 무조건 성립한다. A까지의 거리(현재 최단거리가 가장 짧은 노드) < B까지의 최단거리 + (B -> A까지 거리)
# ! 그러므로, 더 이상 알고리즘을 반복해도 최단거리가 줄어들지 않는 것.

q = []
distance = [1e9] * n # * 출발점으로부터 각 노드까지의 거리를 저장하는 배열
distance[start] = 0
heapq.heappush(q, (0, start))  # 출발점 넣기

while q:
    # * heapq를 이용하여 가장 가중치가 작은 노드부터 검사한다.
    dist, now = heapq.heappop(q)

    # ! 현재 확인하고 있는 노드가 최단거리를 갱신하는데 영향을 주지 않을 경우에는 넘긴다.(dist > distance[now] 일 경우)
    # ! 왜 같은 경우에(dist == distance[now])도 확인을 해야하는가? -> 더 짧은 거리로 갱신되면, 그 갱신된 값으로 q에 정보가 들어간다.(distance[i] = tmp, heappush((tmp,i)))
    # ! 그러면 distance[i] == tmp 일 수 밖에 없는데, 그럼 갱신된 i 노드를 거쳐 더 짧은 거리로 도착할 수 있는 다른 노드가 없는지 탐색해야하기 때문
    if dist > distance[now]:
        continue

    # * now에 연결된 모든 노드에 대하여
    for i, weight in graph[now]:
        
        tmp = dist + weight # * now 까지의 거리 + now -> i 까지의 거리

        # * 현재 새롭게 계산한 거리가 기존에 저장되어있던 최단거리보다 짧으면, 갱신해야함
        if tmp < distance[i]:
            distance[i] = tmp
            # * 더 짧은 경로를 찾은 노드들은 새롭게 큐에 넣는다. -> 왜? 새롭게 갱신된 경로에 의해서 또다른 노드까지의 거리가 갱신될 수 있기 때문
            heapq.heappush(q, (tmp, i))


# ! 플로이드 워셜 알고리즘
# * 그래프의 모든 지점으로부터 다른 모든 지점으로까지의 최단거리를 구하는 알고리즘
# * 그래프에서 노드를 잇는 간선의 가중치 중 음수값이 있어도 사용할 수 있다.
# ! 음수 순환이 존재하는 그래프를 탐지할 수 있다.
distance = [[1e9] * n for _ in range(n)]

# ! 경유할 노드의 반복문이 가장 바깥에 있어야한다.
# ! why? a를 경유하는 모든 케이스를 다 처리하고 나면, 그 다음 b를 경유하는 모든 케이스를 처리할 때, 이미 a를 경유할 때 계산했던 결과가 b를 경유할 떄 계산하는 과정에 포함이 되어있기 때문
# ! a를 경유하는 케이스를 계산 하는 과정에서 s -> a -> e / s -> a -> b 둘다 계산해버리기 때문에, s -> b -> e 를 계산할 때 s -> b 의 값은 이미 s -> a -> b 의 결과를 내포한 값이다.
# 경유할 노드
for k in range(n):
    # 출발 노드
    for i in range(n):
        # 도착 노드
        for j in range(n):
            # !  k를 경유해서 가는 i-> k ->j 경로의 길이가 i->j 까지의 기존 경로의 길이보다 짧다면 갱신한다.
            distance[i][j] = min(
                distance[i][j], distance[i][k] + distance[k][j])

# ! 자기자신으로의 최단거리가 음수인 값이 존재하면, 음수 순환이 존재하는 것.
# ! 자기자신으로의 최단거리는 0이므로, 음수 사이클이 없다면, 자기자신으로의 최단거리가 0보다 작아질수 없다.
for i in range(n):
    if distance[i][i] < 0:
        print("음수 순환 존재")

# ! 벨만포드 알고리즘
# * 그래프 탐색에서 노드를 잇는 간선의 가중치 중 음수값이 있을 경우 사용한다.
# * 기본적으로는 특정 출발점을 기준으로 나머지 모든 점까지의 최단거리를 구하는 알고리즘
# ? 특징으로는, 음수 순환이 존재하는 그래프일 경우, 최단거리를 구할 수 없는데(-inf를 향해 계속 갱신되기 떄문에), 음수 순환을 detect 할 수 있다.

distance = [1e9] * n
distance[start] = 0  # * 출발점에 해당하는 노드 설정

# * n개 노드에 대해 n번 반복
for i in range(n):
    # * 매 반복마다 모든 간선 확인
    for edge in edges:
        dep, dst, cost = edge

        # * dep까지의 거리가 한번이라도 계산된 적이 있다면(distance[dep] != 1e9), 출발점에서 dep까지 갈 수 있는 경로가 있다는 의미
        # ! start -> dep -> dst 경로의 값을 최솟값으로 갱신가능할 수 있다면, 갱신해준다.
        # ? start->dep + dep->dst VS start->dst
        if distance[dep] != 1e9 and distance[dep] + cost < distance[dst]:
            distance[dst] = distance[dep] + cost

            # ! 음수순환이 있는지 체크하는 코드
            # ! 음수순환이 없는 그래프라면 n번째 루프에서 최솟값을 갱신하는 경우가 없음.
            # ! if문이 true를 반환했다는건, 최솟값으로 갱신된다는 것이고, 그게 n-1번의 루프 이후(n번째 루프부터) 라면, 음수순환이 존재하므로 최소비용계산 불가
            if i == n-1:
                return True

return False


# ! dfs
# * 깊이 우선 탐색 -> 최대로 깊이 들어갈 수 있는 만큼 탐색하기 때문에, 재귀적으로 함수를 호출해서 들어가거나 스택을 사용

def dfs(graph, v, visited):
    visited[v] = True
    
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

# ! bfs
# * 너비 우선 탐색 -> 같은 거리에 있는 모든 노드를 전부 탐색하기 떄문에, 최단거리를 구할 때 유리함, 큐를 사용

def bfs(graph, v, visited):
    
    visited[v] = True
    
    q = deque()
    q.append(v)
    
    while q:
        now = q.popleft()
        
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                q.append(i)
    
# ! 0-1 bfs


# ! union-find -> 서로소 집합 자료구조를 이용한 알고리즘

# * find
# 초기에 모든 노드는 자기 자신을 부모 노드로 설정함

def find(parent,x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x]) # * 경로 압축 알고리즘을 이용해서 루트노드를 찾기 위해 발생하는 재귀함수 호출을 줄일 수 있다.
        
    return parent[x] 

# * union

def union(parent,a,b):
    a = find(parent,a)
    b = find(parent,b)
    
    # ! 두 원소를 동일 루트노드를 갖는 하나의 집합으로 합치는 게 목적이므로, 부모가 동일한지 검사하지 않는다.
    
    if a>b:
        parent[a] = b
    else:
        parent[b] = a



# ! 사이클 판별
# * 동일한 루트 노드를 갖는 노드가 간선에 의해 연결된다면, 사이클이 발생한 것.
# * 간선을 입력받고, 간선을 이루는 두 노드가 같은 루트 노드를 갖지 않는다면 union 하고, 같은 루트노드를 가지면 사이클이 발생한 것으로 간주

# ! 크루스칼 알고리즘 (minimum spanning tree)
# * union-find를 이용해서 찾는다
# 1. 그래프에 존재하는 모든 간선을 정렬한다.
# 2. 비용이 적은 간선부터 간선을 잇는 두 노드의 루트 노드를 확인한다.
# 2-1. 두 노드가 동일한 루트 노드를 갖는다면, 해당 간선을 추가하지 않는다
# 2-2. 두 노드가 다른 루트 노드를 갖는다면, 해당 간선을 추가하고, 간선을 이루는 두 노드를 union 한다.

edges.sort()

for edge in edges:
    
    a,b,cost = edge
    
    if find(parent, a) != find(parent, b):
        total_cost += cost
        union(parent, a, b)
        
# ! 위상정렬
# * '순서가 정해져있는 작업'을 차례로 수행해야 할 때 그 순서를 결정해주기 위해 사용하는 알고리즘
indgree 배열을 이용해서 자기 자신으로 들어오는 간선이 몇 개인지 체크하고, indgree가 0이 되는 요소부터 수행한다.
indgree 배열의 변동성을 체크하는 것이 가장 중요함

indegree = []

for a,b in edges:
    graph[a].append(b) # * 방향이 있는 그래프여야함
    indegree[b] += 1
    
q = deque()

for idx, i in enumerate(indegree):
    if i == 0:
        q.append(idx)
        
while q:
    now = q.popleft()
    result.append(now)
    
    for i in graph[now]:
        indegree[i] -= 1 
        
        if indegree[i] == 0:
            q.append(i)


# ! bisect  # 이진 탐색 구현용 라이브러리, 정렬된 배열에서 사용
bisect_left(리스트, 삽입하려는 값):  # * 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 왼쪽 인덱스를 반환
bisect_right(리스트, 삽입하려는 값):  # * 리스트의 정렬된 순서를 유지하면서, 삽입하려는 값을 삽입할 가장 오른쪽 인덱스를 반환
    

# ! 이진 탐색

def binary_search(data, target, start, end):
    while start <= end:
        mid = (start+end)//2
        
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            start = mid + 1
            pass
        else:
            end = mid -1
            
    return False # 데이터 발견 실패 시
            
            

# ! LIS
 # n^2 일반적인 DP
x = int(input())
arr = list(map(int, input().split()))

dp = [1 for i in range(x)]

for i in range(x):
    for j in range(i):
        if arr[i] > arr[j]:
            dp[i] = max(dp[i], dp[j] + 1)

max_dp = max(dp)
print(max_dp)

max_idx = dp.index(max_dp)
lis = []

while max_idx >= 0:
    if dp[max_idx] == max_dp:
        lis.append(arr[max_idx])
        max_dp -= 1
    max_idx -= 1

lis.reverse()
print(*lis)

# nlogn 이분탐색을 이용한 dp
import bisect

x = int(input())
arr = list(map(int, input().split()))

dp = [arr[0]]

for i in range(x):
    if arr[i] > dp[-1]:
        dp.append(arr[i])
    else:
        idx = bisect.bisect_left(dp, arr[i])
        dp[idx] = arr[i]

print(len(dp))

# ! 레벤슈타인 거리
def lev(str1, str2):
    dp = [[0] * (len(str2)+1) for _ in range(len(str1) + 1)]
    for i in range(1, len(str1)+1):
        dp[i][0] = i
    for j in range(1, len(str2)+1):
        dp[0][j] = j

    for i in range(1, len(str1)+1):
        for j in range(1, len(str2)+1):
            if str1[i-1] == str2[j-1]:
                dp[i][j] = dp[i-1][j-1]

            else:
                dp[i][j] = min(dp[i-1][j-1], dp[i-1][j], dp[i][j-1]) + 1

    return dp[-1][-1]


# ! knapsack problem

# 2차원 DP
n, k = map(int, input().split())
lst=[[0, 0]]
for _ in range(n):
    lst.append(list(map(int, input().split())))
dp = [[0]*(k+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, k+1):
        weight = lst[i][0]
        value = lst[i][1]
        if j < weight:  # 가방에 넣을 수 없으면
            dp[i][j] = dp[i - 1][j]  # 위에 값 그대로 가져오기
        else: # 가방에 넣을 수 있으면
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - weight] + value)
print(dp[n][k])

# 1차원 DP

n, k = map(int,input().split())
w = []
v = []
dp = [0] * (k+1)

for _ in range(n):
    weight,value = map(int,input().split())
    w.append(weight)
    v.append(value)
    
    
for i in range(n):
    for j in range(k,0,-1):
        if j >= w[i]:
            dp[j] = max(dp[j], dp[j-w[i]] + v[i])
 
print(dp[k])