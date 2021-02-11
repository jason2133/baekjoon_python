a, b = map(int, input().split())
if b < 0:
    c = a
    print(c)
    print(a-c*b)
else:
    print(a//b)
    print(a-a//b*b)

