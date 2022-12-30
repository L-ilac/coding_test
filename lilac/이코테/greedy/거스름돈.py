coins = [500, 100, 50, 10]

n = int(input())

coin_cnt = 0

for coin in coins:
    while n >= coin:
        n -= coin
        coin_cnt += 1

print(coin_cnt)
