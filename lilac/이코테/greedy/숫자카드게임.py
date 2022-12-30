n, m = map(int, input().split())


min_cards = []
for _ in range(n):
    min_cards.append(min(list(map(int, input().split()))))

print(max(min_cards))
