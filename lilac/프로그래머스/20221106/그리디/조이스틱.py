def min_move(i): # 알파벳 고를때 조이스틱 움직이는 횟수
    return 13 - abs(ord('N')-ord(i))

def solution(name):
    # 초기 최솟값은 그냥 맨 왼쪽에서 맨 오른쪽으로 쭉 이동했을 경우로 초기화
    answer = len(name) - 1
    
    # 연속된 A가 있을 경우 인덱스 범위가 어디인지 알기 위해서 필요한 변수
    idxOfA = 0
    
    for idx, ch in enumerate(name):
        #name 문자열의 첫번째가 A일 경우는 신경 쓸 필요 없으므로, name의 1번 인덱스부터 연속되는 A가 있는지 확인하면 된다.
        idxOfA = idx + 1
        
        # while문을 최종적으로 돌고나오면, idx+1 번 인덱스에서 idxOfA 번 인덱스 까지연속된 A가 있다는 걸 알 수 있음.(연속된 A가 여러개 더라도, 어차피 전부 검사해서 최소값으로 갱신함) 
        while idxOfA < len(name) and name[idxOfA] == 'A':
            idxOfA += 1
        
        # 왼쪽에서 오른쪽으로 쭉 갔을 경우 vs 왼쪽에서 오른쪽으로 가다가 연속된 A를 마주치고, 방향을 반대로(왼쪽) 바꾼뒤 맨뒤로 넘어가는 경우 
        answer = min(answer, (idx*2) + len(name) - idxOfA)
        
        # BBBBAAAAAAAB 와 같이, 처음부터 맨 뒷부분을 먼저 방문하는 것이 더 빠른 경우
        answer = min(answer, (len(name) -idxOfA)*2 + idx)

    # 알파벳 바꾸는 횟수 더해주기
    for i in name:
        answer += min_move(i)
        
    return answer