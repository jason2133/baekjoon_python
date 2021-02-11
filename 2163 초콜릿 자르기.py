a, b = map(int, input().split())

if (a == 1 and b == 1):
    print(0)

if (a == 1 and b != 1):
    print(b - 1)

if (a != 1 and b == 1):
    print(a - 1)

if (a != 1 and b != 1):
    print((b - 1) + (a - 1) * b)






