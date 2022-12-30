def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    cnt = 0

    # 문제 풀이 접근
    # 1. 차례대로 스택에 주식을 넣는다.
    # 2. 스택 맨위의 주식이 현재 넣으려는 주식보다 비싸면, 스택 맨 위 주식은 가격이 떨어진 것으로 처리해야한다.
    # 3. 직전에 넣은 주식을 스택에서 뺀다.(주식을 빼면서 가격이 유지되었던 시간을 답안에 작성)
    # 4. 2~3 과정을 현재 넣으려는 주식의 가격이 스택 맨위의 주식보다 비싸거나 같을 때까지 반복한다. + 조건이 만족되면 주식을 넣는다.
    # 5. 모든 주식을 넣을 때까지 2~4 과정을 반복한다.
    # 6. 주식을 모두 넣었다면, 스택은 가격이 떨어지지 않은 주식들로만 구성되어있다.
    # 7. 스택에서 주식을 하나씩 빼면서, 가격이 유지되었던 시간을 답안에 작성한다.

    for (index, price) in enumerate(prices):
        tmp = (index, price)

        # 스택이 비었거나 넣으려는 주식이 스택 맨위 주식과 같거나 비싸면, 주식을 넣는다.
        if not stack or stack[-1][1] <= tmp[1]:
            stack.append(tmp)
        else:  # 스택이 비어있지 않고, 넣고자하는 주식이 스택 맨위 주식보다 쌀때
            # 현재 넣으려는 주식보다 같거나 싼 주식이 나올때 까지 반복
            while stack and stack[-1][1] > tmp[1]:
                out = stack.pop()  # 스택 맨위 주식을 뺌
                cnt += 1  # 스택에서 뺀 주식 갯수
                answer[out[0]] += cnt

            for item in stack:  # 스택에서 제외된 주식만큼 현재 스택에 남아있는 주식에 시간 추가
                answer[item[0]] += cnt

            cnt = 0  # 초기화

            stack.append(tmp)  # 넣으려던 주식 넣기

    # 주식이 모두 스택에 들어간 후, 스택에 남은 주식들은 모두 가격이 떨어지지 않았음을 보장받는다.

    stack.pop()  # 맨마지막에 들어간 주식은 시간으로 취급하지 않음

    while stack:  # 스택에 남은 주식들에 대해 시간 추가
        for item in stack:
            answer[item[0]] += 1
        stack.pop()  # 시간을 먼저 더 해주고, 스택에서 빼야함.

    return answer

    # 스택을 뒤집어서 생각해보자. 백준 탑, 옥상 정원 정리


def solution(prices):
    prices = prices[::-1]  # 3 2 3 2 1
    # 0 1 1 3 4
    stack = []
    ans = []

    for i in range(len(prices)):
        while stack:
            if stack[-1][1] < prices[i]:  # 현재 값이 스택의 최솟값보다 크면
                ans.append(i-stack[-1][0])  # 인데스 차이 만큼 답 갱신
                break
            else:
                stack.pop()  # 현재 값이 스택의 최솟값보다 작거나 같으면 stack pop

        if not stack:
            …
