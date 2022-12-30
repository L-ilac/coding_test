# 거꾸로 생각하자.
# 입력이 s,t로 주어졌을때, 주어진 규칙에따라 s->t의 변환이 가능한지 판단
# s -> t 로 생각하면 어렵지만, t -> s로 생각하면 결국에 경로가 하나뿐이라는걸 알 수 있다.

s = input()
t = input()

while len(s) != len(t):

    if t[-1] == "A":
        t = t[:-1]
    else:
        t = t[:-1][::-1]

if s == t:
    print(1)
else:
    print(0)
