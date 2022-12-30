def solution(alphabet):
    alphabet = alphabet.upper() # 입력받은 알파벳을 모두 대문자로 변경
    alphabet_list = [] # 알파벳과 갯수를 저장할 리스트

    for al in alphabet: # 입력받은 문자열을 순회하며
        contain = False # 문자열이 리스트 안에 있는지 확인할 boolean
        for alphabet in alphabet_list: # 알파벳과 갯수가 저장된 리스트에 현재 알파벳이 있는지 확인하여
            if alphabet[0] == al: # 알파벳이 있으면
                alphabet[1] += 1 # 갯수를 늘려주고
                contain = True # 포함한다고 true로 변경
                break # 반복문에서 빠져나가기
        if contain == False: # 알파벳이 없으면 
            alphabet_list.append([al, 1]) # 현재 알파벳과 1개 갯수를 포함하는 리스트 추가
    
    sort_list = sorted(alphabet_list, key=lambda x: -x[1]) # 리스트를 갯수를 기준으로 내림차순 

    if len(sort_list) > 1 and sort_list[0][1] == sort_list[1][1]: # 만일 리스트 갯수가 두개 이상이며, 첫번째 갯수와 두번째 갯수가 같으면 
        print("?") # ? 출력
    else: # 아니면 
        print(sort_list[0][0]) # 맨 첫번째 문자출력(이미 대문자로 바꿔줬으므로 문자만 출력하면 됨.)
    
words = input()
solution(words) 