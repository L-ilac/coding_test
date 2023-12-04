n = int(input())
call = list(map(int, input().split()))


y_fee = 0
m_fee = 0
for c in call:
    y_fee += ((c // 30) + 1) * 10
    m_fee += ((c // 60) + 1) * 15


if y_fee > m_fee:
    print("M " + str(m_fee))
elif y_fee < m_fee:
    print("Y " + str(y_fee))
else:
    print("Y M " + str(y_fee))
