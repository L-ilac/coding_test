import sys

stack_l = list(input()) # 입력받은 문자열을 리스트로 변환 (커서의 왼쪽) 
num = int(input()) # 입력받아야 하는 숫자
stack_r = [] # 커서를 표현하기 위한 오른쪽 리스트

for _ in range(num):
    command = sys.stdin.readline().split() # 입력속도 빠르게 하기 위해서(input은 개행문자를 제거하고 나와서 속도가 느림.) sys.stdin.readline() 사용.
    if command[0] == 'P': # p가 입력되면
        stack_l.append(command[1]) # 왼쪽 리스트에 문자 삽입
    elif command[0] == 'L' and stack_l: # L 이 입력되고 왼쪽 리스트에 문자가 있다면
        stack_r.append(stack_l.pop()) # 오른쪽 리스트에 왼쪽 리스트 맨 마지막 문자를 넘겨주기
    elif command[0] == 'D' and stack_r: # D가 입력되고 오른쪽 리스트에 문자가 있다면
        stack_l.append(stack_r.pop()) # 왼쪽 리스트에 오른쪽 리스트의 맨 마지막 문자 넘겨주기
    elif command[0] == 'B'and stack_l: # B를 입력하고 왼쪽리스트(커서의 왼쪽) 에 문자열이 있다면 
        stack_l.pop() # 맨 마지막 문자 지우기
print("".join(stack_l + list(reversed(stack_r)))) # 출력(오른쪽 리스트는 이어주기 위해서 반대로 돌리기.)
