num = list(map(int, list(input())))


total = 0
for n in num:
    # 0과 1은 더해야 숫자를 키울 수 있고, 현 계산까지의 계산값이 0이라면 곱해도 0이므로 더하기를 해야한다.
    if n == 0 or n == 1 or total == 0:
        total += n
    else:  # 그 외의 경우에는 곱하기가 숫자를 키우는데 이득
        total *= n

print(total)
