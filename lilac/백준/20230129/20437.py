from collections import defaultdict
import sys

t = int(sys.stdin.readline().rstrip())


for _ in range(t):
    w = sys.stdin.readline().rstrip()
    k = int(sys.stdin.readline().rstrip())

    shortest = sys.maxsize
    longest = 0

    alphabets = defaultdict(list)

    # * 특정 알파벳이 위치하고 있는 인덱스를 저장한다.
    for idx, c in enumerate(w):
        alphabets[c].append(idx)

    # ! 문제 해결 접근법
    # ! 3. 어떤 문자를 정확히 K개를 포함하는 가장 짧은 연속 문자열의 길이를 구한다.
    # ! 4. 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열의 길이를 구한다.
    # ! 위의 두 경우 모두 결국 정확히 k개 포함되는 특정 문자가 문자열의 맨 앞과 맨 뒤에 해당해야함.
    # ! 즉, 문제는 어떤 문자를 정확히 K개를 포함하고, 문자열의 첫 번째와 마지막 글자가 해당 문자로 같은 가장 긴 연속 문자열과 가장 짧은 연속 문자열을 구하는 문제로 귀결됌.

    # * 특정 알파벳이 위치하고 있는 인덱스를 저장했으므로,
    # * i번째 인덱스 ~ i+k-1 번째 인덱스까지에 해당하는 문자열 w[i:i+k-1] 이 특정 문자를 정확히 k개 포함하는 문자열임.
    # * 위의 조건을 만족하는 모든 문자열에 대해 가장 긴 길이와 가장 짧은 길이를 구하면 된다.
    for idx_list in alphabets.values():
        # ! 인덱스를 저장한 리스트의 길이가 k보다 작은 경우, 특정 문자를 k개를 포함하는 문자열을 만들 수 없으므로 제외한다.
        if len(idx_list) >= k:
            for i in range(0, len(idx_list)-k+1):
                shortest = min(shortest, idx_list[i+k-1]-idx_list[i]+1)
                longest = max(longest, idx_list[i+k-1]-idx_list[i]+1)

    # ! 조건에 맞는 문자열을 구하지 못했을 경우
    # ! 생각해보면 shortest를 구하지 못하면, longest도 구할수가 없다. 그래서 -1 하나만 출력되게 만들었구나...
    # ! 처음에는 '3번은 구할 수 있는데, 4번을 구할수 없으면 그건 어떡하지?' 라는 생각을 했었음 -> 이런 경우가 애초에 생길수 없었던 것.
    if shortest == sys.maxsize:
        print(-1)
    else:
        print(shortest, longest)

# ! Tip. 후보가 될 수 있는 알파벳만 추려서 탐색하는게 시간초과를 피하는 길
