a, b = map(str, input().split())

a0 = a[2]
a1 = a[1]
a2 = a[0]

b0 = b[2]
b1 = b[1]
b2 = b[0]

c = int(a0 + a1 + a2)
d = int(b0 + b1 + b2)

if c > d:
    print(c)
else:
    print(d)