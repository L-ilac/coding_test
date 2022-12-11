phone_book = ["12", "103", "1235", "567", "88", "112039810293817"]
dict_phone_book = {}


phone_book.sort()  # 사전식 정렬
print(phone_book)

for i in range(len(phone_book)-1):
    if phone_book[i].startswith(phone_book[i+1]):
        answer = False
        break


# 실패한 답안
dict_phone_book = {}
phone_book.sort(key=int)  # 숫자로 취급한채로 정렬

for i in range(10):
    dict_phone_book[str(i)] = []

for number in phone_book:
    dict_phone_book[str(number[0])].append(number)

for plist in dict_phone_book.values():
    if not plist:
        continue
    else:
        for i in range(len(plist)-1):
            for j in range(i+1, len(plist)):
                if plist[j].startswith(plist[i]):
                    answer = False
                    break
            if answer == False:
                break
        if answer == False:
            break


def solution(phone_book):
    answer = True
    hash_map = {}
    for phone_number in phone_book:
        hash_map[phone_number] = 1
    for phone_number in phone_book:
        temp = ""
        for number in phone_number:
            temp += number
            if temp in hash_map and temp != phone_number:
                answer = False
    return answer
