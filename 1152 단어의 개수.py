# 나는 띄어쓰기를 기준으로 코드를 잡았는데ㅠ

a = str(input())
b = 0

for i in range(0, len(a)):
    if (a[i] == ' '):
        b = b + 1

if (a[len(a) - 1] == ' '):
    b = b - 1

if (a[0] == ' '):
    b = b - 1

c = b + 1

print(c)

