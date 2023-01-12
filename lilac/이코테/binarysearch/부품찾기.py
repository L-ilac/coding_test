n = int(input())

have = list(map(int, input().split()))
have.sort()

m = int(input())

want = list(map(int, input().split()))


def bsearch(target):
    start = 0
    end = len(have)-1

    while start <= end:
        mid = (start+end)//2

        if have[mid] == target:
            return True
        elif have[mid] < target:
            start = mid+1
        else:
            end = mid-1

    return False


result = ''
for target in want:
    if bsearch(target):
        result += 'yes '
    else:
        result += 'no '

result.rstrip()
print(result)
