a, b, c = map(int, input().split())

if (a > b and b > c) :
    print(b)

if (a > c and c > b) :
    print(c)

if (b > a and a > c) :
    print(a)

if (b > c and c > a) :
    print(c)

if (c > a and a > b) :
    print(a)

if (c > b and b > a):
    print(b)

if a == b and a > c:
    print(a)

if a == b and a < c:
    print(a)

if a == c and a > b:
    print(a)

if a == c and a < b:
    print(a)

if b == c and a < b:
    print(b)

if b == c and a > b:
    print(b)

if (a == b and b == c):
    print(b)


