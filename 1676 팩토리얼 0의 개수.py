a = int(input())
b = 1

# 팩토리얼 ! 계산하기
for i in range(a, 0, -1):
    b = b * i

c = str(b)
d = 0

for i in range(len(c) - 1, 0, -1):
    # 위에서 c가 문자열로 바뀌었으므로
    # 밑에 있는 if문에서 c가 문자열로 처리해야 한다.
    # c[i] = '0' 이런식으로 문자열 처리를 해야 된다.

    if c[i] == '0':
        d = d + 1
    elif c[i] != '0':
        break

print(d)

