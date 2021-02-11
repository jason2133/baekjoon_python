a, b = map(int, input().split())
c = 1
d = 1

for i in range(a, a-b, -1):
    c = i * c

for i in range(b, 0, -1):
    d = i * d

e = str(c // d)

g = 0

for i in range(len(e) - 1, 0, -1):
    # 위에서 e가 문자열로 바뀌었으므로
    # 밑에 있는 if문에서 e가 문자열로 처리해야 한다.
    # e[i] = '0' 이런식으로 문자열 처리를 해야 된다.

    if e[i] == '0':
        g = g + 1
    elif e[i] != '0':
        break

print(g)