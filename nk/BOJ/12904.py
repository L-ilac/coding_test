# 문제의 방법을 거꾸로 풀었다.
# T가 S가 될 수 있는지 판단하기.
# 방법 1에서는 맨마지막 문자가 A면 A 삭제
# 방법 2에서는 맨마지막 문자가 B면 B 삭제, 문자열 뒤집기

# S 와 T 가 같으면 1 출력 다르면 0 출력

def can_1(str):
    if str[-1] == 'A': # A가 맨 마지막 문자이면
        return str[:-1] # A 지우기
    else: # 아니면
        return False # 할수 없어.

def can_2(str):
    if str[-1] == 'B': # B가 맨 마지막 문자이면
        str = str[:-1] # B 지우기
    else: # 아니면
        return False # 할수 없어
    return str[::-1] # 문자열 뒤집기


S = input() # S 입력
T = input() # T 입력

s_len = len(S) # S 길이
t_len = len(T) # T 길이

for _ in range(t_len - s_len): # 문자열을 제거할것이기 떄문에 T에서 S 길이 뺸 만큼 실행
    tmp = can_1(T) # 1번 방법 실행
    if tmp != False: # 1번 방법이 실행이 되었다면
        T = tmp # T를 tmp의 결과값으로 변환
        continue # 다음 반복문으로 진행
    tmp = can_2(T) # 2번 방법 실행
    if tmp != False: # 2번 방법이 실행이 되었다면
        T = tmp # T를 tmp의 결과값으로 변환
        continue # 다음 반복문으로 진행
    if tmp == False: # 만일 1, 2 방법이 모두 되지 않는다면 
        print(0) # 0을 출력하고
        break # 반복문 종료


if T == S: # 모두 실행한 결과 같으면 
    print(1) # 1 출력
else: # 아니면 
    print(0) # 0 출력
    
