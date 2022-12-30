n = list(map(int, list(input())))


left = sum(n[:len(n)//2])
right = sum(n[len(n)//2:])

if left == right:
    print("LUCKY")
else:
    print("READY")
